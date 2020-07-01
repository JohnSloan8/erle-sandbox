var controlPanel = {
    'width': 260,
    'controls':  {
        'expression': {
            'type': 'wheel',
        },
        'surprise': {
            'type': 'slider',
            'value': '0',
        },
        'rotation': {
            'type': 'slider',
            'value': '50',
        },
        'lean': {
            'type': 'slider',
            'value': '50',
        },
        'tilt': {
            'type': 'slider',
            'value': '50',
        },
        'emphasis': {
            'type': 'slider',
            'value': '0',
        },
        'pitch': {
            'type': 'slider',
            'value': '50',
        },
        'speed': {
            'type': 'slider',
            'value': '50',
        },
        'randomTilt': {
            'type': 'radio',
        },
        'blink': {
            'type': 'radio',
        },
        'voice': {
            'type': 'dropdown',
            'options': voices,
        },
        'emotion': {
            'type': 'dropdown',
            'options': [ 'neutral', 'happy', 'sad', 'calm', 'cross' ],
        },
        'sentence': {
            'type': 'textarea',
        },
        'prepare': {
            'type': 'button',
        },
        'speak': {
            'type': 'button',
        },
        'reset': {
            'type': 'button',
        },
    },
    'dropdown': {
        'height': '34px',
    },
    'slider': {
        'height': '24px',
    },
    'radio': {
        'height': '24px',
    },
    'textarea': {
        'height': '80px',
    },
    'button': {
        'height': '30px',
    },
}

function loadControlPanel() {

    $( '#controlsInnerContainer' ).width( controlPanel.width );
    insertPanel( 'expression' );
    insertPanel( 'surprise' );
    insertPanel( 'rotation' );
    insertPanel( 'lean' );
    insertPanel( 'tilt' );
    insertPanel( 'randomTilt' );
    insertPanel( 'blink' );
    insertPanel( 'emphasis' );
    insertPanel( 'speed' );
    insertPanel( 'voice' );
    insertPanel( 'emotion' );
    insertPanel( 'pitch' );
    insertPanel( 'sentence' );
    insertPanel( 'prepare' );
    insertPanel( 'speak' );
    insertPanel( 'reset' );
    insertCover();
    showPrepareButtonOnVoiceChanges();

}

function insertPanel( panel ) {

    console.log( 'panel:', panel );
    if ( controlPanel.controls[ panel ].type === 'slider' ) {

        insertSlider( panel );

    } else if ( controlPanel.controls[ panel ].type === 'radio' ) {

        insertRadio( panel );

    } else if ( controlPanel.controls[ panel ].type === 'dropdown' ) {

        insertDropdown( panel );

    } else if ( controlPanel.controls[ panel ].type === 'wheel' ) {
        
        insertWheel();

    } else if ( controlPanel.controls[ panel ].type === 'textarea' ) {
        
        insertTextarea();

    } else if ( controlPanel.controls[ panel ].type === 'button' ) {

        insertButton( panel );

    }

}

function insertSlider( panel_ ) {

    $( '#controlsInnerContainer' ).append(
        '<div class="single-control-container" id="' + panel_ + 'ControlContainer">' +
            '<div class="erle-row-third" id="' + panel_ + 'NameContainer">' + 
                '<div class="erle-inner-container erle-center">' + panel_ + '</div>' +
            '</div>' +
            '<div class="erle-row-two-thirds slider-container" id="' + panel_ + 'SliderContainer">' +
                '<div class="erle-inner-container erle-center">' +
                    '<input type="range" min="0" max="100" value="' + controlPanel.controls[ panel_ ].value + '" id="' + panel_ + 'Range">' +
                '</div>' +
            '</div>' +
        '</div>'
    )

    $( '#' + panel_ + 'ControlContainer' ).height( controlPanel.slider.height );
    $('#' + panel_ + 'Range').on('change', dealWithSliderEvents )

}

function dealWithSliderEvents() {

    console.log('dealWithSliderEvents')
    if ( this.id === 'surpriseRange' ) {

        initSurpriseEvent( this.value );

    } else if ( this.id === 'rotationRange' ) {

        initRotationEvent( this.value );

    } else if ( this.id === 'leanRange' ) {

        initLeanEvent( this.value );

    } else if ( this.id === 'tiltRange' ) {

        initTiltEvent( this.value );

    } else if ( this.id === 'pitchRange' ) {

        prepareAgain();
    
    } else if ( this.id === 'emphasisRange' ) {
    
        synthesisObject.parameters.emphasis = parseInt( this.value );
        createTempVisemePoses();
    
    } else if ( this.id === 'speedRange' ) {
    
        synthesisObject.parameters.speed = parseInt( this.value );
    
    }

}

