$(function($){
    $("i.basket").addClass("link");

    let trashes = $("div.basket-wrapper div.item p.trash i.trash-icon");
    Array.from(trashes).forEach(trash => {
        $(trash).click(function(event){
            event.preventDefault();
            const pk = $(trash).attr("name");
            $.ajax({
                type: "POST",
                url: $(location).attr("href"),
                dataType: 'json',
                data: {
                    pk: pk,
                    message: "delete",
                    csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
                },
                success: function(response){
                    console.log("Все прошло успешно");
                    $(trash).parent().parent().remove();
                    $("h2.name-page span.total-price").text("к оплате: " + response.summ);
                },
                error: function(){
                    console.log("Вышла ошибочка");
                }
            });
        });
    });
   const checkbox = $("div.basket-wrapper div.item input.select-item");
   Array.from(checkbox).forEach(checkbox => {
        console.log($(checkbox).attr("checked"));
       $(checkbox).click(function(event){
            let request;
            event.preventDefault();
            if ($(checkbox).attr("checked") == "checked"){
                request = "False";
            } else{
                request = "True";
            }
             $.ajax({
                type: "POST",
                url: $(location).attr("href"),
                dataType: 'json',
                data: {
                    message: "change",
                    pk: $(checkbox).attr("name"),
                    req: request,
                    csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
                },
                success: function(response){
                    $("h2.name-page span.total-price").text("к оплате: " + response.summ);
                    if (request == "True"){
                        $(checkbox).prop("checked", true);
                    } else {
                        $(checkbox).prop("checked", false) ;
                    }

                },
                error: function(){
                    console.log("Вышла ошибочка");
                }
            });



       });

   });
});