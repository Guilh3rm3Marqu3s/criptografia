import customtkinter as ctk
from screens.BaseScreen import BaseScreen
class CesarFrame(BaseScreen):
    def __init__(self, master, cifra_class, callback_voltar):
    
        super().__init__(master, cifra_class(), callback_voltar)

        self._build_input_common_components()

       
        self._build_particular_components()

      
        self._build_output_common_components()

     
       
        
    def _build_particular_components(self):
        """Cria o seletor numérico para o Shift da Cifra de César"""
        frame_shift = ctk.CTkFrame(self, fg_color="transparent")
        frame_shift.pack(pady=10)
        
        ctk.CTkLabel(frame_shift, text="Deslocamento (Shift):").pack(side="left", padx=5)
        self.entry_shift = ctk.CTkEntry(frame_shift, width=50)
        self.entry_shift.insert(0, "3")
        self.entry_shift.pack(side="left")
        

    def _processar(self, criptografar: bool = True, **kwargs):
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