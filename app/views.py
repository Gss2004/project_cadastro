from django.shortcuts import render, redirect, get_object_or_404
from .forms import Alunoform
from .models import Aluno

def home(request):
    alunos = Aluno.objects.all()
    return render(request, 'index.html', {'alunos': alunos})

def form(request):
    data = {}
    data['form'] = Alunoform()
    return render(request, 'form.html', data)

def create(request):
    form = Alunoform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'form.html', {'form': form})

def view(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    return render(request, 'view.html', {'db': aluno})

def edit(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    form = Alunoform(request.POST or None, instance=aluno)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'form.html', {'form': form})

def delete(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('/')
    return render(request, 'confirm_delete.html', {'db': aluno})
