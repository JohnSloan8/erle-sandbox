var mainCount = 0;

function animate() {

    runAnimations();
    mainCount += 1;
    requestAnimationFrame( animate );
    renderer.render(scene, camera);

};

function runAnimations() {

    if ( expressionObject.bool ) {

        expression( mainCount );

    }

    if ( movementObject.bool ) {

        movement( mainCount );

    }

    if ( eyelidObject.bool ) {

        moveEyelids( mainCount );

    }

    if ( eyeObject.bool ) {

        moveEyes( mainCount );

    }

    if ( controllerObject.blink.bool ) {

        blinkController();

    }

    if ( blinkObject.bool ) {

        blink();

    }

    // Random tilt spine and neck
    if ( controllerObject.randomTilt.bool ) {

        tilt();

    }

    if ( synthesisObject.talking ) {

        randomHeadTiltController();

    }

}

