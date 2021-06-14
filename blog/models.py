from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from django.urls import reverse


class Category(MPTTModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    category = TreeForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='children',
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.name}'

    class MPTTMeta:
        order_insertion_by = ['name']
        parent_attr = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return f'Tag {self.name}'


class Post(models.Model):
    author = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField(upload_to='articles/')
    category = models.ForeignKey(
        Category,
        related_name='post',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    tags = models.ManyToManyField(Tag, related_name='post')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default='', unique=True)

    def __str__(self):
        return f'Post: {self.title}'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"slug": self.category.slug, 'post_slug': self.slug})


class Recipe(models.Model): 
    name = models.CharField(max_length=50)
    serves = models.CharField(max_length=50)
    prep_time = models.PositiveBigIntegerField(default=0)
    cook_time = models.PositiveBigIntegerField(default=0)
    ingredients = models.TextField()
    directions = models.TextField()
    post = models.ForeignKey(
        Post,
        related_name='recipe',
        on_delete=models.SET_NULL,
        null=True,
        blank=True)


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    message = models.TextField(max_length=500)
    post = models.ForeignKey(
        Post,
        related_name='comment',
        on_delete=models.CASCADE,
    )
