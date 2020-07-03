function activateKeyboard() {

    resetTypedString();
    displayButtons( 'top', [] );
    displayButtons( 'bottom', [] );
    setWordsToViewMode();
    $('#transcriptionContainer').animate({top: '-100%', bottom: '100%'}, 300, function(){ $('#keyboardTextBoxContainer').show() });

}

function exitKeyboard( cb=function(){} ) {

    $('#keyboardTextBoxContainer').hide()
    $('#transcriptionContainer').animate({top: '0%', bottom: '150px'}, 300, function(){ 
        
        cb();

    });

}

let lightBlueHexColor = '#d1d2ff'
function setWordsToViewMode( clearSelection=false ) {

    $( '.transcription-word-space-inner-container' ).off( 'click' );
    $( '.transcription-word-space-inner-container' ).css( 'opacity', '0.3' );

    if ( clearSelection ) {

        $( '.transcription-word-space-inner-container' ).css({
            'background-color': 'white',
            'color': 'black'
        });

        integersStartFinish = [];

    } else {

        integersStartFinish = getOnlyWordIntegers();
        let spaceBefore = integersStartFinish[ 0 ] - 1;
        let spaceAfter = integersStartFinish[ 1 ] + 1;
        $( '#transcriptionWord' + spaceBefore.toString() ).css( 'background-color', lightBlueHexColor );
        $( '#transcriptionWord' + spaceAfter.toString() ).css( 'background-color', lightBlueHexColor );

        for( let i = integersStartFinish[ 0 ]; i <= integersStartFinish[ 1 ]; i++ ) {

            $('#transcriptionWord' + i.toString() ).css( 'opacity', '1' )

        }

    }

}

function getOnlyWordIntegers() {

    let tempIntegerStart = integersStartFinish[ 0 ];
    let tempIntegerFinish = integersStartFinish[ 1 ];
    if ( integersStartFinish[ 0 ] !== integersStartFinish[ 1 ] ) {

        if ( integersStartFinish[ 0 ] % 2 === 0 ) {

            tempIntegerStart = integersStartFinish[ 0 ] + 1;

        }

        if ( integersStartFinish[ 1 ] % 2 === 0 ) {

            tempIntegerFinish = integersStartFinish[ 1 ] - 1;

        }

    }

    return [ tempIntegerStart, tempIntegerFinish ]

}

function setWordsToEditMode() {

    resetTapWordEvents();
    $( '.transcription-word-space-inner-container' ).css( 'opacity', '1' );

}

const keyboardLayout = [['q','w','e','r','t','y','u','i','o','p','delete'],['a','s','d','f','g','h','j','k','l',"'"], ['z','x','c','v','b','n','m'],['space']]

function addKeys() {
  
	keyboardLayout.forEach( function( row, ind ){

		$('#keyboardContainer').append(
		  
			'<div class="erle-col-quarter erle-center" id="keyboardButtonsRow' + ind.toString() + '"></div>'
		
		)
		
		row.forEach( function( letter ) {
			
			$('#keyboardButtonsRow' + ind.toString()).append(
				
				'<div class="letter-container" id="letter' + letter.toUpperCase() + '"><div class="letter-inner-container erle-center" id="letterInner' + letter.toUpperCase() + '">' + letter + '</div></div>'
			
			)
		
		})
	
	})

    $('#letterInnerDELETE').html('&#11013;');
    $('#letterInnerSPACE').html('');

	$('#keyboardButtonsRow3').append(
		
		'<div id="letterCANCEL" class="letter-container"><div class="letter-inner-container erle-center" id="letterInnerCANCEL">&#11015;</div></div>' +
		'<div id="letterENTER" class="letter-container"><div class="letter-inner-container erle-center" id="letterInnerENTER">&#8626;</div></div>'
	
	)

	$('.letter-inner-container').click(letterTapped)

}

addKeys();

var typedString = "";

function letterTapped() {

	let letter = this.id.slice(11);
	if ( letter.length === 1 ) {
		
		if ( letter === "'") {
			
			if ( typedString[ typedString.length - 1 ] !== "'" && typedString.length !== 0 && typedString[ typedString.length - 1 ] !== " " ) {
				
				typedString += letter;
			
			}
		
		} else {
			
			typedString += letter.toLowerCase();
		
		}
	
	} else {
		
		if ( letter === 'SPACE') {
	  		
			if ( typedString[ typedString.length - 1 ] !== ' ' && typedString.length !== 0 ) {
		
				typedString += ' ';
	  
			}
	
		} else if ( letter === 'DELETE') {
	  
			typedString = typedString.slice(0, typedString.length - 1);

		} else if ( letter === 'ENTER') {
	  
			submitTypedString();
	
		} else if ( letter === 'CANCEL') {
	  
			exitKeyboard( function() {
            
                setWordsToEditMode();
                displayAppropriateTopButtons();
                displayButtons( 'bottom', [ 'ear', 'microphone', 'play' ] );
            
            } );

            resetTypedString();
	
		}
	
	}
	
	$('#textBoxContainer').text(typedString)

}

function resetTypedString() {

  	typedString = '';
	$('#textBoxContainer').text('')

}

function submitTypedString() {
  
    if ( typedString !== '' ) {

        let transcriptIndexesToBeDeleted = getIndexesToBeDeleted();
        setWordsToViewMode();
        displayButtons( 'top', [] )
        displayButtons( 'bottom', [''] )
        resetHighlightedTranscript()

        let dataToSend = {
            'typedString': typedString,
            'transcript': audioVariables.transcript,
            'indexesToBeDeleted': transcriptIndexesToBeDeleted,
            'integersStartFinish': integersStartFinish,
            'relativeFilename': audioVariables.relativeFilename,
            'ID': audioVariables.id,
            'count': audioVariables.count
        }
        let JSONData = JSON.stringify( dataToSend );
        audioVariables.modification = 'typed';
        
        exitKeyboard()
        sendAjax( "/pronunciation/store_typed_transcript_correction", "GET", JSONData, 10000, getModifiedVoiceAudio, true, "application/json; charset=utf-8" )

    }

}



//function afterSubmit() {

    //displayButtons( 'top', [] );
    //displayButtons( 'bottom', [ 'ear', 'microphone', 'play' ] );
    //displayTranscript();


//}

