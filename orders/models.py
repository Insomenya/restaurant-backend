from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from menu.models import Meal

# Create your models here.

User = get_user_model()

class Order(models.Model):

    STATUS = (
        ('ADDED', 'Создан'),
        ('COMPLETED', 'Завершен'),
        ('CANCELLED', 'Отменён')
    )

    status = models.CharField("Статус заказа", max_length=20, choices=STATUS, default=STATUS[0][0])
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)
    meals = models.ManyToManyField(
        Meal,
        verbose_name="блюда",
        through='Order_meal'
    )
    customer = models.ForeignKey(
        User,
        verbose_name="Клиент",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Заказ от {self.created_at} ({self.customer.email})"
    
    class Meta:
        verbose_name = _('заказ')
        verbose_name_plural = _('заказы')

class Order_meal(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, verbose_name='Блюдо', on_delete=models.CASCADE)
    quantity = models.IntegerField("Количество", default=1, blank=True, null=False)

    def __str__(self):
        return self.meal.category.name
    
    class Meta:
        unique_together = ('order', 'meal')