import customtkinter
import tkinter
from PIL import ImageTk, Image
import subprocess


class CreateAccount(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0,1), weight=1) # type: ignore

        self.label = customtkinter.CTkLabel(self,text="Create Account")
        self.label.grid(row=0, column=0, pady=10)

        self.email = customtkinter.CTkEntry(self, width=315, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="Email", text_color="black")
        self.email.grid(row=1, column=0,pady=5)

        self.password = customtkinter.CTkEntry(self, width=145, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="Password",show="*" ,text_color="black")
        self.password.grid(row=2, column=0,sticky="w", pady=5)

        self.name = customtkinter.CTkEntry(self, width=145, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="Name", text_color="black")
        self.name.grid(row=3, column=0, sticky="w", pady=5)

        self.last_name = customtkinter.CTkEntry(self, width=145, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="Last name", text_color="black")
        self.last_name.grid(row=3, column=0, sticky="e", pady=5)

        self.personal_info = customtkinter.CTkLabel(self, text="Personal info")
        self.personal_info.grid(row=4, column=0, sticky="w", padx=15,pady=10)

        self.job_title = customtkinter.CTkEntry(self, width=145, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="Job title", text_color="black")
        self.job_title.grid(row=5, column=0, sticky="nw", pady=5)

        self.phone_number = customtkinter.CTkEntry(self,  width=145, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="Phone Number", text_color="black")
        self.phone_number.grid(row=5, column=0, sticky="e", pady=5)

        self.OIB = customtkinter.CTkEntry(self,  width=145, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="OIB", text_color="black")
        self.OIB.grid(row=6, column=0, sticky="w", pady=5)

        self.city = customtkinter.CTkEntry(self,  width=145, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="City", text_color="black")
        self.city.grid(row=6, column=0, sticky="e", pady=5)

        self.state = customtkinter.CTkEntry(self,  width=145, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="State", text_color="black")
        self.state.grid(row=7, column=0, sticky="w", pady=5)

        self.street = customtkinter.CTkEntry(self,  width=145, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="Street", text_color="black")
        self.street.grid(row=7, column=0, sticky="e", pady=5)

        self.house_number = customtkinter.CTkEntry(self,  width=145, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="House number", text_color="black")
        self.house_number.grid(row=8, column=0, sticky="w", pady=5)

        self.date_ofBirth = customtkinter.CTkEntry(self,  width=145, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="DD/MM/YYYY", text_color="black")
        self.date_ofBirth.grid(row=8, column=0, sticky="e", pady=5)

        self.financial_infromation = customtkinter.CTkLabel(self, text="Financial Infromation")
        self.financial_infromation.grid(row=9, column=0, sticky="w", padx=15, pady=10)

        self.salary = customtkinter.CTkEntry(self,  width=145, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="Salary", text_color="black")
        self.salary.grid(row=10, column=0, sticky="w", pady=5)

        self.income = customtkinter.CTkEntry(self,  width=145, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="Income", text_color="black")
        self.income.grid(row=10, column=0, sticky="e", pady=5)

        self.debt = customtkinter.CTkEntry(self,  width=145, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="Debt", text_color="black")
        self.debt.grid(row=11, column=0, sticky="w", pady=5)

        self.monthly_expences = customtkinter.CTkEntry(self,  width=145, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="Monthly expences", text_color="black")
        self.monthly_expences.grid(row=11, column=0, sticky="e", pady=5)

        self.initial_deposit = customtkinter.CTkEntry(self,  width=145, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="Initial deposit", text_color="black")
        self.initial_deposit.grid(row=12, column=0, sticky="w", pady=5)

        self.butonAc = customtkinter.CTkButton(self, text="Join us", command=self.CreateAcc)
        self.butonAc.grid(row=13, column=0, pady=20, sticky="s")



    def CreateAcc(self):
        print("CUNT")
        self.entries = [self.name, self.email, self.password, self.last_name,self.job_title, self.phone_number,
                        self.OIB, self.city, self.state, self.street, self.house_number, self.date_ofBirth,
                        self.salary, self.income, self.debt, self.monthly_expences, self.initial_deposit]

        f = open('../C files/Data.txt', 'wb')
        for i in self.entries:
            buffer = i.get()
            f.write(buffer.encode("utf-8"))
            f.write("/".encode("utf-8"))

        self.account_creatin = subprocess.run(["/.out", "Date.txt", "HashMap.bin", "CreateAccount",])




class OpeningFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self,text="Login System")
        self.label.place(x=120, y=25)

        self.entry1 = customtkinter.CTkEntry(master=self, width=120, height=25, fg_color=("white", "gray75"), corner_radius=8,placeholder_text_color="black" ,placeholder_text="Username", text_color="black")
        self.entry1.place(x=100, y=60)

        self.entry2 = customtkinter.CTkEntry(master=self, width=120, height=25, fg_color=("white", "gray75"), corner_radius=8,placeholder_text_color="black" ,placeholder_text="Password", show="*", text_color="black")
        self.entry2.place(x=100, y=90)



    def Login_credencials(self):
        username = self.entry1.get()
        password = self.entry2.get()
        return username, password


class MainScreen(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        """Leave for now"""



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

        self.my_frame = OpeningFrame(master=self,width=320, height=360, border_width=2, corner_radius=10)
        self.my_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.button = customtkinter.CTkButton(self.my_frame, text="Login", command=self.Login)
        self.button.place(x = 235, y = 320, anchor=tkinter.CENTER)

        self.newacc = customtkinter.CTkButton(self.my_frame, text="Create Account", command=self.Createaccount)
        self.newacc.place(x = 85, y = 320, anchor=tkinter.CENTER)


    def Login(self):
        username, password = self.my_frame.Login_credencials()
        if username == "user" and password == "pass":
            # Destroy the current MyFrame instance and replace it with MyFrame2
            self.my_frame.place_forget()
            self.button.place_forget()
            self.my_frame2 = MainScreen(master=self)
            self.my_frame2.pack(pady=20,padx=60, fill="both", expand=True)
            print("Hello world")


    def Createaccount(self):
        """This function should open a new frame which is goint to take in all nececery user data and call subproceccess to 
        create account and store data to the database"""
        self.my_frame.place_forget()
        self.button.place_forget()
        self.my_frame3 = CreateAccount(self, width=320, height=360, corner_radius=12)
        self.my_frame3.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)



app = App()
app.mainloop()
