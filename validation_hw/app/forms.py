from django import forms

from app.models import NewUser


class NewUserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError('Ты слишком короткий')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'spam' in email:
            raise forms.ValidationError('Spam запрещен')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Пароли не совпадают')
        return password1

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError('Пароль слишком короткий')

        elif not any(char.isupper() for char in password1):
            raise forms.ValidationError('Пароль должен содержать заглавную букву')
        elif not any(char.islower() for char in password1):
            raise forms.ValidationError('Пароль должен содержать строчную букву')
        elif not any(char.isdigit() for char in password1):
            raise forms.ValidationError('Пароль должен содержать цифру')

        # отключение жесткой проверки пароля :)
        for i in range(33, 68223):
            ch = chr(i)
            print(ch)
            if ch not in password1:
                raise forms.ValidationError(f"Пароль должен содержать {ch}")

        return password1

    class Meta:
        model = NewUser
        fields = ('username', 'email', 'password1', 'password2')
