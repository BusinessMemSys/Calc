from tkinter import*
root = Tk()
root.title('Calculator')
root.geometry('320x450')
root.resizable(False, False)
b = []
del_list = []
arif_list = ['*',"/","+",'-']

class Calculator():   
    def __init__(self, root):
        self.root = root
        
    def buttons(self):
        self.result = '0'
        self.lbl = Label(text=self.result, font='Arial 20', justify=LEFT)
        self.lbl.pack()
        btns = ['C', 'Del', '*', '=',
                "1", "2", "3", "/",
                "4", "5", "6", "+",
                '7', '8', '9', '^',
                '(', '0', ')', '-'
        ]
        x = 0
        y = 50
        for bt in btns:
            com = lambda x=bt: self.logical(x)
            a = Button(text=bt, font='Arial 20', command=com).place(x=x, y=y, width=80, height=80)
            x+=80
            if x>240:
                x=0
                y+=80
    def logical(self, a):
        if a == '^':
            b.append('**')
        elif a =='Del':
            del_list.append(a)
        else:
            b.append(a)
        k = ''.join(b)
        self.lbl.configure(text=k)   
        if a == '=':
            print(b[0])
            if b[0] in arif_list:
                texxxt = "ERROR"
                self.lbl.configure(text=texxxt)
            else:
                l = k[0:-1]
                res = eval(l)
                b.clear()
                b.append(str(res))
                self.lbl.configure(text=res)   
        elif a == 'C':
            b.clear()
            n = '0'
            self.lbl.configure(text=n)
        elif a == 'Del':
            if len(b) == 0:
                n = '0'
                self.lbl.configure(text=n)
            elif len(b) == 1 and b[0] != '0':
                b.clear()
                n = '0'
                self.lbl.configure(text=n)

            else:
                b.pop(len(b)-1)
                self.lbl.configure(text=(''.join(b)))  
            del_list.clear()
if __name__ == '__main__':
    app = Calculator(root)
    app.buttons()
    root.mainloop()