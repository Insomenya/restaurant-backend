from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.translation import gettext_lazy as _
from django.utils.crypto import get_random_string

# Create your models here.

def image_dir_path(instance, filename):
    extension = filename.split('.')[-1]
    unique_id = get_random_string(length=8)
    new_filename = "uploads/meal_%s_%s.%s" % (instance_id, unique_id, extension)

    return new_filename

class Category(models.Model):
    name = models.CharField("Название", max_length=40, blank=False, null=False)

    def __str__(self):
        return f"Категория \"{self.name}\""
    
    class Meta:
        verbose_name = _('категория')
        verbose_name_plural = _('категории')

class Meal(models.Model):
    name = models.CharField("Наименование", max_length=40, blank=False, null=False)
    price = models.DecimalField("Цена", max_digits=7, decimal_places=2, null=False, blank=False)
    times_ordered = models.IntegerField("Заказано, раз", default=0, null=False, blank=True)
    description = models.TextField("Описание", max_length=1000, blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    added_at = models.DateTimeField("Дата добавления", auto_now_add=True)
    image = models.ImageField("Картинка", upload_to=image_dir_path, null=True, blank=True)
    image_large = ImageSpecField(source='image', processors=[ResizeToFill(512, 512)], format='PNG', options={'quality': 70})
    image_medium  = ImageSpecField(source='image', processors=[ResizeToFill(256, 256)], format='PNG', options={'quality': 70})
    image_small = ImageSpecField(source='image', processors=[ResizeToFill(128, 128)], format='PNG', options={'quality': 70})
    image_tag = ImageSpecField(source='image', processors=[ResizeToFill(28, 28)], format='PNG', options={'quality': 70})

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('блюдо')
        verbose_name_plural = _('блюда')