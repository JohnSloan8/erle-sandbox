const SINEARRAYFORTILTSECONDS = [ 120, 150, 180, 210, 240, 270, 300 ]
const SINEARRAYFORHEADTILTSECONDS = [ 90, 120, 150 ]
var tiltControllerObject = { newTilt: false };

function tilt() {

    let randomTiltSpineRemaining = mainCount - spineRandomTiltObject.startCount;

    if ( randomTiltSpineRemaining >= spineRandomTiltObject.sinLength || tiltControllerObject.newTilt ) {
        
        spineRandomTiltObject.startRotationZ = tiaObject.bodyBones.spineLower.rotation.z;
        newTilt( spineRandomTiltObject );

    } else {
        
        randomTiltSpine( randomTiltSpineRemaining )

    }
    
    //let randomTiltNeckRemaining = mainCount - neckRandomTiltObject.startCount;

    //if ( randomTiltNeckRemaining >= neckRandomTiltObject.sinLength || tiltControllerObject.newTilt) {
        
        //neckRandomTiltObject.startRotationZ = tiaObject.faceBones.neck.rotation.z;
        //newTilt( neckRandomTiltObject );

    //} else {
        
        //randomTiltNeck( randomTiltNeckRemaining )

    //}

    let randomHeadWobbleRemaining = mainCount - headRandomWobbleObject.startCount;

    if ( randomHeadWobbleRemaining >= headRandomWobbleObject.sinLength || tiltControllerObject.newTilt) {
        
        headRandomWobbleObject.startPositionX = tiaObject.faceBones.head.position.x;
        newTilt( headRandomWobbleObject );
        tiltControllerObject.newTilt = false;

    } else {
        
        randomHeadWobble( randomHeadWobbleRemaining )

    }

}

function newTilt( boneObject ) {

    boneObject.startCount = mainCount;

    if ( boneObject.to ) {

        boneObject.direction *= -1;
        boneObject.to = false;
    

    } else {
        var newSinAmount;
        boneObject.direction *= Math.random() < 0.5 ? -1 : 1;
        if ( boneObject === neckRandomTiltObject || boneObject === spineRandomTiltObject || boneObject === headRandomWobbleObject ) {
         
            newSinAmount = SINEARRAYFORTILTSECONDS[ Math.floor( Math.random() *  SINEARRAYFORTILTSECONDS.length ) ];
            boneObject.sin = sineArrays[ newSinAmount.toString() ];
            boneObject.sinLength = boneObject.sin.length;
            
            if ( boneObject === neckRandomTiltObject ) {
            
                boneObject.mult = Math.random();

            } else if ( boneObject === spineRandomTiltObject ) {

                boneObject.mult = 0.4 + 0.5 * Math.random();
        
            } else if ( boneObject === headRandomWobbleObject ) {

                boneObject.mult = 5 * Math.random();
        
            }

        } else {

            newSinAmount = SINEARRAYFORHEADTILTSECONDS[ Math.floor( Math.random() * SINEARRAYFORHEADTILTSECONDS.length ) ];
            boneObject.sin = sineArrays[ newSinAmount ];
            boneObject.sinLength = boneObject.sin.length;
            
            boneObject.mult = 0.75 + 0.75 * Math.random();

        }

        boneObject.to = true;

    }

}

function randomTiltSpine( remaining ) {

    tiaObject.bodyBones.spineLower.rotation.z = spineRandomTiltObject.startRotationZ + spineRandomTiltObject.direction * spineRandomTiltObject.mult * spineRandomTiltObject.sin[ remaining ];

}

//function randomTiltNeck( remaining ) {

    //tiaObject.faceBones.neck.rotation.z = neckRandomTiltObject.startRotationZ + neckRandomTiltObject.direction * neckRandomTiltObject.mult * neckRandomTiltObject.sin[ remaining ];

//}

function randomHeadWobble( remaining ) {

    tiaObject.faceBones.head.position.x = headRandomWobbleObject.startPositionX + headRandomWobbleObject.direction * headRandomWobbleObject.mult * headRandomWobbleObject.sin[ remaining ];

}

