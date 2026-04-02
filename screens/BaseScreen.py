import customtkinter as ctk
from abc import abstractmethod

class BaseScreen(ctk.CTkFrame):
    def __init__(self, master, cifra_class, callback_voltar):
       super().__init__(master)
       self.cifra_instancia = cifra_class
       self.callback_voltar = callback_voltar
       
    def _build_input_common_components(self):
        self.label_titulo = ctk.CTkLabel(self, text=self.cifra_instancia.NOME, font=("Arial", 24, "bold"))
        self.label_titulo.pack(pady=(20, 5))
      
        self.input_text = ctk.CTkTextbox(self, height=100)
        self.input_text.pack(fill="x", padx=20, pady=10)
        self.input_text.insert("0.0", "Digite sua mensagem aqui...")
      
    @abstractmethod
    def _build_particular_components(self):
        pass   
        
    def _build_output_common_components(self):
        self.output_text = ctk.CTkTextbox(self, height=100, state="disabled")
        self.output_text.pack(fill="x", padx=20, pady=10)

     
        self.btn_container = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_container.pack(pady=20)

        self.btn_voltar = ctk.CTkButton(self.btn_container, text="Voltar", command=self.callback_voltar, fg_color="gray30")
        self.btn_voltar.pack(side="left", padx=10)

        self.btn_executar = ctk.CTkButton(self.btn_container, text="Criptografar", command=self._processar)
        self.btn_executar.pack(side="left", padx=10)
        
        self.btn_executar = ctk.CTkButton(self.btn_container, text="Descriptografar", command=lambda: self._processar(False))
        self.btn_executar.pack(side="left", padx=10)
        
    @ abstractmethod
    def _processar(self, **kwargs):
        pass
    
    
    def _mostrar_erro(self, msg):
        popup = ctk.CTkToplevel(self)
        popup.title("Erro")
        popup.geometry("300x150")
        popup.grab_set()

        ctk.CTkLabel(popup, text=msg, wraplength=260).pack(pady=20, padx=20)
        ctk.CTkButton(popup, text="OK", command=popup.destroy).pack(pady=10)
        
        
        
    