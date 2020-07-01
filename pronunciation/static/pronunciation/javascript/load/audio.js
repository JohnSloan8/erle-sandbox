var audioVariables = {
    speechAudio: null,
    splicedSpeechAudio: null,
    stream: null,
    mediaRecorder: null,
    chunks: [],
}

function readyAudio() {

    // checks that user's browser allows microphone access
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        
        startAudioStream();
        audioVariables.speechAudio = document.getElementById( 'speechAudio' );
        audioVariables.fullSpeechAudio = document.getElementById( 'fullSpeechAudio' );

    } else {

        alert('getUserMedia not supported on your browser!');
    
    }

}

function startAudioStream() {

    navigator.mediaDevices.getUserMedia( { audio: true, video: false } ).then( function( stream ) {
 
        audioVariables.stream = stream;
        audioVariables.mediaRecorder = new MediaRecorder( audioVariables.stream );
        audioVariables.mediaRecorder.onerror = function( e ) {
            alert('mediaRecorder error:', e.error);
            location.reload();
        }

        audioVariables.mediaRecorder.ondataavailable = function( e ) {

            audioVariables.chunks.push( e.data );

        }

        audioVariables.mediaRecorder.onstop = onMediaRecorderStop;

        console.log('mediaRecorder created successfully')

    })

    .catch(function(err) {
        alert('The following getUserMedia error was caught: ' + err);
    });

}

function startRecording() {

    audioVariables.chunks = [];
    audioVariables.mediaRecorder.start();
    audioVariables.recording = true;
    audioVariables.over15secs = false;
    audioVariables.recorder15sTimeout = setTimeout( checkIfClickedStop, 14000 );

}

function checkIfClickedStop() {

    // double check the boolean is true
    if ( audioVariables.recording ) {

        audioVariables.over15secs = true;

        onStopClick();

    }

}

// put this in a function so that I can call it later if the user doesn't click stop after X seconds.
function stopRecording() {

    clearTimeout( audioVariables.recorder15sTimeout );

    audioVariables.mediaRecorder.stop();
    
}

function onMediaRecorderStop() {
 
    if ( audioVariables.over15secs ) {

        audioVariables.over15secs = false;

        alert( 'you have 15 seconds to say each sentence' );

    } else {

        audioVariables.blob = new Blob(audioVariables.chunks, { type : 'audio/mpeg' });

        sendBlobToServer( audioVariables.blob );

    }

}

function sendBlobToServer( blob_to_send ) {

    let fd = new FormData();
    fd.append('data', blob_to_send);
    sendFileAjax( "/pronunciation/store_blob", "POST", fd, 10000, getRecognitionResponse, false, false )

}

