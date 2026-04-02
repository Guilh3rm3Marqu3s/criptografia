from algorithms import RC4

def test_encrypt():
    entrada = "Oi mundo."
    saida_esperada = "1c999fef901a60940b"
    K ='123'
    saida = RC4()(entrada, K)
    
    assert saida_esperada == saida
    
    
def test_decrypt():
    entrada = "1c999fef901a60940b"
    saida_esperada = "Oi mundo."
    K = '123'
    saida = RC4()(entrada, K, False)
    
    assert saida_esperada == saida