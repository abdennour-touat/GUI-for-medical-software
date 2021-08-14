import tkinter as tk
from tkinter import ttk as ttk
from PIL import Image,ImageTk



class App(tk.Tk):
    def __init__(self):
        #root configuration
        super().__init__()
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()-60}")
        self.resizable(width=False, height=False)
        self.title('visualisation')
        self.configure(background='black')
        # configure the grid
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 0, weight=6)
        tk.Grid.columnconfigure(self, 1, weight=4)
        style = ttk.Style()

        style.configure('TButton', font=
        ('Helvetica', 15, 'bold','italic'),
                        foreground='black', width=5)
        self.create_containers()

    def create_containers(self):
        # creating two containers, one for display the images and the other for the buttons
        self.create_images_container()
        self.create_buttons_containers()

    def create_images_container(self):
        images_frame = tk.Frame(self, bg='black', highlightbackground="white", highlightthickness=1 )
        images_frame.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)

        # configure images_frame grid
        tk.Grid.rowconfigure(images_frame, 0, weight=0)
        tk.Grid.rowconfigure(images_frame, 2, weight=1)
        tk.Grid.rowconfigure(images_frame, 1, weight=1)
        tk.Grid.columnconfigure(images_frame, 0, weight=1)
        tk.Grid.columnconfigure(images_frame, 1, weight=1)
        tk.Grid.columnconfigure(images_frame, 3, weight=0)

        # create the top title
        title_label = tk.Label(images_frame, text='visualisation', fg='white', bg='black', highlightbackground="white",
                               highlightthickness=1)
        title_label.grid(row=0,column=0,columnspan=2, sticky='nsew')
        # to create the containers for the images
        self.create_images_frames(master=images_frame)

    def create_images_frames(self, master=None):
        frame1 = tk.Frame(master, bg='black',highlightbackground="white",
                               highlightthickness=1)
        frame2 = tk.Frame(master, bg='black',highlightbackground="white",
                               highlightthickness=1)
        frame3 = tk.Frame(master, bg='black',highlightbackground="white",
                               highlightthickness=1)
        frame4 = tk.Frame(master, bg='black',highlightbackground="white",
                               highlightthickness=1)
        frame1.grid(row=1, column=0,sticky='nwse', pady=10, padx=15)
        frame2.grid(row=1, column=1,sticky='nesw', pady=10, padx=15)
        frame3.grid(row=2, column=0,sticky='swne', pady=10, padx=15)
        frame4.grid(row=2, column=1,sticky='senw', pady=10, padx=15)

        #image resize
        img = (Image.open("./src/nanmi.png"))
        frame4.update()
        resized_image = img.resize((frame4.winfo_width(), frame4.winfo_height()), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image)

        self.set_image_and_title(master=frame1,title='image Original', image=new_image)
        self.set_image_and_title(master=frame2, title='Extraction du Scalp', image=new_image)
        self.set_image_and_title(master=frame3, title='Pretraitement', image=new_image)
        self.set_image_and_title(master=frame4, title='Segmentation/Localisation 2D', image=new_image)

    def set_image_and_title(self,title='', image=None, master=None):

        tk.Grid.rowconfigure(master, 1, weight=1)
        tk.Grid.columnconfigure(master, 0, weight=1)
        title_label = tk.Label(master,text=title, fg='white', bg='gray')

        image_canvas = tk.Label(master,image=image, bg ='black')
        image_canvas.image = image

        title_label.grid(row=0,column=0, sticky='nsew')
        image_canvas.grid(row=1,column=0, sticky='nsew')

    def create_buttons_containers(self):
        buttons_frame = tk.Frame(self, bg='black')
        buttons_frame.grid(row=0, column=1, sticky="nsew")
        self.create_buttons(master=buttons_frame)

    def create_buttons(self,master=None):
        #column and row config
        tk.Grid.columnconfigure(master,index=0,weight=2)
        tk.Grid.columnconfigure(master,index=1,weight=3)
        #tk.Grid.rowconfigure(master, index=0, weight=1)
        #tk.Grid.rowconfigure(master, index=1, weight=1)

        title_label = tk.Label(master, text='Manipulation',bg='black',fg='white',font=('Helvetica bold',16), highlightbackground="white", highlightthickness=1)
        title_label.grid(row=0, column=1, sticky='nswe', pady=(25,25), padx=5)
        title_label = tk.Label(master, text='icon', bg='cyan', fg='black', font=('Helvetica bold', 16))
        title_label.grid(row=0, column=0, sticky='nswe', pady=(25, 25), padx=10)

        title_label1 = tk.Label(master, text='icon', bg='cyan', fg='black', font=('Helvetica bold', 16))
        title_label1.grid(row=1, column=0, columnspan=1, sticky='nswe', pady=23, padx=10)
        button1_label = ttk.Button(master, text='Image Original')
        button1_label.grid(row=1, column=1, sticky='nswe',  pady=23, padx=5)

        title_label2 = tk.Label(master, text='icon', bg='cyan', fg='black', font=('Helvetica bold', 16))
        title_label2.grid(row=2, column=0, sticky='nswe', pady=23, padx=10)
        button2_label = ttk.Button(master, text='Extraction du Scalp')
        button2_label.grid(row=2, column=1, sticky='nswe', pady=23, padx=5)

        title_label3 = tk.Label(master, text='icon', bg='cyan', fg='black', font=('Helvetica bold', 16))
        title_label3.grid(row=3, column=0, sticky='nswe', pady=23, padx=10)
        button3_label = ttk.Button(master, text='Pretraitement')
        button3_label.grid(row=3, column=1, sticky='nswe', pady=23, padx=5)

        title_label4 = tk.Label(master, text='icon', bg='cyan', fg='black', font=('Helvetica bold', 16))
        title_label4.grid(row=4, column=0, columnspan=1, sticky='nswe', pady=23, padx=10)
        button4_label = ttk.Button(master, text='Segmentation')
        button4_label.grid(row=4, column=1, sticky='nswe', pady=23, padx=5)

        title_label4 = tk.Label(master, text='icon', bg='cyan', fg='black', font=('Helvetica bold', 16))
        title_label4.grid(row=5, column=0, columnspan=1, sticky='nswe', pady=23, padx=10)
        button4_label = ttk.Button(master, text='Localisation 2D')
        button4_label.grid(row=5, column=1, sticky='nswe', pady=23, padx=5)

        title_label4 = tk.Label(master, text='icon', bg='cyan', fg='black', font=('Helvetica bold', 16))
        title_label4.grid(row=6, column=0, columnspan=1, sticky='nswe', pady=23, padx=10)
        button4_label = ttk.Button(master, text='Calcul de la surface')
        button4_label.grid(row=6, column=1, sticky='nswe', pady=23, padx=5)


if __name__ == "__main__":
    app = App()
    app.mainloop()
