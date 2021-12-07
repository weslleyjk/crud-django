from django.db import models
from django.contrib.auth.models import User

class Post(models.Model): 
    title = models.CharField(max_length=255) # 255 caracteres max
    slug = models.SlugField(max_length=255, unique = True) # url abaixo do titulo
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    body = models.TextField() # texto do post
    created = models.DateTimeField(auto_now_add=True) # adiciona a data e a hr no post criado
    updated = models.DateTimeField(auto_now=True) # atualiza a data de uma modificacao

    def __str__(self):
        return self.title
     
    
