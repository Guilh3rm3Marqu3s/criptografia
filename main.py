import customtkinter as ctk
from screens import MenuScreen

ctk.set_appearance_mode("dark")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self._set_appearance_mode("dark")
        
        self.title("Técnicas de Criptografia")
        self.geometry("1000X700")
        self.minsize(1000, 700)
        
        
        # contaier para montar todas as outras telas
        self.container = ctk.CTkFrame(self)
        self.container.pack(side="top", fill="both", expand=True)
        
        
        self.show_frame(MenuScreen)
        
    def show_frame(self, page_class):
        
        for frame in self.container.winfo_children():
            frame.destroy()
            
            
            
        new_frame = page_class(self.container, self)
        new_frame.pack(fill="both", expand=True)
        
        
        
        
        
        
        
        
    
app = App()
app.mainloop()