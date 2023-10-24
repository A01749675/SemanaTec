import customtkinter
from PIL import ImageTk
import PIL.Image
from tkinter import *

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")
        #img = ImageTk.PhotoImage(PIL.Image.open("LOGO.png"))
        self.geometry("800x500")
        self.light_blue = "#ADD8E6"
        self.Title = customtkinter.CTkLabel(master=self,text="TASTY TRACKS",width=10,height=3,font=("TimesNewRoman",30),text_color=self.light_blue)
        self.Title.place(relx=0.5,rely=0.05, anchor=customtkinter.CENTER)
        #self.logo = customtkinter.CTkLabel(master=self,image=img)
        #self.logo.place(relx=0.0,rely=0.0)
        optionmenu_1 = customtkinter.CTkOptionMenu(self, values=["Profile", "Options"],command=self.window_choose)
        optionmenu_1.grid(row=0, column=0, pady=50, padx=10)
        optionmenu_1.set("CTk Option Menu")
        #self.button = customtkinter.CTkButton(master=self, text="View Profile", command=self.button_profile)
        #self.button.place(relx=0.1, rely=0.2, anchor=customtkinter.CENTER)

    
    def window_choose(self,choice):
        if(choice=="Profile"):
            text = customtkinter.CTkLabel(master=self,text="Profile information",text_color=self.light_blue,font=("TimesNewRoman",20)) 
            name = customtkinter.CTkLabel(master=self,text="Nombre: "+"default",text_color=self.light_blue)
            birthday = customtkinter.CTkLabel(master=self,text="Cumpleaños: "+"default",text_color=self.light_blue)
            direction = customtkinter.CTkLabel(master=self,text="Dirección: "+"default",text_color=self.light_blue)
            name.place(relx=0.0,rely=0.25)
            birthday.place(relx=0.0,rely=0.35)
            direction.place(relx=0.0,rely=0.45)
        else:
            text=customtkinter.CTkLabel(master=self,text="Options",text_color=self.light_blue,font=("TimesNewRoman",20))
        text.place(relx=0.0,rely=0.2)

    def button_profile(self):
        window = customtkinter.CTk()
        window.geometry("400x600")
        window.title("Profile")
        Title = customtkinter.CTkLabel(master=window,text="Profile information",text_color=self.light_blue,font=("TimesNewRoman",20))
        name = customtkinter.CTkLabel(master=window,text="default",text_color="blue")
        birthday = customtkinter.CTkLabel(master=window,text="default",text_color="blue")
        direction = customtkinter.CTkLabel(master=window,text="default",text_color="blue")
        Title.place(relx=0.5,rely=0.05, anchor=customtkinter.CENTER)
        name.place(relx=0.0,rely=0.1)
        birthday.place(relx=0.0,rely=0.2)
        direction.place(relx=0.0,rely=0.3)
        window.mainloop()

    def button_options(self):
        window = customtkinter.CTk()
        window.geometry("400x600")
        window.title("Options")
        window.mainloop()

if __name__ == "__main__":
    app = App()
    app.mainloop()