from django.db import models

from applications.brand.utils import slug_generator


class Brand(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, primary_key=True, unique=True, blank=True)

    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slug_generator(self.title)
        super(Brand, self).save(*args, **kwargs)

    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.title}'
        return self.title
