from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import pandas as pd
import plotly.express as px

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
        user = request.user
        context = {
            'agenda': Agenda.objects.filter(usuario=user)
        }
        return render(request, 'agenda.html', context)
    else:
        return redirect('login_user')

def agendamento(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = AgendaModelForm(request.POST)
            if form.is_valid():
                agenda = form.save(commit=False) # Evita salvar no banco antes de modificar
                agenda.usuario = request.user  # Define o usuário com base no request.user
                agenda.save()
                messages.success(request, 'Agendamento realizado.')
                form = AgendaModelForm() # Comando para limpar o formulário

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

@login_required
def data_analysis(request):
    # Extraindo dados do banco de dados
    agenda_data = Agenda.objects.select_related('disciplina').values('disciplina__nome', 'data_agendada', 'horario_agendado')
    df = pd.DataFrame(agenda_data)

    # Contagem de agendamentos por disciplina
    if not df.empty:
        count_by_disciplina = df['disciplina__nome'].value_counts().reset_index()
        count_by_disciplina.columns = ['Disciplina', 'Count']
        fig = px.bar(count_by_disciplina, x='Disciplina', y='Count', title='Agendamentos por Disciplina')
        graph = fig.to_html(full_html=False)
    else:
        graph = None

    context = {
        'graph': graph,
    }

    return render(request, 'data_analysis.html', context)