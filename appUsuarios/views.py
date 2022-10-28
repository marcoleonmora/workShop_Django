from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

#******** CONTROL DE INGRESO DE USUARIOS  ***********************************************************
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'home.html')
        else:
            return render(request, 'usuarios/login.html', {'alarma': 'Correo o password no valido!'})
    else:
        return render(request, 'usuarios/login.html')


#********* DESACTIVACION DEL USUARIO **********************************************************
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')


