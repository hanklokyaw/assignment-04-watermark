import os
from add_watermark import start_process
from tkinter import Tk, Label, Button, filedialog

# Take a folder and iterate through each file in that directory
class FILE_IO():

    def __init__(self):
        self.default_logo_name = 'logo.png'
        self.root_dir = os.getcwd()
        self.source_dir = self.root_dir + '/source/'
        self.logo_file = self.root_dir + '/logo/' + self.default_logo_name
        self.output_dir = self.root_dir + '/output/'
        self.source_file = self.root_dir + '/source/image2.jpg'
        self.user_logo_file = self.logo_file
        self.user_source_dir = self.source_dir
        self.user_output_dir = self.output_dir

    def browseLogoFiles(self):
        filename = filedialog.askopenfilename(initialdir=self.logo_file,
                                              title=f"{self.logo_file}",
                                              filetypes=(("PNG files",
                                                          "*.png"),
                                                         ("JPG files",
                                                          "*.jpg"),
                                                         ("GIF files",
                                                          "*.gif"),
                                                         ("all files",
                                                          "*.*")))
        # Change label contents
        self.logo_file_explorer.configure(text=filename)
        if filename == "":
            self.user_logo_file = self.logo_file
            print(f"local - {self.user_logo_file}")
        else:
            self.user_logo_file = filename
            print(f"local - {self.user_logo_file}")

    def browseSourceFolder(self):
        foldername = filedialog.askdirectory(initialdir=self.source_dir,
                                              title=f"{self.source_dir}")
        # Change label contents
        self.source_folder_explorer.configure(text=foldername)
        if foldername == "":
            self.user_source_dir = self.source_dir
            # print(f"local - {self.user_source_dir}")
        else:
            self.user_source_dir = foldername
            # print(f"local - {self.user_source_dir}")

    def browseOutputFolder(self):
        foldername = filedialog.askdirectory(initialdir=self.output_dir,
                                              title=f"{self.output_dir}")
        # Change label contents
        self.output_folder_explorer.configure(text=foldername)
        if foldername == "":
            self.user_output_dir = self.output_dir
            # print(f"local - {self.user_output_dir}")
        else:
            self.user_output_dir = foldername
            # print(f"local - {self.user_output_dir}")


    def open_folder(self):
        try:
            for filename in os.listdir(self.user_source_dir):
                file = os.path.join(self.user_source_dir, filename)
                if os.path.isfile(file):
                    start_process(self.user_logo_file, file).save(self.user_output_dir + filename)
                    print(f"Watermark added to: {file}")
        except:
                print("File open error.")

