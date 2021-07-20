
from django.forms import ModelForm
from .models import Intern

class Intern(ModelForm):
    class Meta:
        model=Intern
        fields=['sender_name','reciver_name','amount']
