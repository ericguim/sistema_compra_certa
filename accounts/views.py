from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages


def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      return redirect('estoque')
    else:
      messages.error(request, 'Usuário ou senha inválidos')
      return redirect('login')
  else:
    return render(request, 'accounts/login.html')
