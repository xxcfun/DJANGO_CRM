from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect, render
from users.forms import LoginForm


def login_view(request):
    next_url = request.GET.get('next', 'index')
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                request.session['user_id'] = user.id
                return redirect(next_url)
        else:
            print(form.errors)
    else:
        form = LoginForm(request)
    return render(request, 'login.html', {
        'form': form,
        'next_url': next_url
    })


def logout_view(request):
    """注销用户"""
    logout(request)
    return redirect('index')


def index_filter(request, pk):
    """查看个人页面"""
    return render(request, 'index_filter.html', {

    })