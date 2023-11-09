$(function($){
    $("i.basket").addClass("link");
    // Удаление блюда из корзины
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
                    $("h2.name-page span.total-price").html("к оплате: " + response.summ + "&#8381;");
                },
                error: function(){
                    console.log("Вышла ошибочка");
                }
            });
        });
    });
    /*Управление чекбоксами для выбора блюд в корзине*/
   const checkboxes = $("div.basket-wrapper div.item input.select-item");
   Array.from(checkboxes).forEach(checkbox => {
        console.log($(checkbox).attr("checked"));
       $(checkbox).click(function(event){
            let request;
            console.log(Boolean($(checkbox).attr("checked")));
            console.log("Изначально у нас было " + $(checkbox).attr("checked"));
            if (Boolean($(checkbox).attr("checked"))){
                request = false;
            } else{
                request = true;
            }
            console.log("На что надо изменить " + request);
             $.ajax({
                type: "POST",
                url: $(location).attr("href"),
                dataType: 'json',
                data: {
                    message: "change",
                    pk: $(checkbox).attr("name"),
                    request: request,
                    csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
                },
                success: function(response){
                    $("h2.name-page span.total-price").html("к оплате: " + response.summ + "&#8381;");
                    console.log("Устанавливаем " +  response.value);
                    $(checkbox).attr("checked", request);
                    console.log("Установили " + $(checkbox).attr("checked"));
                },
                error: function(){
                    console.log("Вышла ошибочка");
                }
        });
       });
   });
   $("#buying").click(function(e){
       $.ajax({
            type: "POST",
            url: $(location).attr("href"),
            dataType: 'json',
            data: {
                message: "order",
                 csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function(response){
                $('input.select-item[checked="checked"]').parent().remove();
                $("p#success-order").removeClass("d-none");
                  $("h2.name-page span.total-price").html("к оплате: " + response.summ + "&#8381;");
            },
            error: function(){
                console.log("Ошибка");
            }
       });
   });
   $("p#success-order").click(function(){
        $("p#success-order").addClass("d-none");
   })
});