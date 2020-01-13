from django.contrib.auth import get_user_model #user model which is current;y active
from django.contrib.auth.forms import UserCreationForm #user creation form

class UserCreateForm(UserCreationForm):
    #different name
    class Meta:
        fields = ('username','email','password1','password2')  #the fields from the auth.forms
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email address'
