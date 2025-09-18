from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomAuthenticationForm, AvatarForm
from usuarios.forms import Registro, EditarPerfil
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .models import Profile

def iniciar_sesion(request):
    if request.method == "POST":
        formulario = CustomAuthenticationForm(request, data=request.POST)  
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
            return redirect('inicio')
    else:
        formulario = CustomAuthenticationForm()  
    return render(request, 'usuarios/iniciar_sesion.html', {'formulario': formulario})


def registro(request):
    if request.method == "POST":
        formulario = Registro(request.POST)
        avatar_form = AvatarForm(request.POST)


        if formulario.is_valid() and avatar_form.is_valid():
            user = formulario.save(commit=False)  
            
            user.first_name = formulario.cleaned_data.get('first_name', '')
            user.last_name = formulario.cleaned_data.get('last_name', '')
            user.email = formulario.cleaned_data.get('email', '')
            user.save()  


            
            from .models import Profile
            Profile.objects.create(user=user, avatar=avatar_form.cleaned_data['avatar'])


            messages.success(request, "Se registró correctamente")
            return redirect("iniciar_sesion")
    else:
        formulario = Registro()
        avatar_form = AvatarForm()


    return render(request, 'usuarios/registro.html', {'formulario': formulario,'avatar_form': avatar_form})




@login_required
def perfil(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'usuarios/perfil.html', {'profile': profile})


@login_required
def editar_perfil(request):
    profile = request.user.profile 


    if request.method == "POST":
        formulario = EditarPerfil(request.POST, instance=request.user)
        avatar_form = AvatarForm(request.POST)
       
        if formulario.is_valid() and avatar_form.is_valid():
            formulario.save()
           
            
            avatar = avatar_form.cleaned_data.get('avatar')
            if avatar:  
                profile.avatar = avatar
                profile.save()
           
            messages.success(request, "Perfil actualizado correctamente")
            return redirect('perfil')
    else:
        formulario = EditarPerfil(instance=request.user)
        avatar_form = AvatarForm(initial={'avatar': profile.avatar}) 


    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario,'avatar_form': avatar_form,'profile': profile})




class EditarContrasenia(PasswordChangeView):
    template_name = 'usuarios/editar_contrasenia.html'
    success_url = reverse_lazy('perfil')
