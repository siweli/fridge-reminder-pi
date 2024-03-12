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


    # variables for later use
        font_size = font.Font(size=self.winfo_screenwidth()//100)
        screen_dim = f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}"


    # window setup
        self.title("Entry-Summon-kb")
        self.geometry("400x400+0+0")
        self.config(bg="#999")
    

    # create a keyboard from my custom keyboard library
        #sub = tk.Toplevel()
        kb = tk_keyboard.Keyboard(self, self.winfo_screenheight(), self.winfo_screenwidth())
        self.kb = kb
        kb.hide()


    
        

    # display some crap
        tk.Label(self, text="entry").grid(row=0, column=0)
        entry = tk.Entry(self)
        self.entry = entry
        entry.grid(row=1, column=0)

        entry.bind("<FocusIn>", self.entry_focus_in)
        #entry.bind("<FocusOut>", self.entry_focus_out)

        self.out = tk.Label(self, text="output")
        self.out.grid(row=2, column=0)

    

    
    # methods
    def entry_focus_in(self, event):
        self.kb.show()

    def entry_focus_out(self, event):
        self.kb.hide()
    

    # handle the keyboard and it's outputs
    def return_key(self, key):
        cursor_i = self.entry.index("insert")
        if not self.caps:
            key = key.lower()

        if key.upper() == "SPACE":
            self.entry.insert(cursor_i, " ")

        elif key.upper() == "BACK":
            contents = self.entry.get()
            index = cursor_i-1
            if index == -1:
                pass
            else:
                self.entry.delete(0, "end")
                contents = contents[:index] + contents[index+1:]
                self.entry.insert(0, contents)
                self.entry.icursor(index)

        elif key.upper() == "CAPS":
            self.caps = not self.caps


        elif key.upper() == "ENTER":
            txt = self.entry.get()
            self.out.config(text=txt)

        elif key == "<":
            self.entry.icursor(cursor_i-1)
        
        elif key == ">":
            self.entry.icursor(cursor_i+1)

        else:
            self.entry.insert(cursor_i, key)
        
        self.entry.focus_set()
    



# RUN
if __name__ == "__main__":
    #main = tk.Tk()

    App().mainloop()