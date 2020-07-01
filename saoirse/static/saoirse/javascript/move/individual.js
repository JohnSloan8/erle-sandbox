//////////////// MOVE ANYTHING 

function initMove( obj, coords, secs, direction ) {

    if ( obj.bool ) {

      //console.log(' initMove cant move: ' + obj.name + '. Still moving previous one!!\n\nCalled by' + initMove.caller.name + '. Try again in 200ms.')
        setTimeout( function() {

            initMove( obj, coords, secs, direction )

        }, 200 );

    } else {

        assignSinArrayForSpeed( secs, obj, sineArrays ) 
        obj.startCount = mainCount;

        for (var i=0; i<2; i++) {

            for (var j=0; j<3; j++) {

                obj.movementCoords[ i ][ j ] = coords[ i ][ j ] - obj.currentCoords[ i ][ j ];

            }

        }

        if ( direction !== undefined ) {

            obj.dir = direction

        }

        obj.currentCoords = coords;
        obj.bool = true;

    }

}

function moveEyes( main ) {

    let main_start = main - eyeObject[ 'startCount' ];
    let sinAmount = eyeObject.sin[ main_start ];
    
    if ( main_start < eyeObject.sinLength ) {

        let XMult = eyeObject.movementCoords[1][0] * sinAmount;
        let YMult = eyeObject.movementCoords[1][1] * sinAmount;

        tiaObject.eyeBones.eyeL.rotation.x += XMult;
        tiaObject.eyeBones.eyeR.rotation.x += XMult;
        tiaObject.eyeBones.eyeL.rotation.y += YMult;
        tiaObject.eyeBones.eyeR.rotation.y += YMult;

    } else {

        eyeObject.bool = false;

    }

}

function lean( main ) {

    let main_start = main - leanObject.startCount;
    let sinAmount = leanObject.sin[ main_start ]
    
    if ( main_start < leanObject.sinLength ) {

        let mult = leanObject.movementCoords[1][0] * sinAmount;
        tiaObject.bodyBones.spineUpperInner.rotation.x += mult;
        tiaObject.faceBones.head.rotation.x -= mult;

    } else {

        leanObject.bool = false;

    }

}

