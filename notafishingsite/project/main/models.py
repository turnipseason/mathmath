from django.db import models


class Job(models.Model):
    title = models.CharField('Title', max_length=50) #до 255 символов?
    task = models.TextField('Description')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.id}/details'

    class Meta:
        verbose_name= 'Вакансия'
        verbose_name_plural = 'Вакансии'
