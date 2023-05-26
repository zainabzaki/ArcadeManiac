from tkinter import *
import tkinter as ttk
from PIL import ImageTk, Image
class start_game(Frame):
     def __init__(self,master=None):
          Frame.__init__(self,master)
          Frame.config(self,width=700,height=600,bg="cyan")
          self.master=master
          self.master.title("Scrambling Words")
          self.pack()
          self.image()
     def open(self):
          game.destroy()
          import s1
     def image(self):
          self.theLabel=Label(self,bg="cyan",fg="black",text="Scrambling Words",font=('Helvetica','50','bold'))
          self.theLabel.pack(side="top")
          self.path="D:/2048/EXTR/scr (1).jpg"
          self.img = ImageTk.PhotoImage(Image.open(self.path))
          self.imglabel = Label(self, image=self.img).pack(fill="both")
          self.start=Button(self,bg="black",fg="white",height=3,width=16,font=("Helvetica","15",'bold'),
                 text="START",command=self.open)
          self.start.pack(side="bottom")
     def loading(self):
          self.loading=ttk.Progressbar(self,orient='horizontal',length=286,mode='determinate')
          self.loading.pack(side="bottom")
          self.loading['maximum']=100
          for i in range(101):
               time.sleep(0.05)
               self.loading["value"]=1
               self.loading.update()
          self.loading["value"]=0
game=Tk()
game.geometry('690x600')
game.config(bg='cyan')
x=start_game(game)

game.mainloop()
