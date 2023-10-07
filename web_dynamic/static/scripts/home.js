$(document).ready(function() {
  // Adjust bg size based on scroll position
  let bgContainer = $('.top');
  $(window).scroll(() => {
    let newSize = 100 + $(window).scrollTop() / 50;
    bgContainer.css(`background-size`, `${newSize}%`);
  });


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
  
  let id = $('.welcome span').text();
  console.log(id);

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
              $('.nav_list').css({'display': 'block'});
              state = true;
          } else {
              $('.nav_list').css({'display': 'none'});
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

      if (id === '') {
        let post_data = {
          query: text,
          action: action
        };
        console.log(post_data);
        $.ajax({
          type: "POST",
          url: "http://0.0.0.0:5000/api/v1/run",
          data: JSON.stringify(post_data),
          contentType: "application/json",
          success: function (data) {
              //console.log(data);
              let result = data.result;
              let html_line;
              if (data.action === 'transcribe') {
                html_line = '<li> Action: ' + data.action +'</li>\
                <li>Sequence type: ' + data.obj._Exprecn__NucleicAcid + '</li>\
                <li>Sequence: ' + data.obj.coding + '</li>\
                <li>Result: ' + result + '</li>\
                <li>Info: ' + data.obj.info + '</li>';
              } else {
                if (result === null) {
                  html_line = '<li> Action: ' + data.action +'</li>\
                  <li>Sequence type: ' + data.obj._Exprecn__NucleicAcid + '</li>\
                  <li>Sequence: ' + data.obj.coding + '</li>\
                  <li>Result status: ' + result + '</li>\
                  <li>Result: ' + result + '</li>\
                  <li>Info: ' + data.obj.info + '</li>';
                } else {
                  html_line = '<li> Action: ' + data.action +'</li>\
                  <li>Sequence type: ' + data.obj._Exprecn__NucleicAcid + '</li>\
                  <li>Sequence: ' + data.obj.coding + '</li>\
                  <li>Result status: ' + result[0] + '</li>\
                  <li>Result: ' + result[1] + '</li>\
                  <li>Info: ' + data.obj.info + '</li>';                            
                }
              }
            $('.api_result').append(html_line);
            console.log(result);
          },
          error: function (xhr, status, error) {
            console.error("Request failed with status: " + xhr.status);
          },
          dataType: "json"
        });
      } else {
        let post_data = {
          query: text,
          action: action,
          user_id: id
        };
        const url = `http://0.0.0.0:5000/api/v1/user/${id}/run`;
        console.log(post_data);
        $.ajax({
          type: "POST",
          url: url,
          data: JSON.stringify(post_data),
          contentType: "application/json",
          success: function (data) {
              //console.log(data);
              let result = data.result;
              let html_line;
              if (data.action === 'transcribe') {
                html_line = '<li> Action: ' + data.action +'</li>\
                <li>Sequence type: ' + data.obj._Exprecn__NucleicAcid + '</li>\
                <li>Sequence: ' + data.obj.coding + '</li>\
                <li>Result: ' + result + '</li>\
                <li>Info: ' + data.obj.info + '</li>';
              } else {
                if (result === null) {
                  html_line = '<li> Action: ' + data.action +'</li>\
                  <li>Sequence type: ' + data.obj._Exprecn__NucleicAcid + '</li>\
                  <li>Sequence: ' + data.obj.coding + '</li>\
                  <li>Result status: ' + result + '</li>\
                  <li>Result: ' + result + '</li>\
                  <li>Info: ' + data.obj.info + '</li>';
                } else {
                  html_line = '<li> Action: ' + data.action +'</li>\
                  <li>Sequence type: ' + data.obj._Exprecn__NucleicAcid + '</li>\
                  <li>Sequence: ' + data.obj.coding + '</li>\
                  <li>Result status: ' + result[0] + '</li>\
                  <li>Result: ' + result[1] + '</li>\
                  <li>Info: ' + data.obj.info + '</li>';                            
                }
              }
            $('.api_result').append(html_line);
            console.log(result);
          },
          error: function (xhr, status, error) {
            console.error("Request failed with status: " + xhr.status);
          },
          dataType: "json"
        });
      }
  });

    // Adjust Result label
  $('#submit').click(function() {
    // set .res_label to sticky
    $('.res_label').css('display', 'none');
  });
});