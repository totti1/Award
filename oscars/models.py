from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/')
    bio = models.CharField(max_length =100)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    @classmethod
    def get_profile(cls, user):
        profile = cls.objects.filter(user=user).first()
        return profile
    

class Project(models.Model):
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length =60)
    description = models.TextField()
    link = models.CharField(max_length =60)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, )
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_all_projects(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def get_projects_by_id(cls, id):
        projects = cls.objects.filter(profile = id).all()
        return projects


class Ratings(models.Model):
    design = models.IntegerField()
    usability = models.IntegerField()
    content = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, )
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, )