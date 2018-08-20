$(document).ready(funtion){
  console.log("loaded");
  $.material.init();

  $(document).on("submit", "#register-form", funtion(e){
    e.preventDefault();
    console.log("form submitted");
    var form = $('#register-form').serialize();
    $.ajax({
        url: '/postregistration',
        type: 'POST',
        data: form,
        success: funtion(response){
            console.log(response);
        }

    })

  })

});
