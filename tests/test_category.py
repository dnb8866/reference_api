import pytest


@pytest.mark.django_db
class TestCategory:
    url = '/api/v1/category/'

    @pytest.mark.parametrize(
        'data',
        [
            {'name': 'test2222', 'code': '456', 'parent': 'Товары'},
            {'name': 'test', 'code': '123'},
        ]
    )
    def test_create_category(self, client, data, category_1):
        response = client.post(self.url, data=data)
        assert response.status_code == 201
        assert 'name' in response.data
        assert 'code' in response.data
        if 'parent' in data:
            assert 'parent' in response.data

    @pytest.mark.parametrize(
        "data",
        [
            {'name': 'test2', 'cde': '456'},
            {},
        ]
    )
    def test_create_category_invalid_data(self, client, data):
        response = client.post(self.url, data=data)
        assert response.status_code == 400

    def test_get_category(self, client, category_1):
        response = client.get(f'{self.url}{category_1.id}/')
        assert response.status_code == 200
        assert response.data['id'] == category_1.id
        assert response.data['parent'] == category_1.parent
        assert response.data['name'] == category_1.name
        assert response.data['code'] == category_1.code

    def test_get_category_not_found(self, client, category_1):
        response = client.get(f'{self.url}999999/')
        assert response.status_code == 404

    def test_put_category(self, client, category_1):
        data = {'name': 'Обновленная категория', 'code': '001'}
        response = client.put(
            f'{self.url}{category_1.id}/',
            data=data,
            content_type='application/json'
        )
        assert response.status_code == 200
        assert response.data['name'] == data['name']
        assert response.data['code'] == data['code']
        assert response.data['parent'] == category_1.parent
        assert response.data['id'] == category_1.id

    def test_patch_category(self, client, category_1):
        data = {'code': '002'}
        response = client.patch(
            f'{self.url}{category_1.id}/',
            data=data,
            content_type='application/json'
        )
        assert response.status_code == 200
        assert response.data['code'] == data['code']
        assert response.data['name'] == category_1.name
        assert response.data['parent'] == category_1.parent
        assert response.data['id'] == category_1.id
