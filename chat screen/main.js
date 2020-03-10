const sendIcon = document.getElementById("sendQuery");
const inputField = document.getElementById("queryInput");
const msgElement = '<div class="outgoing-chats"><div class="outgoing-chats-msg" ><p>new message</p><span class="time">11:01 PM | October 11</span></div ><div class="outgoing-chats-img"><img src="user1.jpg" alt=""></div></div>'
const mainScreen = document.getElementById("mainScreen");
$(document).ready(function () {

  $.fn.sendMessage = function () {

    var str = $("#queryInput").val();
    if (str.trim().length != 0) {
      var newMsgElement = msgElement.replace("new message", str);
      var message = $(newMsgElement);
      $('#mainScreen').append(message);
    }
    $("#queryInput").val("");
    mainScreen.scrollTop = mainScreen.scrollHeight;

  }

  $("#sendQuery").click(function () {
    $.fn.sendMessage();
  });

  $('#queryInput').keypress(function (event) {
    var keycode = (event.keyCode ? event.keyCode : event.which);
    if (keycode == '13') {
      $.fn.sendMessage();
    }
  });


});