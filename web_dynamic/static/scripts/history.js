$(document).ready(function () {
    $('.history #show').click(function () {
        let hist_id = $(this).attr('class');
        let user_id = $('caption').attr('class');
        $('.history').css({'filter': 'blur(20px) brightness(0.5) contrast(0.8)'});
        $('caption').css({'display': 'none'})
        $('.popup_result').css({
            'display': 'flex'
        });
        $.ajax({
            type: "GET",
            url: `http://0.0.0.0:5000/api/v1/users/${user_id}/history/${hist_id}`,
            contentType: "application/json",
            success: function (data) {
                //console.log(data);
                let result = data.result;
                $('.popup_result').html(`<p>${result}</p>`);
                console.log(typeof(result))
                //alert(result)
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
});