from django.db import models

# Create your models here.
class HeartUser(models.Model):
    name = models.CharField(max_length=55)
    age = models.IntegerField()
    sex = models.IntegerField()
    cp = models.IntegerField()  # chest pain type
    trestbps = models.IntegerField()  # resting blood pressure
    restecg = models.IntegerField()  # resting electrocardiographic results
    thalach = models.IntegerField()  # maximum heart rate achieved
    exang = models.IntegerField()  # exercise-induced angina
    oldpeak = models.FloatField()  # ST depression
    slope = models.IntegerField()  # slope of the peak exercise ST segment
    ca = models.IntegerField()  # number of major vessels colored by fluoroscopy
    thal = models.IntegerField()  # thalassemia
    dial = models.IntegerField()

    def __str__(self):
        return f"HeartUser {self.name} - Age: {self.age}"