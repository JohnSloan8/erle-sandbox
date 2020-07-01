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

    $( '.transcription-word-space-inner-container').css({

            'background-color': 'white',
            'color': 'black'

    });

    for( let i = integersStartFinish[ 0 ]; i <= integersStartFinish[ 1 ]; i++ ) {

        $( '#transcriptionWord' + i.toString() ).css({
            'background-color': 'blue',
            'color': 'white'
        });

    };


    $( '#transcriptionWord' + (integersStartFinish[ 0 ] - 1).toString() ).css({

        'background-color': lightBlueHexColor,

    });
    $( '#transcriptionWord' + (integersStartFinish[ 0 ] - 2).toString() ).css({

        'background-color': lightBlueHexColor,

    });
    $( '#transcriptionWord' + (integersStartFinish[ 0 ] - 3).toString() ).css({

        'background-color': lightBlueHexColor,

    });
    if ( integersStartFinish[ 0 ] % 2 !== 0 ) {

        $( '#transcriptionWord' + (integersStartFinish[ 0 ] - 4).toString() ).css({

        'background-color': lightBlueHexColor,

        });

    }

    $( '#transcriptionWord' + (integersStartFinish[ 1 ] + 1).toString() ).css({

        'background-color': lightBlueHexColor,

    });
    $( '#transcriptionWord' + (integersStartFinish[ 1 ] + 2).toString() ).css({

        'background-color': lightBlueHexColor,

    });
    $( '#transcriptionWord' + (integersStartFinish[ 1 ] + 3).toString() ).css({

        'background-color': lightBlueHexColor,

    });
    if ( integersStartFinish[ 1 ] % 2 !== 0 ) {

        $( '#transcriptionWord' + (integersStartFinish[ 1 ] + 4).toString() ).css({

        'background-color': lightBlueHexColor,

        });

    }

}

function displayAppropriateTopButtons() {

    let lenSelectedIntegers = integersStartFinish.length;
    if ( lenSelectedIntegers === 0 ) {

        displayButtons( 'top', [] );

    } else { 

        if ( integersStartFinish[ 0 ] === integersStartFinish[ 1 ] ) {

            if ( integersStartFinish[ 0 ] % 2 === 0 ) {

                displayButtons( 'top', [ 'earBlue', 'keyboard' ] );

            } else {

                displayButtons( 'top', [ 'earBlue', 'keyboard', 'xClose' ] );

            }

        } else {
            
            displayButtons( 'top', [ 'earBlue', 'keyboard', 'xClose' ] );

        }

    }

}

function deleteWords() {

    let transcriptIndexesToBeDeleted = getIndexesToBeDeleted();

    let newTranscript = []
    audioVariables.transcript.forEach( function( w, j ) {

        if ( !transcriptIndexesToBeDeleted.includes( j ) ) {

            newTranscript.push( w );

        }

    })

    if ( newTranscript.length !== 0 ) {
    
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

    audioVariables.transcript = newTranscript;

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

    audioVariables.count = json.updated_audio_count;
    console.log( 'json.updated_relative_filename:', json.updated_relative_filename );
    audioVariables.relativeFilename = json.updated_relative_filename;
    console.log( 'json.updated_words', json.updated_words );
    audioVariables.transcript = json.updated_words;
    console.log( 'json.updated_duration:', json.updated_duration );
    audioVariables.speechAudio.serverDuration = json.updated_duration;
    audioVariables.speechAudio.src = prefixURL + 'media/' + audioVariables.relativeFilename;
    audioVariables.fullSpeechAudio.src = prefixURL + 'media/' + audioVariables.relativeFilename;
    displayTranscript();
    if ( audioVariables.modification === 'typed' ) {

        audioVariables.modification = null;
        displayButtons( 'top', [ 'speak' ] );

        alterTranscript();
        for ( let j=newAlteredWordIndexes[ 0 ] * 2 + 1; j<=newAlteredWordIndexes[ newAlteredWordIndexes.length - 1 ] * 2 + 1; j++ ) {

            $( '#transcriptionWord' + j.toString() ).css({ 
                'background-color': 'green',
                'color': 'white',
            });

        }

    } else {

        displayAppropriateTopButtons();

    }

    readyVoiceAudio();
    displayButtons( 'bottom', [ 'ear', 'microphone', 'play' ] );

}

var newAlteredWordIndexes = []
function alterTranscript() {

    let alteredWordIndexes = []
    let singleSpace = false;
    if ( integersStartFinish[ 0 ] === integersStartFinish[ 1 ] && integersStartFinish[ 0 ] % 2 === 0 ) {

        let singleSpaceIndex = ( integersStartFinish[ 0 ] ) / 2
        alteredWordIndexes = [ singleSpaceIndex, singleSpaceIndex ];
        singleSpace = true;

    } else {

        for( let i = integersStartFinish[ 0 ]; i <= integersStartFinish[ 1 ]; i++ ) {

            if ( i % 2 !== 0 ) {

                alteredWordIndexes.push( ( i - 1 ) / 2 );

            }

        }

    }

    let preAlteration = audioVariables.transcript.slice( 0, alteredWordIndexes[ 0 ] );
    let postAlteration;
    if ( singleSpace ) {
        
        postAlteration = audioVariables.transcript.slice( alteredWordIndexes[ alteredWordIndexes.length - 1 ] );

    } else {

        postAlteration = audioVariables.transcript.slice( alteredWordIndexes[ alteredWordIndexes.length - 1 ] + 1 );
    
    }

    let preAlterationLength = preAlteration.length;
    newAlteredWordIndexes = []
    typedString.split(' ').forEach( function( w, i ) {

        newAlteredWordIndexes.push( preAlterationLength + i );
        preAlteration.push({
        
            'word': w,
            'start_time': null,
            'end_time': null,

        });

    })

    audioVariables.transcript = preAlteration.concat( postAlteration );

}



