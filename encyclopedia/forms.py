from django import forms


class PostModelForm(forms.Form):
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={'required': True, 'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={'required': True, 'class': 'form-control'}))


class Edit(forms.Form):
    textarea = forms.CharField(widget=forms.Textarea(), label='')
