import customtkinter
import tkinter
from PIL import Image
import subprocess
import os
import time

info = []
output = ""
i = 0

def strfunc() :
    history_file = "Path to dir that will contain transaction history"
    start = str(output).rfind("/") -1
    end = str(output).rfind(".") -1
    name = str((output[start:end]))
    history_file += str(name) + "history" + ".txt"
    return history_file

def AccData():
        global info
        with open(output, "r") as file:
            line = file.readline()
            while line:
                info.append(line.strip())  # remove newline character and append to list
                line = file.readline()


class Profile(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)



        self.name = customtkinter.CTkFrame(self, bg_color="black" ,fg_color=("#2e2e2e"),corner_radius=0)
        self.name.place(relwidth=1, relheight=0.307, relx=0.0, rely=0.0)

        self.label = customtkinter.CTkLabel(self.name, font=("bold",35),text=str("Name: " + info[0] + " " + info[3]), fg_color=("#2e2e2e"))
        self.label.place(relx=0.1, rely=0.2)

        self.label = customtkinter.CTkLabel(self, font=("bold",20),text=str("CC: " + info[19]))
        self.label.place(x=10, rely=0.4)

        self.label = customtkinter.CTkLabel(self, font=("bold",20),text=str("IBAN: " + info[20]))
        self.label.place(x=10, rely=0.5)

        self.label = customtkinter.CTkLabel(self, font=("bold",20),text=str("CVV: " + info[21]))
        self.label.place(x=10, rely=0.6)

        self.label = customtkinter.CTkLabel(self, font=("bold",20),text=str("CC exparation date: " + info[22]))
        self.label.place(x=10, rely=0.7)

        self.back = customtkinter.CTkButton(self, text="Back", command=self.Back)
        self.back.place(x=10, rely=0.9)

    def Back(self):
        self.destroy()

