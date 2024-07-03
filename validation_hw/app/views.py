from django.shortcuts import render

from app.forms import NewUserForm
from app.models import NewUser


# Create your views here.
def index(request):

    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = NewUser(
                name=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
            )
            user.save()
    ctx = {
        'form': form,
    }

    return render(request, 'app/index.html', ctx)
