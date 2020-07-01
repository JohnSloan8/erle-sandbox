var SINEARRAYFRAMES = [];
var sineArrays = {};
//var quickTurnaroundSineArrays = {};// for nodding

for ( let i=0; i<601; i++ ){
    
    SINEARRAYFRAMES.push(i);

}

function sinCalc(amount, total_frames, this_frame) {
    return (amount / total_frames) * Math.sin((2 * Math.PI * this_frame / total_frames) - Math.PI / 2) + (amount / total_frames);
}

//function sinCalcQuickTurnaround(amount, total_frames, this_frame) {
    //return (amount / total_frames) * Math.sin(Math.PI * this_frame / total_frames);
//}

for ( let frames of SINEARRAYFRAMES ) {

    let singleSineArray = [];
    //let singleQuickTurnaroundSineArray = [];
    let sumOfArraySoFar = 0;

    for ( let i=0; i<frames; i++ ) {

        sinCalcResult = sinCalc( 1, frames, i )
        //quickTurnaroundSinCalcResult = sinCalcQuickTurnaround( 1, frames, i )

        sumOfArraySoFar += sinCalcResult;

        singleSineArray.push( sinCalcResult );  
        //singleQuickTurnaroundSineArray.push( quickTurnaroundSinCalcResult );  

    }

    sineArrays[ frames.toString() ] = singleSineArray;
    //quickTurnaroundSineArrays[ frames.toString() ] = singleQuickTurnaroundSineArray;

};

function secsToFrames( secs ) {

    let frames =  Math.max( 1, Math.floor( secs * 60 ) );

    return frames;

}

function assignSinArrayForSpeed( secs, object, sArrays ) {

    // get no of frames from the seconds input
    let frames = secsToFrames( secs );
    object.sin = sArrays[ frames ];
    object.sinLength = object.sin.length;
    
}


