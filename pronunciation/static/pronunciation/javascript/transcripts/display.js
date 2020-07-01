function displayTranscript() {

    console.log('in displayTranscript');
    $( '#transcriptionInnerContainer' ).empty();

    if ( audioVariables.transcript.length !== 0 ) {

        $( '#transcriptionContainer' ).show();
        let lastIndex = audioVariables.transcript.length - 1;
        audioVariables.transcript.forEach( function( w, i ) {

            let suffix = ''
            if ( i !== lastIndex ) { suffix = '<!--' }

            let spaceIndex = 2 * i;
            let wordIndex = spaceIndex + 1;

            $( '#transcriptionInnerContainer' ).append(

                '<div class="transcription-word-space-container">' +

                    '<div class="transcription-word-space-inner-container" id="transcriptionWord' + spaceIndex.toString() + '">&nbsp</div>' +

                '</div><!--' + 

                '--><div class="transcription-word-space-container">' +

                    '<div class="transcription-word-space-inner-container" id="transcriptionWord' + wordIndex.toString() + '">' + w.word + '</div>' +

                '</div>' + suffix 

            )

        });

        $( '#transcriptionInnerContainer' ).append(

            '<div class="transcription-word-space-container">' +

                '<div class="transcription-word-space-inner-container" id="transcriptionWord' + ( lastIndex * 2 + 2 ).toString() + '">&nbsp</div>' +

            '</div><!--' 

        );

        resetTapWordEvents();

    } else {

        $( '#transcriptionContainer' ).hide();
        displayButtons( 'bottom', [ 'microphone' ] );

    }

    resetIntegersStartFinish();

}
