from tkinter import *
from tkinter import messagebox
import nltk
from nltk.corpus import words
from collections import Counter
import random
nltk.download('words')
word_list = words.words()

class scrabble(Frame):
     global Matrix_list
     global word_list
     def __init__(self,master=None):
          Frame.__init__(self,master)
          Frame.config(self,width=700,height=600,bg="white")
          self.master=master
          self.master.title("Scrambling Words")
          self.pack()
          self.new_list=[]
          self.timeleft=30
          self.tick()
          self.timer()
          self.word=''
          self.x=str()
          self.Str=StringVar()
          self.score=0
          self.button()
          self.LABEL()
          self.new()
     def counter(self):
          self.L=''
          self.L=self.savedword+self.L
          print(self.L)
     def button_2(self):
          if self.btn_v in self.v2:
               self.btn_v.bind('<Button-1>',self.CHECK)
               

     def clear_1(self):
          positions=[]
          for self.btn_v in self.v: #self.v is shuffled list where self.btn_v is the index no
               for self.btn_new in self.new_list:
                    if self.btn_v==self.btn_new:
                         
                         self.pos=self.v.index(self.btn_v)
                         self.pos2=self.new_list.index(self.btn_new)
                         positions.append(self.pos)
                         print(positions)
                         print(self.pos)
                         for self.index in positions:
                              if self.index==0:
                                   self.v2=self.v
                                   self.btn_new.grid(row=0,column=0)
                                   self.button_2()
          self.x=self.x.strip(self.x)
          self.word_check.delete(0,'end')
          
     def checkspells(self):
          self.savedword=self.x
          self.counter()
          self.word=self.word_check.get()
          lower=self.word.lower()
          print(lower)
          if lower in word_list:
               dict = Counter(lower)
               flag = 1

               if flag == 1 and len(lower) > 3:
                    for letter in self.L:
                         if letter=='A' :
                              self.score+=1
                         elif letter=='E' :
                              self.score+=1
                         elif letter=='L' :
                              self.score+=1
                         elif letter=='I' :
                              self.score+=1
                         elif letter=='N' :
                              self.score+=1
                         elif letter=='O' :
                              self.score+=1
                         elif letter=='R' :
                              self.score+=1
                         elif letter=='S' :
                              self.score+=1
                         elif letter=='T' :
                              self.score+=1
                         elif letter=='U' :
                              self.score+=1
                         elif letter=='D' :
                              self.score+=2
                         elif letter=='G' :
                              self.score+=2
                         elif letter=='B' :
                              self.score+=3
                         elif letter=='C' :
                              self.score+=3
                         elif letter=='M' :
                              self.score+=3
                         elif letter=='P' :
                              self.score+=3
                         elif letter=='V' :
                              self.score+=4
                         elif letter=='W' :
                              self.score+=4
                         elif letter=='Y' :
                              self.score+=4
                         elif letter=='X' :
                              self.score+=8
                         elif letter=='J' :
                              self.score+=8
                         elif letter=='Q' :
                              self.score+=10
                         elif letter=='Z' :
                              self.score+=10
                         elif letter=='K' :
                              self.score+=5
                         
                    total="score = "+str(self.score)
                    self.label.configure(text=total)
                    print(lower)
               else:
                    messagebox.showinfo("check", "Word length should be greater than 3")
                    
          else:
               messagebox.showinfo("check","word '"+ self.word+ "' doesn't exist!")
          
          self.x=self.x.strip(self.x)
          self.word_check.delete(0,'end')
     def quit_pro(self):
          messagebox.showinfo("OOPS!!!!!!!", "Time UP!!! Your Score "+str(self.score))
          self.master.destroy()
     def tick(self):
        self.timeLabel =Label(self, background="skyblue",text = "Time left: " +
                              str(self.timeleft),font = ('Helvetica', 12)) 
        self.timeLabel.grid(row=0,column=11)
     def timer(self):
         if self.timeleft > 0:
              self.timeleft-=1
              self.timeLabel.config(text='Time Left: '+str(self.timeleft)+' s')
              self.timeLabel.after(1000,self.timer)
         elif self.timeleft==0 :
              self.quit_pro()


     def CHECK(self,event):
          choice=event.widget
          self.new_list.append(choice)
          print(self.new_list)
          if choice==self.btn1 or choice== self.btn36 or choice==self.btn30:
               self.x=self.x+"A"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn2 or choice== self.btn31:
               self.x=self.x+"R"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn3 or choice== self.btn32:
               self.x=self.x+"B"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn4:
               self.x=self.x+"Z"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn5 or choice== self.btn38:
               self.x=self.x+"T"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn6 or choice== self.btn37:
               self.x=self.x+"D"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn7:
               self.x=self.x+"H"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn8:
               self.x=self.x+"M"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn9 or choice== self.btn43:
               self.x=self.x+"V"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn10 or choice== self.btn35 or choice== self.btn44:
               self.x=self.x+"S"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn11:
               self.x=self.x+"X"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn12 or choice== self.btn33:
               self.x=self.x+"L"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn13 or choice== self.btn34:
               self.x=self.x+"U"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn14 or choice== self.btn45:
               self.x=self.x+"G"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn15 or choice== self.btn23 or choice== self.btn42:
               self.x=self.x+"O"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn16:
               self.x=self.x+"C"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn17 or choice== self.btn41:
               self.x=self.x+"K"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn18 or choice== self.btn40:
               self.x=self.x+"P"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn19 or choice== self.btn47:
               self.x=self.x+"Y"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn20 or choice== self.btn46:
               self.x=self.x+"N"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn21 or choice== self.btn27 or choice== self.btn39:
               self.x=self.x+"E"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn22 or choice== self.btn28:
               self.x=self.x+"F"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn24 or choice== self.btn29:
               self.x=self.x+"I"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn25:
               self.x=self.x+"J"
               self.Str.set(self.x)
               choice.destroy()
          elif choice==self.btn26:
               self.x=self.x+"Q"
               self.Str.set(self.x)
               choice.destroy()
          
     
     def button(self):
          self.btn1 = Button(self, text="A",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))

          self.btn36 = Button(self, text="A",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))
          
          self.btn2 = Button(self, text="R",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))

          self.btn3 = Button(self, text="B",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))
          
          self.btn4 = Button(self, text="Z",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))
          
          self.btn5 = Button(self, text="T",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))
          
          self.btn6 = Button(self, text="D",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))
          
          self.btn38= Button(self, text="T",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))
          
          self.btn37 = Button(self, text="D",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))
          
          self.btn7 = Button(self, text="H",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))
          
          self.btn8 = Button(self, text="M",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))
          
          self.btn9 = Button(self, text="V",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))
          
          self.btn10 = Button(self, text="S",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))

          self.btn43 = Button(self, text="V",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))

          self.btn44 = Button(self, text="S",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))          

          self.btn11 = Button(self, text="X",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))
          
          self.btn12 = Button(self, text="L",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))
          
          self.btn13 = Button(self, text="U",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))
          
          self.btn14 = Button(self, text="G",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))
          
          self.btn20= Button(self, text="N",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))

          self.btn45 = Button(self, text="G",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))
          
          self.btn46= Button(self, text="N",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))
          
          self.btn19 = Button(self, text="Y",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))

          self.btn47 = Button(self, text="Y",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))

          self.btn18 = Button(self, text="P",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))
          
          self.btn17= Button(self, text="K",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))          

          self.btn40 = Button(self, text="P",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))
          
          self.btn41= Button(self, text="K",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))
          
          self.btn16= Button(self, text="C",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))
          
          self.btn21 = Button(self, text="E",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))

          self.btn39 = Button(self, text="E",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20')) 

          self.btn22 = Button(self, text="F",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))

          self.btn24 = Button(self, text="I",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))

          self.btn25 = Button(self, text="J",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))

          self.btn26 = Button(self, text="Q",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))

          self.btn23 = Button(self, text="O",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))

          self.btn42 = Button(self, text="O",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))

          self.btn15 = Button(self, text="W",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))

          self.btn27 = Button(self, text="E",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))

          self.btn28 = Button(self, text="F",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))

          self.btn29 = Button(self, text="I",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))

          self.btn30 = Button(self, text="A",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))
          
          self.btn31= Button(self, text="R",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))

          self.btn32= Button(self, text="B",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))

          self.btn33 = Button(self, text="L",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))
          
          self.btn34 = Button(self, text="U",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))

          self.btn35 = Button(self, text="S",bg="skyBlue", fg="Black",width=5,height=2,font=('Helvetica','20'))
          
          self.BUTTON=[self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,self.btn9,self.btn10
                       ,self.btn11,self.btn12,self.btn13,self.btn14,self.btn15,self.btn16,self.btn17,
                       self.btn18,self.btn19,self.btn20, self.btn38,self.btn29,self.btn30,self.btn31,
                       self.btn32,self.btn33,self.btn34,self.btn35,self.btn36,self.btn37,self.btn39
                       ,self.btn21,self.btn22,self.btn23,self.btn24,self.btn25,self.btn28,self.btn27,
                       self.btn26,self.btn40,self.btn41,self.btn42,self.btn43,self.btn44,self.btn45,self.btn46,self.btn47]

          self.D={self.btn1:"A",self.btn2:"R",self.btn3:"B",self.btn4:"Z",self.btn5:"T",self.btn6:"D",self.btn7:"H",self.btn8:"M",self.btn9:"V",self.btn10:"S"
                       ,self.btn11:"X",self.btn12:"L",self.btn13:"U",self.btn14:"G",self.btn15:"W",self.btn16:"C",self.btn17:"K",
                       self.btn18:"P",self.btn19:"Y",self.btn20:"N", self.btn38:"T",self.btn29:"I",self.btn30:"A",self.btn31:"R",
                       self.btn32:"B",self.btn33:"L",self.btn34:"U",self.btn35:"S",self.btn36:"A",self.btn37:"D",self.btn39:"E"
                       ,self.btn21:"E",self.btn22:"F",self.btn23:"O",self.btn24:"I",self.btn25:"J",self.btn28:"F",self.btn27:"E",
                       self.btn26:"Q",self.btn40:"P",self.btn41:"K",self.btn42:"O",self.btn43:"V",self.btn44:"S",self.btn45:"G",self.btn46:"N",self.btn47:"Y"}
          self.q=list(self.D.keys())
          print(self.q)

          random.shuffle(self.BUTTON)
          self.v=list(self.BUTTON[0:20])
          i=0
          j=0
          for choices in self.v:
               choices.grid(row=i,column=j)
               j+=1
               if j==5:
                    i+=1
                    j=0
          print(self.v)
          
          for select_btn in self.v:
               select_btn.bind('<Button-1>',self.CHECK)
               
  
               
     def new(self):
          self.word_check=Entry(self,text=self.Str,width=50)
          self.word_check.configure(highlightbackground="red", highlightcolor="red")
          self.word_check.grid(row=5,column=0,columnspan=6)
          
     def LABEL(self):
          
          self.btncheck = Button(self, text="Submit",bg="Green", fg="gold",width=9,height=3,
                                 font=('Helvetica','10'),command=self.checkspells)
          self.btncheck.grid(column=10, row=5)
          self.clear=Button(self, text="Clear",bg="Red", fg="gold",width=9,height=3,
                                 font=('Helvetica','10'),command=self.clear_1)
          self.clear.grid(column=10,row=6)
          self.btncheck.grid(column=10, row=5)
          self.label=Label(self,text="Score = 0")
          self.label.grid(column=11,row=5)
     
     
window=Tk()
window.geometry('680x550')
window.config(bg='white')
o=scrabble(window)

window.mainloop()



