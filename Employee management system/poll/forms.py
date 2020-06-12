from django import forms
from poll.models import Question, Choice

class PollForm(forms.ModelForm):
    title = forms.CharField(max_length=225, label='Question')

    class Meta:
        model = Question
        fields = ['title']


class ChoiceForm(forms.ModelForm):
    text = forms.CharField(max_length=225, label="Choice")

    class Meta:
        model = Choice
        exclude = ('question',)