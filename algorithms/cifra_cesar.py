# Código para o algoritmo da Cifra de César
from algorithms.core import Algorithm

class CifraCesar(Algorithm):
    
    NOME = "Cifra de César"
    DESC = (
    "A Cifra de César é uma das técnicas de criptografia mais antigas conhecidas, "
    "atribuída ao imperador romano Júlio César, que a utilizava para proteger mensagens militares.\n\n"
    "Como funciona\n\n"
    "O algoritmo substitui cada letra do texto original por outra letra deslocada um número fixo "
    "de posições no alfabeto. Esse número é a chave. Por exemplo, com chave 3, a letra 'A' vira 'D', "
    "'B' vira 'E', e assim por diante. Ao chegar no fim do alfabeto, o deslocamento volta ao início.\n\n"
    "Exemplo com chave 3:\n"
    "  Texto:   ATAQUE AO AMANHECER\n"
    "  Cifrado: DWDTXH DR DPDQKHFHU\n\n"
    "Para decifrar, basta aplicar o deslocamento inverso — subtrair a chave em vez de somar.\n\n"
    "Características principais\n\n"
    "É uma cifra de substituição monoalfabética, o que significa que cada letra sempre é "
    "mapeada para a mesma letra cifrada. A chave é um único número inteiro, geralmente entre 1 e 25. "
    "Não altera espaços, números ou caracteres especiais.\n\n"
    "Vulnerabilidades\n\n"
    "A Cifra de César é extremamente fraca para padrões modernos. Como existem apenas 25 chaves "
    "possíveis, um atacante pode testar todas em segundos — ataque de força bruta. Além disso, "
    "por ser monoalfabética, é vulnerável à análise de frequência, onde as letras mais comuns "
    "no texto cifrado revelam as letras mais comuns do idioma original.\n\n"
    "Hoje é estudada exclusivamente para fins didáticos, sendo a porta de entrada para o entendimento "
    "de criptografia clássica."
)

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

