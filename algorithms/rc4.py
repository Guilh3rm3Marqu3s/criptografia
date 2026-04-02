# Implementação do algoritmo baseado em fluxo de substituição RC4

from algorithms.core import Algorithm
class RC4(Algorithm):
    NOME = "RC4"
    DESC = (
    "O RC4 é uma cifra de fluxo (stream cipher) criada por Ron Rivest em 1987 para a RSA Security. "
    "Como funciona\n\n"
    "O algoritmo opera em duas etapas:\n\n"
    "1. KSA (Key Scheduling Algorithm): inicializa um vetor de estado S com os valores de 0 a 255 e então "
    "embaralha esse vetor usando os bytes da chave. O resultado é um estado pseudoaleatório que depende inteiramente da chave fornecida.\n\n"
    "2. PRGA (Pseudo-Random Generation Algorithm): a partir do estado S, gera um fluxo de bytes pseudoaleatórios "
    "(o keystream). Cada byte do keystream é combinado com o byte correspondente do texto via XOR, "
    "cifrando ou decifrando, já que a operação é simétrica.\n\n"
    "Características principais\n\n"
    "Simétrica e de fluxo: a mesma chave e o mesmo algoritmo servem para cifrar e decifrar. "
    "Aceita chaves de 1 a 256 bytes. Não possui vetor de inicialização embutido, o que exige cuidados extras "
    "na implementação para evitar reutilização de keystream. O estado interno muda a cada byte processado.\n\n"
    "Vulnerabilidades conhecidas\n\n"
    "O RC4 é considerado inseguro para uso moderno. Os primeiros bytes do keystream têm viés estatístico, "
    "revelando informações sobre a chave. Reutilizar a mesma chave para cifrar mensagens diferentes compromete "
    "completamente a segurança. Foi quebrado na prática em protocolos como WEP (Wi-Fi) e versões antigas do TLS. "
    "Em 2015, a RFC 7465 proibiu explicitamente o uso do RC4 no TLS.\n\n"
    "Onde foi usado\n\n"
    "WEP, WPA (TKIP), SSL/TLS (versões antigas) e o protocolo RDP da Microsoft em versões mais antigas. "
    "Hoje o RC4 é estudado principalmente por razões históricas e acadêmicas. "
)
    
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
    