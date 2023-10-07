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
});