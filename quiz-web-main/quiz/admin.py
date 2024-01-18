from django.contrib import admin
from .models import Question,QuizAttempt,Course,Result

# Register your models here.

admin.site.register(QuizAttempt)
admin.site.register(Question)
admin.site.register(Result)
admin.site.register(Course)