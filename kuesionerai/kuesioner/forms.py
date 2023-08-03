from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tb_soal_kepuasan_umum, Tb_soal_kepentingan, Tb_soal_kepuasan, Tb_test_kategori

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

        def __init__(self,*args, **kwargs):
            super(UserCreationForm,self).__init__(*args, **kwargs)
            for name,field in self.fields.items():
                field.widget.attrs.update({'class':'input'})
        labels = {
            'username': _('Username'),
            'first_name': _('Nama Pertama'),
            'last_name': _('Next Name'),
            'email': _('Email')
        }
    
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        
class KuesionerForm(forms.ModelForm):
    test_kategori = forms.ModelChoiceField(
        queryset=Tb_test_kategori.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Tb_soal_kepuasan_umum
        fields = ['pertanyaan', 'test_kategori']
        widgets = {
            'pertanyaan': forms.TextInput(attrs={'class': 'form-control'}),
        }

class KepentinganForm(forms.ModelForm):
    test_kategori = forms.ModelChoiceField(
        queryset=Tb_test_kategori.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Tb_soal_kepentingan
        fields = ['pertanyaan', 'test_kategori']
        widgets = {
            'pertanyaan': forms.TextInput(attrs={'class': 'form-control'}),
        }

class KepuasanForm(forms.ModelForm):
    test_kategori = forms.ModelChoiceField(
        queryset=Tb_test_kategori.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Tb_soal_kepuasan
        fields = ['pertanyaan', 'test_kategori']
        widgets = {
            'pertanyaan': forms.TextInput(attrs={'class': 'form-control'}),
        }