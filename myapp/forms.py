from django import forms

NAME_WIDGET = {
    'class': 'form_item',
    'placeholder': 'Имя'
}

EMAIL_WIDGET = {
    'class': 'form_item',
    'placeholder': 'xetpy@mail.ru'
}

PASSWORD_WIDGET = {
    'class': 'form_item',
    'placeholder': '****'
}




class Login(forms.Form):
    name = forms.CharField(label='имя', max_length=100, required=True,
                           widget=forms.TextInput(attrs=NAME_WIDGET))
    password = forms.CharField(label='пароль', max_length=100, required=True,
                               widget=forms.PasswordInput(attrs=PASSWORD_WIDGET))


class Register(Login):
    name = forms.CharField(label='имя', max_length=100, required=True,
                           widget=forms.TextInput(attrs=NAME_WIDGET))
    email = forms.EmailField(label='почта', max_length=100, required=True,
                             widget=forms.EmailInput(attrs=EMAIL_WIDGET))
    password = forms.CharField(label='пароль', max_length=100, required=True,
                               widget=forms.PasswordInput(attrs=PASSWORD_WIDGET))
