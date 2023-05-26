import tkinter
from tkinter import *
import random
import time
from PIL import ImageTk, Image


class BOUNCE(Frame):
    def __init__(self,master=None):
         Frame.__init__(self,master)
         Frame.config(self,width=400,height=100,bg="purple")
         self.master=master
         self.master.title("BOUNCE")
         self.pack()
         self.img()
         self.start_button()

    def img(self):
        self.master.title("BOUNCE")
        self.pack()
        self.path="D:/2048/Rolling-Sky.jpg"
        
        self.img = ImageTk.PhotoImage(Image.open(self.path))
        self.imglabel = Label(self, image=self.img).pack(fill="both")
    def start_button(self):
        self.e=Button(self,bg="purple",fg="gold",height=3,width=16,font="ARIEL",
                 text="START",command=self.open_game)
        self.e.pack(side="bottom")
    def open_game(self):
        root.destroy()
        
        
root=Tk()
root.configure(background="gold")
ob=BOUNCE(root)
root.mainloop()


class Loss(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.master.title("bounce")
        self.pack()
        self.again()
    def again(self):
        self.message1 = Label(self, text='GAME OVER!!!',width=70
                 ,height=4,font=32,bg="purple",fg='gold')
        self.message1.pack(fill=X)
        self.Order1 = Button(self, text='CLICK HERE TO PLAY AGAIN',height=4,width=70,
               font=32,bg="purple",fg='gold',command=self.try1)
        self.Order1.pack(fill=X)
    
    def try1(self):
        self.master.destroy()
        import bounce
tk=Tk()
tk.title("bounce")
tk.resizable(0,0)
canvas=Canvas(tk, width=500, height=500, bg='pink', bd=0, highlightthickness=0)
canvas.pack()
tk.update()


class Ball(Loss):
    
    def __init__(self, canvas, paddle, color):
        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(40,40,20,20, fill=color)
        self.canvas.move(self.id,245, 100)
        start=[-3,-2,-1,0,1,2,3]
        random.shuffle(start)
        self.x=start[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.hit_bottom=False

    def hit_paddle(self, pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                return True
            return False
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos=self.canvas.coords(self.id)
        print(pos)
        if pos[1]<=0:
            self.y=3
        if pos[3]>=self.canvas_height:
            self.hit_bottom=True
            tk.destroy()
            l=Tk()
            h=Loss(l)
            loss.mainloop()
        if pos[0]<=0:
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-3
        if self.hit_paddle(pos)==True:
            self.y=-3
            
class Paddle:
    def __init__(self,canvas, color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10, fill=color)
        canvas.move(self.id, 200,300)
        self.x=0
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self,event):
        self.x=-2
    def turn_right(self,left):
        self.x=2

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        self.canvas.coords(self.id)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=0
        if pos[2]>=self.canvas_width:
            self.x=0
            
paddle=Paddle(canvas,'red')      
ball=Ball(canvas,paddle,'purple')


while 1:
    if ball.hit_bottom==False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
