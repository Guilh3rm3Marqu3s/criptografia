from algorithms.core import Algorithm
import struct

class Salsa20(Algorithm):
    NOME = "Salsa20"
    DESC = (
    "Salsa20 é uma cifra de fluxo criada por Daniel J. Bernstein em 2005, selecionada para "
    "o portfólio final do projeto eSTREAM em 2008.\n\n"
    
    "Em vez de cifrar a mensagem diretamente, gera um fluxo pseudoaleatório de bytes "
    "(keystream) a partir de uma chave de 256 bits e um nonce de 64 bits. A cifração é feita "
    "aplicando XOR entre a mensagem e esse keystream — tornando a decifração idêntica à cifração.\n\n"
    
    "O núcleo do algoritmo aplica 20 rodadas de operações ARX (adição, rotação e XOR) sobre "
    "um estado interno. Ao final, o estado transformado é somado ao original, "
    "impedindo que as rodadas sejam revertidas.\n\n"
    
    "Parâmetros obrigatórios:\n"
    "  - Chave: exatamente 32 bytes (256 bits)\n"
    "  - Nonce: exatamente 8 bytes (64 bits) — nunca reutilize com a mesma chave\n\n"
    
    "Seu design influenciou diretamente o ChaCha20, variante adotada no protocolo TLS 1.3."
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
        b ^= self._rotl32((a + d) % 2**32, 7)
        c ^= self._rotl32((b + a) % 2**32, 9)
        d ^= self._rotl32((c + b) % 2**32, 13)
        a ^= self._rotl32((d + c) % 2**32, 18)
        return a, b, c, d
    
    def _row_round(self, y):
        z = list(y)
        z[1], z[2], z[3], z[0] = self._quarter_round(y[0], y[1], y[2], y[3])
        z[6], z[7], z[4], z[5] = self._quarter_round(y[5], y[6], y[7], y[4])
        z[11], z[8], z[9], z[10] = self._quarter_round(y[10], y[11], y[8], y[9])
        z[12], z[13], z[14], z[15] = self._quarter_round(y[15], y[12], y[13], y[14])
        return z        
    def _column_round(self, x):
        z =list(x)
        z[0],  z[4],  z[8],  z[12] = self._quarter_round(x[0],  x[4],  x[8],  x[12])
        z[5],  z[9],  z[13], z[1]  = self._quarter_round(x[5],  x[9],  x[13], x[1])
        z[10], z[14], z[2],  z[6]  = self._quarter_round(x[10], x[14], x[2],  x[6])
        z[15], z[3],  z[7],  z[11] = self._quarter_round(x[15], x[3],  x[7],  x[11])
        return z
        
    def _double_round(self, x):
        return self._row_round(self._column_round(x))
    
    def _salsa20_block(self, state):
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
            C[0], k[0], k[1], k[2],
            k[3], C[1], n[0], n[1],
            clo, chi, k[4], k[5],
            k[6], k[7], C[2], C[3]
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
            key_stream = self._salsa20_block(state)
            for b_msg, b_ks in zip(chunk, key_stream):
                output.append(b_msg ^ b_ks)

        return output.hex() if criptografar else output.decode('utf-8', errors='replace')