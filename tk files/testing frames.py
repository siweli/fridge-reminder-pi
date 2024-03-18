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

class mainWindow():
    def __init__(self, master):
        mainframe = tk.Frame(master)
        mainframe.pack(fill="both", expand=1)
        self.index = 0

        self.frameList = [firstWindow(mainframe), secondWindow(mainframe)]
        self.frameList[1].forget()

        bottomFrame = tk.Frame(master)
        bottomFrame.pack()

        switch = tk.Button(bottomFrame, text="switch", command=self.switchWindows)
        switch.pack()

    def switchWindows(self):
        self.frameList[self.index].forget()
        self.index = int(not(bool(self.index)))
        self.frameList[self.index].tkraise()
        self.frameList[self.index].pack()

root = tk.Tk()
window = mainWindow(root)
root.mainloop()