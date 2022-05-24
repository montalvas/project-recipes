from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Category(Base):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Recipe(Base):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.PositiveIntegerField()
    preparation_time_unit = models.CharField(max_length=3)
    servings = models.PositiveIntegerField()
    servings_unit = models.CharField(max_length=10)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='recipes/cover/%Y/%m/%d/',
        blank=True,
        default="")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    

    