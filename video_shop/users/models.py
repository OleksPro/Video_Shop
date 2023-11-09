from django.db import models
from django.contrib.auth.models import User
from PIL import Image

TYPE_CHOICES = (
    ('Повний пакет', 'full'),
    ('Безкоштовний пакет', 'free')
)

# Створюемо нову таблицю
class Profile(models.Model):
    # Створює зв'язок між двома моделями
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Користувач')
    img = models.ImageField('Фото профілю', default='default.png', upload_to='user_images')
    account_type = models.CharField(
        choices=TYPE_CHOICES, 
        default='Безкоштовний пакет', 
        max_length=30
        )
    
    def __str__(self):
        return f'Профіль користувача {self.user.username}'
    
    def save(self, *args, **kwargs):
        super().save()
        # Обрізає зображення яке завантажив користувач
        image = Image.open(self.img.path)
        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            # Оновлює (зберігає поверх) фото
            image.save(self.img.path)

    class Meta:
        verbose_name = 'Профіль'
        verbose_name_plural = 'Профілі'