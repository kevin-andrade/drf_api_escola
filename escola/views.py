from rest_framework import viewsets, generics

from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    '''Exibindo alunos'''
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewsSet(viewsets.ModelViewSet):
    '''Exibindo todos os cursos'''
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculasViewSet(viewsets.ModelViewSet):
    '''Exibindo todas as matrículas'''
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculasAlunos(generics.ListAPIView):
    '''Listando as matriculas de um aluno'''
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
    '''Listando alunos matriculados em um curso'''
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id= self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer


