from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


class User(models.Model):
  name = models.CharField(max_length=50)
  identity_number = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(limit_value=10), MaxLengthValidator(limit_value=10)])
  email = models.EmailField(unique=True)
  date_of_birth = models.DateField(
    validators=[MaxValueValidator(limit_value=timezone.now().date(),
    message="Date of birth cannot be exceeded today's date")]
  )
  
  def __str__(self):
      return self.name