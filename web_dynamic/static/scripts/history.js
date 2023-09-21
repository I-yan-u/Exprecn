$(document).ready(function () {

    $('#seq').each(function () {
        let sequence = $('#seq').text();
        let finalSeq = '';
        for (let i = 0; i < sequence.length; i++) {
            if (i % 82 === 0) {
                finalSeq += ' ';
            } else {
                finalSeq += sequence[i];
            }
        }
        $('#seq').text(finalSeq);
    });

    // click on show
    $('.history #show').click(function () {
        let hist_id = $(this).attr('class');
        let user_id = $('caption').attr('class');
        $('.history').css({'filter': 'blur(20px) brightness(0.5) contrast(0.8)'});
        $('caption').fadeOut('fast');

        $('.popup_result').fadeIn();
        $.ajax({
            type: "GET",
            url: `http://127.0.0.1:5000/api/v1/users/${user_id}/history/${hist_id}`,
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