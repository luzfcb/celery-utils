from celery_utils import add


def test_add():
    assert add(1, 1) == 2
