from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Create your models here.

User = get_user_model()

class Order(models.Model):

    STATUS = (
        ('ADDED', 'Создан'),
        ('COMPLETED', 'Завершен'),
        ('CANCELLED', 'Отменён')
    )

    customer = models.ForeignKey(User, verbose_name="Клиент", on_delete=models.CASCADE)
    status = models.CharField("Статус заказа", max_length=20, choices=STATUS, default=STATUS[0][0])
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    def __str__(self):
        return f"Заказ от {self.created_at} ({self.customer.email})"
    
    class Meta:
        verbose_name = _('заказ')
        verbose_name_plural = _('заказы')