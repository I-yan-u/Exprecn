$(document).ready(function() {
    let path = window.location.pathname;
    let page = path.split('/').pop();
    console.log("Document Title: " + page);
    switch (page) {
        case 'about':
            $('a#about').css({"border-bottom":"solid 2px #FC7138"});
            break;
        case 'history':
            $('a#history').css({"border-bottom":"solid 2px #FC7138"});
            break;
        case 'profile':
            $('a#profile').css({"border-bottom":"solid 2px #FC7138"});
            break;
        default:
            break;
    }
});