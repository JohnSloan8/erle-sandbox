function microphoneClicked() {

   	startRecording();
   	displayButtons( 'top', [] );
   	displayButtons( 'bottom', [ 'stop' ] );
   	$('#transcriptionContainer').show();
  	setWordsToViewMode( clearSelection=true );

}

function stopClicked() {

   stopRecording();
   displayButtons( 'bottom', [ '' ] );

}

function getRecognitionResponse( json ) {

    audioVariables.count = 0;
    audioVariables.id = json.id;
    if ( json.words.length !== 0 ) {

        audioVariables.transcript = json.words;
        audioVariables.transcriptWithSpaces = addSpaces( json.words );
        audioVariables.relativeFilename = json.relative_filename
        audioVariables.speechAudio.src = prefixURL + 'media/' + audioVariables.relativeFilename;
        audioVariables.fullSpeechAudio.src = prefixURL + 'media/' + audioVariables.relativeFilename;
        audioVariables.speechAudio.serverDuration = json.duration;
        readyVoiceAudio();
    
    } else {

   		displayButtons( 'bottom', [ 'microphone' ] );

        if ( audioVariables.transcript.length === 0 ) {

            $('#transcriptionContainer').hide();

        }

    }

}

function addSpaces( w ) {

    wordListWithSpaces = []
    if ( w.length !== 0 ) {

        w.forEach( function( word, i ) {

            console.log('word:', word)
            //console.log('w[i-1]:', w[i-1])
            //console.log('w[i-1].voice:', w[i-1].voice)
            //console.log('w[i+1]:', w[i+1])
            //console.log('w[i+1].voice:', w[i+1].voice)
            if ( w[ i - 1 ] !== undefined ) {

                if ( !w[ i - 1 ].voice && !word.voice ) {

                    console.log('word again:', word)
                    wordListWithSpaces.push( { word: "&nbsp", voice: false, start_time: null, end_time: null, highlighted: null } );
            
                } else {

                    wordListWithSpaces.push( { word: "&nbsp", voice: true, start_time: null, end_time: null, highlighted: null  } );

                }

            } else {

                wordListWithSpaces.push( { word: "&nbsp", voice: true, start_time: null, end_time: null, highlighted: null  } );

            }

            wordListWithSpaces.push( word );

        });

        wordListWithSpaces.push( { word: "&nbsp", voice: true, start_time: null, end_time: null, highlighted: null  } );

    }

    return wordListWithSpaces

}

function readyVoiceAudio() {

    audioVariables.speechAudio.oncanplaythrough = function(){

        console.log('can play through')
        displayTranscript();
        displayButtons( 'bottom', [ 'ear', 'microphone', 'play' ] );
        setTimestampsForAudio()

    }

}

function playVoiceSnippet() {

    console.log('in playVoice');
    audioVariables.speechAudio.onplay = setPauseEvent();
    audioVariables.speechAudio.play();
    
}

function setPauseEvent() {

    audioVariables.speechAudio.onplay = null;
    setTimeout( function() {
        
        audioVariables.speechAudio.pause();
        audioVariables.speechAudio.load();
        audioVariables.speechAudio.oncanplaythrough = pauseVoice();

    }, audioVariables.splicedAudioDuration * 1000 );

}

function pauseVoice() {

    audioVariables.speechAudio.oncanplaythrough = null;
    audioVariables.speechAudio.currentTime = audioVariables.splicedAudioStartTime;

}

function playVoiceFull() {

    audioVariables.fullSpeechAudio.play();

}


