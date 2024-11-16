from pprint import pprint

import pytest

from catalog.models import Category


@pytest.mark.django_db
class TestTree:
    url = '/api/v1/tree/'

    def test_get(self, client, many_materials):
        main_category = Category.objects.get(name='Товары')
        response = client.get(f'{self.url}{main_category.pk}/')
        pprint(response.data)
        assert response.status_code == 200
        assert 'children' in response.data
        assert isinstance(response.data['children'], list)
        assert len(response.data['children']) == len(many_materials)
        total_price = sum([material.price for material in many_materials])
        assert float(response.data['total_price']) == total_price
