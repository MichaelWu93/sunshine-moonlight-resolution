import subprocess
import tkinter

resolution = ['1920x1080','1366x768','2266x1488']
exe_path = r"C:/Users/.../QRes.exe"

class Gui():
    def __init__(self,init_name):
        self.init = init_name
        self.x = 1920
        self.y = 1080
    
    def set_init_window(self):
        self.init.title("Resolution")
        self.init.geometry('300x150+200+200')
        self.init.resizable(width=False, height=False)
        self.init.attributes('-topmost',True)
        var = tkinter.StringVar(value=resolution[0])
        def getr():
            #print(var.get())
            temp = var.get().split('x')
            #print(temp)
            self.x = temp[0]
            self.y = temp[1]
            #print(self.x)
            #print(self.y)
        
        for i in resolution:
            button = tkinter.Radiobutton(self.init, text=i, variable=var, value=i, command=getr)
            button.pack()
        
        def QRes():
            subprocess.run([exe_path, "/x:" + str(self.x), "/y:" + str(self.y), '/c:32', '/r:120']) 
        
        button = tkinter.Button(self.init, text='exec', command=QRes)
        button.pack()



def start():
	window = tkinter.Tk()
	Gui(window).set_init_window()
	window.mainloop()
    
start()
