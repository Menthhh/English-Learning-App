# ============================================================= #
#  Python Individual Project, Year 1, Semester 1                #
#                                                               #
#  Course: COMPUTER PROGRAMMING [Section 1][65-1-01286121-1]    #
#  Program: Software Engineering Program                        #
#  University: Faculty of Engineering, KMITL                    #
#                                                               #
#  Project: Vocabs game                                         #
#  Written by: Tonkla Pokaew (65011610)                         #
# ============================================================= #

import wikipedia as wiki
from tkinter import*
from tkinter import messagebox
from tkinter import ttk    
import re
import ast
import os
import random
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk
import shutil
import webbrowser


project = Tk()
project.wm_iconbitmap('images/icon.ico')

class SignIn(object):
    global FONT, color
    FONT = 'Roboto'
    color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}
    def __init__(self,app):
        Label(app, text="note v 1.0",bg="white").pack(anchor="s",side="left")
        self.app = app
        self.SETUP_SIGN_IN()
        self.RUN_SIGN_IN()
        self.app.bind('<Return>', self.enter)

    def SETUP_SIGN_IN(self):
        self.app.geometry("500x700")
        self.app.title('Sign In')
        self.app.config(bg="#fff")
        self.app.resizable(False,False)
        self.app.wm_iconbitmap('images/icon.ico')

    def heading(self):
        self.img = PhotoImage(file="images/logo.png")
        self.image = Label(self.app, image=self.img,bg="white").place(x=75,y=50)

        self.frame = Frame(self.app, width=350, height=350, bg='white')
        self.frame.place(x=75,y=300)

        self.heading = Label(self.app, text="Sign in", fg="orange",bg="white",font=(FONT,23,'bold'))
        self.heading.place(x=200,y=300)

    def username(self):
        #Username
        self.user = Entry(self.frame, width = 30,fg='black',border=0,bg='white',font=(FONT,11,"italic"))
        self.user.place(x=25,y=80)
        self.user.insert(0,"Username or Email")
        Frame(self.frame,width= 295,height=2,bg="black").place(x=25,y=100)

        self.user.bind("<FocusIn>",self.on_enter)
        self.user.bind("<FocusOut>",self.on_leave)

    def enter(self,event):
        self.sign_in_button()

    def on_enter(self,e):
        self.user.delete(0,END)

    def on_leave(self,e):
        name = self.user.get()
        if name == '':
            self.user.insert(0,'Username or Email')

    def password(self):
        #Password
        self.password = Entry(self.frame, width = 30,fg='black',border=0,bg='white',font=(FONT,11,"italic"))
        self.password.place(x=25,y=160)
        self.password.insert(0,'Password')
        Frame(self.frame,width= 295,height=2,bg="black").place(x=25,y=180)

        self.password.bind("<FocusIn>",self.on_enter_p)
        self.password.bind("<FocusOut>",self.on_leave_p)

    def on_enter_p(self,a):
        self.password['show'] = "*"
        self.password.delete(0,END)

    def on_leave_p(self,a):
        name = self.password.get()
        if name == '':
            self.password['show'] = ""
            self.password.insert(0,'Password')

    def sign_in(self):
        #Sign in button
        Button(self.frame, width=39, pady=7,text='Sign in', bg='orange',fg='white',border=0, command=self.sign_in_button).place(x=35,y=230)

    def sign_up(self):
        #Sign up
        self.label = Label(self.frame, text="Don't have an account ?",fg="black",bg="white",font=(FONT,9))
        self.label.place(x=40,y=280)

        self.signup_button = Button(self.frame, width=6,text='sign up', border=0, bg='white',cursor='hand2',fg="#57a1f8",command=self.sign_up_button)
        self.signup_button.place(x=180,y=279)

    def sign_in_button(self):
        email = 0
        password = 1
        Email = self.user.get()
        Username = self.user.get()
        Password = self.password.get()
        
        file = open("data/datasheet.txt",'r')
        d = file.read()
        r = ast.literal_eval(d)
        file.close()

        email_lst = {}
        for key, value in r.items():
            email_lst.update({value[email]:value[password]})
        # print(email_lst)

        if Username == '' or Password == '':
            messagebox.showerror('Error','Please enter username and password')

        elif Username == 'Username' or Password == 'Password':
            messagebox.showerror('Error','Please enter username and password')

        elif Username in r.keys() and Password == r[Username][password]:
            self.app.destroy()
            user = Tk()
            user.wm_iconbitmap('images/icon.ico')
            d = Menu(user,Email,Username)
            user.mainloop()

        elif Email in email_lst.keys() and Password == email_lst[Email]:
            self.app.destroy()
            user = Tk()
            user.wm_iconbitmap('images/icon.ico')
            d = Menu(user,Email,Username)
            user.mainloop()

        elif Username == 'admin' and Password == '1234':
            self.app.destroy()
            admin = Tk()
            admin.wm_iconbitmap('images/icon.ico')
            d = Admin(admin)
            admin.mainloop()

        #if not in all the above conditions then show error message box 
        else:
            messagebox.showerror('Error','Invalid username or password')
                 
    def forget_password(self):
        self.forget = Button(self.frame, text='Forget password?', border=0, bg='white',cursor='hand2',fg="#57a1f8",command=self.forget_password_button)
        self.forget.place(x=230,y=279)

    def forget_password_button(self):
        messagebox.showinfo('Forget password','Please contact admin')
        
    def sign_up_button(self):
        self.app.destroy()
        sign_up = Tk()
        sign_up.wm_iconbitmap('images/icon.ico')
        b = SignUp(sign_up)
        sign_up.mainloop()

    def toggle_password(self):
        if self.checkbutton.var.get():
            self.password['show'] = ""
        else:
            self.password['show'] = "*"    

    def show_password(self,xa,ya):
        self.password.default_show_val = self.password['show']
        self.password['show'] = ""
        self.checkbutton = Checkbutton(self.frame,text="Show password",onvalue=True,offvalue=False,command=self.toggle_password,bg='white')
        self.checkbutton.var = BooleanVar(value=False)
        self.checkbutton['variable'] = self.checkbutton.var
        self.checkbutton.place(x=xa,y=ya)

    def RUN_SIGN_IN(self):
        self.heading()
        self.username()
        self.password()
        self.sign_in()
        self.sign_up()
        self.show_password(25,190)
        self.forget_password()

