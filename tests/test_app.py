from wqu_app.app import app


def test_app():
    """
    GIVEN a test client
    When it visits '/'
    THEN the reponse is OK
    """
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
