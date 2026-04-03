import customtkinter as ctk
from algorithms.core import Algorithm
from screens import CesarFrame, RC4Frame, Salsa20Frame
class MenuScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        
        self.label = ctk.CTkLabel(self, text="Menu Principal", font=("Roboto", 24))
        self.label.pack(pady=20)
        
        # Frame que conterá os botões para escolher qual será a técnica de criptografia
        self.menu_options_frame = ctk.CTkFrame(self)
        self.menu_options_frame.pack(side="left", fill="both", expand=True)

        # Frame que conterá uma breve descrição da técnica escolhida
        self.desc_frame = ctk.CTkFrame(self, width=700)
        
        self.desc_frame.pack_propagate(False)
        self.desc_frame.pack(side="right", fill="y")
        self.label_desc = ctk.CTkLabel(self.desc_frame, text="Passe o mouse sobre um algoritmo para ver a descrição.", justify="left", wraplength=650 , anchor="nw")
        self.label_desc.pack(pady=20, padx=10, fill="x", anchor="nw")

        self._load_options()
        
        self.tela_cripto_ativa = None
      
    def _load_options(self):
        for subclass in Algorithm.__subclasses__():
            # Criando o botão
            btn = ctk.CTkButton(self.menu_options_frame, text=subclass.NOME, command=lambda s=subclass: self._selecionar_criptografia(s))
            btn.pack(pady=5, padx=20, fill="x")
            
            # On Mouse-Enter
            btn.bind("<Enter>", lambda event, s=subclass: self._on_enter(s))
            btn.bind("<Leave>", lambda event, s=subclass: self._on_leave())
            
   
    def _on_enter(self, classe_cripto):
        self.label_desc.configure(text=f"{classe_cripto.NOME}:\n\n{classe_cripto.DESC}", justify="left") 
        
    def _on_leave(self):
        self.label_desc.configure(text="Passe o mouse sobre um algoritmo para ver a descrição.")
    
    def _selecionar_criptografia(self, classe_cripto):
        self._on_leave()
        self.pack_forget()
        if self.tela_cripto_ativa:
            self.tela_cripto_ativa.destroy()
            
        
        if classe_cripto.NOME == "Cifra de César": self.tela_cripto_ativa = CesarFrame(self.master, classe_cripto, self._voltar_ao_menu)
        elif classe_cripto.NOME == "RC4": self.tela_cripto_ativa = RC4Frame(self.master, classe_cripto, self._voltar_ao_menu)
        elif classe_cripto.NOME == 'Salsa20': self.tela_cripto_ativa = Salsa20Frame(self.master, classe_cripto, self._voltar_ao_menu)
        self.tela_cripto_ativa.pack(fill="both", expand=True)
        
    def _voltar_ao_menu(self):
        if self.tela_cripto_ativa:
            self.tela_cripto_ativa.destroy()
            self.tela_cripto_ativa = None
        self.pack(fill="both", expand=True)
        self.update_idletasks()
            
            