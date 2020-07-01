var randomTiltHeadControllerObject = { newTilt: false };
function randomHeadTiltController() {

    let randomTiltHeadXRemaining = mainCount - headXRandomTiltObject.startCount;

    if ( randomTiltHeadXRemaining === headXRandomTiltObject.sinLength || randomTiltHeadControllerObject.newTilt ) {
        
        headXRandomTiltObject.startRotationX = tiaObject.faceBones.head.rotation.x;
        headXRandomTiltObject.eyeStartRotationX = tiaObject.eyeBones.eyeL.rotation.x;
        newTilt( headXRandomTiltObject );

    } else {
        
        randomTiltHeadX( randomTiltHeadXRemaining )

    }
    
    let randomTiltHeadYRemaining = mainCount - headYRandomTiltObject.startCount;

    if ( randomTiltHeadYRemaining === headYRandomTiltObject.sinLength || randomTiltHeadControllerObject.newTilt ) {
        
        headYRandomTiltObject.startRotationY = tiaObject.faceBones.head.rotation.y;
        headYRandomTiltObject.eyeLStartRotationY = tiaObject.eyeBones.eyeL.rotation.y;
        headYRandomTiltObject.eyeRStartRotationY = tiaObject.eyeBones.eyeR.rotation.y;
        newTilt( headYRandomTiltObject );
        randomTiltHeadControllerObject.newTilt = false;

    } else {
        
        randomTiltHeadY( randomTiltHeadYRemaining )

    }
    
}

function randomTiltHeadX( remaining ) {

    let Xmult = headXRandomTiltObject.direction * headXRandomTiltObject.mult * headXRandomTiltObject.sin[ remaining ];
    tiaObject.faceBones.head.rotation.x = headXRandomTiltObject.startRotationX + Xmult;
    eyeObject.currentCoords[ 1 ][ 0 ] =  headXRandomTiltObject.eyeStartRotationX -Xmult;
    tiaObject.eyeBones.eyeL.rotation.x = headXRandomTiltObject.eyeStartRotationX -Xmult;
    tiaObject.eyeBones.eyeR.rotation.x = headXRandomTiltObject.eyeStartRotationX -Xmult;

}

function randomTiltHeadY( remaining ) {

    let Ymult = headYRandomTiltObject.direction * headYRandomTiltObject.mult * headYRandomTiltObject.sin[ remaining ];
    tiaObject.faceBones.head.rotation.y = headYRandomTiltObject.startRotationY + Ymult;
    eyeObject.currentCoords[ 1 ][ 1 ] =  headYRandomTiltObject.eyeLStartRotationY -Ymult - 0.5 * EYEL_ROT.y;
    tiaObject.eyeBones.eyeL.rotation.y = headYRandomTiltObject.eyeLStartRotationY -Ymult;
    tiaObject.eyeBones.eyeR.rotation.y = headYRandomTiltObject.eyeRStartRotationY -Ymult;

}


