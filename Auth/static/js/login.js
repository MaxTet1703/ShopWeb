$(function(){
    $('#login').submit(function(event){
        event.preventDefault();
        data = $(this).serialize();
        data.csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            type: this.method,
            url: this.action,
            data: data,
            dataType: 'json',
            success: function(response){
                if (response.status == 400){
                    $('h6.error-message').text(response.error).removeClass('d-none');
                }
                else{
                     alert("Вы успешно вошли в систему");
                     window.location= response.url;
                }
            },
            error: function(response){
                console.log(response)
            }
        });
    });
});