function insertRadio( panel_ ) {

    $( '#controlsInnerContainer' ).append( 
        '<div class="single-control-container" id="' + panel_ + 'ControlContainer">' +
            '<div class="erle-row-third" id="' + panel_ + 'NameContainer">' + 
                '<div class="erle-inner-container erle-center">' + panel_ + '</div>' +
            '</div>' +
            '<div class="erle-row-two-thirds" id="' + panel_ + 'RadioContainer">' +
                '<div class="erle-inner-container erle-center">' +
                    '<input type="checkbox" id="' + panel_ + 'Checkbox">' +
                '</div>' +
            '</div>' +
        '</div>'
    )

    $( '#' + panel_ + 'ControlContainer' ).height( controlPanel.radio.height );
    insertRadioControl( panel_ );
            
}

function insertDropdown( panel_ ) {

    let selectDropdownHTML = createSelectDropdownHTML();
    
    $( '#controlsInnerContainer' ).append(
        '<div class="single-control-container" id="' + panel_ + 'ControlContainer">' +
            '<div class="erle-row-third" id="' + panel_ + 'NameContainer">' + 
                '<div class="erle-inner-container erle-center">' + panel_ + '</div>' +
            '</div>' +
            '<div class="erle-row-two-thirds slider-container" id="' + panel_ + 'SliderContainer">' +
                '<div class="erle-inner-container erle-center">' +
                    selectDropdownHTML +
                '</div>' +
            '</div>' +
        '</div>'
    )

    $( '#' + panel_ + 'ControlContainer' ).height( controlPanel.dropdown.height );

    function createSelectDropdownHTML() {

        let selectHTML = '<select id="' + panel_ + 'SelectContainer">'
            
        controlPanel.controls[ panel_ ].options.forEach( function( p ) {
            
            selectHTML += '<option value="' + p + '">' + p + '</option>'

        })
        
        selectHTML += '</select>'

        return selectHTML

    }

}
        
function insertWheel() {

    $( '#controlsInnerContainer' ).append(
        '<div class="single-control-container" id="expressionControlContainer">' +
            '<div class="erle-inner-container erle-center">' +
                '<div id="emotionWheelCont">' +
                    '<div id="emotionWheel"></div>' +
                    '<img src="' + happyEmojiURL + '" id="happyLabel" class="emotion-labels">' +
                    '<img src="' + disgustEmojiURL + '" id="disgustLabel" class="emotion-labels">' +
                    '<img src="' + fearEmojiURL + '" id="fearLabel" class="emotion-labels">' +
                    '<img src="' + sadEmojiURL + '" id="sadLabel" class="emotion-labels">' +
                    '<img src="' + contentEmojiURL + '" id="contentLabel" class="emotion-labels">' +
                    '<div id="emotionClickedLocation"></div>' +
                '</div>' +
            '</div>' +
        '</div>'
    );

    $( '#expressionControlContainer' ).height( controlPanel.width );
    initEmotionWheelEvents();

}

