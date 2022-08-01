# Import modules #
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkterminal import Terminal
from pathlib import Path
import idlelib.colorizer as ic
import idlelib.percolator as ip
import subprocess
import ctypes
import sys


# Empty path variables #
file_name = 'No File'
file_path = ''

# Drawing an UI on the screen with given icon and size #
ide = Tk()
ide.iconphoto(False, PhotoImage(file='resources\icon.png'))
ide.title(f'pyde - Python IDE - {file_name}')
ide.geometry("800x600")


# Options #
def set_file_path(path):
    global file_path
    file_path = path


def run_code():
    if file_path == '':
        save_file_as()
        
        file_name = Path(file_path).name
        ide.title(f'pyde - Python IDE - {file_name}')

    command = f'python {file_path}'
    terminal.run_command(command)


def new_file():
    path = ''
    set_file_path(path)
    
    file_name = 'No File'
    ide.title(f'pyde - Python IDE - {file_name}')
    
    editor.delete(1.0, END)
    terminal.clear()
    statusbar.config(text="Hello World!")


def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
       
        editor.delete(1.0, END)
        editor.insert(1.0, code)
        
        set_file_path(path)
        
        file_name = Path(file_path).name
        cd_folder = Path(file_path).parent

        ide.title(f'pyde - Python IDE - {file_name}')

        command = f'cd {cd_folder}'
        terminal.run_command(command)
        statusbar.config(text="Hello World!")


def save_file_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get(1.0, END)
        file.write(code)
        set_file_path(path)
        
        file_name = Path(file_path).name
        cd_folder = Path(file_path).parent

        ide.title(f'pyde - Python IDE - {file_name}')

        command = f'cd {cd_folder}'
        terminal.run_command(command)


def preferences_menu():
    win = Toplevel(ide)
    win.title(f'pyde - Preferences')
    btn = Button(win, text="COMING SOON", font=("Lucida Console",24))
    btn.pack(expand=True, fill=BOTH)
    win.geometry("500x500")


def exit_program():
	exit()

# Adding top menu bar with options #
menu_bar = Menu(ide)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file_as)
file_menu.add_command(label='Save As', command=save_file_as)
file_menu.add_command(label='Preferences', command=preferences_menu)
file_menu.add_command(label='Exit', command=exit_program)
menu_bar.add_cascade(label='File', menu=file_menu)

run_menu = Menu(menu_bar, tearoff=0)
run_menu.add_command(label='Run', command=run_code)
menu_bar.add_cascade(label='Run', menu=run_menu)

ide.config(menu=menu_bar)

# Text Editor #
editor = Text(wrap=NONE)
editor.pack(expand=True, fill=BOTH)
editor.config(bg="#333333", fg="white", font=("Lucida Console",11), height=32, insertbackground='white')

# Status Bar #
statusbar = Label(ide, text="Hello World!", bd=1, relief=SUNKEN, anchor=E)
statusbar.pack(side=BOTTOM, fill=X)
statusbar.config(bg="#333333", fg="gray", font=("System"))

# Command Line #
terminal = Terminal()
terminal.shell = True
terminal.basename = f"pyde > "
terminal.pack(expand=True, fill=BOTH)
terminal.config(bg="#191919", fg="white", font=("Lucida Console",11), width=140)

# Syntax Highlighting #
cdg = ic.ColorDelegator()
# Text highlight colors #
cdg.tagdefs['COMMENT'] = {'foreground': 'Gray', 'background': '#333333'} # Gray
cdg.tagdefs['KEYWORD'] = {'foreground': '#B097F0', 'background': '#333333'} # Lilac
cdg.tagdefs['BUILTIN'] = {'foreground': '#4DC1BF', 'background': '#333333'} # Light Blue
cdg.tagdefs['STRING'] = {'foreground': '#FFC300', 'background': '#333333'} # Yellow
cdg.tagdefs['DEFINITION'] = {'foreground': '#EB77AE', 'background': '#333333'} # Hot Pink


# Function to count lines and columns of text inside a text widget #
def countlines(event):
    (line, c) = map(int, event.widget.index("end-1c").split("."))

    # Show updates in these widgets: #
    statusbar.config(text=("Line:",line ,"Column:", c))

editor.bind("<KeyRelease>", countlines)


# Init text highlighting #
ip.Percolator(editor).insertfilter(cdg)
# Start Discord RPC #
rpc_proc = subprocess.Popen('python discord_rpc.py')
# Change terminal window title #
ctypes.windll.kernel32.SetConsoleTitleW('pyde')

print("The idea was originally inspired from this video. -> https://www.youtube.com/watch?v=f1u3me4GYmw")
print("Star the original repo to make the developer happy and continue the project :) -> https://github.com/8UA/pyde")

ide.mainloop()

# Killing RPC process and exiting program #
rpc_proc.kill()
sys.exit()
