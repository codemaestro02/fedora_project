from django.shortcuts import render,redirect 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
# from allauth.account.forms import SignupForm, ResetPasswordForm, ResetPasswordKeyForm


# class CustomSignupForm(SignupForm):

#     def save(self, request):

#         # Ensure you call the parent class's save.
#         # .save() returns a User object.
#         user = super(CustomSignupForm, self).save(request)
#         user.save()

#         # Add your own processing here.

#         # You must return the original result.
#         return user


# class MyCustomResetPasswordForm(ResetPasswordForm):
#     def save(self, request):
#     # Ensure you call the parent class's save.
#     # .save() returns a string containing the email address supplied
#         email_address = super(MyCustomResetPasswordForm, self).save(request)
#         email_address.save()
#         # Add your own processing here.
#         # Ensure you return the original result
#         return email_address


# class MyCustomResetPasswordKeyForm(ResetPasswordKeyForm):
#     def save(self):
#     # Add your own processing here.
#     # Ensure you call the parent class's save.
#     # .save() does not return anything
#         super(MyCustomResetPasswordKeyForm, self).save()
