var integersStartFinish = []

function resetTapWordEvents() {

    $( '.transcription-word-space-inner-container' ).off( 'click' );
    $( '.transcription-word-space-inner-container' ).click( wordTap );

}

function resetIntegersStartFinish() {

    integersStartFinish = [];

}

function wordTap() {

    let thisId = parseInt( this.id.slice(17) )

    calculateIntegersStartFinish( thisId );

    console.log('in wordTap()');
    setTimestampsForAudio();

    highlightWords();

    displayAppropriateTopButtons();

}

function calculateIntegersStartFinish( idInteger ) {

    if ( integersStartFinish.length === 0 ) {

        integersStartFinish = [ idInteger, idInteger ];

    } else {
        
        if ( idInteger < integersStartFinish[ 0 ] ) {

            if ( integersStartFinish[ 0 ] - idInteger > 3 ) {

                integersStartFinish = [ idInteger, idInteger ];

            } else {

                integersStartFinish[ 0 ] = idInteger;

            }

        } else if ( idInteger > integersStartFinish[ 1 ] ) {

            if ( idInteger - integersStartFinish[ 1 ] > 3 ) {

                integersStartFinish = [ idInteger, idInteger ];

            } else {

                integersStartFinish[ 1 ] = idInteger;

            }

        } else {

            if ( integersStartFinish[ 0 ] === integersStartFinish[ 1 ] ) {

                integersStartFinish = [];

            } else {
                
                let lower = [];
                let higher = [];
                for( let i = integersStartFinish[ 0 ]; i <= integersStartFinish[ 1 ]; i++ ) {
                
                    if ( i < idInteger ) {

                        lower.push( i );

                    } else if ( i > idInteger ) {

                        higher.push( i );

                    }

                }

                let selectedSplitIntegers;
                if ( lower.length > higher.length ) {

                    selectedSplitIntegers = lower;

                } else {

                    selectedSplitIntegers = higher;

                }
                
                integersStartFinish[ 0 ] = selectedSplitIntegers[ 0 ]
                if ( selectedSplitIntegers.length === 1 ) {

                    integersStartFinish[ 1 ] = selectedSplitIntegers[ 0 ];

                } else {

                    integersStartFinish[ 1 ] = selectedSplitIntegers[ selectedSplitIntegers.length - 1 ];

                }

            }

        }
    
    }

}

function highlightWords() {

    audioVariables.transcriptWithSpaces.forEach( function( w ) {
        
        w.highlighted = null;

    })


    let finalIntegerIndex = audioVariables.transcriptWithSpaces.length - 1;
    for ( let i = 1; i<5; i++ ) {
    
        audioVariables.transcriptWithSpaces[ Math.max( 0, integersStartFinish[ 0 ] - i ) ].highlighted = 'secondary';
        audioVariables.transcriptWithSpaces[ Math.min( finalIntegerIndex, integersStartFinish[ 1 ] + i ) ].highlighted = 'secondary';

    }

    for( let i = integersStartFinish[ 0 ]; i <= integersStartFinish[ 1 ]; i++ ) {

        audioVariables.transcriptWithSpaces[ i ].highlighted = 'main';

    };

    displayTranscript();

}

function resetHighlightedTranscript() {

    audioVariables.transcript.forEach( function( w ) {

        w.highlighted = null

    })

}

function deleteWords() {

    let transcriptIndexesToBeDeleted = getIndexesToBeDeleted();

    let newTranscript = []
    audioVariables.transcript.forEach( function( w, j ) {

        w.highlighted = null;
        if ( !transcriptIndexesToBeDeleted.includes( j ) ) {

            newTranscript.push( w );

        }

    })

    if ( newTranscript.length !== 0 ) {
    
        audioVariables.modification === 'delete';
        setWordsToViewMode();
        displayButtons( 'top', [] )
        displayButtons( 'bottom', [''] )
        let dataToSend = {
            'indexesToBeDeleted': transcriptIndexesToBeDeleted,
            'transcript': audioVariables.transcript,
            'relativeFilename': audioVariables.relativeFilename,
            'ID': audioVariables.id,
            'count': audioVariables.count
        }
        let JSONData = JSON.stringify( dataToSend );
        audioVariables.modification = 'delete';
        sendAjax( "/pronunciation/delete_words", "GET", JSONData, 10000, getModifiedVoiceAudio, true, "application/json; charset=utf-8")

    }

}

