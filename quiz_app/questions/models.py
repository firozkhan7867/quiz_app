from django.db import models

# Create your models here.


class   Questions(models.Model):
    Question_var = models.TextField(blank=True)
    option_1 = models.CharField(max_length=900)
    option_2 = models.CharField(max_length=900)
    option_3 = models.CharField(max_length=900)
    option_4 = models.CharField(max_length=900)
    answer = models.CharField(max_length=900)
    answer_no = models.IntegerField()

    def __str__(self):
        return self.answer
