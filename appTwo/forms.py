from django import forms
from appTwo.models import User
from appTwo.models import Login


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
class NewLoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'
