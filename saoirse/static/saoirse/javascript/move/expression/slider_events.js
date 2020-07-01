var surpriseObject = {
    'surprise': 0,
}

function initSurpriseEvent( surpriseValue ) {

    surpriseObject.surprise = surpriseValue / 100;
    changeExpression( emotionWheelObject.coords, surpriseObject.surprise );
    expressionController(expressionObject.calculated, 0.5, function(){})

}

function resetOtherMovementRanges( mov ) {

    if ( mov === 'rotation' ) {

        $( '#leanRange' ).val( 50 );
        $( '#tiltRange' ).val( 50 );

    } else if ( mov === 'lean' ) {

        $( '#rotationRange' ).val( 50 );
        $( '#tiltRange' ).val( 50 );

    } else if ( mov === 'tilt' ) {

        $( '#rotationRange' ).val( 50 );
        $( '#leanRange' ).val( 50 );

    }

}

function initRotationEvent( rotationValue ) {

    resetOtherMovementRanges( 'rotation' );
    let rotation = 2 * ( rotationValue - 50 ) / 100;
    createMovement(movementObject.rel.rotateLeft, rotation);
    movementController(movementObject.calculated, 0.5, 0.5)

}

function initLeanEvent( leanValue ) {

    resetOtherMovementRanges( 'lean' );
    let lean = 2 * ( leanValue - 50 ) / 100;
    createMovement(movementObject.rel.leanBack, lean);
    movementController(movementObject.calculated, 0.5, 0.5)

}

function initTiltEvent( tiltValue ) {

    console.log('in initTiltEvent')
    resetOtherMovementRanges( 'tilt' );
    let tilt = 2 * ( tiltValue - 50 ) / 100;
    createMovement(movementObject.rel.tiltLeft, tilt);
    movementController(movementObject.calculated, 0.5, 0.5)

}

