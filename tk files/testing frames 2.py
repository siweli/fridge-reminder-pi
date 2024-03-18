import tkinter as tk

class firstWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="frame 1").pack()
        self.pack()

class secondWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="frame 2").pack()
        self.pack()

class thirdWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="frame 3").pack()
        self.pack()

class mainWindow():
    def __init__(self, master):
        # MENUBAR
        tabList = tk.Frame(master)
        tabList.pack()

        for c, i in enumerate(["Main", "Account", "Support"]):
            tab = tk.Button(tabList, text=i, command=lambda m=c: self.switchWindows(m))
            tab.grid(row=0, column=c)


        # MAIN WINDOW
        mainframe = tk.Frame(master)
        mainframe.pack(fill="both", expand=1)
        self.index = 0

        self.frameList = [firstWindow(mainframe), secondWindow(mainframe), thirdWindow(mainframe)]
        for c, i in enumerate(self.frameList):
            if c != 0:
                i.forget()

    def switchWindows(self, tab):
        self.frameList[self.index].forget()
        self.index = tab
        self.frameList[self.index].tkraise()
        self.frameList[self.index].pack()

root = tk.Tk()
window = mainWindow(root)
root.mainloop()