$(function($){
    $('.passw-reg').after('<p class="note d-none">Для создания пароля используйте латиницу и цифры</p>');

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    $('#registration').submit(function(event){
        event.preventDefault();
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
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