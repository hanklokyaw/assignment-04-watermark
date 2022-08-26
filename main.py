from tkinter import Tk, Label, Button, filedialog
import os
from open_folder import FILE_IO

app = FILE_IO()
window = Tk()
window.geometry("650x300")
window.resizable(0,0)
window.config(background="white")
window.title("Bulk Image Watermark")

# Files and Directories
# default_logo_name = 'logo.png'
# root_dir = os.getcwd()
# source_dir = root_dir + '/source/'
# logo_file = root_dir + '/logo/' + default_logo_name
# output_dir = root_dir + '/output/'
# source_file = root_dir + '/source/image2.jpg'

# app.open_folder(logo_file, source_dir, output_dir)
# #
# #
# Create a File Explorer label
logo_label = Label(window,
                   text="Logo",
                   width=5,
                   height=1,
                   anchor="s"
                   )
app.logo_file_explorer = Label(window,
                            text=f"{app.logo_file}",
                            width=42,
                            height=1,
                            bg="light grey",
                           anchor="e"
                           )

logo_button_explore = Button(window,
                        text="Browse Files",
                        command=app.browseLogoFiles)

source_label = Label(window,
                   text="Source",
                   width=5,
                   height=1,
                   anchor="s"
                   )
app.source_folder_explorer = Label(window,
                            text=f"{app.source_dir}",
                            width=42,
                            height=1,
                            bg="light grey",
                           anchor="e"
                           )

source_button_explore = Button(window,
                        text="Browse Files",
                        command=app.browseSourceFolder)

output_label = Label(window,
                   text="Output",
                   width=5,
                   height=1,
                   anchor="s"
                   )
app.output_folder_explorer = Label(window,
                            text=f"{app.output_dir}",
                            width=42,
                            height=1,
                            bg="light grey",
                           anchor="e"
                           )

output_button_explore = Button(window,
                        text="Browse Files",
                        command=app.browseOutputFolder)

start_btn = Button(window,
                     text="Start",
                     width=15,
                     background="light blue",
                     command=app.open_folder)
exit_btn = Button(window,
                     text="Exit",
                     width=9,
                     command=exit)
note_label = Label(window,
                   text=f"Note: 1.Default logo file, source folder, and output folder could modify by user.\n"
                        f"          2.All images in source folder will be added with logo.png water mark then saved to outputfolder.\n"
                        f"          3.All images in output folder will be overwritten every time user start the process.\n"
                        f"          4.The logo file is expanded according to the source images files, 20% of height or width.\n"
                        f"          5.The output images will appear after the program close.",
                   height=5,
                   fg="grey",
                   justify="left"
                   )


# Grid method is chosen for placing the widgets at respective positions
# in a table like structure by specifying rows and columns
logo_label.grid(column=0, row=0, padx=10, pady= 10)
app.logo_file_explorer.grid(column=1, row=0, padx=10, pady= 10)
logo_button_explore.grid(column=2, row=0)
source_label.grid(column=0, row=1, padx=10, pady= 10)
app.source_folder_explorer.grid(column=1, row=1, padx=10, pady= 10)
source_button_explore.grid(column=2, row=1)
output_label.grid(column=0, row=2, padx=10, pady= 10)
app.output_folder_explorer.grid(column=1, row=2, padx=10, pady= 10)
output_button_explore.grid(column=2, row=2)
start_btn.grid(column=1, row=3)
exit_btn.grid(column=2, row=3)
note_label.grid(column=0, row=4, padx=10, pady= 10,columnspan=3)

window.mainloop()