from django.db import models
from Auth.models import MyUser


# Create your models here.

class Menu(models.Model):
    type_of_position = models.ForeignKey('Chapter', on_delete=models.CASCADE, related_name="get_menu")
    name = models.CharField(verbose_name="Название товара", max_length=25)
    description = models.TextField(verbose_name="Описание товара", blank=True)
    price = models.IntegerField(verbose_name="Цена за товар")
    image = models.ImageField(verbose_name="Внешний вид товара", upload_to="menu/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"


class Chapter(models.Model):
    title = models.CharField(verbose_name="Название раздела", max_length=25)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сатегории"
        verbose_name_plural = "Категории"


class Order(models.Model):
    is_done = models.BooleanField(verbose_name="Готово/Не готово", default=False)
    cooker = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, related_name="cooker", null=True)
    user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, related_name="user", null=True)


class OrdersItem(models.Model):
    """

    Класс, отображающий позиции в корзине пользовтеля

    """

    user_id = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, verbose_name="Пользователь",
                                related_name="order")
    item = models.ForeignKey(Menu, on_delete=models.DO_NOTHING, verbose_name="Заказ")
    count = models.IntegerField(verbose_name="Количество блюд")
    is_selected = models.BooleanField(verbose_name="Выбор для покупки", default=False)
    is_ordered = models.BooleanField(verbose_name="Заказано/не заказано", default=False)
    order_id = models.ForeignKey(Order, on_delete=models.DO_NOTHING, verbose_name="Номер заказа", related_name="order_id", null=True)
