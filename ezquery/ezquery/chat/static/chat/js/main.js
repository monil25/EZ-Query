$(document).ready(function () {
  const sendIcon = document.getElementById("sendQuery");
  const inputField = document.getElementById("queryInput");
  const startRecord = document.getElementById("startRecord");
  const stopRecord = document.getElementById("stopRecord");
  stopRecord.disabled = true;
  const stopFA = document.getElementById("stopFA");
  const msgElement = '<div class="outgoing-chats"><div class="outgoing-chats-msg" ><p>new message</p></div ><div class="outgoing-chats-img"><img alt=""></div></div>'

  const loadingMessage = '<div id = "loading" class="received-chats"> <div class = "received-msg"><div class = "received-msg-inbox"><div class = "bubble"><div class = "ellipsis one" > </div> <div class = "ellipsis two"> </div> <div class = "ellipsis three"></div></div></div><div></div>'
  const sendReplyMessage = `<div class="received-chats"> <div class = "received-chats-img" ></div> <div class = "received-msg" ><div class = "received-msg-inbox" > ReplyMessage </div> </div> </div>`
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
        query_type = response.type;
        console.log(query_type);
        var addReplyDiv;
        if (query_type.localeCompare("select") == 0) {
          console.log(query_type);
          let details = response.information;
          var tableHeading = '<div style="overflow-x:auto;"><table class="table table-bordered table-striped"><thead class="thead-dark"><tr>'
          //adding colnames
          console.log(details[0])
          Object.entries(details[0]).forEach(([key, value]) => {
            tableHeading = tableHeading.concat(`<th>${value}</th>`)
          })
          tableHeading = tableHeading.concat(`</tr></thead>`);
          details.shift(); //removing colnames
          var tableBody = '<tbody>'
          details.forEach(row => {
            tableBody = tableBody.concat("<tr>")
            Object.entries(row).forEach(([key, value]) => {
              tableBody = tableBody.concat(`<th>${value}</th>`)
            })
            tableBody = tableBody.concat("<tr>")
          })
          tableBody = tableBody.concat("</tbody></table></div>");
          //console.log(addReplyDiv);
          addReplyDiv = tableHeading.concat(tableBody);
        } else {
          addReplyDiv = sendReplyMessage.replace("ReplyMessage", `<p>${response.message}</p>`);
        }
        //console.log(addReplyDiv);
        $("#loading").remove();
        addReplyDiv = $(addReplyDiv);
        $('#mainScreen').append(addReplyDiv);
        mainScreen.scrollTop = mainScreen.scrollHeight;
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

});