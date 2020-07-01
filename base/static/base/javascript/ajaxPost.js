//function setCookie() {

    //// This function gets cookie with a given name
    //function getCookie(name) {
        //var cookieValue = null;
        //if (document.cookie && document.cookie != '') {
            //var cookies = document.cookie.split(';');
            //for (var i = 0; i < cookies.length; i++) {
                //var cookie = jQuery.trim(cookies[i]);
                //// Does this cookie string begin with the name we want?
                //if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    //cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    //break;
                //}
            //}
        //}
        //return cookieValue;
    //}
    //[>
    //The functions below will create a header with csrftoken
    //*/
    
    ////var csrftoken = getCookie('csrftoken');
    //var csrftoken = "A44sM0BWbxk67O2sx27mxmVgTbJovg2XbEIXmuTFRDClX23p54574OfPjcOvz1Sh"
    //console.log('csrftoken:', csrftoken)

    //function csrfSafeMethod(method) {
        //// these HTTP methods do not require CSRF protection
        //return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    //}
    //function sameOrigin(url) {
        //// test that a given url is a same-origin URL
        //// url could be relative or scheme relative or absolute
        //var host = document.location.host; // host + port
        //var protocol = document.location.protocol;
        //var sr_origin = '//' + host;
        //var origin = protocol + sr_origin;
        //// Allow absolute or scheme relative URLs to same origin
        //return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            //(url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            //// or any other URL that isn't scheme relative or absolute i.e relative.
            //!(/^(\/\/|http:|https:).*/.test(url));
    //}

    ////$.ajaxSetup({
        ////beforeSend: function(xhr, settings) {
            ////if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                ////// Send the token to same-origin, relative URLs only.
                ////// Send the token only if the method warrants CSRF protection
                ////// Using the CSRFToken value acquired earlier
                ////xhr.setRequestHeader("X-CSRFToken", csrftoken);
            ////}
        ////}
    ////});

//};

function sendAjax( url, type, JSONData, timeout, response, processData, contentType ) { 
    $.ajax({
        url: url,
        type: type,
        data: { 'JSONData': JSONData },
        processData: processData,
        contentType: contentType,
        timeout: timeout,
        success: function( JSONResponse ) { response( JSONResponse ) },
        error: function( e, jqXHR, ajaxSettings, thrownError ) {
            console.log(
                '----- ajax error -----' +
                '\n\nstatus: ', e.status,
                '\n\nstatusText: ', e.statusText,
                '\n\nresponseText: ', e.responseText,
                '\n\njqXHR: ', jqXHR,
                '\n\najaxSettings: ', ajaxSettings,
                '\n\nthrownError: ', thrownError,
                '\n\n\n'
            )
        }

    });

}

function sendFileAjax( url, type, fd, timeout, response, processData, contentType ) { 
    $.ajax({
        url: url,
        type: type,
        data: fd,
        processData: processData,
        contentType: contentType,
        timeout: timeout,
        success: function( JSONResponse ) { response( JSONResponse ) },
        error: function( e, jqXHR, ajaxSettings, thrownError ) {
            console.log(
                '----- ajax error -----' +
                '\n\nstatus: ', e.status,
                '\n\nstatusText: ', e.statusText,
                '\n\nresponseText: ', e.responseText,
                '\n\njqXHR: ', jqXHR,
                '\n\najaxSettings: ', ajaxSettings,
                '\n\nthrownError: ', thrownError,
                '\n\n\n'
            )
        }

    });

}
