# Hello everyone! this is Rahul Tiwari. I tried my best to make an app for user friendly GUI and added some basic tools to made user more Efficient.

import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os


main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('Textpad: Text Writer & Editor')

####--------- Main Menu -----------------########
main_menu = tk.Menu()

#file icons
new_icon=tk.PhotoImage(file='icons2/new.png')
open_icon=tk.PhotoImage(file='icons2/open.png')
save_icon=tk.PhotoImage(file='icons2/save.png')
save_as_icon=tk.PhotoImage(file='icons2/save_as.png')
exit_icon=tk.PhotoImage(file='icons2/exit.png')

#file_menu
file = tk.Menu(main_menu, tearoff=False)

#Edit bar 
edit = tk.Menu(main_menu, tearoff=False)

#View bar
view = tk.Menu(main_menu, tearoff=False)

#Color Theme
color_theme = tk.Menu(main_menu, tearoff=False)

light_theme = tk.PhotoImage(file='icons2/light_default.png')
light_plus_theme=tk.PhotoImage(file='icons2/light_plus.png')
dark_theme=tk.PhotoImage(file='icons2/dark.png')

theme_choice = tk.StringVar()
color_icons=(light_theme, light_plus_theme, dark_theme)

color_dict ={
    'ultra light':('#474747','#e0e0e0'),
    'light':('#000000', '#ffffff'),
    'Dark' : ('#c4c4c4', '#2d2d2d')
}

#cascading 
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Theme', menu=color_theme)

###----------- Ending --------------- #####


####--------- toolbar -----------------########
tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

#Font Box
font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0, column=0, padx=5)

#Size box
size_var = tk.IntVar()
font_size=ttk.Combobox(tool_bar, width=14, textvariable=size_var, state='readonly')
font_size['values'] = tuple(range(6,80,2))
font_size.current(1)
font_size.grid(row=0, column=1, padx=0.2)

#Bold Button
bold_icon = tk.PhotoImage(file='icons2/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

#italic icon
italic_icon=tk.PhotoImage(file='icons2/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

#Underline icon
underline_icon = tk.PhotoImage(file='icons2/underline.png')
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

#Font Color Button
font_color_icon = tk.PhotoImage(file='icons2/font_color.png')
font_color_btn = ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column = 5, padx=5)

#Allign left button
Allign_left_color_icon = tk.PhotoImage(file='icons2/align_left.png')
Allign_left_color_btn = ttk.Button(tool_bar, image=Allign_left_color_icon)
Allign_left_color_btn.grid(row=0, column = 6, padx=5)

#Allign Centre button
Allign_centre_color_icon = tk.PhotoImage(file='icons2/align_center.png')
Allign_centre_color_btn = ttk.Button(tool_bar, image=Allign_centre_color_icon)
Allign_centre_color_btn.grid(row=0, column = 7, padx=5)

#Allign Right button
Allign_right_color_icon = tk.PhotoImage(file='icons2/align_right.png')
Allign_right_color_btn = ttk.Button(tool_bar, image=Allign_right_color_icon)
Allign_right_color_btn.grid(row=0, column = 8, padx=5)

###----------- end toolbar --------------- #####

####--------- text editor -----------------########
text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

text_editor.focus_set()
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# Font Family & Font Size Functionality
current_font_family = 'Arial'
current_font_Size = 12

def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_Size))

def change_fontsize(event=None):
    global current_font_Size
    current_font_Size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_Size))

font_box.bind('<<ComboboxSelected>>', change_font)
font_size.bind('<<ComboboxSelected>>', change_fontsize)

#Bold buttons fumctionality
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(current_font_family, current_font_Size, 'normal'))
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_family, current_font_Size, 'bold'))

bold_btn.configure(command=change_bold)

#italic button functionality
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family, current_font_Size, 'italic'))
    if text_property.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family, current_font_Size, 'roman'))
 
italic_btn.configure(command=change_italic)

#underline button functionality
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==0:
        text_editor.configure(font=(current_font_family, current_font_Size, 'underline'))
    if text_property.actual()['underline']==1:
        text_editor.configure(font=(current_font_family, current_font_Size, 'normal'))

underline_btn.configure(command=change_underline)

#change font color functionality 
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=change_font_color)

