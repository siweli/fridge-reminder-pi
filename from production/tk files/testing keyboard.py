# IMPORTS
import tkinter as tk
from tkinter import font
import tk_keyboard



# APP
class App(tk.Tk):
    caps = False
    def __init__(self):
        tk.Tk.__init__(self)

        screen_width = self.winfo_screenwidth()

        cl_darkblue = "#13131B"
        cl_red = "#F2285B"
        cl_white = "#DDDDDD"



        # variables for later use
        font_size = font.Font(size=screen_width//20)
        btn_size = font.Font(size=screen_width//50)
        # screen_dim = f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}"

        # window setup
        self.title("entry label test kb")
        self.attributes("-fullscreen", True)
        self.config(bg=cl_darkblue)
        self.option_add("*insertBackground", cl_red)

        fr_main = tk.Frame(self, bg=cl_darkblue)
        fr_main.pack(anchor="center", side="top", fill="x")

        btn = tk.Button(fr_main, text="X", bg=cl_red, font=btn_size, command=lambda: self.quit())
        btn.pack(anchor="ne", side="right")
    
        # create a keyboard from my custom keyboard library
        kb = tk_keyboard.Keyboard(self, self.winfo_screenheight(), self.winfo_screenwidth())
        self.kb = kb
        kb.hide()

        # entry
        fr_entries = tk.Frame(fr_main, bg=cl_darkblue)
        fr_entries.pack(anchor="n", side="top", pady=screen_width//50)

        item_name = tk.Entry(fr_entries, 
                            highlightbackground=cl_red,
                            highlightcolor=cl_red,
                            highlightthickness=2,
                            bg=cl_darkblue,
                            fg=cl_white,
                            font=font_size)
        item_name.grid(row=0, column=0)

        expiry = tk.Entry(fr_entries,
                            highlightbackground=cl_red,
                            highlightcolor=cl_red,
                            highlightthickness=2,
                            bg=cl_darkblue,
                            fg=cl_white,
                            font=font_size)
        expiry.grid(row=1, column=0)

        item_name.bind("<FocusIn>", self.entry_focus_in)
        expiry.bind("<FocusIn>", self.entry_focus_in)

        self.entries = [item_name, expiry]

        submit = tk.Button(fr_entries, text="Submit", bg=cl_red, font=btn_size, command=self.get_contents)
        submit.grid(row=2, column=0)

    

    # METHODS
    # get focus of current window as well as show the keyboard
    def entry_focus_in(self, event):
        self.focus = self.focus_get()
        self.kb.show()

    # get contents of the labels as well as hide the keyboard
    def get_contents(self):
        self.kb.hide()
        for i in self.entries:
            print(str(i.winfo_name())+":",i.get())
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
            # print(self.entry_contents)

        elif key == "<":
            self.focus.icursor(cursor_i-1)
        
        elif key == ">":
            self.focus.icursor(cursor_i+1)

        else:
            self.focus.insert(cursor_i, key)



# RUN
if __name__ == "__main__":
    App().mainloop()