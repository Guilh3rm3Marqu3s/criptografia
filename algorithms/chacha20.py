from algorithms.core import Algorithm
import struct

class ChaCha20(Algorithm):
    NOME = "ChaCha20"
    DESC = (
    "ChaCha20 é uma cifra de fluxo de alto desempenho baseada no Salsa20, "
    "projetada por Daniel J. Bernstein. Diferente do seu antecessor, o ChaCha "
    "reorganiza as operações de mistura para aumentar a difusão por rodada e "
    "otimizar a performance em arquiteturas SIMD (vetoriais). O algoritmo opera "
    "sobre um estado de 512 bits (matriz 4x4 de palavras de 32 bits), alternando "
    "entre Round de Colunas e Round de Diagonais (Double Round). É amplamente "
    "utilizado em protocolos modernos como TLS 1.3 e SSH devido à sua resistência "
    "a ataques de temporização e eficiência em software."
)
    
    def _rotl32(self, v, n:int):
        # rotaciona 32 bits de v, n posições para a esquerda
        # << shift à esquerda
        # | or lógico
        # >> shift à direita
        # & AND bit a bit
        # ^ XOR
        
        # utiliza-se o AND bit-wise com 0xFFFFFFFF para forçar a saída ter 4 bytes
        return ((v << n) | (v >> (32 - n))) & 0xFFFFFFFF
    
    def _quarter_round(self, a, b, c, d):
        # XOR com rodação para esquerda (bits) da adicão de 2^32
        a = (a + b) % (2**32)
        d = d ^ a
        d = self._rotl32(d, 16)
        c = (c + d) % (2**32)
        b = b ^ c
        b = self._rotl32(b,12)
        a = (a + b) % (2**32)
        d = d ^ a
        d = self._rotl32(d, 8)
        c = (c + d) % (2**32)
        b = b ^ c
        b = self._rotl32(b, 7)
        
        return a, b, c, d
    
    def _diagonal_round(self, y):
        z = list(y)
        z[0], z[5], z[10], z[15] = self._quarter_round(y[0], y[5], y[10], y[15])
        z[1], z[6], z[11], z[12] = self._quarter_round(y[1], y[6], y[11], y[12])
        z[2], z[7], z[8], z[13] = self._quarter_round(y[2], y[7], y[8], y[13])
        z[3], z[4], z[9], z[14] = self._quarter_round(y[3], y[4], y[9], y[14])
        return z        
    def _column_round(self, x):
        z =list(x)
        z[0],  z[4],  z[8],  z[12] = self._quarter_round(x[0],  x[4],  x[8],  x[12])
        z[1],  z[5],  z[9], z[13]  = self._quarter_round(x[1],  x[5],  x[9], x[13])
        z[2], z[6], z[10],  z[14]  = self._quarter_round(x[2], x[6], x[10],  x[14])
        z[3], z[7],  z[11],  z[15] = self._quarter_round(x[3], x[7],  x[11],  x[15])
        return z
        
    def _double_round(self, x):
        return self._diagonal_round(self._column_round(x))
    
    def _chacha20_block(self, state):
        x = list(state)
        
        for _ in range(10):
            x = self._double_round(x) # 10 doubles rounds = 20 rodadas
            
        # soma a palavra com o estado original
        
        output = [(x[i] + state[i]) % 2**32 for i in range(16)]
        
        # serializa em bytes
        return struct.pack('<16I', *output)
    
    def _make_state(self, key: bytes, nonce: bytes, counter: int):
        # constantes -> 'expand 32-byte k'
        C = [0x61707865, 0x3320646e, 0x79622d32, 0x6b206574]
        
        k = struct.unpack('<8I', key)
        n = struct.unpack('<2I', nonce)
        clo = counter & 0xFFFFFFFF # contador low
        chi = (counter >> 32) & 0xFFFFFFFF # contador high
        
        return [
            C[0], C[1], C[2], C[3],
            k[0], k[1], k[2], k[3],
            k[4], k[5], k[6], k[7],
            n[0], n[1], clo, chi
        ]
        
    def _preparar_entrada(self, key, nonce):
        if isinstance(key, str):
            key = key.encode('utf-8')

        if isinstance(nonce, str):
            nonce = nonce.encode('utf-8')

        return key, nonce
        
    def __call__(self, texto_entrada, key, nonce, criptografar:bool =True, **kwargs):
        
        
        key, nonce = self._preparar_entrada(key, nonce)
        
        if criptografar:
            msg = texto_entrada.encode('utf-8') if isinstance(texto_entrada, str) else texto_entrada
        else:
            if isinstance(texto_entrada, str):
                try:
                    msg = bytes.fromhex(texto_entrada.strip())
                except ValueError:
                    return "[erro: texto para decifrar deve estar em formato hex]"
            else:
                msg = texto_entrada

        output = bytearray()
        for bloco_num, i in enumerate(range(0, len(msg), 64)):
            chunk = msg[i:i + 64]
            state = self._make_state(key, nonce, bloco_num)
            key_stream = self._chacha20_block(state)
            for b_msg, b_ks in zip(chunk, key_stream):
                output.append(b_msg ^ b_ks)

        return output.hex() if criptografar else output.decode('utf-8', errors='replace')