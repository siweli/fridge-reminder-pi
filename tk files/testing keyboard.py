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

    caps = False
    def __init__(self):
        tk.Tk.__init__(self)

        # self.winfo_screenwidth()
        # self.winfo_screenheight()


    # variables for later use
        font_size = font.Font(size=self.winfo_screenwidth()//100)
        screen_dim = f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}"


    # window setup
        self.title("Entry-Summon-kb")
        # self.geometry("400x400+0+0")
        self.attributes("-fullscreen", True)
        self.config(bg="#999")

        btn = tk.Button(self, text="X", command=lambda: self.quit())
        btn.grid(row=0, column=1)
    

    # create a keyboard from my custom keyboard library
        #sub = tk.Toplevel()
        kb = tk_keyboard.Keyboard(self, self.winfo_screenheight(), self.winfo_screenwidth())
        self.kb = kb
        kb.hide()


    
        

    # entry
        tk.Label(self, text="entry").grid(row=0, column=0)
        item_name = tk.Entry(self)
        item_name.grid(row=1, column=0)

        expiry = tk.Entry(self)
        expiry.grid(row=2, column=0)

        item_name.bind("<FocusIn>", self.entry_focus_in)
        expiry.bind("<FocusIn>", self.entry_focus_in)

        self.out = tk.Label(self, text="output")
        self.out.grid(row=3, column=0)

    

    
    # methods
    def entry_focus_in(self, event):
        self.focus = self.focus_get()
        self.kb.show()

    def entry_focus_out(self, event):
        self.kb.hide()

    def output(self, _from, text):
        print(_from+":",text)
    

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

        elif key.upper() == "ENTER":
            txt = self.focus.get()
            # self.out.config(text=txt)
            self.output(self.focus.winfo_name(), txt)

        elif key == "<":
            self.focus.icursor(cursor_i-1)
        
        elif key == ">":
            self.focus.icursor(cursor_i+1)

        else:
            self.focus.insert(cursor_i, key)
        
        self.focus.focus_set()
    



# RUN
if __name__ == "__main__":
    #main = tk.Tk()

    App().mainloop()