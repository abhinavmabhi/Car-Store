from django import forms
from app.models import Contact


class Contact_Form(forms.ModelForm):

    class Meta:

        model=Contact

        fields=["name","phone","email","message"]

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control border border-2 my-2","placeholder":"Enter Name"}),
            "phone":forms.TextInput(attrs={"class":"form-control border border-2 mb-2","placeholder":"Enter Phone"}),
            "email":forms.EmailInput(attrs={"class":"form-control border border-2 mb-2","placeholder":"Enter Email"}),
            "message": forms.Textarea(attrs={"class": "form-control border border-2 mb-7", "rows": 7, "placeholder": "Enter Message..."}),
        }