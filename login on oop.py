import tkinter as tk
from tkinter import *
import string

class EXCempty(Exception):
    pass
class Exlenpass(Exception):
    pass
class Expassword(Exception):
    pass
class Exusername(Exception):
    pass
class popupmsg:
    def __init__(self,msg):
        self.msg=msg
    def message(self):
        
        self.F=("Verdana",12)
        self.popup=tk.Tk()
        w=len(self.msg)*15
        h=len(self.msg)*3
        self.popup.geometry('{}x{}+{}+{}'.format(w,h,600,150))
        self.popup.wm_title("INVALID")
        self.label=tk.Label(self.popup, text=self.msg, font=self.F)
        self.label.pack(side='top', fill='x' , pady=20)
        self.B1=tk.Button(self.popup, text='Close', command= self.popup.destroy)
        self.B1.pack()
        
class main(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        Frame.config(self,background='black')
        self.master=master
        self.master.title('Main Screen')
        self.pack()
        self.labels()
    def game1(self):
        self.master.destroy()
        import s1
    def game3(self):
        self.master.destroy()
        import bounce
    def game2(self):
        self.master.destroy()
        import COLORS
        
    def labels(self):
        self.lbl5=Label(self,text='WELCOME!', bd=20, bg='black',fg='white',font=('Monotype Corsiva',50))
        self.lbl5.pack()
        self.lbl6=Label(self,text='What do you want to play?', bd=40, bg='black',fg='white',font=('Monotype Corsiva',30))
        self.lbl6.pack()
        self.button2=Button(self, bg='pink', height=20, width=50, text='SCRABBLE',command=self.game1)
        self.button2.pack(side=LEFT,fill=Y)
        self.button3=Button(self,bg='cyan',height=20,width=50,text='THE COLORS',command=self.game2)
        self.button3.pack(side=RIGHT,fill=Y)
        self.button4=Button(self,bg='yellow',height=50,width=50,text='BOUNCE',command=self.game3)
        self.button4.pack(side=BOTTOM,fill=Y)

class LOG(Frame,popupmsg):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        Frame.config(self,background='white')
        self.master=master
        self.master.title("LOGIN SCREEN")
        self.pack()
        self.buttons()
    def command1(self,event):
        try:
            self.lc=list(string.ascii_lowercase)
            self.uc=list(string.ascii_uppercase)
            self.n=[1,2,3,4,5,6,7,8,9,0]
            self.alphnum=self.lc+self.uc+self.n
            
            if self.entry1.get()=='' or self.entry2.get()=='':
                self.entry1.delete(0,"end")
                self.entry2.delete(0,"end")
                raise EXCempty()
            
            elif self.entry1.get()!='' and self.entry2.get()!='':
    
                for x in self.entry1.get():
                    if x not in self.alphnum:
                        self.entry1.delete(0,"end")
                        self.entry2.delete(0,"end")
                        raise Exusername()
                    
                for x in self.entry2.get():
                    if x in self.uc:
                        self.entry1.delete(0,"end")
                        self.entry2.delete(0,"end")
                        raise Expassword()

                if len(self.entry2.get())<8:
                    self.entry1.delete(0,"end")
                    self.entry2.delete(0,"end")
                    raise Exlenpass()
                else:
                    self.entry1.delete(0,"end")
                    self.entry2.delete(0,"end")
                    self.root=Tk()
                    self.root.geometry('1100x650+400+50')
                    b=main(self.root)
                    self.root.resizable(0,0)
                    log.destroy()


                    

        except Exlenpass:
            exp=popupmsg("PASSWORD MUST BE OF ATLEAST 8 CHARACTERS")
            exp.message()
        except Expassword:
            exp=popupmsg("PASSWORD CAN NOT HAVE CAPITAL LETTERS")
            exp.message()
        except Exusername:
            exp=popupmsg("USERNAME CAN NOT HAVE NON-ALPHANUMERIC CHARACTERS")
            exp.message()
        except EXCempty:
            exp=popupmsg("USERNAME OR PASSWORD CAN NOT BE BLANK")
            exp.message()

    def command2(self,evt):
        log.destroy()
    def buttons(self):
        self.photo1=PhotoImage(file='pic.gif')
        self.photo=Label(self,image=self.photo1, bg='white', bd='20')
        self.photo.pack()
        self.lbl1=Label(self,text='Username',font=('Helvetica',10))
        self.lbl1.pack()
        self.entry1=Entry(self, bd=10)
        self.entry1.pack()
        self.lbl2=Label(self, text='Password',font=('Helvetica',10))
        self.lbl2.pack()
        self.entry2=Entry(self, show='*',bd=10)
        self.entry2.pack()
        self.Login=Button(self, text='Log-in')
        self.Login.bind ('<Button-1>', self.command1)
        self.Login.pack()
        self.button1=Button(self,text='cancel')
        self.button1.bind('<Button-1>',self.command2)
        self.button1.pack()
        self.lbl4= Label(self,font=('Arial',9),text='Copyright Login Screen 2019')
        self.lbl4.pack()
    

log=Tk()
o=LOG(log)
log.geometry('800x650+500+100')