class Transfer(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title_frame = customtkinter.CTkFrame(self, bg_color="black" ,fg_color=("#2e2e2e"),corner_radius=0)
        self.title_frame.place(relwidth=1, relheight=0.3, relx=0.0, rely=0.0)

        self.deposit_frame = customtkinter.CTkFrame(self,corner_radius=0,fg_color=("#808080"))
        self.deposit_frame.place(relwidth=0.5, relheight=0.7, relx=1, rely=0.65, anchor="e")

        self.withdraw_frame = customtkinter.CTkFrame(self,corner_radius=0,fg_color=("#333333"))
        self.withdraw_frame.place(relwidth=0.5, relheight=0.7, relx=0, rely=0.65, anchor="w")

        self.label = customtkinter.CTkLabel(self.title_frame, font=("bold",35),text="Transfer", fg_color=("#333333"))
        self.label.place(relx=0.43, rely=0.0)


        self.amount = customtkinter.CTkEntry(self.deposit_frame, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="Amount", text_color="black")
        self.amount.place(relx=0.27, rely=0.1, relwidth=0.5)

        self.CC = customtkinter.CTkEntry(self.deposit_frame, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="CC", text_color="black")
        self.CC.place(relx=0.57, rely=0.3, relwidth=0.2)

        self.ccv = customtkinter.CTkEntry(self.deposit_frame, width=100, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="ccv", text_color="black")
        self.ccv.place(relx=0.27, rely=0.2,relwidth=0.2)

        self.exdate = customtkinter.CTkEntry(self.deposit_frame, width=110, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="Experation date", text_color="black")
        self.exdate.place(relx=0.57, rely=0.2,relwidth=0.23)

        self.iban_num = customtkinter.CTkEntry(self.deposit_frame, width=100, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="IBAN", text_color="black")
        self.iban_num.place(relx=0.27, rely=0.3,relwidth=0.2)

        self.button1 = customtkinter.CTkButton(self.deposit_frame, text="Deposit", command=self.Deposit)
        self.button1.place(relx=0.37, rely=0.5)

        self.amount1 = customtkinter.CTkEntry(self.withdraw_frame, width=220, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="Amount", text_color="black")
        self.amount1.place(relx=0.27, rely=0.1, relwidth=0.5)

        self.CC1 = customtkinter.CTkEntry(self.withdraw_frame, width=100, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="CC", text_color="black")
        self.CC1.place(relx=0.57, rely=0.3,relwidth=0.2)

        self.ccv1 = customtkinter.CTkEntry(self.withdraw_frame, width=100, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="ccv", text_color="black")
        self.ccv1.place(relx=0.27, rely=0.2,relwidth=0.2)

        self.exdate1 = customtkinter.CTkEntry(self.withdraw_frame, width=110, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="Experation date", text_color="black")
        self.exdate1.place(relx=0.57, rely=0.2,relwidth=0.23)

        self.iban_num1 = customtkinter.CTkEntry(self.withdraw_frame, width=100, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="IBAN", text_color="black")
        self.iban_num1.place(relx=0.27, rely=0.3,relwidth=0.2)

        self.button = customtkinter.CTkButton(self.withdraw_frame, text="Withdraw", command=self.Withdraw)
        self.button.place(relx=0.37, rely=0.5)

        self.entries = [self.CC, self.iban_num,self.ccv, self.exdate]
        self.entries1 = [self.CC1, self.iban_num1, self.ccv1, self.exdate1]

    def Deposit(self):

        history = "New deposit: "
        salary = ""
        lines = []

        salary = int(info[16])
        amount = int(self.amount.get())
        if amount <= 0:
            self.amount.delete(0, tkinter.END)
            self.amount.configure(placeholder_text="Invalid amount. Enter more thean 0")
            self.label.focus()
            return

        j = 19
        for m in self.entries:
            buffer = m.get()
            if str(buffer) != str(info[j]):
                self.amount.delete(0, tkinter.END)
                self.amount.configure(placeholder_text="Invalid CC credencials")
                self.label.focus()
                return
            elif j == 22:
                break
            j+=1

        salary += amount
        info[16] = str(salary)
        with open(output, 'r') as file:
            lines = file.readlines()

        with open(output, 'w') as file:
            lines[16] = str(salary) + '\n'
            file.writelines(lines)

        history_file = strfunc()
        with open(history_file, "a+") as hf:
            history += str(self.amount.get()) + '\n'
            history.encode('utf-8')
            hf.writelines(history)
        self.destroy()



    def Withdraw(self):

        history = "New withdraw: "
        salary = ""
        lines = []

        salary = int(info[16])
        amount = int(self.amount1.get())
        if amount <= 0:
            self.amount1.delete(0, tkinter.END)
            self.amount1.configure(placeholder_text="Invalid amount. Enter more thean 0")
            self.label.focus()
            return

        j = 19
        for m in self.entries1:
            buffer = m.get()
            if str(buffer) != str(info[j]):
                self.amount1.delete(0, tkinter.END)
                self.amount1.configure(placeholder_text="Invalid CC credencials")
                self.label.focus()
                return
            elif j == 22:
                break
            j+=1
        salary -= amount
        info[16] = str(salary)
        with open(output, 'r') as file:
            lines = file.readlines()

        with open(output, 'w') as file:
            lines[16] = str(salary) + '\n'
            file.writelines(lines)


        history_file = strfunc()
        print(history_file)
        with open(history_file, "a+") as hf:
            history += str(self.amount1.get()) + '\n'
            history.encode('utf-8')
            hf.writelines(history)
        self.destroy()



class MainScreen(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        n = 1

        self.button_frame = customtkinter.CTkFrame(master=self, bg_color="black" ,fg_color=("#333333"),corner_radius=0)
        self.button_frame.place(relwidth=0.2, relheight=1.0,relx=0.0, rely=0.5, anchor="w",bordermode="outside")

        self.balance_frame = customtkinter.CTkFrame(master=self,corner_radius=0,fg_color=("#2e2e2e"))
        self.balance_frame.place(relwidth=0.8, relheight=0.307, relx=0.6, rely=0.0, anchor="n")

        self.label = customtkinter.CTkLabel(self.balance_frame, font=("bold",35),text=str("Balance: " + info[16] + "$"), fg_color=("#2e2e2e"))
        self.label.place(relx=0.2, rely=0.2)

        self.history_frame = customtkinter.CTkScrollableFrame(master=self,corner_radius=0,fg_color=("#383838"))
        self.history_frame.place(relwidth=0.8, relheight=0.7, relx=1, rely=0.65, anchor="e")

        self.img = customtkinter.CTkImage(dark_image=Image.open(os.path.join("Path to image", "image name")),
                                          light_image=Image.open(os.path.join("Path to image", "image name" )),size=(50, 50))

        self.img1 = customtkinter.CTkImage(dark_image=Image.open(os.path.join("Path to image", "image name" )),
                                          light_image=Image.open(os.path.join("Path to image",  "image name")),size=(50, 50))

        self.img2 = customtkinter.CTkImage(dark_image=Image.open(os.path.join("Path to image",  "image name")),
                                          light_image=Image.open(os.path.join("Path to image",  "image name")),size=(50, 50))

        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(("Path to image",  "image name")), size=(180, 100))

        self.logout = customtkinter.CTkButton(self.button_frame,corner_radius=0, height=40, border_spacing=10, text="Logout",
                                                      font=("bold", 25),fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.img, anchor="w", command=self.LogOut)
        self.logout.place(relwidth=0.98, relheight=0.1, relx=0.01, rely=0.899)

        self.transfer = customtkinter.CTkButton(self.button_frame,corner_radius=0, height=40, border_spacing=10, text="Transfer",
                                                      font=("bold", 25),fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.img1, anchor="w", command=self.Transfer)
        self.transfer.place(relwidth=0.98, relheight=0.1, relx=0.01, rely=0.3)

        self.transfer = customtkinter.CTkButton(self.button_frame,corner_radius=0, height=40, border_spacing=10, text="Profile",
                                                      font=("bold", 25),fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.img2, anchor="w", command=self.Profile)
        self.transfer.place(relwidth=0.98, relheight=0.1, relx=0.01, rely=0.18)

        self.img_label = customtkinter.CTkLabel(self.button_frame,text="", image=self.logo_image,
                                                compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.img_label.place(relwidth=0.97, relheight=0.2, relx=0.02, rely=0.05, anchor="w")

        if n == 1:
            history_file = strfunc()
            try:
                hm = open(history_file, "x")
                hm.close()
            except:
                with open(history_file, "r") as hf:
                    line = hf.readline()
                    while line:
                        global i
                        self.histroy = customtkinter.CTkLabel(self.history_frame, text=str(line), fg_color=("#383838"))
                        self.histroy.grid(row=i, column=0, padx=10, pady=2)
                        i+=1
                        line = hf.readline()
                    history_file = "setting it to the orgiginal string"
                    i=0


    def Transfer(self):
        history_file = strfunc()
        self.transfer_frame = Transfer(self)
        self.transfer_frame.pack(fill="both", expand=True)
        self.wait_window(self.transfer_frame)
        with open(history_file, "r") as hf:
            line = hf.readline()
            while line:
                global i
                self.histroy = customtkinter.CTkLabel(self.history_frame, text=str(line), fg_color=("#383838"))
                self.histroy.grid(row=i, column=0, padx=10, pady=2)
                i+=1
                line = hf.readline()
        self.label.configure(text=str("Balance: " + info[16]))
        history_file = "Setting it to the orgiginal string"
        i=0


    def LogOut(self):
        info.clear()
        self.destroy()

    def Profile(self):
        self.profile = Profile(self,fg_color=("#383838"))
        self.profile.pack(expand=True, fill="both")



class CreateAccount(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


        self.grid_rowconfigure(0, weight=1) # type: ignore
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

        self.cc = customtkinter.CTkEntry(self,  width=145, height=25, fg_color=("white", "gray75"), placeholder_text_color="black", placeholder_text="type of credit card", text_color="black")
        self.cc.grid(row=12, column=0, sticky="e", pady=5)



    def CreateAcc(self):

        entries = [self.name, self.email, self.password, self.last_name,self.job_title, self.phone_number,
                        self.OIB, self.city, self.state, self.street, self.house_number, self.date_ofBirth,
                        self.salary, self.income, self.debt, self.monthly_expences, self.initial_deposit, self.cc]

        return entries


    def CleanEntires(self):
        entries = []
        entries = self.CreateAcc()
        for i in entries:
            i.delete(0, tkinter.END)


class OpeningFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self,text="Login System")
        self.label.place(x=120, y=25)

        self.entry1 = customtkinter.CTkEntry(master=self, width=120, height=25, fg_color=("white", "gray75"), corner_radius=8,placeholder_text_color="black" ,placeholder_text="Username", text_color="black")
        self.entry1.place(x=100, y=60)

        self.entry2 = customtkinter.CTkEntry(master=self, width=120, height=25, fg_color=("white", "gray75"), corner_radius=8,placeholder_text_color="black" ,placeholder_text="Password", show="*", text_color="black")
        self.entry2.place(x=100, y=90)

        self.login_faild = customtkinter.CTkLabel(self, text="Password or username invalid")
        self.login_faild.place(x=100, y=90)
        self.login_faild.place_forget()

    def Login_credencials(self):
        username = self.entry1.get()
        password = self.entry2.get()
        return username, password


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("BMS")
        self.geometry("1000x650")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        img = tkinter.PhotoImage(file=("Path to background image")
        self.imglabel = customtkinter.CTkLabel(master=self, image=img) # type: ignore
        self.imglabel.place(x=0, y=0, relwidth=1, relheight=1)

        self.my_frame = OpeningFrame(master=self,width=320, height=360, border_width=2, corner_radius=10)
        self.my_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.button = customtkinter.CTkButton(self.my_frame, text="Login", command=self.Login)
        self.button.place(x = 235, y = 320, anchor=tkinter.CENTER)

        self.newacc = customtkinter.CTkButton(self.my_frame, text="Create Account",command=self.CreateAccFrame)
        self.newacc.place(x = 85, y = 320, anchor=tkinter.CENTER)


    def CreateAccFrame(self):

        """This function should open a new frame which is goint to take in all nececery user data and call subproceccess from
        Createaccount function which creates accaunt and stores it to the the databas"""

        self.my_frame3 = CreateAccount(self, width=320, height=360, corner_radius=12)
        self.my_frame3.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.butonAc = customtkinter.CTkButton(self.my_frame3, text="Join us", command=self.Createaccount)
        self.butonAc.grid(row=13, column=0, pady=20, sticky="s")

        self.mainlabel = customtkinter.CTkLabel(self.imglabel, text="All fields must be filled")
        self.mainlabel.place(relx=0.5, y=50, anchor=tkinter.CENTER)

        self.butonAc = customtkinter.CTkButton(self.my_frame3, text="Back", command=self.Back)
        self.butonAc.grid(row=14, column=0, pady=20, sticky="s")

        self.my_frame.login_faild.place_forget()
        self.my_frame.label.focus()



    def Login(self):
        username, password = self.my_frame.Login_credencials()
        self.my_frame.entry1.delete(0,tkinter.END)
        self.my_frame.entry2.delete(0,tkinter.END)

        self.path = "Path to login.exe"
        self.hmpath = "Path to binary file containing hmdata"

        self.login = subprocess.run([self.path, username, password, self.hmpath], stdout=subprocess.PIPE)
        print(self.login.returncode)
        global output
        output = self.login.stdout
        print(output)
        if self.login.returncode == 0:
            AccData()
            self.my_frame.login_faild.place_forget()
            self.mainScreen()
        else:
            self.my_frame.login_faild.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            self.my_frame.login_faild.focus()



    def Createaccount(self):

        """Request data enterd by the user and writes to a file which is goint to be proccesess by './out'"""
        data = []
        global info
        data = self.my_frame3.CreateAcc()


        f = open("path to file that will contain data enterd in CreateAccount frame" 'wb')
        for i in data:
            buffer = i.get()
            if len(str(buffer))  == 0:
                return
            f.write(buffer.encode("utf-8"))
            f.write('\n'.encode("utf-8"))


        f.close()
        self.hmpath = "path to binary file containing hm data"
        self.path = "Path to file CreateAccount.exe"
        self.datapath = "path to file that will contain data enterd in CreateAccount frame"
        self.out = subprocess.run([self.path, self.hmpath, self.datapath], stdout=subprocess.PIPE)

        global output
        output = self.out.stdout
        print(output)
        if self.out.returncode == 0:
            self.my_frame3.place_forget()
            self.my_frame.login_faild.place_forget()
            AccData()
            self.mainlabel.place_forget()
            self.mainScreen()

    def Back(self):
        self.my_frame3.CleanEntires()
        self.my_frame3.place_forget()
        self.mainlabel.destroy()


    def mainScreen(self):
        self.frame = MainScreen(self)
        self.frame.pack(expand=True, fill="both")


def main():

    login_window = App()
    login_window.mainloop()


if __name__ == "__main__":
    # call the main function if the script is being run directly
    main()

