from django import forms
from .models import User, CompanyAccount, PersonalAccount

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'full_name', 'phone_number', 'email']
    
class CompanyAccountForm(forms.ModelForm):
    class Meta:
        model = CompanyAccount
        fields = ['company_name', 'registration_number', 'secret_number', 'security_question', 'security_answer', 'address', 'key_officers_details', 'organization_type']

class PersonalAccountForm(forms.ModelForm):
    class Meta:
        model = PersonalAccount
        fields = ['age', 'sex', 'address', 'security_question', 'security_answer']
