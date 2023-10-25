import customtkinter
from PIL import ImageTk
import PIL.Image
import tkinter as tk
from functions import *
import qrcode
from send_mail import*
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")
        img = ImageTk.PhotoImage(PIL.Image.open("scripts\Logo.png"))
        self.geometry("800x500")
        self.light_blue = "#ADD8E6"
        self.Title = customtkinter.CTkLabel(master=self,text="TASTY TRACKS",width=10,height=3,font=("TimesNewRoman",30),text_color=self.light_blue)
        self.Title.place(relx=0.5,rely=0.05, anchor=customtkinter.CENTER)
        self.logo = customtkinter.CTkLabel(master=self,image=img,text="")
       # self.logo.place(relx=0.3,rely=0.0)
        optionmenu_1 = customtkinter.CTkOptionMenu(self, values=["Profile", "Options"],command=self.window_choose)
        optionmenu_1.grid(row=0, column=0, pady=50, padx=10)
        optionmenu_1.set("Menu")
        self.title_show = False
        self.product=""
        self.contents = []
        self.carrito = []
        self.prod={}
        #self.button = customtkinter.CTkButton(master=self, text="View Profile", command=self.button_profile)
        #self.button.place(relx=0.1, rely=0.2, anchor=customtkinter.CENTER)

    def delete(self):
        for content in self.contents:
            content.destroy()
        self.contents=[]

    def choose_company(self,choice):
        def select(choice):
            self.product = choice
        def buy():
            if(self.product!="" and self.product not in self.carrito):
                self.carrito.append(self.product)
                self.prod[self.product]=1
            elif(self.product in self.carrito):
                self.prod[self.product]=self.prod.get(self.product,0)+1
            else:
                window = customtkinter.CTk()
                window.geometry("200x200")
                window.configure(bg_color="black")
                Label = customtkinter.CTkLabel(window,text="SELECCIONE PRODUCTO",text_color="red")
                Label.place(relx=0.5,rely=0.05, anchor=customtkinter.CENTER)
                window.mainloop()

        def ver_carrito():
            x = 0.75
            y = 0.42
            L1 = customtkinter.CTkLabel(self,text="Carrito de compras",text_color=self.light_blue,font=("TimesNewRoman",20))
            L1.place(relx=0.75,rely=0.37,anchor=customtkinter.CENTER)
            self.contents.append(L1)
            for producto in self.carrito:
                L = customtkinter.CTkLabel(self,text=str(self.prod[producto])+" : "+producto)
                L.place(relx=x,rely=y,anchor=customtkinter.CENTER)
                y+=0.05
                self.contents.append(L)
        def generate_code():
            if(self.carrito !=[]):
                data = str(self.prod)
                img = qrcode.make(data)
                f = open("output.png", "wb")
                img.save(f)
                f.close()
                send_mail(data)
                self.prod={}
                self.carrito=[]
            else:
                window = customtkinter.CTk()
                window.geometry("200x200")
                window.configure(bg_color="black")
                Label = customtkinter.CTkLabel(window,text="CARRITO VACIO",text_color="red")
                Label.place(relx=0.5,rely=0.05, anchor=customtkinter.CENTER)
                window.mainloop()

        data = menu_empresa(choice)
        optionmenu_3 = customtkinter.CTkOptionMenu(self, values=data,command=select)
        optionmenu_3.grid(row=2, column=0, pady=10, padx=0)
        optionmenu_3.set("Productos")
        button = customtkinter.CTkButton(master=self, text="Añadir a carrito", command=buy)
        button.place(relx=0.3, rely=0.37, anchor=customtkinter.CENTER)
        button2= customtkinter.CTkButton(master=self, text="Ver carrito", command=ver_carrito)
        button2.place(relx=0.5, rely=0.37, anchor=customtkinter.CENTER)
        button3 =customtkinter.CTkButton(master=self, text="Salir", command=generate_code)
        button3.place(relx=0.4, rely=0.44, anchor=customtkinter.CENTER)
        self.contents.append(optionmenu_3)
        self.contents.append(button)
        self.contents.append(button2)
        self.contents.append(button3)
        

    def window_choose(self,choice):
        if(self.title_show):
            self.delete()
            self.title_show=False
        if(choice=="Profile"):
            data = info_cliente()
            self.text = customtkinter.CTkLabel(master=self,text="Profile information",text_color=self.light_blue,font=("TimesNewRoman",20)) 
            name = customtkinter.CTkLabel(master=self,text="Nombre: "+data[0],text_color=self.light_blue)
            birthday = customtkinter.CTkLabel(master=self,text="Cumpleaños: "+data[1],text_color=self.light_blue)
            direction = customtkinter.CTkLabel(master=self,text="Dirección: "+data[2],text_color=self.light_blue)
            name.place(relx=0.0,rely=0.25)
            birthday.place(relx=0.0,rely=0.35)
            direction.place(relx=0.0,rely=0.45)
            self.contents.append(name)
            self.contents.append(birthday)
            self.contents.append(direction)

        elif choice=="Options":
            data = lista_empresas()
            optionmenu_2 = customtkinter.CTkOptionMenu(self, values=data,command=self.choose_company)
            optionmenu_2.grid(row=1, column=0, pady=0, padx=0)
            optionmenu_2.set("Restaurantes")
            self.text=customtkinter.CTkLabel(master=self,text="Options",text_color=self.light_blue,font=("TimesNewRoman",20))
            self.contents.append(optionmenu_2)
        self.text.place(relx=0.0,rely=0.2)
        self.title_show=True
        self.contents.append(self.text)

if __name__ == "__main__":
    app = App()
    app.mainloop()