function insertTextarea() {

    $( '#controlsInnerContainer' ).append( 
        '<div class="single-control-container" id="sentenceControlContainer">' +
            '<div class="erle-col-quarter">' +
                '<div class="erle-inner-container erle-center">sentence</div>' +
            '</div>' +
            '<div class="erle-col-three-quarters">' +
                '<div class="erle-inner-container erle-center">' +
                    '<textarea rows="3" maxlength="83" class="erle-textarea" id="textInputTextarea"></textarea>' +
                '</div>' +
            '</div>' +
        '</div>'
    );

    synthesisObject.parameters.emphasis = 0;
    synthesisObject.parameters.pitch = 50;
    synthesisObject.parameters.speed = 50;
    synthesisObject.parameters.text = "Hello there, nice to meet you. My name is Saoirse, and I'm an expressive avatar";
    synthesisObject.parameters.voice = "Irish";
    synthesisObject.parameters.emotion = "neutral";
    synthesisObject.synthesisObject = "neutral";
    synthesisObject.audio.src = prefixURL + "media/synthesisedSpeech/Irish-neutral-50-Hello_there,_nice_to_meet_you._My_name_is_Saoirse,_and_I'm_an_expressive_avatar.mp3";
    synthesisObject.visemes = [{"name": "h", "start": 900, "end": 1030, "Viseme": "eTemp", "stress": "0"}, {"name": "e", "start": 1030, "end": 1080, "Viseme": "eTemp", "stress": "0"}, {"name": "l", "start": 1080, "end": 1140, "Viseme": "lTemp", "stress": "0"}, {"name": "ou", "start": 1140, "end": 1340, "Viseme": "eTemp", "stress": "1"}, {"name": "dh", "start": 1340, "end": 1420, "Viseme": "thTemp", "stress": "0"}, {"name": "e", "start": 1420, "end": 1590, "Viseme": "eTemp", "stress": "1"}, {"name": "r", "start": 1590, "end": 1790, "Viseme": "rTemp", "stress": "0"}, {"name": "n", "start": 1990, "end": 2070, "Viseme": "tTemp", "stress": "0"}, {"name": "ai", "start": 2070, "end": 2200, "Viseme": "eTemp", "stress": "1"}, {"name": "s", "start": 2200, "end": 2320, "Viseme": "sTemp", "stress": "0"}, {"name": "t", "start": 2320, "end": 2400, "Viseme": "tTemp", "stress": "0"}, {"name": "@", "start": 2400, "end": 2440, "Viseme": "eTemp", "stress": "0"}, {"name": "m", "start": 2440, "end": 2510, "Viseme": "bTemp", "stress": "0"}, {"name": "ii", "start": 2510, "end": 2610, "Viseme": "eTemp", "stress": "1"}, {"name": "t", "start": 2610, "end": 2699, "Viseme": "tTemp", "stress": "0"}, {"name": "y", "start": 2699, "end": 2769, "Viseme": "eTemp", "stress": "0"}, {"name": "uu", "start": 2769, "end": 2879, "Viseme": "uTemp", "stress": "1"}, {"name": "m", "start": 3280, "end": 3400, "Viseme": "bTemp", "stress": "0"}, {"name": "ai", "start": 3400, "end": 3499, "Viseme": "eTemp", "stress": "1"}, {"name": "n", "start": 3499, "end": 3589, "Viseme": "tTemp", "stress": "0"}, {"name": "ei", "start": 3589, "end": 3799, "Viseme": "eTemp", "stress": "1"}, {"name": "m", "start": 3799, "end": 3879, "Viseme": "bTemp", "stress": "0"}, {"name": "i", "start": 3879, "end": 3929, "Viseme": "eTemp", "stress": "0"}, {"name": "z", "start": 3929, "end": 4019, "Viseme": "sTemp", "stress": "0"}, {"name": "s", "start": 4019, "end": 4139, "Viseme": "sTemp", "stress": "0"}, {"name": "ii", "start": 4139, "end": 4269, "Viseme": "eTemp", "stress": "1"}, {"name": "r", "start": 4269, "end": 4329, "Viseme": "rTemp", "stress": "0"}, {"name": "sh", "start": 4329, "end": 4479, "Viseme": "sTemp", "stress": "0"}, {"name": "@", "start": 4479, "end": 4649, "Viseme": "eTemp", "stress": "0"}, {"name": "a", "start": 4849, "end": 4989, "Viseme": "eTemp", "stress": "1"}, {"name": "n", "start": 4989, "end": 5049, "Viseme": "tTemp", "stress": "0"}, {"name": "d", "start": 5049, "end": 5089, "Viseme": "tTemp", "stress": "0"}, {"name": "ai", "start": 5089, "end": 5239, "Viseme": "eTemp", "stress": "1"}, {"name": "m", "start": 5239, "end": 5309, "Viseme": "bTemp", "stress": "0"}, {"name": "@", "start": 5309, "end": 5349, "Viseme": "eTemp", "stress": "0"}, {"name": "n", "start": 5349, "end": 5399, "Viseme": "tTemp", "stress": "0"}, {"name": "i", "start": 5399, "end": 5439, "Viseme": "eTemp", "stress": "0"}, {"name": "k", "start": 5439, "end": 5519, "Viseme": "kTemp", "stress": "0"}, {"name": "s", "start": 5519, "end": 5578, "Viseme": "sTemp", "stress": "0"}, {"name": "p", "start": 5578, "end": 5638, "Viseme": "bTemp", "stress": "0"}, {"name": "r", "start": 5638, "end": 5688, "Viseme": "rTemp", "stress": "0"}, {"name": "e", "start": 5688, "end": 5778, "Viseme": "eTemp", "stress": "1"}, {"name": "s", "start": 5778, "end": 5868, "Viseme": "sTemp", "stress": "0"}, {"name": "i", "start": 5868, "end": 5908, "Viseme": "eTemp", "stress": "0"}, {"name": "v", "start": 5908, "end": 5988, "Viseme": "fTemp", "stress": "0"}, {"name": "a", "start": 5988, "end": 6108, "Viseme": "eTemp", "stress": "1"}, {"name": "v", "start": 6108, "end": 6188, "Viseme": "fTemp", "stress": "0"}, {"name": "@", "start": 6188, "end": 6238, "Viseme": "eTemp", "stress": "0"}, {"name": "t", "start": 6238, "end": 6338, "Viseme": "tTemp", "stress": "0"}, {"name": "aa", "start": 6338, "end": 6478, "Viseme": "eTemp", "stress": "2"}, {"name": "r", "start": 6478, "end": 6608, "Viseme": "rTemp", "stress": "0"}]

    $( '#sentenceControlContainer' ).height( controlPanel.textarea.height );
    $( '#textInputTextarea' ).on( 'keyup', textInputEvent );
    $( '#textInputTextarea' ).val( "Hello there, nice to meet you. My name is Saoirse, and I'm an expressive avatar" )

}

