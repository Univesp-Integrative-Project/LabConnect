from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import AgendaModelForm
from .models import Agenda

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login_user')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('agenda')
        else:
            messages.error(request, "Usuário ou senha inválido")
    return redirect('login_user')

def agenda(request):
    if str(request.user) != 'AnonymousUser':
        context = {
            'agenda': Agenda.objects.all()
        }
        return render(request, 'agenda.html', context)
    else:
        return redirect('login_user')

def agendamento(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = AgendaModelForm(request.POST)
            if form.is_valid():
                form.save()

                messages.success(request, 'Agendamento realizado.')
                form = AgendaModelForm() # Comando para limpar o formulário
            else:
                messages.error(request, 'Erro ao realizar o agendamento.')
        else:
            form = AgendaModelForm()
        context = {
            'form': form
        }
        return render(request, 'agendamento.html', context)
    else:
        return redirect('login_user')
