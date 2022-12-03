from django import forms
from .models import Department,Manager


class RegForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter your name","class":"form-control"}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Enter your age","class":"form-control"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Enter your email","class":"form-control"}))
    experience=forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":"Enter your experience","class":"form-control"}))
    def clean(self):
        cleaned_data=super().clean()
        ex=cleaned_data.get('experience')
        if ex<0:
            msg="Experience Inavalid"
            self.add_error('experience',msg)

            
# class Meta - combine models to form

class DeptForm(forms.ModelForm):
    class Meta:
        model=Department
        fields="__all__"   
        widgets={
            'DeptNo':forms.NumberInput(attrs={'placeholder':'Enter Department Room No','class':'form-control'}),
            'DeptName':forms.TextInput(attrs={'placeholder':'Enter Department Name','class':'form-control'}),
            'DeptDescription':forms.TextInput(attrs={'placeholder':'Enter Department Description','class':'form-control'}),            
        }              


class ManagerForm(forms.ModelForm):
    class Meta:
        model=Manager
        fields="__all__"
        widgets={
            'first_name':forms.TextInput(attrs={'placeholder':'Enter your Firstname','class':'form-control'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Enter your Lastname','class':'form-control'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter your email','class':'form-control'}),
            'phone':forms.NumberInput(attrs={'placeholder':'Enter your number','class':'form-control'}),
        }