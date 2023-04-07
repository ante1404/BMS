import customtkinter
import tkinter
from PIL import ImageTk, Image
import subprocess

info = []
output = ""

class MainScreen(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.balance = 234534
        
        with open(output, "r", encoding=('utf-8')) as file:
            line = file.readline()
            while line:
                info.append(line.strip())  # remove newline character and append to list
                line = file.readline()

        
        self.button_frame = customtkinter.CTkFrame(master=self, bg_color="black" ,fg_color=("#1A2F3C"), border_width=2,corner_radius=0)
        self.button_frame.place(relwidth=0.2, relheight=1.0,relx=0.0, rely=0.5, anchor="w",bordermode="outside")
    
        self.balance_frame = customtkinter.CTkFrame(master=self, border_width=2,corner_radius=0,fg_color=("#222222")) 
        self.balance_frame.place(relwidth=0.8, relheight=0.307, relx=0.6, rely=0.0, anchor="n")
        
        self.label = customtkinter.CTkLabel(self.balance_frame, font=("bold",23),text=str(info[16]), fg_color=("#222222"))
        self.label.place(relx=0.2, rely=0.2)
        
        self.history_frame = customtkinter.CTkFrame(master=self,border_width=2,corner_radius=0)
        self.history_frame.place(relwidth=0.8, relheight=0.7, relx=1, rely=0.65, anchor="e")
        
        self.transfer = customtkinter.CTkButton(self.history_frame, text="Transfer", fg_color=("#222222"), command=self.Transfer)
        self.transfer.place(relwidth=0.1, relheight=0.1, relx=0.949, rely=0.004, anchor="n")
        
    def Transfer(self):
        info[16] = str(int(info[16]) + 1)
        self.label.configure(text=str(info[16]))
        
        

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
    
    
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("BMS")
        self.geometry("1000x650")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        img = tkinter.PhotoImage(file="C:/Users/Ante/Desktop/GUI/C files/pattern.png")
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
        
        
    def Login(self):
        username, password = self.my_frame.Login_credencials()
        
        self.path = 'C:/Users/Ante/Desktop/GUI/C files/login.exe'
        self.hmpath = 'C:/Users/Ante/Desktop/GUI/C files/HashMap.bin'
        
        self.login = subprocess.run([self.path, username, password, self.hmpath], stdout=subprocess.PIPE)
        print(self.login.returncode)
        global output
        output = self.login.stdout
        print(output)
        if self.login.returncode == 0:
            self.my_frame.place_forget()
            self.button.place_forget()
            self.mainScreen()
            
            
          
    def Createaccount(self):
        
        """Request data enterd by the user and writes to a file which is goint to be proccesess by './out'"""
        data = []
        global info
        data = self.my_frame3.CreateAcc()
        
        f = open('C:/Users/Ante/Desktop/GUI/C files/Data.txt', 'wb')
        for i in data:
            buffer = i.get()
            f.write(buffer.encode("utf-8"))
            f.write('\n'.encode("utf-8"))
            info.append(buffer)
            
        f.close()  
        self.hmpath = 'C:/Users/Ante/Desktop/GUI/C files/HashMap.bin'
        self.path = 'C:/Users/Ante/Desktop/GUI/C files/out.exe'
        self.datapath = 'C:/Users/Ante/Desktop/GUI/C files/Data.txt'
        self.output1 = 12
        self.out = subprocess.run([self.path, self.hmpath, self.datapath], stdout=subprocess.PIPE)
        
        global output
        output = self.out.stdout
        print(output)
        if self.out.returncode == 0:
            self.my_frame.place_forget()
            self.my_frame3.place_forget()
            self.mainScreen()
             
            
    def mainScreen(self):
        self.frame = MainScreen(self)
        self.frame.pack(expand=True, fill="both")
        
    
        
        
        
        
def main():
    
    login_window = App()
    
    
        

   
    login_window.mainloop()
    
    
if __name__ == "__main__":
    # call the main function if the script is being run directly
    main()
        
