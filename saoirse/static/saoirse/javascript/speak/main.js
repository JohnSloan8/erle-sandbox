var synthesisObject = {
    'audio': document.getElementById( 'synthAudio' ),
    'parameters': {},

}

function setPrepareButtonEvent() {

    $( '#prepareButton' ).hide();
    $( '#prepareButton' ).click( gatherSpeechSettingsAndText );

}

function gatherSpeechSettingsAndText() {

    synthesisObject.parameters.emphasis = parseInt( $( '#emphasisRange' ).val() );
    synthesisObject.parameters.pitch = parseInt( $( '#pitchRange' ).val() );
    synthesisObject.parameters.speed = parseInt( $( '#speedRange' ).val() );
    synthesisObject.parameters.text = $( '#textInputTextarea' ).val();
    synthesisObject.parameters.voice = $( '#voiceSelectContainer' ).val();
    synthesisObject.parameters.emotion = $( '#emotionSelectContainer' ).val();

    activateControlPanelWaiting();

    getSynthesis();

}
    
function activateControlPanelWaiting() {

    $( '#prepareButton' ).hide();
    $( '#controlsInnerContainerCover' ).show();

}

function hideControlPanelWaiting() {

    $( '#controlsInnerContainerCover' ).hide();
    $( '#speakButton' ).show();

}

function getSynthesis() {
    let data = {
        'pitch': synthesisObject.parameters.pitch,
        'voice': synthesisObject.parameters.voice,
        'emotion': synthesisObject.parameters.emotion,
        'text': synthesisObject.parameters.text
    }
    let JSONData = JSON.stringify( data )
    sendAjax( "get_speech_synthesis", "GET", JSONData, 10000, getSynthesisResponse, true, "application/json; charset=utf-8" )

}

function getSynthesisResponse( msg, success ) {

    console.log( 'success msg:', msg )
    synthesisObject.url = msg.url;
    synthesisObject.visemes = JSON.parse( msg.visemes );
    prepareToSpeak();

}

var visemes = [ 'f', 'th', 'b', 't', 's',  'k', 'w', 'r', 'l', 'u', 'e', 'i' ]
function createTempVisemePoses() {

    console.log('in createTempVisemePoses')
    visemes.forEach( function (v) {

        expressionObject.abs.visemes[ v + 'Temp' ] = createCalculatedExpression( [expressionObject.rel.visemes[ v ], expressionObject.rel.visemes[ v + 'Emp' ] ], 1 - ( synthesisObject.parameters.emphasis / 100 ), 1, 0)[ 0 ]
        expressionObject.abs.visemes[ v + 'Temp' ].name = v + 'Temp';

    });
    //getAbsoluteCoordsOfVisemes(); // gets coordinates for all main expressions

}

//function csrfSafeMethod(method) {

    //return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
//}

//function getCookie(name) {
    //var cookieValue = null;
    //if (document.cookie && document.cookie !== '') {
        //var cookies = document.cookie.split(';');
        //for (var i = 0; i < cookies.length; i++) {
            //var cookie = cookies[i].trim();
            //// Does this cookie string begin with the name we want?
            //if (cookie.substring(0, name.length + 1) === (name + '=')) {
                //cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                //break;
            //}
        //}
    //}
    //return cookieValue;
//}
//var csrftoken = getCookie('csrftoken');

//$.ajaxSetup({
    //crossDomain: false,
    //beforeSend: function(xhr, settings) {
        //if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            //xhr.setRequestHeader("X-CSRFToken", csrftoken);
        //}
    //}
//});


