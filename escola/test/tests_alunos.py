from rest_framework.test import APITestCase
from escola.models import Aluno
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

class AlunosTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
        email='asdf@gmail.com',
        password='hiwa_asdf',
        username='smile as we go ahead'
        )
        self.client.force_authenticate(self.user)
        #self.client.force_login(username=self.user.username, password=self.user.password)

        self.list_url = reverse('Alunos-list')
        self.aluno_1 = Aluno.objects.create(
            nome='Aluno1', rg='117885592', cpf='43484090307', data_nascimento="2013-01-01", celular=''
        )
        self.aluno_2 = Aluno.objects.create(
            nome='Aluno2', rg='117885591', cpf='43484090307', data_nascimento="2013-01-01", celular=''
        )

    def test_get_alunos(self):
        """Teste para verificar a requisição get de listagem de alunos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)  

    def test_post_aluno(self):
        """Teste para verificar a requisição post de criação de alunos"""
        data = {
            'nome':'Aluno1',
            'rg':'117885592', 
            'cpf':'43484090307', 
            'data_nascimento':"2013-01-01", 
            'celular':''
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)  

    def test_delete_aluno(self):
        """Teste para verificar a requisição delete não permitida para deletar um aluno"""
        response = self.client.delete('/alunos/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_aluno(self):
        """Teste para verificar a requisição put para atualizar um aluno"""
        data = {
            'nome':'Aluno1 atualizado',
            'rg':'117885592', 
            'cpf':'43484090307', 
            'data_nascimento':"2013-01-02", 
            'celular':''
        }

        response = self.client.put('/alunos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)