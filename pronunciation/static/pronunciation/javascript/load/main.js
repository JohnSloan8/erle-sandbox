$(window).on( 'load', function() {

    definePrefixURL();
    readyAudio();
    setButtonEvents();
    displayButtons( 'bottom', [ 'microphone' ] )
    //developmentPrep();

});

// DEVELOPMENT STUFF

function developmentPrep() {

    displayTranscript();
    //activateKeyboard();

}

