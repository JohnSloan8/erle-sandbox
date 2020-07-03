function displayTranscript() {

    console.log('in displayTranscript');
    $( '#transcriptionInnerContainer' ).empty();

    if ( audioVariables.transcriptWithSpaces.length !== 0 ) {

        $( '#transcriptionContainer' ).show();
        let lastIndex = audioVariables.transcriptWithSpaces.length - 1;
        let firstSynthesisedWord = true;
        audioVariables.transcriptWithSpaces.forEach( function( w, i ) {

            classToAdd = getClassesToAdd( w )

            $( '#transcriptionInnerContainer' ).append(

                '<div class="transcription-word-space-container">' +

                    '<div class="transcription-word-space-inner-container ' + classToAdd + '" id="transcriptionWord' + i.toString() + '">' + w.word + '</div>' +

                '</div><!--'

            )

        });

        resetTapWordEvents();

    } else {

        $( '#transcriptionContainer' ).hide();
        displayButtons( 'bottom', [ 'microphone' ] );

    }

}

function getClassesToAdd( w_ ) {

    let classToAdd = 'inactive-word-voice';


    if ( w_.voice === false ) {

        classToAdd = 'active-synthesised-word' ;
        w_.voice = null;
        //w_.highlighted = null;

    } else if ( w_.voice === null ) {

        if ( w_.highlighted === 'main' ) {
        
            //classToAdd = 'main-highlighted-word-synthesised';
            classToAdd = 'main-highlighted-word';

        } else if ( w_.highlighted === 'secondary' ) {

            //classToAdd = 'secondary-highlighted-word-synthesised';
            classToAdd = 'secondary-highlighted-word';

        } else {

            classToAdd = 'inactive-synthesised-word';

        }

    } else {

        if ( w_.voice ) {

            if ( w_.highlighted === 'main' ) {
            
                classToAdd = 'main-highlighted-word';

            } else if ( w_.highlighted === 'secondary' ) {

                classToAdd = 'secondary-highlighted-word';

            }

        }

    }

    return classToAdd

}
