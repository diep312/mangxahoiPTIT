from django import forms
from .models import Post, Comment, UserAdditionalInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import DateInput


class PostForm(forms.ModelForm):
    body = forms.CharField(
        label = '',
        widget = forms.Textarea(attrs={
            'rows':'3',
            'placeholder': 'Say something...'
        })
    )
    class Meta:
        model = Post
        fields = ['body']

class CreateUserForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username' : forms.TextInput(attrs = {'placeholder': 'Nhập tên người dùng...'}),
            'email'    : forms.TextInput(attrs = {'placeholder': 'Nhập e-mail...'}),
            'password1': forms.TextInput(attrs = {'placeholder': 'Nhập mật khẩu...'}),
            'password2': forms.TextInput(attrs = {'placeholder': 'Nhập lại mật khẩu...'})
        }

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label = '',
        widget = forms.Textarea(attrs={
            'rows':'3',
            'placeholder': 'Say something...'
        })
    )
    class Meta:
        model = Comment
        fields = ['comment']


class UpdateUserForm(forms.ModelForm):
    class Meta: 
        model = UserAdditionalInfo
        fields = ['avt' , 'bg', 'dob', 'gender', 'location', 'description']
        Choices = [("MALE", "Nam") , ("FEMALE", 'Nữ'), ("Other", 'Không muốn chia sẻ')]
        
        widgets = {
            'dob': DateInput(attrs={'type' : 'date'}), 
            'gender': forms.Select(choices=Choices),
            'location': forms.TextInput(attrs = {'placeholder': 'Nhập vị trí...'}),
            'description': forms.Textarea(attrs = {'placeholder': 'Nhập mô tả...'}),
        }