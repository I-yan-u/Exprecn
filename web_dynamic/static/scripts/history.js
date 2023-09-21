$(document).ready(function () {
    // click on show
    $('.history #show').click(function () {
        let hist_id = $(this).attr('class');
        let user_id = $('caption').attr('class');
        $('.history').css({'filter': 'blur(20px) brightness(0.5) contrast(0.8)'});
        $('caption').fadeOut('fast');

        $('.popup_result').fadeIn();
        $.ajax({
            type: "GET",
            url: `http://web-02.yandev.tech/api/v1/users/${user_id}/history/${hist_id}`,
            contentType: "application/json",
            success: function (data) {
                let result = data.result;
                let final = '';
                for (let i = 0; i < result.length; i++) {
                    if (i % 29 === 0) {
                        final += ' ';
                    } else {
                        final += result[i];
                    }
                }
                console.log(final);
                $('.popup_result').append(`<p id="popout_result">${final}</p>`);
            },
            error: function (xhr, status, error) {
                console.error("Request failed with status: " + xhr.status);
            },
            dataType: "json"
        });
    });
    $('.history #delete').click(function () {
        alert('Deleted, Thank you');
    });

    $("#close").click(function () {
        $('.history').css({'filter': 'none'});
        $('caption').fadeIn('fast')
        $('.popup_result').fadeOut();
        $('#popout_result').remove();
    });
});