class SignUp(object):
    global FONT
    FONT = 'Roboto'
    def __init__(self,app):
        Label(app, text="note v 1.0",bg="white").pack(anchor="s",side="left")
        self.app = app
        self.SETUP_SIGN_UP()
        self.RUN_SIGN_UP()
        self.app.bind('<Return>', self.enter)

    def heading(self):
        self.img = PhotoImage(file="images/logo.png")
        self.image = Label(self.app, image=self.img,bg="white").place(x=230,y=100,anchor="center")

        self.frame = Frame(self.app, width=350, height=500, bg='white')
        self.frame.place(x=250,y=420,anchor="center")

        self.heading = Label(self.frame, text="Sign up", fg="orange",bg="white",font=(FONT,23,'bold'))
        self.heading.place(x=175,y=40,anchor="center")

    def email(self):
        #email
        self.email = Entry(self.frame, width = 30,fg='black',border=0,bg='white',font=(FONT,11,"italic"))
        self.email.place(x=25,y=100)
        self.email.insert(0,"Email")
        Frame(self.frame,width= 295,height=2,bg="black").place(x=25,y=120)

        self.email.bind("<FocusIn>",self.on_enter_email)
        self.email.bind("<FocusOut>",self.on_leave_email)

    def username(self):
        #Username
        self.username = Entry(self.frame, width = 30,fg='black',border=0,bg='white',font=(FONT,11,"italic"))
        self.username.place(x=25,y=180)
        self.username.insert(0,"Username")
        Frame(self.frame,width= 295,height=2,bg="black").place(x=25,y=200)

        self.username.bind("<FocusIn>",self.on_enter)
        self.username.bind("<FocusOut>",self.on_leave)

    def password(self):
        #password
        self.password = Entry(self.frame, width = 30,fg='black',border=0,bg='white',font=(FONT,11,"italic"))
        self.password.place(x=25,y=260)
        self.password.insert(0,"Password")
        Frame(self.frame,width= 295,height=2,bg="black").place(x=25,y=280)

        self.password.bind("<FocusIn>",self.on_enter_p)
        self.password.bind("<FocusOut>",self.on_leave_p)

    def ConPassword(self):
        #Password
        self.ConPassword = Entry(self.frame, width = 30,fg='black',border=0,bg='white',font=(FONT,11,"italic"))
        self.ConPassword.place(x=25,y=340)
        self.ConPassword.insert(0,"Confirm password")
        Frame(self.frame,width= 295,height=2,bg="black").place(x=25,y=360)

        self.ConPassword.bind("<FocusIn>",self.on_enter_c)
        self.ConPassword.bind("<FocusOut>",self.on_leave_c)

    def on_enter_email(self,e):
        self.email.delete(0,END)

    def on_leave_email(self,e):
        name = self.email.get()
        if name == '':
            self.email.insert(0,'Email')

    def enter(self,event):
        self.sign_up_button()

    def on_enter(self,e):
        self.username.delete(0,END)

    def on_leave(self,e):
        name = self.username.get()
        if name == '':
            self.username.insert(0,'Username')

    def on_enter_p(self,a):
        self.password['show'] = "*"
        self.password.delete(0,END)

    def on_leave_p(self,a):
        self.password['show'] = "*"
        name = self.password.get()
        if name == '':
            self.password['show'] = ""
            self.password.insert(0,'Password')

    def on_enter_c(self,a):
        self.ConPassword['show'] = "*"
        self.ConPassword.delete(0,END)

    def on_leave_c(self,a):
        name = self.ConPassword.get()
        if name == '':
            self.ConPassword['show'] = ""
            self.ConPassword.insert(0,'Confirm password')

    def sign_up(self):
        Button(self.frame, width=39, pady=7,text='Sign up', bg='orange',fg='white',border=0, command=self.sign_up_button).place(x=35,y=410)
    
    def sign_in(self):

        self.label = Label(self.frame, text="I have an account.",fg="black",bg="white",font=(FONT,9))
        self.label.place(x=100,y=460)

        self.signup_button = Button(self.frame, width=6,text='sign in', border=0, bg='white',cursor='hand2',fg="#57a1f8",command=self.sign_In_button)
        self.signup_button.place(x=200,y=459)

    def sign_In_button(self):
        self.app.destroy()
        sign_in = Tk()
        sign_in.wm_iconbitmap('images/icon.ico')
        b = SignIn(sign_in)
        sign_in.mainloop()

    def sign_up_button(self):
        Email = self.email.get()
        Username = self.username.get()
        Password = self.password.get()
        Confirm = self.ConPassword.get()

        file = open("data/datasheet.txt","r+")
        d = file.read()
        r = ast.literal_eval(d)

        if Email == "" or Email == "Email" or Username == "" or Password == "" or Confirm == "" or Username == "Username" or Password == "Password" or Confirm == "Confirm password":
            messagebox.showerror("Error","Please fill in all the boxes")

        elif Email in r:
            messagebox.showerror("Error","Email already exist")

        #check email in email format 
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", Email):
            messagebox.showerror("Error","Invalid email format, example: name@gmail.com")

        elif Username in r:
            messagebox.showerror("Error","Username already exist")
        #set password length to 8 characters 
        elif len(Password) < 8:
            messagebox.showerror("Error","Password must be at least 8 characters")

        elif Confirm == Password and Username not in r and Email not in r:
            try:
            #save email, username, password to a file
                r[Username] = [Email,Password]
                file = open("data/datasheet.txt","w")
                file.write(str(r))
                file.close()
                messagebox.showinfo("Success","Account created")
                file = open("data/"+Username+".txt","w")
                file.close()
                self.app.destroy()
                sign_in = Tk()
                sign_in.wm_iconbitmap('images/icon.ico')
                b = SignIn(sign_in)
                sign_in.mainloop()
                #create new new folder for each user in auidio folder 
                os.mkdir("audio/"+Username)
                #create instantly a new folder for each user in auidio folder by do not need to restart the app 

            except:
                messagebox.showerror("Error","Something went wrong")


        else:
            messagebox.showerror("Error","Password does not matched")
    
    def RUN_SIGN_UP(self):
        self.heading()
        self.ConPassword()
        self.password()
        self.sign_up()
        self.sign_in()
        self.username()
        self.email()
        self.show_password(25,370)

    def SETUP_SIGN_UP(self):
        self.app.geometry("500x700")
        self.app.title('Sign Up')
        self.app.config(bg="#fff")
        self.app.resizable(False,False)

    def toggle_password(self):
        if self.checkbutton.var.get():
            self.password['show'] = ""
            self.ConPassword['show'] = ""
        else:
            self.password['show'] = "*" 
            self.ConPassword['show'] = "*"   

    def show_password(self,xa,ya):
        self.password.default_show_val = self.password['show']
        self.password['show'] = ""
        self.ConPassword.default_show_val = self.ConPassword['show']
        self.ConPassword['show'] = ""
        self.checkbutton = Checkbutton(self.frame,text="Show password",onvalue=True,offvalue=False,command=self.toggle_password,bg='white')
        self.checkbutton.var = BooleanVar(value=False)
        self.checkbutton['variable'] = self.checkbutton.var
        self.checkbutton.place(x=xa,y=ya)

