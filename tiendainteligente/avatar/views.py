from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Avatar

@login_required
def crear_avatar(request):
    usuario = request.user
    avatar, created = Avatar.objects.get_or_create(usuario=usuario)
    if request.method == "POST":
        # Actualiza avatar_url si recibes una URL desde el frontend
        avatar.avatar_url = request.POST.get("avatar_url")
        avatar.save()
        return redirect("ver_avatar")

    return render(request, "avatar/crear_avatar.html", {"avatar": avatar})
