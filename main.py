from tkinter import *

def handle_keypress(event):
    print(event.char)

def handle_click(event):
    print('The button was clicked')

def main():
    window = Tk()
    event_list = []
    message = Label(text='There is something here ...')
    message.pack()
    frame = Frame(window) 
    frame.pack() 
    bottomframe = Frame(window) 
    bottomframe.pack(side=BOTTOM) 
    redbutton = Button(
        frame, 
        text='Red', 
        fg ='red'
    ) 
    redbutton.pack(side=LEFT) 
    bluebutton = Button(
        frame, 
        text='Blue', 
        fg='blue'
    ) 
    bluebutton.pack(side=LEFT) 
    blackbutton = Button(
        bottomframe, 
        text='Black', 
        fg='black'
    ) 
    blackbutton.pack(side=BOTTOM) 
    window.mainloop() 
    window.bind('<Key>', handle_keypress)
    window.bind('<Button-1>', handle_click)
    window.mainloop()
    

if __name__ == '__main__':
    main()