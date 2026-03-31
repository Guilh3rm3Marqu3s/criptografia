import customtkinter as ctk

class MenuScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        
        self.label = ctk.CTkLabel(self, text="Menu Principal", font=("Roboto", 24))
        self.label.pack(pady=20)
        
        # Frame que conterá os botões para escolher qual será a técnica de criptografia
        self.menu_options_frame = ctk.CTkFrame(self)
        self.menu_options_frame.pack(side="right", fill="both", expand=True)

        # Frame que conterá uma breve descrição da técnica escolhida
        self.desc_frame = ctk.CTkFrame(self, width=200)
        self.desc_frame.pack(side="left", fill="both", expand=True)

      
      