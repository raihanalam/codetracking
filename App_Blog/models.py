from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
     name = models.CharField(max_length=264, verbose_name="Category Name")

     class Meta:
          verbose_name_plural = "Categories"

     def __str__(self):
          return self.name




class Blog(models.Model):
     author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_author')
     category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='post_category')
     blog_title = models.CharField(max_length=264,verbose_name="Put a Title")
     slug = models.SlugField(max_length=264,unique=True)
     blog_content = RichTextField(blank=True,null=True)
     #blog_content = models.TextField(verbose_name="Write your article here...")
     blog_image = models.ImageField(upload_to='blog_images', verbose_name="Image")
     publish_date = models.DateTimeField(auto_now_add=True)
     update_date = models.DateTimeField(auto_now=True)


     #A way to show blog list in acending and decending order using the - sign
     #we can also make it from views file
     class Meta:
          ordering = ['-publish_date']

     def __str__(self):
         return self.blog_title

class Comment(models.Model):
     blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog_comment')
     user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_comment')
     comment = RichTextField(blank=True,null=True)
     comment_date = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.comment

class Likes(models.Model):
     blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='liked_blog')
     user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='liked_user')

     def __str__(self):

          return str(self.user)+ " liked " + str(self.blog)

