$(function($){
    jarallax(document.querySelectorAll('.wrapper-head'), {
      speed: 0.5
    });

    var buttons = $("nav span.menu");
    var chapters = $("div.chapter");
    $(buttons[0]).addClass('pointer');
    $(chapters[0]).removeClass("d-none");
    Array.from(buttons).forEach((button, index) => {
        $(button).click(function(e){
            e.preventDefault();
            $(buttons).removeClass("pointer");
            $(button).addClass("pointer");
            $(chapters).addClass("d-none");
            $(chapters[index]).removeClass("d-none");
        });
    });

    var modalButton = $("span.modal-open");
    var modalWindows = $("div.modal-container");
    var modalClose = $("span.modal-close");
    // Открытие модального окна
    Array.from(modalButton).forEach((button, index) =>{
        $(button).click(function(e){
            $(modalButton).removeClass("opened");
            $(button).addClass("opened");
            $(modalWindows[index]).removeClass("d-none");
        });
    });
    // Закрытие модального окна
    Array.from(modalWindows).forEach((wind, index) => {
        $(wind).click(function(e){
            if ($(e.target).hasClass("modal-container")
                || $(e.target).hasClass("modal-close")){
                $(wind).addClass("d-none");
                $(modalButton[index]).removeClass("opened");
            }
        });
    });
    // Счетчик количества товаров
    let counterButtons = $("button.counter-button");
    Array.from(counterButtons).forEach(button => {
        $(button).click(function(event){
            const direction = button.dataset.direction;
            var counter = $(button).parent().find(".counter-value");
            var currentValue = $(counter).attr("value");
            console.log(currentValue);
            if (direction == "plus"){
                currentValue ++;
                console.log("Плюс " + currentValue);
            }
            else{
               currentValue = currentValue - 1 > 1 ? currentValue - 1 : 1;
               console.log("Минус " + currentValue);
            }
            $(counter).attr("value", currentValue);
        });
    });
    // Отправляем заказы в корзину
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    const submitAdd = $("button.submit-add");
    Array.from(submitAdd).forEach(button =>{
        $(button).click(function(event){

            const name = $(button).parent().parent().find("p.name-food-modal").text();
            const count = $(button).parent().find("input.counter-value").attr("value");
            console.log(name);
            $.ajax({
                type: "POST",
                url: "employee/",
                data: {
                    name: name,
                    count: count,
                    csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
                },
                dataType: 'json',
                success: function(response){
                    console.log("Все прошло успешно");
                    alert(response.message);
                },
                error: function(){
                    console.log("Вышла ошибочка");
                    alert("Ошибка");
                }
            });
        });
    });
});