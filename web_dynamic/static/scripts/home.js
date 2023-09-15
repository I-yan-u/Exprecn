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
    
    $('.try_now_arrow').click(function() {
        $('html, body').animate({
            scrollTop: $(".home-container").offset().top
        }, 1000);
        $("#seq_text").focus();
    });

    let deviceWidth = $(window).width();
    if (deviceWidth <= 640) {
        $('.top').attr('style', "background-image: url('static/images/DNA_imagex390.jpg')");
        let nav = $('.nav').detach();
        let state = false;
        console.log(deviceWidth);
        $('#lines').click(() => {
            if (state === false) {
                $('header.header').append(nav);
                $('#lines').css({'left': '0'});
                $('#favicon').css({'display': 'none'});
                $('H1').css({'display': 'none'});
                state = true;
            } else {
                nav = $('.nav').detach();
                $('#lines').css({'left': '85%'});
                $('#favicon').css({'display': 'block'});
                $('H1').css({'display': 'block'});
                state = false;               
            };
        });
    } else {
        $('#lines').css({'display': 'none'});
    };

    $('#submit').click(function() {
        $('.api_result').empty();
        let text = $('#seq_text').val();
        let action = $('.dropdown').val();

        let data = {
            query: text,
            action: action
        };

        console.log(data);

        $.ajax({
            type: "POST",
            url: "http://0.0.0.0:5000/api/v1/run",
            data: JSON.stringify(data),
            contentType: "application/json",
            success: function (data) {
                //console.log(data);
                let result = data.result;
                let html_line = '<li> Action: ' + data.action +'</li><li>Sequence type: ' + data.obj._Exprecn__NucleicAcid + '</li><li>Sequence: ' + data.obj.coding + '</li><li>Result: ' + result + '</li>';
                $('.api_result').append(html_line);
                console.log(result);
            },
            error: function (xhr, status, error) {
                console.error("Request failed with status: " + xhr.status);
            },
            dataType: "json"
        });
    });
});