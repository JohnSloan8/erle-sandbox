var tiaObject = {
    'faceBones': {},
    'bodyBones': {},
    'eyeBones': {},
    'mouthBones': {}
};

function MoveObj() {

    this.neutralCoords = [[0,0,0],[0,0,0]];
    this.currentCoords = [[0,0,0],[0,0,0]];
    this.movementCoords = [[0,0,0],[0,0,0]];
    this.bool = false;
    this.dir = 1;
    this.startCount = 0;
    this.sin = [];
    this.sinLengh = 0;

}

var eyeObject = new MoveObj();
eyeObject.name = 'eye'

var eyelidObject = new MoveObj();
eyelidObject.coords = {
    close: 1,
    beforeBlinkUpper: 0,
    beforeBlinkLower: 0,
    currentUpper: 0,
    currentLower: 0,
    movementUpper: 0,
    movementLower: 0
}

var controllerObject = {
    'blink': {
        'bool': false,
        'nextBlinkCount': 60,//frames until next blink. set at 60 for first but random afterward 
    },
    'randomTilt': {
        'bool': false,
    }
}

var blinkObject = {
    'bool': false,
    'countdown': 15,
}

//var tiltControllerObject = {
    //'bool': false,
//}

var spineRandomTiltObject = {
    'startCount': 0,
    'sin': sineArrays[ '120' ],
    'sinLength': 120,
    'mult': 0.3, 
    'direction': Math.random() < 0.5 ? -1 : 1,
    // call the sway to and fro
    'to': true,
    'name': 'spineTilt',
}

var neckRandomTiltObject = {
    'startCount': 0,
    'sin': sineArrays[ '180' ],
    'sinLength': 180,
    'mult': 0.2, 
    'direction': Math.random() < 0.5 ? -1 : 1,
    // call the sway to and fro
    'to': true,
    'name': 'neckTilt',
}

var headRandomWobbleObject = {
    'startCount': 0,
    'sin': sineArrays[ '120' ],
    'sinLength': 120,
    'mult': 2, 
    'direction': Math.random() < 0.5 ? -1 : 1,
    // call the sway to and fro
    'to': true,
    'name': 'headWobble',
}

var headXRandomTiltObject = {
    'startCount': 0,
    'sin': sineArrays[ 120 ],
    'sinLength': 120,
    'mult': 0.75, 
    'direction': Math.random() < 0.5 ? -1 : 1,
    // call the sway to and fro
    'to': true,
    'name': 'headXTilt',
}

var headYRandomTiltObject = {
    'startCount': 0,
    'sin': sineArrays[ 90 ],
    'sinLength': 90,
    'mult': 0.75,
    'direction': Math.random() < 0.5 ? -1 : 1,
    // call the sway to and fro
    'to': true,
    'name': 'headYTilt',
}

//var nodObject = {
    //'bool': false,
    //'startCount': 0,
    //'sin': [ ],
    //'sinLength': 0,
    //'amount': 0,
    //'decay': [ 0.3, -0.35, 0.3, -0.275, 0.2, -0.175 ],
    //'iter': 0,
//};

//var shakeObject = {
    //'bool': false,
    //'startCount': 0,
    //'sin': [ ],
    //'sinLength': 0,
    //'amount': 0,
    //'decay': [ 0.2, -0.4, 0.35, -0.3, 0.225, -0.075 ],
    //'iter': 0,
//};

//var talkObject = {
    //bool: false,
//}

//var mouthingObject = {

    //wordNo: 0,
    //mouthing: false,
    //phoneCount: 0,
    //noOfPhones: 0,
    //emphasis: false, // if emphasis on Noun or Verb so slower and raised eyebrows n had movement

//}

var synthesisObject = {
    //finalTextInBox : "blank",
    //text: "",
    audio: null,
    audioS3: null,// dom element added in <load_scene/main.js>
    sentenceNo: 0, //if multiple sentences it will start at first, iterates in <tiaSpeech.js>
    talking: false,
    pitch: 0,
    //speaking_rate: 0.70,
    //continuous: true,
    firstClip: false,
    now: {}, 
    stockPhrases: {},
    data: {
        'prompt': {
            'URLs': [],
            'texts': [],
            'visemes': [],
        }
    },
}