class English_audio:
    def __init__(self,english_audio, background_color, top):
        self.english_audio = english_audio
        self.background_color = background_color
        self.top = top
        self.page()

    def page(self):
        Label(self.english_audio,text="English Audio",font=('Comic Sans MS',30),bg='white',fg="green").pack()
        # Initialze Pygame Mixer
        pygame.mixer.init()
        self.songbox = Listbox(self.english_audio,font=('Comic Sans MS',15),bg='black',fg="white",width=60,selectbackground='grey')
        self.songbox.pack(pady=20)
        self.load_file()

        self.controls_frame = Frame(self.english_audio,bg='white')
        self.controls_frame.pack()

        self.back_btn_img = PhotoImage(file="images/previous.png")
        self.forward_btn_img = PhotoImage(file="images/next.png")
        self.play_btn_img = PhotoImage(file="images/play64.png")
        self.pause_btn_img = PhotoImage(file="images/pause64.png")
        self.add_img = PhotoImage(file="images/add64.png")
        self.del_img = PhotoImage(file="images/delete64.png")

        #display the buttons on the screen \\
            
        self.songbox.bind("<Double-Button-1>",self.play)
        self.songbox.bind("<Delete>",self.delete_song)

        self.back_btn = Button(self.controls_frame, image=self.back_btn_img, borderwidth=0,bg='white', command=self.back)
        self.forward_btn = Button(self.controls_frame, image=self.forward_btn_img, borderwidth=0, bg='white',command=self.forward)
        self.play_btn = Button(self.controls_frame, image=self.play_btn_img, borderwidth=0, bg='white',command=self.play)
        self.add = Button(self.controls_frame, image=self.add_img, borderwidth=0, bg='white',command=self.add_songs_byfile)
        self.delete = Button(self.controls_frame, image=self.del_img, borderwidth=0, bg='white',command=self.delete_song)

        self.add.grid(row=0,column=0,padx=10)
        self.back_btn.grid(row=0,column=1,padx=10)
        self.play_btn.grid(row=0,column=2,padx=10)
        self.forward_btn.grid(row=0,column=3,padx=10)
        self.delete.grid(row=0,column=4,padx=10)

        self.current_song_label = Label(self.controls_frame, text="", font=('Comic Sans MS',12),bg='white',fg="green")
        self.current_song_label.grid(row=1, column=1, columnspan=3, pady=10)

    def add_songs_byfile(self):
        self.songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose one or more songs", filetypes=(("mp3 Files", "*.mp3"),))
        destination_folder = "audio/"

        for song in self.songs:
            mp3_name = os.path.basename(song)
            if not os.path.exists(os.path.join(destination_folder, mp3_name)):
                shutil.copy(song, destination_folder)
                self.songbox.insert(END, mp3_name)
            else:
                messagebox.showerror("Error",f"A file with the name {mp3_name} already exists in the destination folder. Skipping.")

    def delete_song(self,event=None):
        try:
            pygame.mixer.music.unload()
            pygame.mixer.music.stop()
            name = self.songbox.get(ANCHOR)
            self.songbox.delete(ANCHOR)
            os.remove('audio/'+name)
            self.current_song_label['text'] = ""
            self.play_btn.config(image=self.play_btn_img, command=self.play)
        except:
            messagebox.showerror("Error","Please select files")

    def load_file(self):
        #add the song from /audio folder to the listbox
        for file in os.listdir("audio/"):
            if file.endswith(".mp3"):
                self.songbox.insert(END,file)

    def back(self):
        try:
            self.next = self.songbox.curselection()
            self.next = self.next[0] - 1
            self.name = self.songbox.get(self.next)
            self.name = "audio/" + self.name

            pygame.mixer.music.load(self.name)
            pygame.mixer.music.play(loops=0)

            self.songbox.selection_clear(0, END)
            self.songbox.activate(self.next)
            self.songbox.selection_set(self.next, last=None)
            #if pause is pressed then the next song will be played
            self.play_btn.config(image = self.pause_btn_img)
            self.play_btn.config(command=self.pause)
            self.current_song_label.config(text=os.path.basename(self.name))
        except:
            messagebox.showerror("Error","No files is selected.")

    def forward(self):
        try:
            self.next = self.songbox.curselection()
            self.next = self.next[0] + 1
            self.name = self.songbox.get(self.next)
            self.name = "audio/" + self.name

            pygame.mixer.music.load(self.name)
            pygame.mixer.music.play(loops=0)

            self.songbox.selection_clear(0, END)
            self.songbox.activate(self.next)
            self.songbox.selection_set(self.next, last=None)
            #if pause is pressed then the next song will be played
            self.play_btn.config(image = self.pause_btn_img)
            self.play_btn.config(command=self.pause)
            self.current_song_label.config(text=os.path.basename(self.name))

        except:
            messagebox.showerror("Error","No files is selected.")

    def play(self, event=None):
        self.plays = self.songbox.get(ACTIVE)
        self.plays = "audio/" + self.plays
        pygame.mixer.music.load(self.plays)
        pygame.mixer.music.play(loops=0)
        self.play_btn.config(image = self.pause_btn_img)
        self.play_btn.config(command=self.pause)
        self.current_song_label.config(text=os.path.basename(self.plays)) 


    def pause(self):
        if pygame.mixer.music.get_busy():  # Check if music is currently playing
            pygame.mixer.music.pause()  # Pause the music
            self.play_btn.config(image = self.play_btn_img)  # Update the button image to show "play"
        else:
            pygame.mixer.music.unpause()  # Unpause the music
            self.play_btn.config(image = self.pause_btn_img)  # Update the button image to show "pause"

    def delete_pages(self):
        for widget in self.english_audio.winfo_children():
            widget.destroy()
    
    def stop_music(self):
        pygame.mixer.music.stop()

