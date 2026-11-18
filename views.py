from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tasks:list')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@require_POST
def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('home')