# test_app.py

import app
import json

def test_create_book():
    with app.app.test_client() as client:
        book = {
            'title': 'Test Book',
            'author': 'Test Author',
            'published': '2022-01-01'
        }
        response = client.post('/books', json=book)
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['id'] is not None
        assert data['message'] == 'Book created successfully'

def test_get_books():
    with app.app.test_client() as client:
        response = client.get('/books')
        data = json.loads(response.data)
        assert response.status_code == 200
        assert len(data) > 0

def test_get_book():
    with app.app.test_client() as client:
        response = client.get('/books/2')
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['id'] == 2
        assert data['title'] == 'Test Book'
        assert data['author'] == 'Test Author'
        assert data['published'] == '2022-01-01'

def test_update_book():
    with app.app.test_client() as client:
        book = {
            'title': 'Updated Test Book',
            'author': 'Updated Test Author',
            'published': '2023-01-01'
        }
        response = client.put('/books/1', json=book)
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['message'] == 'Book updated successfully'

def test_delete_book():
    with app.app.test_client() as client:
        response = client.delete('/books/1')
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['message'] == 'Book deleted successfully'