function getIndexesToBeDeleted() {

    let transcriptIndexesToBeDeleted = [];
    for( let i = integersStartFinish[ 0 ]; i <= integersStartFinish[ 1 ]; i++ ) {

        if ( i % 2 !== 0 ) {

            transcriptIndexesToBeDeleted.push( ( i - 1 ) / 2 );

        }

    }

    return transcriptIndexesToBeDeleted

}

function setTimestampsForAudio() {

    audioVariables.speechAudio.oncanplaythrough = null;
    audioVariables.splicedAudioStartTime = 0;
    audioVariables.splicedAudioEndTime = audioVariables.speechAudio.serverDuration;

    if ( integersStartFinish.length !== 0 ) {

        let wordIntegers = getOnlyWordIntegers();
        let transcriptIntegers = [ convertWordInteger( wordIntegers[ 0 ] ), convertWordInteger( wordIntegers[ 1 ] ) ];

        let wordMinus2 = Math.max( transcriptIntegers[ 0 ] - 2, 0 );
        audioVariables.splicedAudioStartTime = audioVariables.transcript[ wordMinus2 ].start_time; 

        if ( audioVariables.transcript.length - 1 - transcriptIntegers[ 1 ] > 2 ) {

            let wordPlus2 = transcriptIntegers[ 1 ] + 2;
            audioVariables.splicedAudioEndTime = audioVariables.transcript[ wordPlus2 ].end_time + 0.2;
        
        }


    }

    audioVariables.speechAudio.load(); //put this here cause blue ear was only wokring on second click (seems to work on first try)
    audioVariables.speechAudio.currentTime = audioVariables.splicedAudioStartTime;
    audioVariables.splicedAudioDuration = audioVariables.splicedAudioEndTime - audioVariables.splicedAudioStartTime;

    console.log( 'audioVariables.splicedAudioStartTime:', audioVariables.splicedAudioStartTime)
    console.log( 'audioVariables.splicedAudioEndTime:', audioVariables.splicedAudioEndTime)
    console.log( 'audioVariables.speechAudio.currentTime:', audioVariables.speechAudio.currentTime)
    console.log( 'audioVariables.splicedAudioDuration:', audioVariables.splicedAudioDuration)

}

function convertWordInteger( integer_ ) {

    return parseInt( ( integer_ - 1 ) / 2 );

}

function getModifiedVoiceAudio( json ) {

    resetIntegersStartFinish();
    audioVariables.count = json.updated_audio_count;
    audioVariables.relativeFilename = json.updated_relative_filename;
    audioVariables.transcript = json.updated_words;
    audioVariables.transcriptWithSpaces= addSpaces( json.updated_words );
    audioVariables.speechAudio.serverDuration = json.updated_duration;
    audioVariables.speechAudio.src = prefixURL + 'media/' + audioVariables.relativeFilename;
    audioVariables.fullSpeechAudio.src = prefixURL + 'media/' + audioVariables.relativeFilename;
    //displayTranscript();
    if ( audioVariables.modification === 'typed' ) {

        displayButtons( 'top', [ 'speak' ] );

    } else if ( audioVariables.modification === 'delete' ) {

        displayButtons( 'top', [] );

    } else {

        displayAppropriateTopButtons();

    }

    audioVariables.modification = null;
    readyVoiceAudio();
    displayButtons( 'bottom', [ 'ear', 'microphone', 'play' ] );

}

