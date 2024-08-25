from django import forms
from .models import Review

'''
class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=25, error_messages={
        "required":"O nome precisa ser preenchido",
        "max_length": "Por favor, coloque um nome curto"
    })

    review_text = forms.CharField(label = "Yout Feedback", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
'''
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }
        error_messages = {
             "user_name": {
              "required": "Seu nome não pode ser vazio!",
              "max_length": "Please enter a shorter name!"
            }
        }