class Menu(English_audio):
    global color
    def __init__(self,menu,email,username):
        self.menu = menu
        self.email = email
        self.username = username
        self.SETUP_MENU()
        self.page()
    
    def SETUP_MENU(self):
        self.sidecolor = "orange"
        self.navbarcolor = "orange"
        self.background_color = "white"
        self.buttonfontcolor = "black"
        self.menu.geometry("%dx%d" % (900, 800))
        self.menu.title('Menu')
        self.menu.config(bg=self.background_color)
        self.navIcon = PhotoImage(file="images/menu.png")
        self.closeIcon = PhotoImage(file="images/close.png")
        self.btnState = False

    def page(self):
        self.topFrame = Frame(self.menu, bg=self.navbarcolor)
        self.topFrame.pack(side="top", fill=X)

        self.back_level = Frame(self.menu, bg=self.background_color)
        self.back_level.place(x=0, y=90, relwidth=1, relheight=1)

        # Header label text:
        self.homeLabel = Label(self.topFrame, text=f"{self.username}", font=('Comic Sans MS',15), bg=self.navbarcolor, fg=self.background_color, height=2, padx=20)
        self.homeLabel.pack(side="right")

        # Navbar button:
        self.navbarBtn = Button(self.topFrame, image=self.navIcon, bg=self.navbarcolor, activebackground=self.navbarcolor, bd=0, padx=20, command=self.switch)
        self.navbarBtn.place(x=10, y=10)

        self.home()
        # setting Navbar frame:
        self.navRoot = Frame(self.menu, bg=self.sidecolor, height=1000, width=300)
        self.navRoot.place(x=-300, y=0)
        Label(self.navRoot, font=('Comic Sans MS',15), bg=self.navbarcolor, fg="black", height=2, width=300, padx=20).place(x=0, y=0)

        # set y-coordinate of Navbar widgets:
        y = 80
        # option in the navbar:
        options = ["Home","Vocab game","English audio","Read article","review vocabs","Logout", "Settings", "Help", "About", "Feedback"]
        self.translate_img = PhotoImage(file="images/translate32.png")
        # Navbar Option Buttons
        Button(self.navRoot, text=options[0], font=('Comic Sans MS',20), bg=self.sidecolor, fg=self.buttonfontcolor, activebackground=self.sidecolor, activeforeground="green", bd=0,command=self.home).place(x=25, y=10)
        Button(self.navRoot, text=options[1], font=('Comic Sans MS',15), bg=self.sidecolor, fg=self.buttonfontcolor, activebackground=self.sidecolor, activeforeground="green", bd=0,command=self.flashcard).place(x=25, y=80)
        Button(self.navRoot, text=options[2], font=('Comic Sans MS',15), bg=self.sidecolor, fg=self.buttonfontcolor, activebackground=self.sidecolor, activeforeground="green", bd=0,command=self.english_audio).place(x=25, y=120)
        Button(self.navRoot, text=options[3], font=('Comic Sans MS',15), bg=self.sidecolor, fg=self.buttonfontcolor, activebackground=self.sidecolor, activeforeground="green", bd=0, command=self.read_article).place(x=25, y=160)
        Button(self.navRoot, text=options[5], font=('Comic Sans MS',15), bg=self.sidecolor, fg=self.buttonfontcolor, activebackground=self.sidecolor, activeforeground="green", bd=0, command=self.signout).place(x=25, y=200)
        self.translateBtn = Button(self.topFrame, image =self.translate_img, font=('Comic Sans MS',15), bg=self.navbarcolor,activebackground=self.sidecolor, borderwidth=0,command=self.translate)
        self.translateBtn.pack(side="right")

        # Navbar Close Button
        closeBtn = Button(self.navRoot, image=self.closeIcon, bg = self.navbarcolor, activebackground=self.navbarcolor, bd=0, command=self.switch)
        closeBtn.place(x=250, y=10)

    def home(self):
        self.delete_pages()
        open = Home(self.back_level,self.email,self.username)
    def flashcard(self):
        self.delete_pages()
        open = Flashcard(self.back_level,self.background_color,self.topFrame,self.username)

    def english_audio(self):
        self.delete_pages()
        open = English_audio(self.back_level,self.background_color,self.topFrame)

    def read_article(self):
        self.delete_pages()
        open = Reading(self.back_level)

    def translate(self):
        webbrowser.open("https://translate.google.co.th/?hl=th")

    # def start_webview(self):
    #     tk = Tk()
    #     tk.geometry("800x450")
    #     webview.create_window('Translate', "https://translate.google.co.th/")
    #     webview.start()

    def close_navbar(self):
        self.navRoot.place(x=-300, y=0)
        self.topFrame.update()
        self.btnState = False

    def delete_pages(self):
        for widget in self.back_level.winfo_children():
            widget.destroy()

    def signout(self):
        try:
            if pygame.mixer.music.get_busy():
                self.stop_music()
                self.menu.destroy()
                tk = Tk()
                g = SignIn(tk)
                tk.mainloop()
            else:
                self.menu.destroy()
                tk = Tk()
                g = SignIn(tk)
                tk.mainloop()
        except:
            self.menu.destroy()
            tk = Tk()
            g = SignIn(tk)
            tk.mainloop()

    def switch(self):
        if self.btnState is True:
            # create animated Navbar closing:
            for x in range(301):
                self.navRoot.place(x=-x, y=0)
                self.topFrame.update()

            # resetting widget colors:
            self.homeLabel.config(bg=self.navbarcolor)
            self.topFrame.config(bg=self.navbarcolor)
            self.menu.config(bg=self.background_color)

            # turning button OFF:
            self.btnState = False
            self.translateBtn.pack(side="right")
        else:
            # make root dim:
            self.homeLabel.config(bg=self.background_color)
            self.topFrame.config(bg=self.background_color)
            self.menu.config(bg=self.background_color)
            self.translateBtn.pack_forget()

            # created animated Navbar opening:
            for x in range(-300, 0):
                self.navRoot.place(x=x, y=0)
                self.topFrame.update()

            # turing button ON:
            self.btnState = True

