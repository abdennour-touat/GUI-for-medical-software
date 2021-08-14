import tkinter as tk
from tkinter import ttk as ttk



class ButtonsFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg='black',highlightbackground="white",highlightthickness=1)
        self.master = master
        self.buttons_texts = ['Image Original', 'Extraction du Scalp', 'Pretraitement', 'Segmentation', 'Localisation 2D', 'Calcul de la surface']
        #style config
        self.style = ttk.Style()
        self.style.configure('TButton', font=
        ('Helvetica', 15, 'bold', 'italic'),
                       foreground='black', width=5)
        self.grid(row=0, column=1, sticky="nsew")
        #grid config
        tk.Grid.columnconfigure(self, index=0, weight=2)
        tk.Grid.columnconfigure(self, index=1, weight=3)
        self.create_title_label(text='Manipulation')
        self.create_buttons()

    def create_title_label(self, text=''):
        title_label = tk.Label(self, text=text, bg='black', fg='white', font=('Helvetica bold', 16),
                               highlightbackground="white", highlightthickness=1)
        title_label.grid(row=0, column=1, sticky='nswe', pady=(25, 25), padx=5)
        icon_label = tk.Label(self, text='icon', bg='cyan', fg='black', font=('Helvetica bold', 16))
        icon_label.grid(row=0, column=0, sticky='nswe', pady=(25, 25), padx=10)

    def create_buttons(self):
        for i in range(1, 6):
            self.create_button(row=i)

    def create_button(self, row=0):
        title_label4 = tk.Label(self, text='icon', bg='cyan', fg='black', font=('Helvetica bold', 16))
        title_label4.grid(row=row, column=0, columnspan=1, sticky='nswe', pady=23, padx=10)
        button4_label = ttk.Button(self, text=self.buttons_texts[row])
        button4_label.grid(row=row, column=1, sticky='nswe', pady=23, padx=5)

if __name__ == "__main__":
    app = tk.Tk()
    app.geometry(f"{app.winfo_screenwidth()}x{app.winfo_screenheight() - 60}")
    app.resizable(width=False, height=False)
    app.title('visualisation')
    app.configure(background='white')
    tk.Grid.rowconfigure(app, 0, weight=1)
    tk.Grid.columnconfigure(app, 0, weight=4)
    tk.Grid.columnconfigure(app, 1, weight=4)

    root = ButtonsFrame(app)
    root.grid(row=0,column=0, sticky='nswe')
    root.mainloop()
