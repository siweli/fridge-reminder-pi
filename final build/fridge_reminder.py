import tkinter as tk
from tkinter import font
import tk_keyboard
import requests
from uuid import getnode

# DEV_TOKEN = str(getnode())
# main window with table contents in
class firstWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        dv=str(getnode())

        url = "http://localhost:3000/api/getcontents"
        # data = {"data" : DEV_TOKEN}
        data={"data":dv}

        self.table = tk.Frame(self)

        try:
            response = requests.post(url, json=data)
            contents = response.json()["contents"]
            for i in contents:
                row = tk.Frame(self.table)
                row.pack()

                tk.Label(row, text=i["name"]).grid(row=0, column=0)
                tk.Label(row, text=i["expires"]).grid(row=0, column=1)
        except requests.ConnectionError:
            print("Could not establish a connection")

        
        self.pack()
        self.table.pack()
        
        self.reload()

    def reload(self):
        lo = self.pack_slaves()
        # lo[0].destroy()


# account window
class secondWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="frame 2").pack()
        self.pack()

# support window
class thirdWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="frame 3").pack()
        self.pack()

# main code
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # colour variables
        cl_darkblue = "#13131B"
        cl_red = "#F2285B"
        cl_white = "#DDDDDD"

        # token
        dev_token = str(getnode())

        # widget sizes based off screen width
        screen_width = self.winfo_screenwidth()
        font_size = font.Font(size=screen_width//20)
        btn_size = font.Font(size=screen_width//50)

        # window setup
        self.title("entry label test kb")
        self.attributes("-fullscreen", True)
        self.config(bg=cl_darkblue)
        self.option_add("*insertBackground", cl_red)

        # menu bar
        tabList = tk.Frame(self)
        tabList.pack()
        for c, i in enumerate(["Main", "Account", "Support"]):
            tab = tk.Button(tabList, text=i, command=lambda m=c: self.switchWindows(m))
            tab.grid(row=0, column=c)


        # main window
        mainframe = tk.Frame(self)
        mainframe.pack(fill="both", expand=1)
        self.index = 0

        self.frameList = [firstWindow(mainframe), secondWindow(mainframe), thirdWindow(mainframe)]
        for c, i in enumerate(self.frameList):
            if c != 0:
                i.forget()

    # switch between different frames
    def switchWindows(self, tab):
        self.frameList[self.index].forget()
        self.index = tab
        self.frameList[self.index].tkraise()
        self.frameList[self.index].pack()

# RUN
if __name__ == "__main__":
    App().mainloop()