from algorithms import Salsa20

def test_encrypt():
    salsa = Salsa20()
    key = "12345678901234567890123456789012"
    nonce = "12345678"
    texto = "Olá, mundo!"

    assert salsa(texto, key, nonce, criptografar=True) == "d131ac2a4655e11b044aed25"

def test_decrypt():
    salsa = Salsa20()
    key = "12345678901234567890123456789012"
    nonce  = "12345678"
    cifrado = "d131ac2a4655e11b044aed25"

    assert salsa(cifrado, key, nonce, criptografar=False) == "Olá, mundo!"

def test_ciclo_completo():
    salsa = Salsa20()
    key = "12345678901234567890123456789012"
    nonce = "12345678"
    texto = "Olá, mundo!"

    cifrado = salsa(texto, key, nonce, criptografar=True)
    decifrado = salsa(cifrado, key, nonce, criptografar=False)

    assert decifrado == texto