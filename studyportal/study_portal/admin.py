from django.contrib import admin
from .models import Video
from .models import Course
from .models import Material, User, Tutorial, Question, Answer
# Register your models here.


admin.site.register(Video)
admin.site.register(Course)
admin.site.register(Material)
admin.site.register(User)
admin.site.register(Tutorial)
admin.site.register(Question)
admin.site.register(Answer)

