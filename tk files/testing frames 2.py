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

        tab1 = tk.Button(tabList, text="tab1", command=lambda m=0: self.switchWindows(m))
        tab1.pack()

        tab2 = tk.Button(tabList, text="tab2", command=lambda m=1: self.switchWindows(m))
        tab2.pack()

        tab3 = tk.Button(tabList, text="tab3", command=lambda m=2: self.switchWindows(m))
        tab3.pack()


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