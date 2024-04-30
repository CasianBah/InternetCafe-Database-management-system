from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import commands
from commands import *
import sqlite3



class Window:

    def __init__(self,master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.new_username = StringVar()
        self.new_password = StringVar()
        self.tree = ttk.Treeview()
        #self.widgets()
        self.openapp()

    def new_user(self):
        conn=sqlite3.connect('database.db')
        c=conn.cursor()
        c.execute('SELECT * FROM admin WHERE username = ?',[(self.username.get())])
        if c.fetchall():
            messagebox.showerror('','Admin name taken!')
        else:
            messagebox.showwarning('','Admin account created!')
            self.log()
        c.execute('INSERT INTO admin(username,password) VALUES(?,?)',[(self.new_username.get()),(self.new_password.get())])
        conn.commit()
        conn.close()

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logframe.pack()

    def create(self):
        self.new_username.set('')
        self.new_password.set('')
        self.logframe.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    def login(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('SELECT * FROM admin WHERE username = ? AND password = ?',[(self.username.get()),(self.password.get())])
        if c.fetchall():
            conn.commit()
            conn.close()
            self.master.destroy()
            self.openapp()
        else:
            messagebox.showerror('','Admin Not Found!')

    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN', font = ('',35),pady=10)
        self.head.pack()
        self.logframe = Frame(self.master ,padx=10, pady =10)
        Label(self.logframe, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logframe, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logframe, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logframe, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logframe, text=' Login ', bd=3, font=('', 15), padx=5, pady=5, command=self.login, bg="gold2").grid()
        Button(self.logframe, text=' Create Account ', bd=3, font=('', 15), padx=5, pady=5, command=self.create,bg="powder blue").grid(row=2, column=1)
        self.logframe.pack()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.new_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.new_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.crf, text='Create Account', bd=3, font=('', 15), padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text='Go to Login', bd=3, font=('', 15), padx=5, pady=5, command=self.log).grid(row=2, column=1)


    def add_user(self):
        def add_user_b():
            commands.insert(username_text.get(), phone_text.get(), email_text.get(), password_text.get(), 0, 0)
            w.destroy()

        w = Tk()
        w.title("New user")
        w.configure(background="aliceblue")
        label1 = Label(w,text="Username",font=('none 13 bold'))
        label1.grid(row=0,column=0,padx=10,pady=10)

        label2 = Label(w,text="Phone",font=('none 13 bold'))
        label2.grid(row=1,column=0,padx=10,pady=10)

        label3 = Label(w, text="Email", font=('none 13 bold'))
        label3.grid(row=2, column=0, padx=10, pady=10)

        label4 = Label(w, text="Password", font=('none 13 bold'))
        label4.grid(row=3, column=0, padx=10, pady=10)

        username_text = StringVar()
        entry1 = Entry(w, textvariable = username_text)
        entry1.grid(row=0,column=1,padx=10,pady=10)

        phone_text = StringVar()
        entry2 = Entry(w,textvariable=phone_text)
        entry2.grid(row=1,column=1,padx=10,pady=10)

        email_text = StringVar()
        entry3 = Entry(w, textvariable=email_text)
        entry3.grid(row=2, column=1, padx=10, pady=10)

        password_text=StringVar()
        entry4 = Entry(w, textvariable=password_text)
        entry4.grid(row=3, column=1, padx=10, pady=10)


        b = Button(w,text="Add user",command=add_user_b,width=8,font=('none 13 bold'),relief=RAISED)
        b.grid(row=4, column=1,padx=10,pady=10)



    def view_all(self):
        user_data = view_all_users()
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in user_data:
            self.tree.insert('', 'end', values=row)

    def search_user(self):
        def search_button():
            s = search(username_search.get(),number_search.get())
            for item in self.tree.get_children():
                self.tree.delete(item)
            for row in s:
                self.tree.insert('','end',values=row)
            w.destroy()

        w = Tk()
        w.title("Search user")
        w.configure(background="aliceblue")

        label1 = Label(w, text="Username", font=('none 13 bold'))
        label1.grid(row=0, column=0, padx=10, pady=10)

        username_search = StringVar()
        entry1 = Entry(w,textvariable=username_search)
        entry1.grid(row=0, column=1, padx=10, pady=10)


        label2 = Label(w, text="Phone", font=('none 13 bold'))
        label2.grid(row=1, column=0, padx=10, pady=10)

        number_search = StringVar()
        entry2 = Entry(w, textvariable=number_search)
        entry2.grid(row=1, column=1, padx=10, pady=10)

        b = Button(w,text="Search",width = 8,command=search_button, font=('none 13 bold'),relief=RAISED)
        b.grid(row=2,column = 1,padx=10,pady=10)

    def delete_user(self):
        selected_item = self.tree.selection()[0]
        user_id = self.tree.item(selected_item, 'values')[0]
        delete(user_id)
        self.tree.delete(selected_item)

    def recharge_selected_user_ron(self):
        selected_item = self.tree.selection()[0]
        user_id = self.tree.item(selected_item, 'values')[0]
        w = Tk()
        w.title("Recharge Ron")
        w.configure(background='aliceblue')

        label = Label(w,text="amount",font=('none 13 bold'))
        label.grid(row=0,column=0,padx=10,pady=10)

        amount_text = StringVar()
        entry = Entry(w,textvariable=amount_text)
        entry.grid(row=0,column=1,padx=10,pady=10)

        b = Button(w, text="Submit", width=8, font=('none 13 bold'), relief=RAISED)
        b.grid(row=1, column=1, padx=10, pady=10)

    def openapp(self):
        window = Tk()
        window.title("CyberCafe Management System")
        window.configure(background="aliceblue")
        window.geometry("1000x400")

        columns = ('User ID', 'Username', 'Number', 'Email', 'Password', 'Ron', 'Time')

        self.tree = ttk.Treeview(window, columns=columns, show='headings')

        self.tree.heading('User ID', text='User ID')
        self.tree.heading('Username', text='Username')
        self.tree.heading('Number', text='Number')
        self.tree.heading('Email', text='Email')
        self.tree.heading('Password', text='Password')
        self.tree.heading('Ron', text='Ron')
        self.tree.heading('Time', text='Time')

        for col in columns:
            self.tree.column(col, width=143, minwidth=50, anchor='center', stretch=False)

        self.tree.grid(row=0, column=0, columnspan=20, sticky='n')

        b1 = Button(window,text="new user",width=12,command=self.add_user,font=('none 13 bold'), relief=RAISED)
        b1.grid(row=1,column=0, sticky='w',padx=10,pady=10)

        b2 = Button(window,text="search user",width=12,command=self.search_user, font=('none 13 bold'), relief=RAISED)
        b2.grid(row=1, column=1,sticky='w',padx=10,pady=10)

        b3 = Button(window,text="recharge ron",width=12,command=self.recharge_selected_user_ron,font=('none 13 bold'), relief=RAISED)
        b3.grid(row=2,column=0,sticky='w',padx=10,pady=10)

        b4 = Button(window,text="recharge time",width=12,font=('none 13 bold'), relief=RAISED)
        b4.grid(row=2,column=1,sticky='w',padx=10,pady=10)

        b5 = Button(window, text="view all", width=12,command=self.view_all, font=('none 13 bold'), relief=RAISED)
        b5.grid(row=3, column=0, sticky='w', padx=10, pady=10)

        b6 = Button(window, text="delete user", width=12,command=self.delete_user, font=('none 13 bold'), relief=RAISED)
        b6.grid(row=3, column=1, sticky='w', padx=10, pady=10)

        window.mainloop()
