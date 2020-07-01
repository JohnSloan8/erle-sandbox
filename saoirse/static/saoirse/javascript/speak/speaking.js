function prepareToSpeak() {

    synthesisObject.audio.src = prefixURL + 'media/' + synthesisObject.url;
    synthesisObject.audio.load();
    synthesisObject.checkIfLoadedCount = 0;
    checkIfLoaded()

}

function setSpeakEvent() {

    $( '#speakButton' ).click( playAudio );

}

function checkIfLoaded() {

    //console.trace()
    if ( synthesisObject.audio.readyState === 4 ) {

        hideControlPanelWaiting();

    } else {

        if ( synthesisObject.checkIfLoadedCount < 8 ) {

            synthesisObject.checkIfLoadedCount += 1;
            setTimeout( checkIfLoaded, 1000 );

        } else {

            alert( 'your internet connection may be too slow to play audio' );

        }

    }

}

function playAudio() {

    $( '#controlsInnerContainerCover' ).text('');
    activateControlPanelWaiting();
    if ( controllerObject.randomTilt.bool ) {

        prepareHeadBobAndTalkingBoolOnFirstSentence();

    }
    synthesisObject.audio.playbackRate = 0.5  + synthesisObject.parameters.speed / 100;
    let dur = synthesisObject.audio.duration
    synthesisObject.noOfFrames = Math.floor( dur * 60 )
    synthesisObject.noOfPhones = synthesisObject.visemes.length;
    synthesisObject.audio.onplay = speak();
    synthesisObject.audio.play();

}

function prepareHeadBobAndTalkingBoolOnFirstSentence() {

    randomTiltHeadControllerObject.newTilt = true;
    synthesisObject.talking = true; 
    headXRandomTiltObject.startCount = mainCount;
    headYRandomTiltObject.startCount = mainCount;

}

function speak() {
    
    synthesisObject.phoneCount = 0;
    synthesisObject.visemeOverrun = 0;
    animatePhonesInOrder();

}

function animatePhonesInOrder() {

    if ( synthesisObject.phoneCount < synthesisObject.noOfPhones ) {

        pronunciationController( expressionObject.abs.visemes[ synthesisObject.visemes[ synthesisObject.phoneCount ][ 'Viseme' ] ], synthesisObject.visemes[ synthesisObject.phoneCount ][ 'end' ], function() {
            
            if ( isAudioFinished() ) { // stops phone animation ate end of audio when it is running slow

                endAnimatePhonesInOrder();

            } else {

                synthesisObject.phoneCount += 1;
                animatePhonesInOrder();

            }
                
        })

    } else if ( synthesisObject.phoneCount === synthesisObject.noOfPhones ) { 
        
        let finalMoveTime = 0.5 + ( 0.5 - ( synthesisObject.parameters.speed / 200 ) )
        console.log('finalMoveTime:', finalMoveTime);
        expressionController( expressionObject.calculated, finalMoveTime )
        checkIfAudioIsFinished();
    
    }

}

function isAudioFinished() {

    if ( synthesisObject.audio.paused ) {
    
        return true;

    } else {

        return false;

    }

}

var checkAudioFinishedCount = 0;
function checkIfAudioIsFinished() {

    let finished = isAudioFinished();

    if ( finished ) {

        checkAudioFinishedCount = 0;
        endAnimatePhonesInOrder();

    } else {

        if ( checkAudioFinishedCount < 20 ) {

            checkAudioFinishedCount += 1;
            setTimeout( checkIfAudioIsFinished, 200 );

        } else {

            checkAudioFinishedCount = 0;
            endAnimatePhonesInOrder();

        }

    }

}

function endAnimatePhonesInOrder() {

    synthesisObject.talking = false;
    randomTiltHeadControllerObject.newTilt = false;
    hideControlPanelWaiting();
    $( '#controlsInnerContainerCover' ).text('loading...');


}

function pronunciationController( expressionTo, phoneEndTime, cb ) {
    //console.log('expressionTO:', expressionTo)
    //let weightedPhoneEndTime = phoneEndTime / 0.9;
    //console.log('weightedPhoneEndTime 0:', weightedPhoneEndTime)
    let weightedPhoneEndTime = phoneEndTime / synthesisObject.audio.playbackRate;
    //console.log('weightedPhoneEndTime 1:',weightedPhoneEndTime)
    //console.log('in pronunciation controller')
    //console.log( 'phoneEndTime:', phoneEndTime );
    //console.log( 'phonneCount:', synthesisObject.phoneCount );
    expressionObject.bool = false;//if other expression delayed, just stop it before calculating absolute position
    expressionObject.now = getAbsoluteCoordsOfExpressionNow();
    expressionObject.movement = createRelativeExpression( expressionTo );
    expressionObject.callback = cb;
    
    let phoneLength;
    if ( synthesisObject.phoneCount === 0 ) {
    
        phoneLength = weightedPhoneEndTime
    
    } else {

        phoneLength = weightedPhoneEndTime - synthesisObject.previousWeightedPhoneEndTime;

    }
    
    //console.log( 'phoneLength:', phoneLength );
    synthesisObject.previousWeightedPhoneEndTime = weightedPhoneEndTime;
    
    let frames = Math.round( phoneLength * 6 ) / 100;
    //console.log( 'frames:', frames );
    let framesPlusOverrun = Math.round( phoneLength * 6 - 100 * synthesisObject.visemeOverrun ) / 100;
    //console.log( 'framesPlusOverrun:', framesPlusOverrun );
    let decimals = Math.round( 100 * ( framesPlusOverrun % 1 ) ) / 100;
    //console.log( 'decimals:', decimals );
    let overrun = 0;
    if ( decimals < 0.5 ) {
        overrun = decimals;
    } else {
        overrun = - Math.round( 100 * ( Math.abs( 1 - decimals ) ) ) / 100;
    }
    //console.log( 'overrun:', overrun );
    synthesisObject.visemeOverrun = overrun;

    let roundedFrames = Math.round( framesPlusOverrun );
    //console.log( 'roundedFames:', roundedFrames );
    expressionObject.sinLength = roundedFrames; 
    //console.log( 'sinLength:', expressionObject.sinLength );
    expressionObject.sin = sineArrays[ expressionObject.sinLength ];
    expressionObject.startCount = mainCount;
    expressionObject.bool = true;

}

