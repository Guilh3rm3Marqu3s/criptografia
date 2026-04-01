import customtkinter as ctk
from screens.MenuPrincipal import MenuScreen


class App(ctk.CTk):
    def __init__(self):
        ctk.set_appearance_mode("dark")
        super().__init__()
        self._set_appearance_mode("dark")
        
        self.title("Técnicas de Criptografia")
        self.geometry("1000X700")
        self.minsize(1000, 700)
        
        
        # contaier para montar todas as outras telas
        self.container = ctk.CTkFrame(self)
        self.switch_theme_var = ctk.StringVar(value="on")
        self.switch_theme = ctk.CTkSwitch(self, onvalue="on", offvalue="off", variable=self.switch_theme_var, command=self._set_window_theme, text="Dark Theme")
        self.switch_theme.pack(pady=10, padx=10, anchor="ne")
        
        
        self.container.pack(side="top", fill="both", expand=True)
        
        self._show_frame(MenuScreen)
        
    def _set_window_theme(self):
        switch_state = self.switch_theme_var.get()
        
        if switch_state == 'off': ctk.set_appearance_mode("light")
        else: ctk.set_appearance_mode("dark")
    def _show_frame(self, page_class):
        
        for frame in self.container.winfo_children():
            frame.destroy()
            
            
            
        new_frame = page_class(self.container, self)
        new_frame.pack(fill="both", expand=True)
        
        
        
        
        
        
        
        
    
app = App()
app.mainloop()