from django import forms
from users.forms import UserRegisterForm, UserProfileForm
from users.models import Users
from products.models import Products, ProductCategories


class UserAdminRegistrationForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = Users
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'password1', 'password2')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4'}))


class ProductAdminCreateForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'description', 'price', 'quantity', 'category', 'image',)
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control py-4'}),
                   'description': forms.TextInput(attrs={'class': 'form-control py-4'}),
                   'price': forms.NumberInput(attrs={'class': 'form-control py-4'}),
                   'quantity': forms.NumberInput(attrs={'class': 'form-control py-4'}),
                   'category': forms.Select(attrs={'class': 'form-check label'}),
                   'image': forms.FileInput(attrs={'class': 'custom-file-input'})
                   }


class CategoriesAdminCreateForm(forms.ModelForm):
    class Meta:
        model = ProductCategories
        fields = ('name',)
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control py-4'})}
