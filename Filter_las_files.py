from tkinter import *
from tkinter import filedialog


# searching file path
def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))

    ent1.insert(END, filename)

    return filename


def saveFile():
    save = filedialog.askdirectory()
    ent2.insert(END, save)


def filter():
    try:
        searching_class = input_1.get()
        searching_class = searching_class + '.000000'
        path = ent1.get()
        x = ent2.get()
        y = input_2.get()
        save_path = x + '/' + y + '.txt'
        f = open(path, "r")
        f2 = open(save_path, "w")
        for line in f:
            clas = line.split()[13]
            if clas == searching_class:
                f2.write(line)
        f.close()
        f2.close()

        Done.configure(text="Success", fg='green')

    except:
        Done.configure(text="Error: Wrong data", fg='red')


# creating window
window = Tk()
window.title('Filter .las files')
window.geometry("700x400")

###window


# Instruction
instruction = Label(window, text="""
    Classes:
        0 - Never classified
        1 - Unassigned
        2 - Ground
        3 - Low Vegetation
        4 - Medium Vegetation
        5 - High Vegetation
        6 - Building
        7 - Low Point
        8 - Reserved
        9 - Water
        10 - Rail
        11 - Road Surface
        12 - Reserved
        13 - Wire - Guard Shield
        14 - Wire - Conductor Phase
        15 - Transmission Tower
        16 - Wire Structure Connector Insulator
        17 - Bridge Deck
        18 - High Noise
        """, font=('bold', 10), pady=20, justify=LEFT)

instruction.grid(rowspan=6, row=0, column=0)

# Enter class value
input_class = StringVar()

input_file_text = Label(window, text='Enter class :', font=('bold', 10), pady=20)
input_file_text.grid(row=1, column=1)

input_1 = Entry(window, textvariable=input_class)
input_1.grid(row=1, column=2)

# searching
button_explore = Button(window,
                        text="Choose file",
                        command=browseFiles)

button_explore.grid(row=2, column=1)

# save path
ent1 = Entry(window, font=10)
ent1.grid(row=2, column=2)

# Start
start_button = Button(window,
                      text="Filter",
                      command=filter)

start_button.grid(row=5, column=1)

# save file button
save_button = Button(text='Save path', command=saveFile)
save_button.grid(row=3, column=1)

# show save file button
ent2 = Entry(window, font=10)
ent2.grid(row=3, column=2)

# file name to save
input_file_name = Label(window, text='Insert file name :', font=('bold', 10), pady=20)
input_file_name.grid(row=4, column=1)

input_name = StringVar()
input_2 = Entry(window, textvariable=input_name)
input_2.grid(row=4, column=2)

# writing "Done"
Done = Label(window, text='', font=('bold', 10), pady=20)
Done.grid(row=5, column=2)

window.mainloop()