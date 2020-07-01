function setResetEvent() {

    $( '#resetButton' ).click( resetSaoirse );

}

function resetSaoirse() {

    $( '#blinkCheckbox' ).prop( 'checked', true );
    controllerObject.blink.bool = true;
    $( '#randomTiltCheckbox' ).prop( 'checked', true );
    controllerObject.randomTilt.bool = true;

    synthesisObject.parameters.emphasis = 0;
    createTempVisemePoses();
    synthesisObject.parameters.speed = 50;
    synthesisObject.audio.playbackRate = 1;

    $( '#surpriseRange' ).val( 0 );
    $( '#rotationRange' ).val( 50 );
    $( '#leanRange' ).val( 50 );
    $( '#tiltRange' ).val( 50 );
    $( '#emphasisRange' ).val( 0 );
    $( '#speedRange' ).val( 50 );
    
    setPositionOfClickedEmotionWheelMarker(0, 0);
    emotionWheelObject.coords = [0, 0];
    surpriseObject.surprise = 0;
    changeExpression( emotionWheelObject.coords, surpriseObject.surprise );
    expressionController(expressionObject.calculated, 0.5, function(){})

    expressionController( expressionObject.abs.expressions.neutral, 0.5 );
    movementController( movementObject.abs.blank, 0.5, 0.5 );

}

