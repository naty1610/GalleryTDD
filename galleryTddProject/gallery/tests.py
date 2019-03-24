from django.test import TestCase, Client

# Create your tests here.
from .models import Image, Usuario
import json

# Create your tests here.
class GalleryTestCase(TestCase):

    def test_list_image_status(self):
        url = '/gallery/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_count_images_list(self):
        user_model = Usuario.objects.create(username="testUser", name="Test",
                                            lastname="User", password="AnyPas#5", email="test@test.com",
                                            photo="https://banner2.kisspng.com/20180331/czw/kisspng-computer-icons-user-profile-female-avatar-user-5abff416099122.7881303215225293020392.jpg",
                                            educationLevel="Pregrado", profession="Ingeniera de sistemas")
        Image.objects.create(name='nuevo', url='No', description='testImage', type='jpg', user=user_model)
        Image.objects.create(name='nuevo2', url='No', description='testImage', type='jpg', user=user_model)

        response=self.client.get('/gallery/')
        current_data=json.loads(response.content)

        self.assertEqual(len(current_data), 2)

    def test_verify_first_from_images_list(self):
        user_model = Usuario.objects.create(username="testUser", name="Test",
                                            lastname="User", password="AnyPas#5", email="test@test.com",
                                            photo="https://banner2.kisspng.com/20180331/czw/kisspng-computer-icons-user-profile-female-avatar-user-5abff416099122.7881303215225293020392.jpg",
                                            educationLevel="Pregrado", profession="Ingeniera de sistemas")

        Image.objects.create(name='nuevo1', url='No', description='testImage', type='jpg', user=user_model)
        Image.objects.create(name='nuevo2', url='No', description='testImage', type='jpg', user=user_model)

        response = self.client.get('/gallery/')
        current_data = json.loads(response.content)

        self.assertEqual(current_data[0]['fields']['name'], "nuevo1")

    def test_add_user(self):
        response = self.client.post('/gallery/addUser/', json.dumps(
            {"username": "testUser", "name": "Test", "lastname": "User", "password": "AnyPas#5",
             "email": "test@test.com", "photo": "https://banner2.kisspng.com/20180331/czw/kisspng-computer-icons-user-profile-female-avatar-user-5abff416099122.7881303215225293020392.jpg", "educationLevel":"Pregrado", "profession":"Ingeniera de sistemas"}), content_type='application/json')
        current_data = json.loads(response.content)
        self.assertEqual(current_data[0]['fields']['username'], 'testUser')

    def test_images_publics(self):
        user_model = Usuario.objects.create(username="testUser", name="Test",
                                            lastname="User", password="AnyPas#5", email="test@test.com",
                                            photo="https://banner2.kisspng.com/20180331/czw/kisspng-computer-icons-user-profile-female-avatar-user-5abff416099122.7881303215225293020392.jpg",
                                            educationLevel="Pregrado", profession="Ingeniera de sistemas")
        Image.objects.create(name='nuevo', url='No', description='testPortafolio', type='jpg', profile='priv', user=user_model)
        Image.objects.create(name='nuevo2', url='No', description='testPortafolio', type='jpg', profile='publ', user=user_model)
        Image.objects.create(name='nuevo3', url='No', description='testPortafolio', type='jpg', profile='publ', user=user_model)
        Image.objects.create(name='nuevo4', url='No', description='testPortafolio', type='jpg', profile='publ', user=user_model)

        response = self.client.get('/gallery/publicPortfolio/' + str(user_model.id))
        current_data = json.loads(response.content)

        self.assertEqual(len(current_data), 3)