class Home(English_audio):
    def __init__(self,home,email,username):
        self.home = home
        self.email = email
        self.username = username
        try:
            if pygame.mixer.music.get_busy():
                self.home_page()
                self.stop_music()
            else:
                self.home_page()
        except:
            self.home_page()

    def home_page(self):

        # Home Page Label 
        self.home_label = Label(self.home, text="Home Page", font=('Comic Sans MS',30), fg="black",bg='white',padx=10,pady=10)
        self.home_label.place(anchor='center', relx=0.5, rely=0.05)

        self.facebook_img = PhotoImage(file="images/facebook64.png")
        self.discord_img = PhotoImage(file="images/discord64.png")
        self.logo_img = PhotoImage(file="images/logo.png")

        #welcome message with username and email
        self.welcome = Label(self.home, image=self.logo_img,bg='white')
        self.welcome.place(anchor='center', relx=0.5, rely=0.2)

        #create contact button
        self.facebook = Button(self.home, image=self.facebook_img, borderwidth=0 ,bg='white', activebackground='white', activeforeground="white",command=self.contact_facebook)
        self.facebook.place(anchor='center', relx=0.45, rely=0.4)

        self.discord = Button(self.home, image=self.discord_img, borderwidth=0 ,bg='white', activebackground='white', activeforeground="white",command=self.contact_discord)
        self.discord.place(anchor='center', relx=0.55, rely=0.4)

    def contact_discord(self):
        webbrowser.open("https://discord.gg/HAt2j6yhyQ")

    def contact_facebook(self):
        pass

class Flashcard(English_audio):
    def __init__(self,flashcard,background_color,top,username):
        self.username = username
        self.background_color = background_color
        self.flashcard = flashcard
        self.top = top
        try:
            if pygame.mixer.music.get_busy():
                self.flashcard_page()
                self.stop_music()
            else:
                self.flashcard_page()
        except:
            self.flashcard_page()

    def flashcard_page(self):
        self.aaa = Label(self.flashcard, text="Vocab game", font=('Comic Sans MS',30), bg=self.background_color, fg="green",background=self.background_color)
        self.aaa.place(anchor='center', relx=0.5, rely=0.1)

        self.toefl = Button(self.flashcard, text="TOEFL Vocabs", font=('Comic Sans MS',20), bg='black', fg="yellow", activebackground=self.background_color, activeforeground="green",width=30,command=self.toefl_flashcard)
        self.ielts = Button(self.flashcard, text="IELTS Vocabs", font=('Comic Sans MS',20), bg='black', fg="yellow", activebackground=self.background_color, activeforeground="green",width=30,command=self.ielts_flashcard)
        
        self.toefl.place(anchor='center', relx=0.5, rely=0.3)
        self.ielts.place(anchor='center', relx=0.5, rely=0.4)

    def toefl_flashcard(self):
        self.delete_pages()
        open = TOEFL_flashcard(self.flashcard,self.top,self.username)

    def ielts_flashcard(self):
        self.delete_pages()
        open = IELTS_flashcard(self.flashcard,self.top,self.username)

    def delete_pages(self):
        for widget in self.flashcard.winfo_children():
            widget.destroy()
    
