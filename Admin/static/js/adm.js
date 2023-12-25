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
                    $(".error").text(response.error);
                    $(".window-error").removeClass("d-none");
                    $('input').addClass('red');
                    $('.passw-reg').next().removeClass("d-none");
                } else{
                    $("div.list").append(
                        `
                            <div class="person d-flex">
                            <p class="name">${response.name}</p>
                            <p class="email">${response.email}</p>
                            <p class="d-flex align-items-center justify-content-center"><i name="${response.pk}" class="fa fa-trash trash-icon"></i></p>
                            </div>
                        `
                    );
                    alert(response.success);
                }
            },
            error: function(err){
                console.log(err);
            }
        });
    });
    $(".close").click(function(e){
        $(".window-error").addClass("d-none");
        $(".passw-reg").next().addClass("d-none");
    });
})