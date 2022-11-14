from coursework2_source.main import app
from pytest import fixture

@fixture()
def posts_keys():
    return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


@fixture()
def client():
    return app.test_client()


def test_index(client):
    responce = client.get('/api/post')

    assert responce.status_code == 200
    assert isinstance(responce.json, list)


def test_posts(client, posts_keys):
    responce = client.get('/api/post/1')

    assert responce.status_code == 200
    assert isinstance(responce.json, dict)
    assert set(responce.json.keys()) == posts_keys
