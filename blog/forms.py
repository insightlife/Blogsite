from django import forms

from .models import Comment, feedback

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
                'email': forms.EmailInput(attrs={'class':'form-control'}),
                'body': forms.Textarea(attrs={'class':'form-control','rows':4}),
                }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['name', 'email', 'body']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
                'email': forms.EmailInput(attrs={'class':'form-control'}),
                'body': forms.Textarea(attrs={'class':'form-control','rows':4}),
                }