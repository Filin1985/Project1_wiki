from django import forms


class PostModelForm(forms.Form):
    class Meta:
        fields = [
            'title',
            'content'
        ]