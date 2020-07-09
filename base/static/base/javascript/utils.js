var prefixURL;
function definePrefixURL() {

    if ( inDevelopment ) {

        prefixURL = "http://127.0.0.1:8000/"

    } else {

        prefixURL = "https://erle-sandbox.ucd.ie/"

    }

}


