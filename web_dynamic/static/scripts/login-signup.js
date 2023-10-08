$(document).ready(() => {
  // For login page hide and show password field
  $('#show').click(() => {
    $('#hide').css('display', 'block');
    $('#show').css('display', 'none');
    $('#inPass').attr('type', 'text');
  });
  $('#hide').click(() => {
    $('#show').css('display', 'block');
    $('#hide').css('display', 'none');
    $('#inPass').attr('type', 'password');
  });

  // For sign in page hide and show password field
  // First password
  $('#show1').click(() => {
    $('#hide1').css('display', 'block');
    $('#show1').css('display', 'none');
    $('#inPass1').attr('type', 'text');
  });
  $('#hide1').click(() => {
    $('#show1').css('display', 'block');
    $('#hide1').css('display', 'none');
    $('#inPass1').attr('type', 'password');
  });

  // Confirm password
  $('#show2').click(() => {
    $('#hide2').css('display', 'block');
    $('#show2').css('display', 'none');
    $('#inPass2').attr('type', 'text');
  });
  $('#hide2').click(() => {
    $('#show2').css('display', 'block');
    $('#hide2').css('display', 'none');
    $('#inPass2').attr('type', 'password');
  });

  // For signup, compare the two password fields
  $('#signup_submit').click((event) => {
    const passwd = $('#inPass1').val();
    const confirmPassword = $('#inPass2').val();
    if (confirmPassword !== passwd) {
      $('#inPass2').css({'animation': 'shake-pos 0.5s ease', 'border-color': 'red'});
      alert('Confirm Password and Password not the same.');
      event.preventDefault();
    }
    $('#inPass2').on('focus', () => {
      $('#inPass2').css({'border-color': '#A3E7D9'});
    })
  });
});