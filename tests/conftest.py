import pytest

from catalog.models import Category, Material


@pytest.fixture
def category_1():
    return Category.objects.create(name='Товары', code='000001')


@pytest.fixture
def category_1_1(category_1):
    return Category.objects.create(name='Болты', code='000003', parent=category_1)


@pytest.fixture
def category_1_2(category_1):
    return Category.objects.create(name='Винты', code='000004', parent=category_1)


@pytest.fixture
def category_2():
    return Category.objects.create(name='Услуги', code='000002')


@pytest.fixture
def category_2_1(category_2):
    return Category.objects.create(name='Монтажные работы', code='000005', parent=category_2)


@pytest.fixture
def category_2_2(category_2):
    return Category.objects.create(name='Сборка и установка', code='000006', parent=category_2)


@pytest.fixture
def many_categories(
    category_1,
    category_1_1,
    category_1_2,
    category_2,
    category_2_1,
    category_2_2,
):
    return (
        category_1,
        category_1_1,
        category_1_2,
        category_2,
        category_2_1,
        category_2_2,
    )


@pytest.fixture
def material_1(category_1_1):
    return Material.objects.create(
        name='Болт 10x25',
        code='BOLT-10X25',
        price=100.00,
        category=category_1_1,
    )


@pytest.fixture
def material_2(category_1_2):
    return Material.objects.create(
        name='Винт 12x30',
        code='Vint-12X30',
        price=150.34,
        category=category_1_2
    )

@pytest.fixture
def many_materials(material_1, material_2):
    return material_1, material_2
