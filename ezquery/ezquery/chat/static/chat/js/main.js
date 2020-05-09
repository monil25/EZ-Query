$(document).ready(function () {
  const sendIcon = document.getElementById("sendQuery");
  const inputField = document.getElementById("queryInput");
  const startRecord = document.getElementById("startRecord");
  const stopRecord = document.getElementById("stopRecord");
  stopRecord.disabled = true;
  const stopFA = document.getElementById("stopFA");
  const msgElement = '<div class="outgoing-chats"><div class="outgoing-chats-msg" ><p>new message</p></div ><div class="outgoing-chats-img"><img alt=""></div></div>'

  const loadingMessage = '<div id = "loading" class="received-chats"> <div class = "received-msg"><div class = "received-msg-inbox"><div class = "bubble"><div class = "ellipsis one" > </div> <div class = "ellipsis two"> </div> <div class = "ellipsis three"></div></div></div><div></div>'
  const mainScreen = document.getElementById("mainScreen");
  $.fn.sendMessage = function () {
    var str = $("#queryInput").val();
    if (str.trim().length != 0) {
      var newMsgElement = msgElement.replace("new message", str);
      var messageDiv = $(newMsgElement);
      $('#mainScreen').append(messageDiv);
      var loading = $(loadingMessage);
      $('#mainScreen').append(loading);
      sendtoServer(str)
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
  startRecord.addEventListener("click", startRecording);
  stopRecord.addEventListener("click", stopRecording);

  function sendtoServer(str) {
    console.log("Send to server");
    $.ajax({
        url: "/chat/nlp_process/",
        type: "POST",
        data: {
          message: str,
        },
      })
      .done(function (response) {
        console.log(response);
        $("#loading").remove();
        //Add new Div heres
      })
      .fail(function () {
        console.log("Error Occured");
      });
  }

  function startRecording() {
    console.log("Reached Here");
    startRecord.disabled = true;
    stopRecord.disabled = false;
    stopFA.style.color = "red";
    $.ajax({
        url: "/chat/record_audio_start/",
        type: "POST",
        data: {
          start: "StartRecording",
        },
      })
      .done(function (response) {
        console.log(response);
        inputField.value = response["text"]
      })
      .fail(function () {
        console.log("Error Occured");
      });
  }

  function stopRecording() {
    startRecord.disabled = false;
    stopRecord.disabled = true;
    stopFA.style.color = "white";
    $.ajax({
        url: "/chat/record_audio_stop/",
        type: "POST",
        data: {
          start: "StopRecording",
        },
      })
      .done(function (response) {
        console.log(response);
      })
      .fail(function () {
        console.log("Error Occured");
      });
  }
  // stopRecord.onclick = e => {
  //   startRecord.disabled = false;
  //   stopRecord.disabled = true;
  //   stopRecord.style.color = "white";
  //   rec.stop();
  // };

});