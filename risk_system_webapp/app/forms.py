from django import forms

# Login form
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=100)

# Data input form
class DataInputForm(forms.Form):
    ticker = forms.CharField(max_length=10)
    shares = forms.IntegerField()
    purchase_price = forms.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = forms.DateField()