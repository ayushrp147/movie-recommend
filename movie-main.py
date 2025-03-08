import customtkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import backend

side_img_data = Image.open("login-background.png")
new_img_data = Image.open("site-background.png")
user_data = {}

def read_user_data():
    try:
        with open("user_data.txt","r") as file:
            for line in file:
                username, password = line.strip().split(":")
                user_data[username] = password
    except FileNotFoundError:
        pass

def write_user_data():
    with open("user_data.txt", "w") as file:
        for username, password in user_data.items():
            file.write(f"{username}:{password}\n")

read_user_data()
write_user_data()

def login():
    username = e1.get()
    password = e2.get()
    if username in user_data and user_data[username]==password:
        u=e1.get()
        root.destroy()
        nw=customtkinter.CTk()
        nw.title("Movie Recommendation Site")
        nw.geometry("1600x800")
        bg_photo = customtkinter.CTkImage(dark_image=new_img_data, light_image=new_img_data, size=(1600,800))
        bg_label = customtkinter.CTkLabel(nw, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        frame=customtkinter.CTkScrollableFrame(master=nw,border_color="purple",border_width=1,bg_color="yellow",height=800,width=700,fg_color="#94ebdc")
        frame.pack(expand="True")
        label2=customtkinter.CTkLabel(frame,text="MOVIE RECOMMENDATION SITE",font=("Times New Roman",40),text_color="red",fg_color="transparent",bg_color="transparent")
        label2.pack(pady=20,padx=20)
        label=customtkinter.CTkLabel(frame,text=f"Welcome, {u}",fg_color="transparent",font=("Times New Roman",30),text_color="black")
        label.pack(padx=50,pady=10)
        l3=customtkinter.CTkLabel(frame,text="*MOVIES AVAILABLE TILL 2016",font=("Times New Roman",15,"bold"),text_color="green",fg_color="transparent")
        l3.pack(pady=(10,0))
        l3=customtkinter.CTkLabel(frame,text="*KINDLY FILL THE BELOW CHOICES TO GET YOUR DESIRED MOVIE",font=("Times New Roman",15,"bold"),text_color="green",fg_color="transparent")
        l3.pack(pady=(0,10))
        l4=customtkinter.CTkLabel(frame,text="Select the Genre: ",font=("Times New Roman",24),fg_color="transparent")
        l4.pack(pady=(10,0))
        genres=["Adventure","Action","Comedy","Drama","Romance","Sci-Fi","Mystery","Horror","Biography","Fantasy","Animation","History","Western"]
        options= customtkinter.CTkOptionMenu(frame, values=genres)
        options.pack(pady=20)
        l5=customtkinter.CTkLabel(frame,text="Select Minimum Runtime of Movie(minutes): ",font=("Times New Roman",24),fg_color="transparent")
        l5.pack()
        runtime=["100","110","120","150"]
        options1= customtkinter.CTkOptionMenu(frame, values=runtime)
        options1.pack(pady=20)
        l7=customtkinter.CTkLabel(frame,text="Minimum IMDB Rating: ",font=("Times New Roman",24),fg_color="transparent")
        l7.pack()
        e7=customtkinter.CTkEntry(frame,fg_color="transparent")
        e7.pack(pady=20)
        l8=customtkinter.CTkLabel(frame,text="Minimum Year of Movie Release: ",font=("Times New Roman",24),fg_color="transparent")
        l8.pack()
        e8=customtkinter.CTkEntry(frame,fg_color="transparent")
        e8.pack(pady=20)
        l6=customtkinter.CTkLabel(frame,text="Number of Movie to Recommend: ",font=("Times New Roman",24),fg_color="transparent")
        l6.pack()
        e6=customtkinter.CTkEntry(frame,fg_color="transparent")
        e6.pack(pady=20)
        frame1_list=[]
        def recom():
            for frame1 in frame1_list:
                frame1.destroy()
            frame1_list.clear()
            output=backend.recommend(options.get(),float(e7.get()),int(options1.get()),int(e8.get()),int(e6.get()))
            c=1
            for item in output:
                frame1=customtkinter.CTkFrame(master=frame,fg_color="#94ebdc")
                frame1.pack()
                frame1_list.append(frame1)
                label = customtkinter.CTkLabel(master=frame1, text=f"{c}. {item[0]}",text_color="red",font=("Times New Roman",15,"bold"))
                label.pack()
                label = customtkinter.CTkLabel(master=frame1, text=f"Description: {item[1]}\nYear Of Release: {item[2]}\nIMDB Rating: {item[3]}\nRuntime: {item[4]}\nGenre: {item[5]}",text_color="green",font=("Times New Roman",15,"bold"),wraplength=500)
                label.pack(pady=5)
                c+=1
        button=customtkinter.CTkButton(frame,text="Recommend",font=("Times New Roman",15),command=recom,hover_color="#4158D0")
        button.pack(pady=20)         
        nw.mainloop()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def signup():
    username = e1.get()
    password = e2.get()
    if username=="":
        messagebox.showerror("Sign Up Failed", "Username cannot be blank")
    elif password=="":
        messagebox.showerror("Sign Up Failed", "Password cannot be blank")
    elif username in user_data:
        messagebox.showerror("Sign Up Failed", "Username already exists")
    else:
        user_data[username] = password
        write_user_data()
        messagebox.showinfo("Sign Up Successful", "Account created successfully")

root=customtkinter.CTk()
root.geometry("1600x800")
bg_photo = customtkinter.CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(1000,800))
bg_label = customtkinter.CTkLabel(root,text="",image=bg_photo)
bg_label.pack_propagate(0)
bg_label.pack(expand=True,side="left")
frame=customtkinter.CTkFrame(master=root,border_color="purple",border_width=1,fg_color="#ffffff",height=800,width=600)
frame.pack(expand="True")
frame.pack_propagate(0)
l1=customtkinter.CTkLabel(master=frame,text="Login System",font=("Roboto",24,"bold"),anchor="center")
l1.pack(anchor="center",pady=(300,5),padx=10)
e1=customtkinter.CTkEntry(master=frame,placeholder_text="Username",width=250,height=30)
e1.pack(pady=12,padx=10)
e2=customtkinter.CTkEntry(master=frame,placeholder_text="Password",show="*",width=250,height=30)
e2.pack(pady=12,padx=10)
b1=customtkinter.CTkButton(master=frame,text="Login",command=login,fg_color="#C850C0",hover_color="#4158D0",corner_radius=32,height=35,width=200)
b1.pack(pady=12,padx=10)
b2=customtkinter.CTkButton(master=frame,text="Sign Up",command=signup,fg_color="#C850C0",hover_color="#4158D0",corner_radius=32,height=35,width=200)
b2.pack(pady=12,padx=10)
root.mainloop()