#Allign Left functionality
def allign_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify =tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

Allign_left_color_btn.configure(command = allign_left)

#Allign Right functionality
def allign_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify =tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

Allign_right_color_btn.configure(command = allign_right)

#Allign Centre functionality
def allign_centre():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify =tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

Allign_centre_color_btn.configure(command=allign_centre)

text_editor.configure(font=('Arial', 12))

###----------- End text editor --------------- #####



####--------- main status bar -----------------########

status_bar = ttk.Label(main_application, text = 'Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False
def status_status(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        charecters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f'Charecters : {charecters} words : {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>', status_status )
###----------- End main status bar --------------- #####

####--------- Functionality -----------------########

# Variable

url = ''
def new_file(event=None):
    global url
    url=''
    text_editor.delete(1.0, tk.END)

#file command functionality 

file.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='ctrl+N', command=new_file)

# opne command functionality 
def open_file(event=None):
    global url
    url= filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('All Files', '*.*'),('Text Files', '*.txt')))
    try:
        with open(url, 'r') as rf:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, rf.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))


file.add_command(label='Open',image=open_icon, compound=tk.LEFT, accelerator='ctrl+O', command=open_file)

#Save File functionality
def save_file(event=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as rf:
                rf.write(content)
        else:
            url= filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('All Files', '*.*'),('Text Files', '*.txt')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return

file.add_command(label='Save',image=save_icon, compound=tk.LEFT, accelerator='ctrl+S', command=save_file)

##SAve as Functionality

def save_as_file(event=None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('All Files', '*.*'),('text files', '*.txt')))
        url.write(content)
        url.close()
    except:
        return
file.add_command(label='Save As',image=save_as_icon, compound=tk.LEFT, accelerator='ctrl+alt+S', command=save_as_file)

#Exit Button Functionality
def exit_fn(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = text_editor.get(1.0, tk.END)
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetype=(('text file', '*.txt'),('All File', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()

            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return

file.add_command(label='Exit',image=exit_icon, compound=tk.LEFT, accelerator='ctrl+Q', command = exit_fn)

#edit commands

edit.add_command(label='Cut', compound=tk.LEFT, accelerator='cntr+X', command = lambda:text_editor.event_generate("<<Control x"))
edit.add_command(label='Copy', compound=tk.LEFT, accelerator='cntr+C', command = lambda:text_editor.event_generate("<<Control c"))
edit.add_command(label='Paste', compound=tk.LEFT, accelerator='cntr+V', command = lambda:text_editor.event_generate("<<Control v"))
edit.add_command(label='Clear All', compound=tk.LEFT, accelerator='cntr+alt+x', command = lambda:text_editor.delete(1.0, tk.END))

def find_fn(event=None):
    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches=0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos} + {len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches +=1
                start_pos = end_pos
                text_editor.tag_config('match', foreground = 'red', background='yellow')

    def replace():
        word = find_input.get()
        replacing_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replacing_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    text_find_label = ttk.Label(find_frame, text='Find :')
    text_replace_label = ttk.Label(find_frame, text='Replace : ')

    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text='Replace', command=replace)

    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()
edit.add_command(label='Find', compound=tk.LEFT, accelerator='cntr+F', command=find_fn)
# edit.add_command(label='Replace', compound=tk.LEFT, accelerator='cntr+H', command=find_fn)
# edit.add_command(label='Select All', compound=tk.LEFT, accelerator='cntr+A', command = lambda:text_editor.)

# view checkbuttons
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True

view.add_checkbutton(label='Tool Bar',onvalue=True, offvalue=0, variable = show_toolbar, compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label='Status Bar', onvalue=True, offvalue=0, variable = show_statusbar, compound=tk.LEFT, command=hide_statusbar)


#Color themes command
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, foreground=fg_color)

count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT, command = change_theme)
    count +=1
###----------- End Functionality --------------- #####

main_application.config(menu=main_menu)


#binding shortcut keys
main_application.bind('<Control-n>', new_file)
main_application.bind('<Control-o>', open_file)
main_application.bind('<Control-s>', save_file)
main_application.bind('<Control-Alt-s>', save_as_file)
main_application.bind('<Control-q>', exit_fn)
main_application.bind('<Control-f>', find_fn)

main_application.mainloop()
