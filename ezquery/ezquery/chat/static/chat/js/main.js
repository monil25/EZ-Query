$(document).ready(function () {
  const sendIcon = document.getElementById("sendQuery");
  const inputField = document.getElementById("queryInput");
  const msgElement = '<div class="outgoing-chats"><div class="outgoing-chats-msg" ><p>new message</p><span class="time">11:01 PM | October 11</span></div ><div class="outgoing-chats-img"><img src="user1.jpg" alt=""></div></div>'
  const mainScreen = document.getElementById("mainScreen");
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
  // var audioChunks;
  // startRecord.onclick = e => {
  //   startRecord.disabled = true;
  //   stopRecord.disabled = false;
  //   stopRecord.style.color = "red";
  //   // This will prompt for permission if not allowed earlier
  //   navigator.mediaDevices
  //     .getUserMedia({
  //       audio: true
  //     })
  //     .then(stream => {
  //       audioChunks = [];
  //       rec = new MediaRecorder(stream);
  //       rec.ondataavailable = e => {
  //         audioChunks.push(e.data);
  //         if (rec.state == "inactive") {
  //           let blob = new Blob(audioChunks, {
  //             type: "audio/wav"
  //           });
  //           recordedAudio.src = URL.createObjectURL(blob);
  //           // recordedAudio.controls = true;
  //           // recordedAudio.autoplay = true;
  //           audioDownload.href = recordedAudio.src;
  //           audioDownload.download = "wav";
  //           console.log(typeof (blob));
  //           console.log(blob);
  //           sendAudioToserver(blob)
  //           // audioDownload.innerHTML = "download";
  //         }
  //       };
  //       rec.start();
  //     })
  //     .catch(e => console.log(e));
  // };


  function startRecording() {
    $.ajax({
        url: "/chat/audio_to_text/",
        type: "POST",
        data: {
          start: "StartRecording",
        },
      })
      .done(function (response) {
        console.log(response);
      })
      .fail(function () {
        console.log("Error Occured");
      });
  }

  function StopRecording() {
    $.ajax({
        url: "/chat/stop_recording/",
        type: "POST",
        data: {
          start: "StartRecording",
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