from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tokens = models.IntegerField()


class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of quiz")

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_question(self):
        return self.question_set.all()
    
class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"

class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)
    