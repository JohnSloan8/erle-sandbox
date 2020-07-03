function displayButtons( position, buttons ) {

    $( '.erle-' + position + '-button-container' ).hide();

    buttons.forEach( function( b ) {

        $('#' + b + 'ButtonContainer' ).show();

    })

    if ( buttons.length === 0 ) {
    
        $( '#' + position + 'ButtonsContainer' ).hide();

    } else {

        $( '#' + position + 'ButtonsContainer' ).show();

    }

}

function setButtonEvents() {

    $( '#xCloseButtonContainer' ).click( deleteWords );
    $( '#keyboardButtonContainer' ).click( activateKeyboard );
    $( '#microphoneButtonContainer' ).click( microphoneClicked );
    $( '#stopButtonContainer' ).click( stopClicked );
    $( '#earBlueButtonContainer' ).click( playVoiceSnippet );
    $( '#earButtonContainer' ).click( playVoiceFull );

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

