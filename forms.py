from django import forms


class FeedbackForm(forms.Form):
    title = forms.CharField(label="Title", max_length=50, min_length=1)
    subject = forms.CharField(label="Subject", max_length=200, min_length=1)
