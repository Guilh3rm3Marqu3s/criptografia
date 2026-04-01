from algorithms import cifra_cesar

def test_encrypt():
    entrada = "Exemplo de teste."
    shift = 3
    saida_esperada = "Hahpsor gh whvwh."
    
    saida = cifra_cesar(entrada, shift, True)
    
    assert saida_esperada == saida
    
    
def test_decrypt():
    entrada = "Hahpsor gh whvwh."
    shift = 3
    saida_esperada = "Exemplo de teste."
    
    saida = cifra_cesar(entrada, shift, False)
    
    assert saida_esperada == saida