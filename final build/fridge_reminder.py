import tkinter as tk
from tkinter import font
import tk_keyboard
import requests
from uuid import getnode

DEV_TOKEN = str(getnode())
# main window with table contents in
class firstWindow(tk.Frame):
    def __init__(self, parent, font_size):
        super().__init__(parent)
        self.pack()

        self.font_size = font_size

        self.option_add("*Label.Font", "aerial 22 bold")

        self.bind_all("<Any-ButtonPress>", self.interact_event)
        self.bind_all("<Any-KeyPress>", self.interact_event)

        self.interacted = False

        self.run_loop()
        
        
    # run loop for this window
    def run_loop(self):
        if self.interacted == False:
            self.load_contents()
            # not interacted with recently so reload
        else:
            self.interacted = False
            # interacted with recently so dont reload
        self.after(10000, self.run_loop)
    
    # on any interaction with the screen then hold off on reloading window
    def interact_event(self, event):
        self.interacted = True

    # table contents and add row to load
    def load_contents(self):
        widgets = self.pack_slaves()
        for i in widgets:
            i.destroy()

        url = "http://localhost:3000/api/pi/getcontents"
        data = {"data" : DEV_TOKEN}

        try:
            response = requests.post(url, json=data)
            contents = response.json()["contents"]
            for i in contents:
                row = tk.Frame(self)
                row.pack()

                tk.Label(row, text=i["name"], bg="#DDDDDD", relief="solid").grid(row=0, column=0)
                tk.Label(row, text=i["expires"], bg="#DDDDDD", relief="solid").grid(row=0, column=1)

                id=i["id"]
                tk.Button(row, text="-", bg="#DD3333", command=lambda m=id: self.remove_row(m)).grid(row=0, column=2)

            AR_frame = tk.Frame(self)
            AR_frame.pack()
            tk.Label(AR_frame, text="Item name:").grid(column=0,row=0)
            tk.Label(AR_frame, text="Expires:").grid(column=0, row=1)

            self.item_name = tk.StringVar(self)
            self.expiry_d = tk.StringVar(self)
            self.expiry_m = tk.StringVar(self)
            self.expiry_y = tk.StringVar(self)


            self.days = [str(i) for i in range(1,32)]
            self.months = [str(i) for i in range(1,13)]
            self.years = [str(i) for i in range(2024,2035)]

            tk.Entry(AR_frame, textvariable=self.item_name, width=15, font=self.font_size).grid(column=1,row=0)

            # expiry frame for positioning
            EX_frame = tk.Frame(AR_frame)
            EX_frame.grid(column=1,row=1)
            tk.Spinbox(EX_frame, values=[str(i) for i in range(1,32)], width=3, font=self.font_size, textvariable=self.expiry_d).grid(column=0,row=0)
            tk.Spinbox(EX_frame, values=[str(i) for i in range(1,13)], width=3, font=self.font_size, textvariable=self.expiry_m).grid(column=1,row=0)
            tk.Spinbox(EX_frame, values=[str(i) for i in range(2024,2035)], width=5, font=self.font_size, textvariable=self.expiry_y).grid(column=2,row=0)


            tk.Button(AR_frame, text="Add item", bg="#33DD33", command=self.add_row).grid(column=1,row=2)



        except requests.ConnectionError:
            tk.Label(self, text="Could not establish a connection").pack()
    
    def add_row(self):
        item_name = self.item_name.get()
        d = self.expiry_d.get()
        m = self.expiry_m.get()
        y = self.expiry_y.get()
        expiry = f"{y}-{m}-{d}"

        if item_name != "":
            url = "http://localhost:3000/api/pi/addrow"
            data = {"data" : DEV_TOKEN, "item_name" : item_name, "expires" : expiry}

            try:
                response = requests.post(url, json=data)
                self.load_contents()
            except requests.ConnectionError:
                tk.Label(self, text="Could not establish a connection").pack()
    
    def remove_row(self, id):
        url = "http://localhost:3000/api/pi/removerow"
        data = {"data" : DEV_TOKEN, "id" : id}

        try:
            response = requests.post(url, json=data)
            self.load_contents()
        except requests.ConnectionError:
            tk.Label(self, text="Could not establish a connection").pack()




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
        font_size = font.Font(size=screen_width//35)
        btn_size = font.Font(size=screen_width//50)

        # window setup
        self.title("entry label test kb")
        self.attributes("-fullscreen", True)
        self.config(bg=cl_darkblue)
        self.option_add("*insertBackground", cl_red)
        self.option_add("*Background", cl_darkblue)
        self.option_add("*Entry.Background", cl_white)
        self.option_add("*Spinbox.Background", cl_white)

        # menu bar
        tabList = tk.Frame(self)
        tabList.pack()
        for c, i in enumerate(["Main", "Account", "Support"]):
            tab = tk.Button(tabList, text=i, bg=cl_red, command=lambda m=c: self.switchWindows(m))
            tab.grid(row=0, column=c)


        # main window
        mainframe = tk.Frame(self)
        mainframe.pack(fill="both", expand=1)
        self.index = 0

        self.frameList = [firstWindow(mainframe, font_size), secondWindow(mainframe), thirdWindow(mainframe)]
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