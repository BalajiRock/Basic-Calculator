from tkinter import *

def click(event):
  global scvalue
  text=event.widget.cget('text')

  if text=='=':
    try:
      if scvalue.get().isdigit():
        value= int(scvalue())
      else:
        value=eval(scvalue.get())
        scvalue.set(value)
        screen.update()
    except:
      scvalue.set('ERROR')
      screen.update()

  elif text== '√':
    text='**(1/2)'
    scvalue.set(scvalue.get() + text)   
    screen.update()

  elif text== 'x':
    text='*'
    scvalue.set(scvalue.get() + text)   
    screen.update()

  elif text== '(':
    text='('
    scvalue.set(scvalue.get() + text)   
    screen.update()

  elif text== ')':
    text=')'
    scvalue.set(scvalue.get() + text)   
    screen.update()

  elif text=='AC':
    scvalue.set('')

  else :
     scvalue.set(scvalue.get() + text)   
     screen.update()
  
window=Tk()
window.title('calculator')
window.geometry('400x500')
window.resizable(0, 0)

scvalue=StringVar()
scvalue.set("")

screen=Entry(window,textvar=scvalue,bg='black',fg='white',font='lucida 26')
screen.place(x=10,y=10)



l=Button(window,text='=',bg='orange',fg='white',width=7,height=3)
l.place(x=320,y=420)
l.bind("<Button-1>",click)

l=Button(window,text='.',bg='gray',fg='white',width=7,height=3)
l.place(x=220,y=420)
l.bind("<Button-1>",click)

l=Button(window,text='0',bg='gray',fg='white',width=7,height=3)
l.place(x=120,y=420)
l.bind("<Button-1>",click)

l=Button(window,text='AC',bg='gray',fg='white',width=7,height=3)
l.place(x=20,y=420)
l.bind("<Button-1>",click)

def add ():
  x1=int(l.get())
  x2=int(l.get())
  l.insert(END,str(x1+x2))

l=Button(window,text='+',bg='dark gray',fg='white',width=7,height=3)
l.place(x=320,y=340)
l.bind("<Button-1>",click)

l=Button(window,text='3',bg='gray',fg='white',width=7,height=3)
l.place(x=220,y=340)
l.bind("<Button-1>",click)

l=Button(window,text='2',bg='gray',fg='white',width=7,height=3)
l.place(x=120,y=340)
l.bind("<Button-1>",click)

l=Button(window,text='1',bg='gray',fg='white',width=7,height=3)
l.place(x=20,y=340)
l.bind("<Button-1>",click)

l=Button(window,text='-',bg='dark gray',fg='white',width=7,height=3)
l.place(x=320,y=260)
l.bind("<Button-1>",click)

l=Button(window,text='6',bg='gray',fg='white',width=7,height=3)
l.place(x=220,y=260)
l.bind("<Button-1>",click)

l=Button(window,text='5',bg='gray',fg='white',width=7,height=3)
l.place(x=120,y=260)
l.bind("<Button-1>",click)

l=Button(window,text='4',bg='gray',fg='white',width=7,height=3)
l.place(x=20,y=260)
l.bind("<Button-1>",click)

l=Button(window,text='x',bg='dark gray',fg='white',width=7,height=3)
l.place(x=320,y=180)
l.bind("<Button-1>",click)

l=Button(window,text='9',bg='gray',fg='white',width=7,height=3)
l.place(x=220,y=180)
l.bind("<Button-1>",click)

l=Button(window,text='8',bg='gray',fg='white',width=7,height=3)
l.place(x=120,y=180)
l.bind("<Button-1>",click)

l=Button(window,text='7',bg='gray',fg='white',width=7,height=3)
l.place(x=20,y=180)
l.bind("<Button-1>",click)

l=Button(window,text='/',bg='dark gray',fg='white',width=7,height=3)
l.place(x=320,y=100)
l.bind("<Button-1>",click)

l=Button(window,text='√',bg='gray',fg='white',width=7,height=3)
l.place(x=220,y=100)
l.bind("<Button-1>",click)

l=Button(window,text=')',bg='gray',fg='white',width=7,height=3)
l.place(x=120,y=100)
l.bind("<Button-1>",click)

l=Button(window,text='(',bg='gray',fg='white',width=7,height=3)
l.place(x=20,y=100)
l.bind("<Button-1>",click)

l.mainloop()