class IELTS_flashcard:
    def __init__(self,ielts,top,username):
        self.username = username
        self.ielts = ielts
        self.top = top
        self.score = 0
        self.importfile()
        self.load_ielts_score()
        self.page()
      
    def page(self):
        self.delete_pages()
        self.save_ielts_score()
        #create frame line surrounding the page border line color = black
        self.frame = LabelFrame(self.ielts, bg="black")
        self.frame.pack()

        self.label = Label(self.ielts,text="IELTS Vocabs",font=('Comic Sans MS',30),bg="white",fg="green")
        self.label.place(anchor='n', relx=0.5, rely=0)

        #display score
        self.score_label = Label(self.ielts,text='Score: ' + str(self.score),font=('Comic Sans MS',20),bg="white",fg="black")
        self.score_label.place(anchor='n', relx=0.8, rely=0)

        self.high_score_label = Label(self.ielts,text='High Score: ' + str(self.high_score),font=('Comic Sans MS',20),bg="white",fg="black")
        self.high_score_label.place(anchor='n', relx=0.8, rely=0.05)

        self.reset_img = PhotoImage(file="images/reset.png")
        self.restart_scoreBtn = Button(self.ielts, image=self.reset_img, borderwidth=0 ,bg='white', activebackground='green', activeforeground="green",command=self.restart_score)
        self.restart_scoreBtn.place(anchor='n', relx=0.8, rely=0.15)

        #random word and meaning from dictionary 
        self.random_word = random.choice(list(self.words.keys()))
        self.random_meaning = self.words[self.random_word]

        #display word and meaning as a choice to let user choose the correct meaning 
        self.word = Label(self.ielts,text=self.random_word,font=('Comic Sans MS',75),bg="black",fg="white",padx=10)
        self.word.place(anchor='center', relx=0.5, rely=0.3)
        
        #random the number in place list to random the position of meaning 
        place = [0.5,0.6,0.7,0.8]
        self.random_place = random.choice(place)
        self.ch = []
        for i in range(3):
            cho = random.randint(0,len(self.meaning)-1)
            if cho not in self.ch and cho != self.meaning.index(self.random_meaning):
                self.ch.append(cho)

            else:
                while cho in self.ch or cho == self.meaning.index(self.random_meaning):
                    cho = random.randint(0,len(self.meaning)-1)
                self.ch.append(cho)

        #random 4 choices of meaning and place in different position for word and 4 choices must be different 
        self.choice1 = Button(self.ielts,text=self.random_meaning,font=('Comic Sans MS',15),bg="white",padx=15,pady=15,command=self.correct)
        self.choice1.place(anchor='center', relx=0.5, rely= self.random_place)
        place.remove(self.random_place)
        self.random_place = random.choice(place)

        self.choice2 = Button(self.ielts,text=self.meaning[self.ch[0]],padx=15,pady=15,font=('Comic Sans MS',15),bg="white",command=self.wrong)
        self.choice2.place(anchor='center', relx=0.5, rely= self.random_place)

        place.remove(self.random_place)
        self.random_place = random.choice(place)

        self.choice3 = Button(self.ielts,text=self.meaning[self.ch[1]],padx=15,pady=15,font=('Comic Sans MS',15),bg="white",command=self.wrong)
        self.choice3.place(anchor='center', relx=0.5, rely= self.random_place)
        
        place.remove(self.random_place)
        self.random_place = random.choice(place)

        self.choice4 = Button(self.ielts,text=self.meaning[self.ch[2]],padx=15,pady=15,font=('Comic Sans MS',15),bg="white",command=self.wrong)
        self.choice4.place(anchor='center', relx=0.5, rely= self.random_place)
        place.remove(self.random_place)
        self.ch.clear()

    def save_ielts_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open(f"data/{self.username}.txt","r+")
            d = file.read()
            r = ast.literal_eval(d)
            r['ielts'] = self.high_score
            file = open(f"data/{self.username}.txt","w")
            file.write(str(r))
            file.close()
        else:
            pass

    def load_ielts_score(self):
        file = open(f"data/{self.username}.txt",'r')
        d = file.read()
        r = ast.literal_eval(d)
        file.close()
        self.high_score = r["ielts"]

    def restart_score(self):
        self.high_score = 0
        self.score = 0
        file = open(f"data/{self.username}.txt","r+")
        d = file.read()
        r = ast.literal_eval(d)
        r['ielts'] = self.high_score
        file = open(f"data/{self.username}.txt","w")
        file.write(str(r))
        file.close()
        self.word.destroy()
        self.choice1.destroy()
        self.choice2.destroy()
        self.choice3.destroy()
        self.choice4.destroy()
        self.page()

    def correct(self):
        #add sound effect when user choose the correct answer
        pygame.mixer.init()
        self.correct_sound = pygame.mixer.Sound("sound/correct.wav")
        self.correct_sound.play()
        #delete the word and meaning 
        self.word.destroy()
        self.choice1.destroy()
        self.choice2.destroy()
        self.choice3.destroy()
        self.choice4.destroy()
        #display correcct message
        self.correct_sym = Label(self.ielts,text="\u2713Correct" ,font=('Comic Sans MS',50),bg="white",fg="green",padx=10,pady=10)
        self.correct_sym.place(anchor='center', relx=0.5, rely=0.4)
       
        self.correct_word = Label(self.ielts,text=self.random_word,font=('Comic Sans MS',70),bg="black",fg="white",padx=10,pady=10,wraplength=1000)
        self.correct_word.place(anchor='center', relx=0.5, rely=0.2)

        self.correct_meaning = Label(self.ielts,text=self.random_meaning,font=('Comic Sans MS',30),bg="white",fg="green",wraplength=1000)
        self.correct_meaning.place(anchor='center', relx=0.5, rely=0.55)
        #display the next button
        self.next = Button(self.ielts,text="Next",font=('Comic Sans MS',20),bg="white",fg="green",command=self.page)
        self.next.place(anchor='center', relx=0.5, rely=0.8)
        self.score += 1
    
    def wrong(self):
        #add sound effect when user choose the wrong answer
        pygame.mixer.init()
        self.wrong_sound = pygame.mixer.Sound("sound/wrong.wav")
        self.wrong_sound.play()
        #delete the word and meaning
        self.word.destroy()
        self.choice1.destroy()
        self.choice2.destroy()
        self.choice3.destroy()
        self.choice4.destroy()
        #display fault message
        self.fault = Label(self.ielts,text="\u2717Wrong" ,font=('Comic Sans MS',50),bg="white",fg="red",padx=10,pady=10)
        self.fault.place(anchor='center', relx=0.5, rely=0.4)
        #display the correct word and meaning
        self.correct_word = Label(self.ielts,text=self.random_word,font=('Comic Sans MS',70),bg="black",fg="white",padx=10,pady=10)
        self.correct_word.place(anchor='center', relx=0.5, rely=0.2)
        self.correct_meaning = Label(self.ielts,text=self.random_meaning,font=('Comic Sans MS',30),bg="white",fg="red")
        self.correct_meaning.place(anchor='center', relx=0.5, rely=0.55)
        #display the next button
        self.next = Button(self.ielts,text="Next",font=('Comic Sans MS',20),bg="white",fg="red",command=self.page)
        self.next.place(anchor='center', relx=0.5, rely=0.8)
        self.score = 0
    
    def show_score(self):
        #delete the word and meaning
        self.word.destroy()
        self.choice1.destroy()
        self.choice2.destroy()
        self.choice3.destroy()
        self.choice4.destroy()
        #display the score
        self.score = Label(self.top,text="Your Score is "+str(self.correct)+"/"+str(self.total),font=('Comic Sans MS',30),bg="white",fg="green")
        #show score on the top right corner of the screen 
        self.score.place(anchor='center', relx=0.9, rely=0.1)
        #display the next button
        self.next = Button(self.ielts,text="Next",font=('Comic Sans MS',20),bg="white",fg="green",command=self.page)
        self.next.place(anchor='center', relx=0.5, rely=0.8)

    def importfile(self):
        self.old_words = {}
        try:
            with open("words_list/ielts_vocabs") as f:
                for line in f:
                    line = line.strip()
                    equal = line.find('=')
                    self.old_words[line[:equal]] = line[equal+1:]
                    self.old_words[line[:equal]] = self.old_words[line[:equal]].replace("\t","")
                    self.old_words[line[:equal]] = self.old_words[line[:equal]].replace("\n","")
            self.meaning = [word for word in self.old_words.values()]
            self.total = len(self.meaning)
        except:
            messagebox.showerror("Error","File not found")
        self.words = {}
        #check in words dictionary that there is not an empty value 
        for key in self.old_words:
            if key != "":
                self.words[key] = self.old_words[key]
        #check in meaning list that there is not an empty value
        for i in self.meaning:
            if i == "":
                self.meaning.remove(i)

    def delete_pages(self):
        for widget in self.ielts.winfo_children():
            widget.destroy()

