from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Categories'

class Blog(models.Model):
    category = models.ForeignKey(Category, related_name='blog_category')
    title = models.CharField(max_length=250)
    posted_by = models.ForeignKey(User)
    posted_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    description = RichTextField()
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=500)
    hits = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Blog.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

    # for sitemaps
    def get_absolute_url(self):
        return '/details/%s' %self.slug

