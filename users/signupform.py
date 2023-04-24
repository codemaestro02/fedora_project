from django import forms
from allauth.account.forms import SignupForm


# class CustomSignupForm(SignupForm):
    
#     username = forms.CharField(required=True)
#     email = forms.CharField(required=True)
#     password1 = SetPasswordField(label=("Password"))
#     password2 = PasswordField(label=("Password (again)"))

#     def clean_password2(self):
#         if ("password1" in self.cleaned_data and "password2" in self.cleaned_data):
#             if (self.cleaned_data["password1"] != self.cleaned_data["password2"]):
#                 raise forms.ValidationError(("You must type the same password each time."))
#         return self.cleaned_data["password2"]

#     def signup(self, request, user):
#         pass
    
#     def save(self, request):
#         user = super(CustomSignupForm, self).save(request)
#         user.username = self.cleaned_data['username']
#         user.email = self.cleaned_data['email']
#         user.set_password(self.user, self.cleaned_data["password1"])
#         user = user.save()
#         return user
    
class MyCustomSignupForm(SignupForm):

    def save(self, request):

    # Ensure you call the parent class's save.
    # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)
        user.save()

        # Add your own processing here.

        # You must return the original result.
        return user

