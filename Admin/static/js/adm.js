$(function($){
    $('.passw-reg').after('<p class="note d-none">Для создания пароля используйте латиницу и цифры</p>');


    Array.from($('.trash-icon')).forEach(button =>{
        $(button).click(function(e){
            e.preventDefault();
            const user = $(button).parent().parent()
            $.ajax({
                type: 'POST',
                url: '/administrator/',
                data: {
                        pk:  $(button).attr('name'),
                        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
                    },
                dataType: 'json',
                success: function(response){
                    user.remove();
                }
            });
        })
    });

    $('#create').submit(function(event){
        event.preventDefault();
        data = $(this).serialize();
        data['csrfmiddlewaretoken'] = $('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            type: this.method,
            url: this.action,
            data: data,
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