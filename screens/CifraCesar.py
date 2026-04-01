import customtkinter as ctk

class CesarFrame(ctk.CTkFrame):
    def __init__(self, master, cifra_class, callback_voltar):
        super().__init__(master)
        self.cifra_instancia = cifra_class() # Instancia a Cifra de César
        self.callback_voltar = callback_voltar

      
        self.label_titulo = ctk.CTkLabel(self, text=self.cifra_instancia.NOME, font=("Arial", 24, "bold"))
        self.label_titulo.pack(pady=(20, 5))
        
        self.label_desc = ctk.CTkLabel(self, text=self.cifra_instancia.DESC, wraplength=400)
        self.label_desc.pack(pady=10)

      
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
        """Cria o seletor numérico para o Shift da Cifra de César"""
        frame_shift = ctk.CTkFrame(self, fg_color="transparent")
        frame_shift.pack(pady=10)
        
        ctk.CTkLabel(frame_shift, text="Deslocamento (Shift):").pack(side="left", padx=5)
        self.entry_shift = ctk.CTkEntry(frame_shift, width=50)
        self.entry_shift.insert(0, "3")
        self.entry_shift.pack(side="left")

    def processar(self, criptografar: bool = True):
        self.output_text.configure(state="normal")
        texto_puro = self.input_text.get("1.0", "end-1c")
        
        
        try:
            val_shift = int(self.entry_shift.get())
        except ValueError:
            self.output_text.delete("1.0", "end")
            self.output_text.insert("0.0", "ERRO: O Shift deve ser um número inteiro!")
            return

        
        resultado = self.cifra_instancia(texto_puro, shift=val_shift, criptografar=criptografar)

       
        self.output_text.delete("1.0", "end")
        self.output_text.insert("0.0", resultado)
        self.output_text.configure(state="disabled")