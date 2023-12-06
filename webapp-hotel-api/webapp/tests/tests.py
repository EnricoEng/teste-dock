import unittest
import json
from impl.app import app, db

class YourAppTestCase(unittest.TestCase):
    def setUp(self):
        # Configurar o ambiente de teste
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        # Limpar o ambiente de teste
        db.session.remove()
        db.drop_all()

    def test_get_hoteis(self):
        # Teste para a rota de obtenção de hotéis por cidade
        data = {
            'nome': 'HotelExemplo1',
            'cidade': 'CidadeExemplo1'
        }
        self.app.post('/hoteis', data=json.dumps(data), content_type='application/json')

        data = {
            'nome': 'HotelExemplo2',
            'cidade': 'CidadeExemplo2'
        }
        self.app.post('/hoteis', data=json.dumps(data), content_type='application/json')

        response = self.app.get('/hoteis/CidadeExemplo1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(isinstance(data, list))
        self.assertEqual(len(data), 1)

    def test_create_reserva(self):
        # Teste para a criação de uma reserva
        data = {
            'cidade': 'CidadeExemplo',
            'hotel': 'HotelExemplo',
            'quarto': 'QuartoExemplo',
            'data': '2023-11-08'
        }
        response = self.app.post('/reservas', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_reservas(self):
        # Teste para a rota de obtenção de todas as reservas
        data = {
            'cidade': 'CidadeExemplo',
            'hotel': 'HotelExemplo',
            'quarto': 'QuartoExemplo',
            'data': '2023-11-08'
        }
        self.app.post('/reservas', data=json.dumps(data), content_type='application/json')

        data = {
            'cidade': 'OutraCidade',
            'hotel': 'OutroHotel',
            'quarto': 'OutroQuarto',
            'data': '2023-11-09'
        }
        self.app.post('/reservas', data=json.dumps(data), content_type='application/json')

        response = self.app.get('/reservas')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(isinstance(data, list))
        self.assertEqual(len(data), 2)

    def test_get_reserva(self):
        # Teste para a rota de obtenção de uma reserva específica
        data = {
            'cidade': 'CidadeExemplo',
            'hotel': 'HotelExemplo',
            'quarto': 'QuartoExemplo',
            'data': '2023-11-08'
        }
        self.app.post('/reservas', data=json.dumps(data), content_type='application/json')

        response = self.app.get('/reservas/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(isinstance(data, dict))
        self.assertEqual(data['cidade'], 'CidadeExemplo')
        self.assertEqual(data['hotel'], 'HotelExemplo')
        self.assertEqual(data['quarto'], 'QuartoExemplo')

    def test_update_reserva(self):
        # Teste para a atualização de uma reserva
        data = {
            'cidade': 'CidadeExemplo',
            'hotel': 'HotelExemplo',
            'quarto': 'QuartoExemplo',
            'data': '2023-11-08'
        }
        self.app.post('/reservas', data=json.dumps(data), content_type='application/json')

        updated_data = {
            'cidade': 'NovaCidade',
            'hotel': 'NovoHotel',
            'quarto': 'NovoQuarto',
            'data': '2023-11-09'
        }
        response = self.app.patch('/reservas/1', data=json.dumps(updated_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['cidade'], 'NovaCidade')
        self.assertEqual(data['hotel'], 'NovoHotel')
        self.assertEqual(data['quarto'], 'NovoQuarto')
        self.assertEqual(data['data'], '2023-11-09')

    def test_delete_reserva(self):
        # Teste para a exclusão de uma reserva
        data = {
            'cidade': 'CidadeExemplo',
            'hotel': 'HotelExemplo',
            'quarto': 'QuartoExemplo',
            'data': '2023-11-08'
        }
        self.app.post('/reservas', data=json.dumps(data), content_type='application/json')
        response = self.app.delete('/reservas/1')
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/reservas/1')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
