import tkinter
from tkinter import *
import random
from PIL import ImageTk, Image
t_score=int()

class Loss(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        Frame.config(self,width=400,height=100,bg="red")
        self.master=master
        self.master.title("THE COLORS")
        self.pack()
        self.again()
    def again(self):
        self.message1 = Label(self, text='ALAS!!! YOU LOST THE GAME! :(',width=70
                 ,height=5,font=30,bg="red",fg='white')
        self.message1.pack(fill=X)
        self.Order1 = Button(self, text='CLICK HERE TO PLAY AGAIN',height=5,width=70,
               font=30,bg="red",fg='white',command=self.try1)
        self.Order1.pack(fill=X)
    
    def try1(self):
        self.master.destroy()
        import COLORS
        
class Highscore(Loss,Frame):
    global t_score
    def __init__(self,master=None):
        Frame.__init__(self,master)
        Frame.config(self,width=400,height=100,bg="blue")
        self.master=master
        self.master.title("THE COLORS")
        self.pack()
        self.condition()
        self.msg()
    def condition(self):
        global t_score
        if t_score>=300:
            self.depends="PLAYED WELL! with a great score of "+str(t_score)
        elif t_score>=200:
            self.depends="Nicely played! with a score of " + str(t_score)
        elif t_score>=100:
            self.depends="good your score is "+ str(t_score)
        elif t_score<50:
            self.depends="poorly played!. your score is "+ str(t_score)
    def msg(self):
        self.message2 = Label(self, text=self.depends ,width=70
             ,height=6,font=30,bg="blue",fg='white')
        self.message2.pack(fill=X)
        self.Order2 = Button(self, text='CLICK HERE TO PLAY AGAIN',height=5,width=70,
               font=30,bg="blue",fg='white' ,command=self.try1)
        self.Order2.pack(fill=X)

class GAME(Frame):
    global t_score
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master
        Frame.config(self,width=650,height=600,bg="antiquewhite")
        self.colours = ['Red','Blue','Green','deep Pink','Black', 
           'Yellow','Orange','White','Purple','Brown','Cyan']
        self.colour = ['    Red    ','    Blue    ','  Green  ','    Pink    ','   Black   ', 
           ' Yellow ',' Orange ','  White  ','  Purple ',' Brown ','   Cyan   ']
        self.master.title("THE COLORS")
        self.pack()
        self.timeleft=10
        self.num=IntVar()
        
        self.color_labels()
        self.time()
        self.timer()
        self.Score()
        self.game_buttons()
        self.Quit()
    def color_labels(self):
        random.shuffle(self.colours)
        random.shuffle(self.colour)
        self.label = Label(self, font = ('Helvetica', 60))
        self.label.config(fg = str(self.colours[1]),bg='antiquewhite',
                          text = str(self.colour[0]))
        self.label.grid(row=2,column=1)
        print(self.colours[1])
        
    def Score(self):
        self.theLabel=Label(self,background="antiquewhite",text="SCORE")
        self.theLabel.grid(row=0,column=1)
        self.display=Entry(self,text=self.num,bd=10,insertwidth=25,font=15)
        self.display.grid(row=1,column=1)
    def time(self):
        self.timeLabel =Label(self, background="antiquewhite",text = "Time left: " +
                              str(self.timeleft),
                              font = ('Helvetica', 12)) 
        self.timeLabel.grid(row=0,column=2)
        
    def timer(self):
        if self.timeleft > 0:
                  self.timeleft-=1
                  self.timeLabel.config(text='Time Left: '+str(self.timeleft)+' s')
                  self.timeLabel.after(1000,self.timer)
        else:
            self.master.destroy()
            self.timeup()
    def timeup(self):
        high=Tk()
        a=Highscore(high)
        high.mainloop()
        
    def Quit(self):
        q=Button(self, text='Quit', command=self.master.destroy,padx=14
                 ,pady=2,bg="pink")
        q.grid(row=7,column=1)
    
    def CheckAnswer(self,event):
         global t_score
         answer=event.widget
         print(answer.cget('bg'))
         print(self.colours[1].lower())
         if answer.cget('bg')==self.colours[1].lower():
              t_score = t_score+10
              self.num.set( t_score )
              self.color_labels()
         else:
              t_score-=15
              self.num.set(t_score)
         if t_score <= 0:
              self.destroy_Game()
    def destroy_Game(self):
            self.master.destroy()
            loss=Tk()
            a=Loss(loss)
            loss.mainloop()
    
    def game_buttons(self):
            
        self.Green = Button(self,bg="green")
        self.Green.grid(row=4,column=0)
        
        self.Red = Button(self,bg="red")
        self.Red.grid(row=4,column=1)

        self.Yellow = Button(self,bg="yellow")
        self.Yellow.grid(row=3,column=2)

        self.Orange = Button(self,bg="orange")
        self.Orange.grid(row=6,column=0)

        self.purple = Button(self,bg="purple")
        self.purple.grid(row=6,column=2)

        self.Pink = Button(self,bg="deep pink")
        self.Pink.grid(row=5,column=0)

        self.Blue = Button(self,bg="blue")
        self.Blue.grid(row=3,column=1)

        self.SkyBlue = Button(self,bg="cyan")
        self.SkyBlue.grid(row=5,column=2)

        self.Black = Button(self,bg="black")
        self.Black.grid(row=3,column=0)

        self.White = Button(self,bg="white")
        self.White.grid(row=4,column=2)

        self.Brown = Button(self,bg="brown")
        self.Brown.grid(row=5,column=1)

        self.options=[self.Brown,self.White,self.Black,self.
                      SkyBlue,self.Blue,self.Pink,self.purple,
                      self.Orange,self.Yellow,self.Green,self.Red]
        for btn in self.options:
            btn.config(height=5, width=16)
            btn.bind('<Button-1>', self.CheckAnswer)


            
class START(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        Frame.config(self,width=600,height=500,bg="antiquewhite")

        self.master = master
        self.img()
        self.start_button()

    def img(self):
        self.master.title("THE COLORS")
        self.pack()
        self.path="D:/2048/Color-Wheel.jpg"
        
        self.img = ImageTk.PhotoImage(Image.open(self.path))
        self.imglabel = Label(self, image=self.img).pack(fill="both")
    def start_button(self):
        self.e=Button(self,bg="pink",height=3,width=16,font="ARIEL",
                 text="START",command=self.open_game)
        self.e.pack(side="bottom")
    def open_game(self):
        root1.destroy()
        self.start()
    def start(self):
        root=Tk()
        root.geometry('650x600')
        root.configure(background="antiquewhite")
        ob=GAME(root)
        root.mainloop()

                    
root1=Tk()
root1.geometry('600x520')
root1.configure(background="antiquewhite")
ob=START(root1)
root1.mainloop()








