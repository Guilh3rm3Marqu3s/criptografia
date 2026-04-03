from algorithms import ChaCha20

def test_encrypt():
    chacha = ChaCha20()
    key = "12345678901234567890123456789012"
    nonce = "12345678"
    texto = "Olá, mundo!"

    assert chacha(texto, key, nonce, criptografar=True) == "29924e2404cfb2b4d6231ba1"

def test_decrypt():
    chacha = ChaCha20()
    key = "12345678901234567890123456789012"
    nonce  = "12345678"
    cifrado = "29924e2404cfb2b4d6231ba1"

    assert chacha(cifrado,key, nonce, criptografar=False) == "Olá, mundo!"

def test_ciclo_completo():
    chacha = ChaCha20()
    key = "12345678901234567890123456789012"
    nonce = "12345678"
    texto = "Olá, mundo!"

    cifrado = chacha(texto, key, nonce, criptografar=True)
    decifrado = chacha(cifrado, key, nonce, criptografar=False)

    assert decifrado == texto