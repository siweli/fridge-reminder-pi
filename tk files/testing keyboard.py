# IMPORTS
import tkinter as tk
from tkinter import font
import tk_keyboard



# # hide exe window on run when converted into an exe
# import win32gui, win32con
# exe_window = win32gui.GetForegroundWindow()
# if win32gui.GetWindowText(exe_window)[-3:] == "exe":
#     win32gui.ShowWindow(exe_window, win32con.SW_HIDE)



# APP
class App(tk.Tk):
    bg_colour = "#000000"
    tx_colour = "#AAAAAA"
    hl_colour = "#009900"

    entry_contents = {}
    caps = False
    def __init__(self):
        tk.Tk.__init__(self)



    # variables for later use
        font_size = font.Font(size=self.winfo_screenwidth()//20)
        screen_dim = f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}"

    # window setup
        self.title("entry label test kb")
        self.attributes("-fullscreen", True)
        self.config(bg="#999")

        btn = tk.Button(self, text="X", command=lambda: self.quit())
        btn.grid(row=0, column=1)
    
    # create a keyboard from my custom keyboard library
        kb = tk_keyboard.Keyboard(self, self.winfo_screenheight(), self.winfo_screenwidth())
        self.kb = kb
        kb.hide()

    # entry
        item_name = tk.Entry(self, font=font_size)
        item_name.grid(row=1, column=0)

        expiry = tk.Entry(self, font=font_size)
        expiry.grid(row=2, column=0)

        item_name.bind("<FocusIn>", self.entry_focus_in)
        expiry.bind("<FocusIn>", self.entry_focus_in)

        submit = tk.Button(self, text="Submit", command=lambda: self.get_contents())
        submit.grid(row=3, column=0)

    

    # METHODS
    # get focus of current window as well as show the keyboard
    def entry_focus_in(self, event):
        self.focus = self.focus_get()
        self.kb.show()

    # get contents of the labels as well as hide the keyboard
    def get_contents(self):
        self.kb.hide()
        for i in self.entry_contents.items():
            print(i[0]+":",i[1])
        print()
    
    # handle the keyboard and it's outputs
    def return_key(self, key):
        cursor_i = self.focus.index("insert")
        if not self.caps:
            key = key.lower()

        if key.upper() == "SPACE":
            self.focus.insert(cursor_i, " ")

        elif key.upper() == "BACK":
            contents = self.focus.get()
            index = cursor_i-1
            if index == -1:
                pass
            else:
                self.focus.delete(0, "end")
                contents = contents[:index] + contents[index+1:]
                self.focus.insert(0, contents)
                self.focus.icursor(index)

        elif key.upper() == "CAPS":
            self.caps = not self.caps
            print(self.entry_contents)

        elif key == "<":
            self.focus.icursor(cursor_i-1)
        
        elif key == ">":
            self.focus.icursor(cursor_i+1)

        else:
            self.focus.insert(cursor_i, key)
        
        self.entry_contents[self.focus.winfo_name()] = self.focus.get()
    


# RUN
if __name__ == "__main__":
    App().mainloop()