from pprint import pprint

import pytest


@pytest.mark.django_db
class TestMaterial:
    url = '/api/v1/materials/'

    @pytest.mark.parametrize(
        'data',
        [
            {'name': 'Болт 1', 'code': '0010', 'price': '100.32',
             'category': 'Болты'},
            {'name': 'Винт 1', 'code': '0020', 'price': '99.32',
             'category': 'Винты'},
        ]
    )
    def test_create_material(self, client, many_categories, data):
        response = client.post(self.url, data=data)
        assert response.status_code == 201
        assert response.data['name'] == data['name']
        assert response.data['code'] == data['code']
        assert response.data['price'] == data['price']
        assert response.data['category'] == data['category']

    @pytest.mark.parametrize(
        'data',
        [
            {'name': 'Болт 1', 'price': '100.32',
             'category': 'Болты'},
            {'name': 'Винт 1', 'code': '0020', 'price': '99.322',
             'category': 'Винты'},
            {'name': 'Винт 1', 'code': '0020', 'price': '99.32'},
        ]
    )
    def test_create_material_invalid_data(self, client, many_categories, data):
        response = client.post(self.url, data=data)
        assert response.status_code == 400

    def test_get_material(self, client, material_1):
        response = client.get(f'{self.url}{material_1.id}/')
        assert response.status_code == 200
        assert response.data['name'] == material_1.name
        assert response.data['code'] == material_1.code
        assert float(response.data['price']) == float(material_1.price)
        assert response.data['category'] == material_1.category.name

    def test_get_material_not_found(self, client, material_1):
        response = client.get(f'{self.url}999999/')
        assert response.status_code == 404

    def test_put_material(self, client, material_1):
        data = {'name': 'Болт 1 updated', 'price': '10.33', 'code': '123',
                 'category': 'Болты'}
        response = client.put(
            f'{self.url}{material_1.id}/',
            data=data,
            content_type='application/json'
        )
        assert response.status_code == 200
        assert response.data['name'] == data['name']
        assert response.data['code'] == data['code']
        assert float(response.data['price']) == float(data['price'])
        assert response.data['category'] == data['category']

    def test_patch_material(self, client, material_1):
        data = {'name': 'Болт 32'}
        response = client.patch(
            f'{self.url}{material_1.id}/',
            data=data,
            content_type='application/json'
        )
        assert response.status_code == 200
        assert response.data['name'] == data['name']
        assert response.data['code'] == material_1.code
        assert float(response.data['price']) == float(material_1.price)
        assert response.data['category'] == material_1.category.name
