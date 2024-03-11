from django.db import models

class School(models.Model):
    Name = models.CharField(max_length=255)

class AssessmentAreas(models.Model):
    Name = models.CharField(max_length=255)

class Awards(models.Model):
    Name = models.CharField(max_length=255)

class Class(models.Model):
    ClassName = models.CharField(max_length=255)

class Subject(models.Model):
    SubjectName = models.CharField(max_length=255)
    StudentScore = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  

class Answers(models.Model):
    Answer = models.CharField(max_length=255)

class Student(models.Model):
    Name = models.CharField(max_length=255)
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    School = models.ForeignKey(School, on_delete=models.CASCADE)

class Summary(models.Model):
    School = models.ForeignKey(School, on_delete=models.CASCADE)
    SydneyParticipant = models.CharField(max_length=255)
    SydneyPercentile = models.DecimalField(max_digits=5, decimal_places=2)
    AssessmentArea = models.ForeignKey(AssessmentAreas, on_delete=models.CASCADE)
    Award = models.ForeignKey(Awards, on_delete=models.CASCADE)
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    CorrectAnswerPercentagePerClass = models.DecimalField(max_digits=5, decimal_places=2)
    CorrectAnswer = models.ForeignKey(Answers, on_delete=models.CASCADE, related_name='correct_answers')
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Participant = models.CharField(max_length=255)
    StudentScore = models.DecimalField(max_digits=5, decimal_places=2)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    YearLevelName = models.CharField(max_length=255)
    Answer = models.ForeignKey(Answers, on_delete=models.CASCADE, related_name='answers')
