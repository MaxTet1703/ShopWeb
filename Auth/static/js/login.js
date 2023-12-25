$(function(){
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
    const csrftoken = getCookie('csrftoken');
    $('#login').submit(function(event){
        event.preventDefault();
        console.log($('input[type="password"]').val());
        console.log($(this).serialize());
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success: function(response){
                if (response.status == 400){
                    $('h6.error-message').text(response.error).removeClass('d-none');
                }
                else{
                     alert("Вы успешно вошли в систему");
                }
            },
            error: function(response){
                console.log(response)
            }
        });
    });
});