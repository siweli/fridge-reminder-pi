# IMPORTS
import tkinter as tk
from tkinter import font


# # hide exe window on run when converted into an exe
# import win32gui, win32con
# exe_window = win32gui.GetForegroundWindow()
# if win32gui.GetWindowText(exe_window)[-3:] == "exe":
#     win32gui.ShowWindow(exe_window, win32con.SW_HIDE)


# APP
class Keyboard(tk.Toplevel):
    bg_colour = "#000000" # background colour
    ky_colour = "#555555" # key background colour
    fg_colour = "#DDDDDD" # text colour
    bd_colour = "#000000" # border colour
    av_colour = "#777777" # colour when key is clicked

    last_key = None
    
    def __init__(self, parent=None, s_height=300, s_width=400): # 300x400 chosen for default size if none passed in
        self.parent = parent
        tk.Toplevel.__init__(self)


    # variables for later use
        font_size = font.Font(size=int(s_height*0.025))
        h = s_height // 2.5
        geom = f"{s_width}x{s_height//3}+0+{int(s_height-h)}" # set it at the bottom of the screen
        #geom = f"{s_width}x{s_height//3}+0+200"
        # look into removing the 1px border around the window

    # window setup
        self.title("Keyboard")
        self.geometry(geom)
        self.resizable(0, 0)
        self.overrideredirect(True)
        self.config(bg=self.bg_colour)
        self.attributes('-topmost', True)
        


    # keys
        # define a custom layout for the keys    
        keyboard = [["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "BACK"],
                    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "CAPS"],
                    ["A", "S", "D", "F", "G", "H", "J", "K", "L", "-", "/"],
                    ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "<", ">"],
                    ["SPACE"]]
        
        # loop through each row of the keyboard and each key of each row
        for row_count, rows in enumerate(keyboard):
            col_shift=0
            for column_count, key in enumerate(rows):
                if key in ["BACK", "CAPS", "ENTER"]:
                    col_span = 2
                else: col_span = 1
                if key == "SPACE": col_shift, col_span = 4, 4

            # border for key
                border = tk.Frame(self,
                                  bg=self.bg_colour,
                                  highlightbackground=self.bd_colour,
                                  highlightthickness=1,
                                  takefocus = 0)
                border.grid(padx=2,
                            pady=2,
                            sticky="nsew",
                            row=row_count,
                            column=column_count+col_shift,
                            columnspan=col_span)
            
            # button for each key
                tk.Button(border,
                          text=key,
                          font=font_size,
                          bg=self.ky_colour,
                          fg=self.fg_colour,
                          activebackground=self.av_colour,
                          relief="flat",
                          takefocus=0,
                          command=lambda m=key: self.on_press(m)
                          ).pack(expand=True, fill='both')
                
                self.rowconfigure(row_count, weight=1)
                self.columnconfigure(column_count, weight=1)
                if key == "CAPS": col_shift=1 # handle the double width keys that arent on the end or the keys overlap
                
# on each key press
    def on_press(self, key):
        self.parent.return_key(key)

# show the keyboard window
    def show(self):
        self.deiconify()

# hide the keyboard window
    def hide(self):
        self.withdraw()

# close the keyboard window
    def kill(self):
        self.destroy()