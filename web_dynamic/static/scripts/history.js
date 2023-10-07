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
        url: `http://0.0.0.0:5000/api/v1/users/${user_id}/history/${hist_id}`,
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
      let hist_id = $(this).attr('class');
      let user_id = $('caption').attr('class');
      // console.log(`hist_id: ${hist_id} \n user: ${user_id} `)
      if (confirm("Are you sure you want to delete this item?")) {
        $.ajax({
            type: "DELETE",
            url: `http://0.0.0.0:5000/api/v1/users/${user_id}/history/${hist_id}`,
            success: function (data) {
              console.log(data.result);
              alert(`Deleted, ${hist_id}`);
              location.reload();
            },
            error: function (xhr, status, error) {
              console.error("Request failed with status 0_0: " + xhr.status);
            },
        });
      } else {
        alert(`Not deleted`);
      }
  
  });

  $("#close").click(function () {
    $('.history').css({'filter': 'none'});
    $('caption').fadeIn('fast')
    $('.popup_result').fadeOut();
    $('#popout_result').remove();
  });
});