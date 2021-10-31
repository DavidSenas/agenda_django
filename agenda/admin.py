from django.contrib import admin

# Importando os Models criados

from .models import Amigos
from .models import Trabalho
from .models import Família

# Cadastrando em Admin os Models

admin.site.register(Amigos)
admin.site.register(Trabalho)
admin.site.register(Família)

# Register your models here.
