$(function($){
    Array.from($("button.cook")).forEach(button =>{
        $(button).click(function(){
            $.ajax({
                type: "POST",
                url: $(location).attr("href"),
                dataType: "json",
                data: {
                    pk: $(button).parent().attr("name"),
                    csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
                },
                success: function(response){
                    console.log("Всё успешно удалилось");
                    $(button).parent().remove();
                },
                error: function(response){
                    console.log("Ошибка");
                }
        });
        });
    });
});