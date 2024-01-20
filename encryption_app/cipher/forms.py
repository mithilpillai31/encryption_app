from django import forms


class CipherForm(forms.Form):
    input_text = forms.CharField(widget=forms.Textarea)
    algorithm_choices = [
        ('monoalphabetic', 'Monoalphabetic Cipher'),
        ('caesar', 'Caesar Cipher'),
        ('railfence', 'Railfence Cipher'),
        ('vignere', 'Vigenere Cipher'),
    ]
    algorithm = forms.ChoiceField(choices=algorithm_choices)
    key = forms.CharField(required=False, label='Key')
    operation = forms.CharField(widget=forms.HiddenInput())

