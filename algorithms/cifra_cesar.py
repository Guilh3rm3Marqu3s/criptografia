# Código para o algoritmo da Cifra de César
from algorithms.core import Algorithm

class CifraCesar(Algorithm):
    
    NOME = "Cifra de César"
    DESC = "Substituição monoalfabética que rotaciona as letras do alfabeto."

    def __call__(self, texto_entrada: str, shift: int, criptografar: bool = True, **kwargs):
        """
            Função que aplica a Cifra de César:
            C = (P + K) mod 26
            Onde:
            - P: posição da letra
            - K: deslocamento (M)
            - C: caractere cifrado
            
            Args:
                entry (str): O texto de entrada
                shift (int): Valor do deslocamento
                encrypt (bool, optional): Indica se é para criptografia. Defaults to True.

            Returns:
                str: Texto criptografado/descriptografado
        """""
        # terei como refeência o código decimal da Tabela ASCII
        M_minusculo, M_maiusculo = 97, 65
        # o algoritmo fará distinção entre maiúsculas e minúsculas (preservar o case sensitive)
        entry_ascii_code = [ord(a) for a in texto_entrada]
        if criptografar == False: shift *= -1
        result = ""
        
        encrypted_entry_ascii = [
        ((a - M_minusculo + shift) % 26 + M_minusculo) if 97 <= a <= 122 else # minúsculas
        ((a - M_maiusculo + shift) % 26 + M_maiusculo) if 65 <= a <= 90 else  # maiúsculas
        a for a in entry_ascii_code # mantém o resto (espaços, etc)
        ]
        
        result = "".join([chr(a) if isinstance(a, int) else a for a in encrypted_entry_ascii])
        
        return result

