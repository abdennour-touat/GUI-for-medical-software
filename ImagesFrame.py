import tkinter as  tk
from PIL import Image,ImageTk

class ImageContainer(tk.Frame):
    def __init__(self, master=None,row=None, column=None,title='', image=None):
        super().__init__(master, bg='black',highlightbackground="white",highlightthickness=1)
        self.master = master
        self.row = row
        self.column = column
        self.image = image
        self.set_image_and_title(title=title, image=self.image)




    def set_image_and_title(self, title='', image = None):
        self.grid(row=self.row, column=self.column, sticky='nwse', pady=10, padx=15)
        tk.Grid.rowconfigure(self, 1, weight=1)
        tk.Grid.columnconfigure(self, 0, weight=1)
        self.update()
        print(self.winfo_width())

        title_label = tk.Label(self, text=title, fg='white', bg='gray')
        resized_image = image.resize((330, 310), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image)
        image_label = tk.Label(self, image=new_image, bg='black')
        image_label.image = new_image

        title_label.grid(row=0, column=0, sticky='nsew')
        image_label.grid(row=1, column=0, sticky='nsew')


class ImagesContainer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master,bg='black', highlightbackground="white", highlightthickness=1)
        self.master = master

        #grid Config

        tk.Grid.rowconfigure(self, 0, weight=0)
        tk.Grid.rowconfigure(self, 2, weight=1)
        tk.Grid.rowconfigure(self, 1, weight=1)
        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 1, weight=1)
        tk.Grid.columnconfigure(self, 3, weight=0)
        #create the frames
        self.img = (Image.open("./src/nanmi.png"))
        self.create_title()
        self.create_frames()

    def create_frames(self):

        frame1 = ImageContainer(row=1, column=0, master=self,title = 'image Original',image= self.img)
        frame2 = ImageContainer(row=1, column=1, master=self, title='image Original', image=self.img)
        frame3 = ImageContainer(row=2, column=0, master=self, title='image Original', image=self.img)
        frame4 = ImageContainer(row=2, column=1, master=self, title='image Original', image=self.img)

    def create_title(self):
        # create the top title
        title_label = tk.Label(self, text='visualisation', fg='white', bg='black', highlightbackground="white",highlightthickness=1)
        title_label.grid(row=0, column=0, columnspan=2, sticky='nsew')






if __name__ == "__main__":
    app = tk.Tk()
    app.geometry(f"{app.winfo_screenwidth()}x{app.winfo_screenheight() - 60}")
    app.resizable(width=False, height=False)
    app.title('visualisation')
    app.configure(background='white')
    tk.Grid.rowconfigure(app, 0, weight=1)
    tk.Grid.columnconfigure(app, 0, weight=4)
    tk.Grid.columnconfigure(app, 1, weight=4)

    root = ImagesContainer(app)
    root.grid(row=0,column=0, sticky='nswe')
    root.mainloop()
