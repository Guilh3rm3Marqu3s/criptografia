import customtkinter as ctk
from screens.BaseScreen import BaseScreen

class Salsa20Frame(BaseScreen):
    def __init__(self, master, cifra_class, callback_voltar):
        super().__init__(master, cifra_class(), callback_voltar)

        self._build_input_common_components()

       
        self._build_particular_components()

      
        self._build_output_common_components()
        
    def _build_particular_components(self):
        """Cria um novo campo de entrada para a Chave key e nonce do Salsa20"""
        frame_K = ctk.CTkFrame(self, fg_color="transparent")
        frame_K.pack(pady=10)
        
        ctk.CTkLabel(frame_K, text="Chave").pack(side="left", padx=5)
        self.entry_K = ctk.CTkEntry(frame_K, width=300)
        self.entry_K.insert(0, "11111111111111111111111111111111")
        self.entry_K.pack(side="left")
        
        frame_nonce = ctk.CTkFrame(self, bg_color='transparent')
        frame_nonce.pack(pady=10)
        
        ctk.CTkLabel(frame_nonce, text="Nonce").pack(side='left', padx=5)
        self.entry_Nonce = ctk.CTkEntry(frame_nonce, width=200)
        self.entry_Nonce.insert(0,"11111111")
        self.entry_Nonce.pack(pady=10)

    def _processar(self, criptografar: bool = True, **kwargs):
        self.output_text.configure(state="normal")
        texto_puro = self.input_text.get("1.0", "end-1c")
        K = self.entry_K.get()
        Nonce = self.entry_Nonce.get()

        try:
            resultado = self.cifra_instancia(texto_puro, key=K, nonce=Nonce,criptografar=criptografar)
        except Exception as ex:
            self._mostrar_erro(str(ex))
            self.output_text.configure(state="disabled")
            return

        self.output_text.delete("1.0", "end")
        self.output_text.insert("0.0", resultado)
        self.output_text.configure(state="disabled")