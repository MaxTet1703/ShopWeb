$(function($){
    Array.from($("button.cook")).forEach(button =>{
        $(button).click(function(){
            $.ajax({
                type: "POST",
                url: $(location).attr("href"),
                data: {
                    pk: $(button).parent().attr("name"),
                    csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
                },
                dataType: "json",
                success: function(response){
                    console.log("Всё успешно удалилось");
                    $(button).parent().remove();
                },
                error: function(err){
                    console.log(err);
                }
        });
        });
    });
});