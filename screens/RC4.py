import customtkinter as ctk

class RC4Frame(ctk.CTkFrame):
    def __init__(self, master, cifra_class, callback_voltar):
        super().__init__(master)
        self.cifra_instancia = cifra_class() 
        self.callback_voltar = callback_voltar

      
        self.label_titulo = ctk.CTkLabel(self, text=self.cifra_instancia.NOME, font=("Arial", 24, "bold"))
        self.label_titulo.pack(pady=(20, 5))
        

      
        self.input_text = ctk.CTkTextbox(self, height=100)
        self.input_text.pack(fill="x", padx=20, pady=10)
        self.input_text.insert("0.0", "Digite sua mensagem aqui...")

       
        self.setup_controles()

      
        self.output_text = ctk.CTkTextbox(self, height=100, state="disabled")
        self.output_text.pack(fill="x", padx=20, pady=10)

     
        self.btn_container = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_container.pack(pady=20)

        self.btn_voltar = ctk.CTkButton(self.btn_container, text="Voltar", command=self.callback_voltar, fg_color="gray30")
        self.btn_voltar.pack(side="left", padx=10)

        self.btn_executar = ctk.CTkButton(self.btn_container, text="Criptografar", command=self.processar)
        self.btn_executar.pack(side="left", padx=10)
        
        self.btn_executar = ctk.CTkButton(self.btn_container, text="Descriptografar", command=lambda: self.processar(False))
        self.btn_executar.pack(side="left", padx=10)
        

    def setup_controles(self):
        """Cria um novo campo de entrada para a Chave J do RC4"""
        frame_K = ctk.CTkFrame(self, fg_color="transparent")
        frame_K.pack(pady=10)
        
        ctk.CTkLabel(frame_K, text="Chave (máximo 256 caracteres):").pack(side="left", padx=5)
        self.entry_K = ctk.CTkEntry(frame_K, width=300)
        self.entry_K.insert(0, "123")
        self.entry_K.pack(side="left")

    def processar(self, criptografar: bool = True):
        self.output_text.configure(state="normal")
        texto_puro = self.input_text.get("1.0", "end-1c")
        K = self.entry_K.get()

        try:
            resultado = self.cifra_instancia(texto_puro, K=K, criptografar=criptografar)
        except Exception as ex:
            self._mostrar_erro(str(ex))
            self.output_text.configure(state="disabled")
            return

        self.output_text.delete("1.0", "end")
        self.output_text.insert("0.0", resultado)
        self.output_text.configure(state="disabled")
        
        
    def _mostrar_erro(self, msg):
        popup = ctk.CTkToplevel(self)
        popup.title("Erro")
        popup.geometry("300x150")
        popup.grab_set()

        ctk.CTkLabel(popup, text=msg, wraplength=260).pack(pady=20, padx=20)
        ctk.CTkButton(popup, text="OK", command=popup.destroy).pack(pady=10)