# Implementação do algoritmo baseado em fluxo de substituição RC4

from algorithms.core import Algorithm
class RC4(Algorithm):
    NOME = "RC4"
    DESC = ""
    
    def __call__(self, texto_entrada:str, K: str, criptografar: bool = True, **kwargs) -> str:
        
        if len(K) > 256:
            raise ValueError("A chave deve ter no máximo 256 caracteres")
        
        # Incialização
        
        S = list(range(256))
        j = 0
        key_length = len(K)
        
        for i in range(256):
            j = (j + S[i] + ord(K[i % key_length])) % 256
            S[i], S[j] = S[j], S[i]
            

        
        # Geração da Stream e Cifragem
        
        i = j = 0
        
        if criptografar:
            bytes_entrada = (ord(c) for c in texto_entrada)
        else:
            bytes_entrada = bytes.fromhex(texto_entrada)
        
        result = []
        for byte in bytes_entrada:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            
            # Swap
            S[i], S[j] = S[j], S[i]
            t = (S[i] + S[j]) % 256
            k = S[t]
           
            result.append(byte ^k)
            
        if criptografar:     
            return "".join(f"{b:02x}" for b in result)
        else:
            return bytes(result).decode("utf-8")
    