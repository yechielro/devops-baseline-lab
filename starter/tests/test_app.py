from app import app


def test_health():
    with app.test_client() as client:
        response = client.get('/health')
        assert response.status_code == 200
        assert response.get_json() == {'status': 'ok'}


def test_home():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert response.get_json()['service'] == 'devops-course'


def test_version():
    with app.test_client() as client:
        assert client.get('/version').get_json()['version'] == '1.0.0'
