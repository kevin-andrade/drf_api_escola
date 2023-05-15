from django.contrib import admin

from escola.models import Aluno, Curso


class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'nivel_curso')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)
    list_per_page = 10

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'curso', 'periodo')
    list_display_links = ('id', 'curso')
    