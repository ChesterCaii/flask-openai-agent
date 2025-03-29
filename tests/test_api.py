"""
Test suite for the Flask API endpoints.
"""

import pytest
from app import create_app
from config import DEFAULT_SYSTEM_PROMPT

@pytest.fixture
def app():
    """Create a test Flask application."""
    app = create_app()
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    """Create a test client for the Flask application."""
    return app.test_client()

def test_ping_endpoint(client):
    """Test the health check endpoint."""
    response = client.get('/ping')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'ok'
    assert data['message'] == 'Server is running'

def test_ask_endpoint(client):
    """Test the chat endpoint."""
    payload = {
        "prompt": "Hello, how are you?",
        "system": "You are a friendly assistant.",
        "history": []
    }
    
    response = client.post('/ask', json=payload)
    assert response.status_code == 200
    data = response.get_json()
    
    # Check response structure
    assert 'response' in data
    assert 'history' in data
    assert len(data['history']) == 3  # system + user + assistant messages
    
    # Check message roles
    assert data['history'][0]['role'] == 'system'
    assert data['history'][1]['role'] == 'user'
    assert data['history'][2]['role'] == 'assistant'

def test_ask_endpoint_with_history(client):
    """Test the chat endpoint with existing conversation history."""
    history = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Python?"},
        {"role": "assistant", "content": "Python is a programming language."}
    ]
    
    payload = {
        "prompt": "Tell me more about Python.",
        "history": history
    }
    
    response = client.post('/ask', json=payload)
    assert response.status_code == 200
    data = response.get_json()
    
    # Check that history was preserved and extended
    assert len(data['history']) == len(history) + 2  # original + new user + new assistant 