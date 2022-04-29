from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'

    name = models.CharField(max_length=20)
    description = models.TextField(max_length=50)
    img = models.ImageField()
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    project_url = models.URLField(max_length=50)
    date = models.DateField()
    github_link = models.URLField(max_length=50)

    def __str__(self):
        return self.name

class Blog(models.Model):
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'
    
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=1000)
    description_next = models.TextField(max_length=1000)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    img = models.ImageField()
    quote = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.name

class Partner(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=100)
    img = models.ImageField()

    def __str__(self):
        return self.name