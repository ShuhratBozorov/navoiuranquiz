from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    selected_subject = models.ForeignKey(
        'quiz.Course', on_delete=models.CASCADE, null=True, blank=True, related_name='students'
    )
    SUBJECT_CHOICES = [
        ('region1', 'Навоийуран'),
        ('region2', 'Нуробод'),
        ('region3', 'Зафаробод'),
        ('region4', 'Учқудуқ'),
        ('region5', 'Уран ва ноёб ишлаб чиқариш маркази')
    ]
    
    regions = models.CharField(
        max_length=20,
        choices=SUBJECT_CHOICES,
        null=True,
        blank=True,
    )
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name