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

    $('#create').submit(function(event){
        event.preventDefault();
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success: function(response){
                if (response.status == 400){
                    console.log( $("h4.error span.close").before())
                    $("h4.error span.close").before("");
                    $("h4.error span.close").before(response.error);
                    $("h4.error").removeClass("d-none");
                } else{
                    alert(response.success);
                }
            },
            error: function(response){

            }
        });
    });
    $("h4.error span.close").click(function(e){
        $("h4.error").addClass("d-none");
    });
})