from app import app

def test_home_endpoint():
    """
    Testa o endpoint principal (/).
    Verifica se a resposta é 200 OK e contém a mensagem esperada.
    """
    # Cria um cliente de teste a partir da aplicação Flask
    client = app.test_client()
    
    # Faz uma requisição GET para a rota '/'
    response = client.get('/')
    
    # Verifica o código de status
    assert response.status_code == 200
    
    # Verifica se o corpo da resposta contém a string esperada
    # Usamos .data.decode() para converter os bytes da resposta em string
    assert "API Flask está rodando!" in response.data.decode('utf-8')