function textInputEvent() {

    if ( $( '#textInputTextarea' ).val() !== '' ) {

        $( '#prepareButton' ).show();

    } else {

        $( '#prepareButton' ).hide();

    }

    $( '#speakButton' ).hide();

}

function insertButton( panel_ ) {

    $( '#controlsInnerContainer' ).append(
        '<div class="single-control-container" id="' + panel_ + 'ControlContainer">' +
            '<div class="erle-inner-container erle-center">' +
                '<button type="button" id="' + panel_ + 'Button">' + panel_ + '</button>' + 
             '</div>' +
         '</div>'
    );

    $( '#' + panel_ + 'ControlContainer' ).height( controlPanel.dropdown.height );
    insertButtonControl( panel_ );

}

function insertRadioControl( panel_ ) {
    
    console.log('insertRadioControl')
    $( '#' + panel_ + 'Checkbox' ).prop( 'checked', true );
    if ( panel_ === "randomTilt" ) {

        tiltControllerObject.newTilt = true;

    }
    controllerObject[ panel_ ].bool = true;

    $( '#' + panel_ + 'Checkbox' ).click( function() {
    
        if ( this.checked ) {

            if ( panel_ === "randomTilt" ) {

                tiltControllerObject.newTilt = true;

            }
        
            controllerObject[ panel_ ].bool = true;

        } else {
            
            controllerObject[ panel_ ].bool = false;
        
        }

    });

}

function insertButtonControl( panel_ ) {

    if ( panel_ === 'prepare' ) {

        setPrepareButtonEvent();

    } else if ( panel_ === 'reset' ) {

        setResetEvent();

    } else if ( panel_ === 'speak' ) {

        setSpeakEvent();

    }

}

function insertCover() {

    let height = $( '#controlsInnerContainer' ).height().toString();
    let width = controlPanel.width.toString();
    let top = $( '#controlsContainer' ).css( 'padding' );

    $( '#controlsInnerContainerCover' ).css( {

        'width': width,
        'height': height,
        'position': 'absolute',
        'top': top,
        'background-color': 'rgba(255, 255, 255, 0.5)',
        'font-size': '3vw',
        'display': 'none'

    });

}

function showPrepareButtonOnVoiceChanges() {

    let emotion = document.getElementById("emotionSelectContainer");
    let voice = document.getElementById("voiceSelectContainer");

    emotion.addEventListener('change', prepareAgain );
    voice.addEventListener('change', prepareAgain );

}

function prepareAgain() {

    $( '#speakButton' ).hide();
    textInputEvent();

}

