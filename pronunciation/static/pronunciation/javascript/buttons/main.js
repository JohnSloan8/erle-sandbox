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
