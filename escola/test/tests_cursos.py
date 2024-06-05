from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

class CursosTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_superuser(
        email='asdf@gmail.com',
        password='hiwa_asdf',
        username='smile as we go ahead'
        )
        self.client.force_authenticate(self.user)
        #self.client.force_login(username=self.user.username, password=self.user.password)

        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT1', descricao='Curso de teste 1', nivel='B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso='CTT2', descricao='Curso de teste 2', nivel='A'
        )

    def test_get_cursos(self):
        """Teste para verificar a requisição get de listagem de cursos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)  

    def test_post_cursos(self):
        """Teste para verificar a requisição post de criação de cursos"""
        data = {
            'codigo_curso':'CTT1',
            'descricao':'Curso de teste 1', 
            'nivel':'B'
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)  

    def test_delete_curso(self):
        """Teste para verificar a requisição delete não permitida para deletar um curso"""
        response = self.client.delete('/cursos/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)  

    def test_put_curso(self):
        """Teste para verificar a requisição put para atualizar um curso"""
        data = {
            'codigo_curso':'CTT1',
            'descricao':'Curso de teste 1 atualizado', 
            'nivel':'I'
        }

        response = self.client.put('/cursos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        
    # def test_falhador(self):
    #     self.fail('Teste falhou de propósito, não se preocupe')
