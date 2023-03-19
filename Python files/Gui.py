import customtkinter
import tkinter
from PIL import ImageTk, Image


class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self,text="Login System")
        self.label.pack(pady=12, padx=10)

        self.entry1 = customtkinter.CTkEntry(master=self, width=120, height=25, fg_color=("white", "gray75"), corner_radius=8,placeholder_text="Username")
        self.entry1.place(relx=0.5, rely=0.5)
        self.entry1.pack(pady=12, padx=10)

        self.entry2 = customtkinter.CTkEntry(master=self, width=120, height=25, fg_color=("white", "gray75"), corner_radius=8, placeholder_text="Password", show="*")
        self.entry2.place(relx=0.5, rely=0.5)
        self.entry2.pack(pady=12, padx=10)


    def get_entries(self):
        username = self.entry1.get()
        password = self.entry2.get()
        return username, password


class MyFrame2(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.textbox = customtkinter.CTkTextbox(master=self, width=400, corner_radius=0)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textbox.insert("0.0", "Your account\n")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("BMS")
        self.geometry("1000x650")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        img = tkinter.PhotoImage(file="../Python files/pattern.png")
        self.imglabel = customtkinter.CTkLabel(master=self, image=img) # type: ignore
        self.imglabel.place(x=0, y=0, relwidth=1, relheight=1)

        self.my_frame = MyFrame(master=self,width=320, height=360, border_width=2, corner_radius=10)
        self.my_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.my_frame.grid(row=0, column=0, padx=350, pady=150, sticky="nsew")

        self.button = customtkinter.CTkButton(self, text="Login", command=self.Login)
        self.button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)


    def Login(self):
        username, password = self.my_frame.get_entries()
        if username == "user" and password == "pass":
            # Destroy the current MyFrame instance and replace it with MyFrame2
            self.my_frame.destroy()
            self.button.pack_forget()
            self.my_frame2 = MyFrame2(master=self)
            self.my_frame2.pack(pady=20,padx=60, fill="both", expand=True)
            print("Hello world")


app = App()
app.mainloop()