class TOEFL_flashcard:
    def __init__(self,tofel,top,username):
        self.username = username
        self.tofel = tofel
        self.top = top
        self.score = 0
        self.importfile()
        self.load_tofel_score()
        self.page()
      
    def page(self):
        self.delete_pages()
        self.save_tofel_score()
        self.label = Label(self.tofel,text="TOEFL Vocabs",font=('Comic Sans MS',30),bg="white",fg="green")
        self.label.place(anchor='n', relx=0.5, rely=0)

        #display score
        self.score_label = Label(self.tofel,text='Score: ' + str(self.score),font=('Comic Sans MS',20),bg="white",fg="black")
        self.score_label.place(anchor='n', relx=0.8, rely=0)

        self.high_score_label = Label(self.tofel,text='High Score: ' + str(self.high_score),font=('Comic Sans MS',20),bg="white",fg="black")
        self.high_score_label.place(anchor='n', relx=0.8, rely=0.05)

        self.reset_img = PhotoImage(file="images/reset.png")
        self.restart_scoreBtn = Button(self.tofel, image=self.reset_img, borderwidth=0 ,bg='white', activebackground='green', activeforeground="green",command=self.restart_score)
        self.restart_scoreBtn.place(anchor='n', relx=0.8, rely=0.15)

        #random word and meaning from dictionary 
        self.random_word = random.choice(list(self.words.keys()))
        self.random_meaning = self.words[self.random_word]

        #display word and meaning as a choice to let user choose the correct meaning 
        self.word = Label(self.tofel,text=self.random_word,font=('Comic Sans MS',75),bg="black",fg="white",padx=10)
        self.word.place(anchor='center', relx=0.5, rely=0.3)
        
        #random the number in place list to random the position of meaning 
        place = [0.5,0.6,0.7,0.8]
        self.random_place = random.choice(place)
        self.ch = []
        for i in range(3):
            cho = random.randint(0,len(self.meaning)-1)
            if cho not in self.ch and cho != self.meaning.index(self.random_meaning):
                self.ch.append(cho)

            else:
                while cho in self.ch or cho == self.meaning.index(self.random_meaning):
                    cho = random.randint(0,len(self.meaning)-1)
                self.ch.append(cho)

        #random 4 choices of meaning and place in different position for word and 4 choices must be different 
        self.choice1 = Button(self.tofel,text=self.random_meaning,font=('Comic Sans MS',15),bg="white",padx=15,pady=15,command=self.correct)
        self.choice1.place(anchor='center', relx=0.5, rely= self.random_place)
        place.remove(self.random_place)
        self.random_place = random.choice(place)

        self.choice2 = Button(self.tofel,text=self.meaning[self.ch[0]],padx=15,pady=15,font=('Comic Sans MS',15),bg="white",command=self.wrong)
        self.choice2.place(anchor='center', relx=0.5, rely= self.random_place)

        place.remove(self.random_place)
        self.random_place = random.choice(place)

        self.choice3 = Button(self.tofel,text=self.meaning[self.ch[1]],padx=15,pady=15,font=('Comic Sans MS',15),bg="white",command=self.wrong)
        self.choice3.place(anchor='center', relx=0.5, rely= self.random_place)
        
        place.remove(self.random_place)
        self.random_place = random.choice(place)

        self.choice4 = Button(self.tofel,text=self.meaning[self.ch[2]],padx=15,pady=15,font=('Comic Sans MS',15),bg="white",command=self.wrong)
        self.choice4.place(anchor='center', relx=0.5, rely= self.random_place)
        place.remove(self.random_place)
        self.ch.clear()

    def save_tofel_score(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            file = open(f"data/{self.username}.txt","r+")
            d = file.read()
            r = ast.literal_eval(d)
            r['tofel'] = self.high_score
            file = open(f"data/{self.username}.txt","w")
            file.write(str(r))
            file.close()
        else:
            pass

    def load_tofel_score(self):

        file = open(f"data/{self.username}.txt",'r')
        d = file.read()
        r = ast.literal_eval(d)
        file.close()
        self.high_score = r["tofel"]

    def restart_score(self):
        self.high_score = 0
        self.score = 0
        file = open(f"data/{self.username}.txt","r+")
        d = file.read()
        r = ast.literal_eval(d)
        r['tofel'] = self.high_score
        file = open(f"data/{self.username}.txt","w")
        file.write(str(r))
        file.close()
        self.choice1.destroy()
        self.choice2.destroy()
        self.choice3.destroy()
        self.choice4.destroy()
        self.page()

    def correct(self):
        #add sound effect when user choose the correct answer
        pygame.mixer.init()
        self.correct_sound = pygame.mixer.Sound("sound/correct.wav")
        self.correct_sound.play()
        #delete the word and meaning 
        self.word.destroy()
        self.choice1.destroy()
        self.choice2.destroy()
        self.choice3.destroy()
        self.choice4.destroy()
        self.score += 1
        #display correcct message
        self.correct_sym = Label(self.tofel,text="\u2713Correct" ,font=('Comic Sans MS',50),bg="white",fg="green",padx=10,pady=10)
        self.correct_sym.place(anchor='center', relx=0.5, rely=0.4)
       
        self.correct_word = Label(self.tofel,text=self.random_word,font=('Comic Sans MS',70),bg="black",fg="white",padx=10,pady=10,wraplength=1000)
        self.correct_word.place(anchor='center', relx=0.5, rely=0.2)

        self.correct_meaning = Label(self.tofel,text=self.random_meaning,font=('Comic Sans MS',30),bg="white",fg="green",wraplength=1000)
        self.correct_meaning.place(anchor='center', relx=0.5, rely=0.55)
        #display the next button
        self.next = Button(self.tofel,text="Next",font=('Comic Sans MS',20),bg="white",fg="green",command=self.page)
        self.next.place(anchor='center', relx=0.5, rely=0.8)
    
    def wrong(self):
        #add sound effect when user choose the wrong answer
        pygame.mixer.init()
        self.wrong_sound = pygame.mixer.Sound("sound/wrong.wav")
        self.wrong_sound.play()
        #delete the word and meaning
        self.word.destroy()
        self.choice1.destroy()
        self.choice2.destroy()
        self.choice3.destroy()
        self.choice4.destroy()
        self.score = 0
        #display fault message
        self.fault_sym = Label(self.tofel,text="\u2717Wrong" ,font=('Comic Sans MS',50),bg="white",fg="red",padx=10,pady=10)
        self.fault_sym.place(anchor='center', relx=0.5, rely=0.4)
        #display the correct word and meaning
        self.correct_word = Label(self.tofel,text=self.random_word,font=('Comic Sans MS',70),bg="black",fg="white",padx=10,pady=10)
        self.correct_word.place(anchor='center', relx=0.5, rely=0.2)
        self.correct_meaning = Label(self.tofel,text=self.random_meaning,font=('Comic Sans MS',30),bg="white",fg="red")
        self.correct_meaning.place(anchor='center', relx=0.5, rely=0.55)
        #display the next button
        self.next = Button(self.tofel,text="Next",font=('Comic Sans MS',20),bg="white",fg="red",command=self.page)
        self.next.place(anchor='center', relx=0.5, rely=0.8)
        

    def importfile(self):
        self.old_words = {}
        try:
            with open("words_list/tofel_vocabs") as f:
                for line in f:
                    line = line.strip()
                    equal = line.find('=')
                    self.old_words[line[:equal]] = line[equal+1:]
                    self.old_words[line[:equal]] = self.old_words[line[:equal]].replace("\t","")
                    self.old_words[line[:equal]] = self.old_words[line[:equal]].replace("\n","")
            self.meaning = [word for word in self.old_words.values()]
            self.total = len(self.meaning)
        except:
            messagebox.showerror("Error","File not found")
        self.words = {}
        #check in words dictionary that there is not an empty value 
        for key in self.old_words:
            if key != "":
                self.words[key] = self.old_words[key]
        #check in meaning list that there is not an empty value
        for i in self.meaning:
            if i == "":
                self.meaning.remove(i)

    def delete_pages(self):
        for widget in self.tofel.winfo_children():
            widget.destroy()

    #stop the music when user change the page 

class Reading(English_audio):
    def __init__(self, parent):
        # Set the parent and title of the window
        self.parent = parent
        # Set the news API key
        self.api_key = "7672572f9cbc49c3a71449c6b26e4a38"
        try:
            if pygame.mixer.music.get_busy():
                self.reading_page()
                self.stop_music()
            else:
                self.reading_page()
        except:
            self.reading_page()

    def reading_page(self):

        self.search_img = PhotoImage(file="images/search.png")
        self.clear_img = PhotoImage(file="images/clear.png")

        self.my_label_frame = LabelFrame(self.parent, text="Search Wikipedia",font=('Comic Sans MS',15),bg="white",fg="green")
        self.my_label_frame.pack(pady=20)

        # Create entry box
        self.my_entry = Entry(self.my_label_frame, font=('Comic Sans MS',20), width=47)
        self.my_entry.pack(pady=20, padx=20)

        # create text box frame
        self.my_frame = Frame(self.parent)
        self.my_frame.pack(pady=5)

        # Create Vertical Scrollbar
        self.text_scroll = Scrollbar(self.my_frame)
        self.text_scroll.pack(side=RIGHT, fill=Y)

        # Create Horizontal Scrollbar
        self.hor_scroll = Scrollbar(self.my_frame, orient='horizontal')
        self.hor_scroll.pack(side=BOTTOM, fill=X)

        # Create Text Box
        self.my_text = Text(self.my_frame, yscrollcommand=self.text_scroll.set, wrap="none", xscrollcommand=self.hor_scroll.set,font=('Comic Sans MS',10), width=100)
        self.my_text.pack()

        # Configure Scrollbars
        self.text_scroll.config(command=self.my_text.yview)
        self.hor_scroll.config(command=self.my_text.xview)

        # Button Frame
        button_frame = Frame(self.parent,bg='white')
        button_frame.pack(pady=10)
        self.parent.bind('<Return>', self.search)
        # Buttons
        search_button = Button(button_frame,image=self.search_img,bg='white',borderwidth=0, command=self.search)
        search_button.grid(row=0, column=0, padx=100)

        clear_button = Button(button_frame, image=self.clear_img,bg='white',borderwidth=0, command=self.clear)
        clear_button.grid(row=0, column=1)

    def clear(self):
        self.my_entry.delete(0, END)
        self.my_text.delete(0.0, END)


    def search(self):
        try:
            self.data = wiki.page(self.my_entry.get())
            self.my_text.insert(0.0, self.data.content)
        except:
            messagebox.showerror("Error","No results found")



class Admin:
    def __init__(self,admin):
        self.admin = admin
        self.SETUP_ADMIN()
        self.page()
    
    def SETUP_ADMIN(self):
        self.admin.geometry("700x700")
        self.admin.title('Admin')
        self.admin.resizable(False,False)

    def page(self):
        #Create table to show orders username password status
        self.tree = ttk.Treeview(self.admin,columns=('Email','Username','Password'))
        self.tree.heading('#0',text='ID')
        self.tree.heading('#1',text='Email')
        self.tree.heading('#2',text='Username')
        self.tree.heading('#3',text='Password')
        self.tree.column('#0',width=50)
        self.tree.column('#1',width=200)
        self.tree.column('#2',width=200)
        self.tree.column('#3',width=200)
        self.tree.place(relx=0.5, rely=0.4, anchor=CENTER)
        #Make table higher 
        style = ttk.Style()
        style.configure("Treeview", rowheight=50)

        #Username and password
        file = open("data/datasheet.txt",'r')
        d = file.read()
        r = ast.literal_eval(d)
        #get Email,Username,Password from datasheet.txt and put them in the table 
        count = 1
        for i in r.keys():
            self.tree.insert(parent='',index='end',iid=count,text=count,values=(r[i][0],i,r[i][1]))
            count += 1
            #if beyond the table, make a scroll bar
            if count > 10:
                self.scroll = Scrollbar(self.admin,orient=VERTICAL,command=self.tree.yview)
                self.scroll.place(relx=0.98,rely=0.4,anchor=CENTER)
                self.tree.configure(yscrollcommand=self.scroll.set)
        file.close()
        #Create delete button on the left side and below the table and beutify it
        self.delete = Button(self.admin,text='Delete',font='Bahnschrift 15',bg='red',fg='white',command=self.delete_user)
        self.delete.place(relx=0.1,rely=0.9,anchor=CENTER)
        
        #Create a button get back to sign in page and beutify it
        self.back = Button(self.admin,text='Back',font='Bahnschrift 15',bg='green',fg='white',command=self.back)
        self.back.place(relx=0.9,rely=0.9,anchor=CENTER)

        
    def delete_user(self):
        try:
            item = self.tree.selection()[0]
            username = self.tree.item(item,"values")[0]
            file = open("data/datasheet.txt",'r')
            d = file.read()
            r = ast.literal_eval(d)
            file.close()
            del r[username]
            file = open("data/datasheet.txt",'w')
            file.write(str(r))
            file.close()
            self.tree.delete(item)
            os.remove('data/'+username+".txt")
        except:
            messagebox.showerror("Error","Please select a user to delete")

    def back(self):
        self.admin.destroy()
        sign_in = Tk()
        sign_in.wm_iconbitmap('images/icon.ico')
        b = SignIn(sign_in)
        sign_in.mainloop()

if __name__ == "__main__":
    signIn = SignIn(project)
    project.mainloop()

