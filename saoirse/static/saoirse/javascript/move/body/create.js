function createMovement( mov, mult ) {

    let calcMov = $.extend(true, {}, mov);

    Object.keys( mov.AUs ).forEach( function( AU ) {

        Object.keys( mov.AUs[ AU ] ).forEach( function( bone ) {

            let movThisBone = mov.AUs[ AU ][ bone ]

            for ( var j=0; j < 2; j++ ) {

                for ( var k=0; k < 3; k++ ) {

                    let movementAmount = movThisBone[ j ][ k ] * mult;

                    calcMov.AUs[ AU ][ bone ][ j ][ k ] = movementAmount;

                }

            }

        })

    })

    for ( var l=0; l < 2; l++ ) {

        for ( var m=0; m < 3; m++ ) {

            calcMov.sacc[ l ][ m ] = mov.sacc[ l ][ m ] * mult;

        }

    }

    movementObject.calculated = getAbsoluteCoordsOfMovementTo( calcMov ); 

}


