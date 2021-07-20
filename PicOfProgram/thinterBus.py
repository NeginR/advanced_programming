import tkinter as tk
import tkinter.messagebox

class myThinter:
    def __init__(self):
        pass
    def beginigPart(self):
        master = tk.Tk()
        welcomeMassage = "hello!\nWelcome to my reservation system!"
        msg = tk.Message(master, text = welcomeMassage)
        msg.config(bg='lightgreen', font=('times', 24, 'italic'))
        #button = tk.Button(master, 
                        #text="Ok", 
                        #fg="red",
                        #command=exit)
        msg.pack()
        #button.pack(side=tk.BOTTOM)
        tk.mainloop()
    def startPart(self,massage):
        master2 = tk.Tk()
        msg = tk.Message(master2,text = massage)
        msg.config(bg='lightgreen', font=('times', 24, 'italic'))
        msg.pack()
        tk.mainloop()
        """

        tk.Label(master2, 
            text=#Choose:,
            justify = tk.RIGHT,
            padx = 20).pack()

        tk.Radiobutton(master2, 
               text="1  ",
               padx = 20, 
               variable=v, 
               value=1).pack(anchor=tk.W)

        tk.Radiobutton(master2, 
               text="2  ",
               padx = 20, 
               variable=v, 
               value=2).pack(anchor=tk.W)
        tk.Radiobutton(master2, 
               text="3  ",
               padx = 20, 
               variable=v, 
               value=3).pack(anchor=tk.W)

        tk.Radiobutton(master2, 
               text="4  ",
               padx = 20, 
               variable=v, 
               value=4).pack(anchor=tk.W)
        tk.mainloop()
"""
    def inputNumber(self):
        master = tk.Tk()
        tk.Label(master, text="inputNumber").grid(row=0)
        e1 = tk.Entry(master)
        e1.grid(row=0, column=1)
        master.mainloop()

mythinter = myThinter()
mythinter.beginigPart()
mythinter.startPart("Hi")
mythinter.inputNumber()
print("hello")

print("here 2")