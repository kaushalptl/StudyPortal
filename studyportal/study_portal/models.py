from django.db import models
import datetime

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    cimage = models.ImageField(upload_to="study_portal/images", default="")

    def __str__(self):
        return self.course_name


class Video(models.Model):
    video_id = models.AutoField(primary_key=True)
    link = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    order = models.IntegerField()
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)
    course_name = models.CharField(max_length=255,default="")

    def __str__(self):
        return str(self.order)+ " - " +self.course_name



class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=10)

    def __str__(self):
        return self.name




class Tutorial(models.Model):
    tut_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=50)
    topic_name = models.CharField(max_length=100)
    sq_no = models.IntegerField(default=0)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.course_name + "  " + str(self.sq_no) + "-" + self.topic_name




class Material(models.Model):
    mat_id = models.AutoField(primary_key=True)
    mat_link = models.CharField(max_length=255)
    mat_description = models.CharField(max_length=255)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)
    course_name = models.CharField(max_length=255,default="")

    def __str__(self):
        return self.course_name



class Question(models.Model):
    que_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=255, null=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.question


class Answer(models.Model):
    que_id=models.ForeignKey(Question, on_delete=models.CASCADE,null=True)
    ans_id = models.AutoField(primary_key=True)
    answer = models.CharField(max_length=255)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)        



