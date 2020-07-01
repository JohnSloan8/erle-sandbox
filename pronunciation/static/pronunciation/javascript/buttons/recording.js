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


