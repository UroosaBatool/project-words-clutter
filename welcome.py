from tkinter import *

ws = Tk()
ws.geometry('350x400+400+300')
ws.title('press Start and Enjoy\U0001F60D')
ws['bg']='#ffbf00'

f = ("times bold", 14)
 
def nextPage():
    ws.destroy()
    import game

def quit():
    ws.destroy()

Label(
    ws,
    text='"WELCOME TO WORDS CLUTTER"...\U0001f600',
    padx=20,
    pady=20,
    bg='#ffbf00',
    font=f
).pack(expand=True, fill=BOTH)

Button(
    ws, 
    text="Start", 
    font=f,
    bg = "black",
    fg = "yellow",
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)
Button(
    ws, 
    text="Quite", 
    font=f,
    bg = "red",
    fg = "yellow",
    command=quit
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()

