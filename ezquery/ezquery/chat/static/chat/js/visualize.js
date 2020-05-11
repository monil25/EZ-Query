$(document).ready(function () {
  $("#table_fields").submit(function (e) {
    e.preventDefault(); // avoid to execute the actual submit of the form.
    var form = $(this);
    $.ajax({
      type: "POST",
      url: "/chat/table_fields/",
      data: form.serialize(), // serializes the form's elements.
      success: function (data) {
        console.log(data) // show response from the php script.
      }
    });
  });
})