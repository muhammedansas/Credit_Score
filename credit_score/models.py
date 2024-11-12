from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    text = models.TextField()
    answer_choices = [
        ('A', 'Sometimes'),
        ('B', 'Never'),
        ('C', 'Always'),
        ('D', 'Nil'),
    ]
    def __str__(self):
        return self.text


class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=9, choices=Question.answer_choices)  
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.question.text}: {self.answer}"
    
class CreditScore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"{self.user.username}'s Credit Score: {self.score}"
