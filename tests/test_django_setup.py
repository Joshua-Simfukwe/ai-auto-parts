import pytest
from django.apps import apps

@pytest.mark.django_db
def test_carshape_model_exists():
    CarShape = apps.get_model('parts', 'CarShape')
    assert CarShape is not None

