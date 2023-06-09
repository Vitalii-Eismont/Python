from django.db import models
import os


def get_photo_upload_path(instance, filename):
    # Отримати назву оголошення
    task_title = instance.task.title
    # Генерувати нове ім'я для фотографії
    new_filename = f'{task_title}_{filename}'
    # Повернути повний шлях до завантаженого файлу
    return os.path.join('image', task_title, new_filename)


class Task(models.Model):
    title = models.CharField('Name', max_length=50)
    text = models.TextField('Text')
    data = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    available = models.BooleanField(default=True, verbose_name='Наявність')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'


class Photo(models.Model):
    task = models.ForeignKey(Task, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField('photo', upload_to=get_photo_upload_path)

    def __str__(self):
        return str(self.image)
