from django.db import models
berth_choices=[('lower','lower'),('upper','upper')]
sex=[('Male','M'),("Female","F")]

# Create your models here.
class Member(models.Model):
  id = models.AutoField(primary_key=True)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  sex=models.CharField(max_length=255,choices=sex)
  age=models.IntegerField()
  berth_choice=models.CharField('berthchoices',max_length=255,blank=False,choices=berth_choices)

  
