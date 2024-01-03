$(function($){
    $('.passw-reg').after('<p class="note d-none">Для создания пароля используйте латиницу и цифры</p>');



    $('#registration').submit(function(event){
        event.preventDefault();
        data = $(this).serialize()
        data.csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            type: this.method,
            url: this.action,
            data: data,
            dataType: 'json',
            success: function(response){
                if (response.status == 400){
                    console.log(response.error)

                    $('h6.error-message').text(response.error).removeClass('d-none');
                    $('input').addClass('red');
                    $('.passw-reg').next().removeClass("d-none");
                }
                else{
                    alert(response.success);
                    window.location.pathname = "";
                }
            },
            error: function(response){

            }
        })
    })
})