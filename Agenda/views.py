from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            messages.error(request, "Usuário ou senha inválido")
    return redirect('/')

def home(request):
    if str(request.user) != 'AnonymousUser':
        # if str(request.method) == 'POST':
        #     form = AgendaModelForm(request.POST)
        #     if form.is_valid():
        #         form.save()

        #         messages.success(request, 'Agendamento realizado.')
        #         form = AgendaModelForm()
        #     else:
        #         messages.error(request, 'Erro ao agendar.')
        # else:
        #     form = AgendaModelForm()
        # context = {
        #     'form': form
        # }
        return render(request, 'home.html')
    else:
        return redirect('/')
