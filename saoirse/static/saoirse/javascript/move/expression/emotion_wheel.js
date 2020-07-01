var emotionWheelObject = {
    'coords': [ 0, 0 ],
};

function initEmotionWheelEvents() {

    getLocationOfEmotionWheel();
    setPositionOfClickedEmotionWheelMarker(0, 0);
    $('#emotionWheel').on( 'click', getEmotionCoords );
    
}

function getLocationOfEmotionWheel() {

    let posLeft = $('#emotionWheel').offset().left;
    let width = $('#emotionWheel').width() * 1.;
    let posTop = $('#emotionWheel').offset().top;
    let height = width * 1.025;
    
    let centreX = posLeft + width / 2;
    let centreY = posTop + height / 2;
    
    emotionWheelObject.relativeCenter = [ width / 2, height / 2 ];
    emotionWheelObject.centre = [ centreX, centreY ];
    emotionWheelObject.radius = width / 2;

}
 
function getEmotionCoords(e) {

    let mouseX = e.clientX;
    let mouseY = e.clientY;
    //console.log('mouseX:', mouseX)
    //console.log('mouseY:', mouseY)
    let Xraw = mouseX - emotionWheelObject.centre[ 0 ];
    let Yraw = emotionWheelObject.centre[ 1 ] - mouseY;
    let X = Math.round( 100 * Xraw / emotionWheelObject.radius ) / 100;
    let Y = Math.round( 100 * Yraw / emotionWheelObject.radius ) / 100;

    emotionWheelObject.coords = [X, Y]

    changeExpression( emotionWheelObject.coords, surpriseObject.surprise );
    expressionController(expressionObject.calculated, 0.5, function(){})
    setPositionOfClickedEmotionWheelMarker( Xraw, Yraw, true );

}

function setPositionOfClickedEmotionWheelMarker( x, y, highlight ) {

    $('#emotionClickedLocation').css({ 
        
        'left': emotionWheelObject.radius + x - 4, 
        'top': emotionWheelObject.radius - y - 4,

    });

    if ( highlight ) {

        $( '#emotionWheelObject' ).css( 'opacity', '1' );
        $("#emotionWheelObject").hover( function(e) {

            $(this).css("opacity",e.type==="mouseenter"?"1":"1");
          
        });

    } else {

        $( '#emotionWheelObject' ).css( 'opacity', '0.7' );
        $("#emotionWheelObject").hover(function(e) {

            $(this).css("opacity",e.type==="mouseenter"?"1":"0.7");
          
        });

    }

}

