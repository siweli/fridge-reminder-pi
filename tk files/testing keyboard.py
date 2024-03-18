# IMPORTS
import tkinter as tk
from tkinter import font
import tk_keyboard



# APP
class App(tk.Tk):
    bg_colour = "#13131B"
    tx_colour = "#F2285B"
    hl_colour = "#009900"

    caps = False
    def __init__(self):
        tk.Tk.__init__(self)



        # variables for later use
        font_size = font.Font(size=self.winfo_screenwidth()//20)
        screen_dim = f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}"

        # window setup
        self.title("entry label test kb")
        self.attributes("-fullscreen", True)
        self.config(bg=self.bg_colour)

        btn = tk.Button(self, text="X", bg=self.tx_colour, command=lambda: self.quit())
        btn.pack(anchor="ne")
    
        # create a keyboard from my custom keyboard library
        kb = tk_keyboard.Keyboard(self, self.winfo_screenheight(), self.winfo_screenwidth())
        self.kb = kb
        kb.hide()

        # entry
        frame = tk.Frame(self, bg=self.bg_colour)
        frame.pack(anchor="center")

        item_name = tk.Entry(frame, 
                            highlightbackground=self.tx_colour,
                            highlightcolor=self.tx_colour,
                            highlightthickness=2,
                            bg=self.bg_colour,
                            font=font_size)
        item_name.grid(row=0, column=0)

        expiry = tk.Entry(frame,
                            highlightbackground=self.tx_colour,
                            highlightcolor=self.tx_colour,
                            highlightthickness=2,
                            bg=self.bg_colour,
                            font=font_size)
        expiry.grid(row=1, column=0)

        item_name.bind("<FocusIn>", self.entry_focus_in)
        expiry.bind("<FocusIn>", self.entry_focus_in)

        self.entries = [item_name, expiry]

        submit = tk.Button(frame, text="Submit", command= lambda: self.get_contents())
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