import customtkinter
import conventer

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title('YT conventer')
        self.geometry('300x95')

        self.resizable(False,False)

        self.columnconfigure(0, weight=1)
        self.rowconfigure((0,1),weight=1)

        self.button = customtkinter.CTkButton(self, text="Convert", command=self.button_callback)
        self.button.grid(row=1, column=0, padx=10, pady=(0,10))

        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter URL")
        self.entry.grid(row= 0, column = 0, padx=10, pady=10, sticky='ew')


    def button_callback(self):
        Given_URL = self.entry.get()
        length = len(Given_URL)
        # print(type(Given_URL))
        try:
            conventer.url_to_mp3(Given_URL)
            self.entry.delete(0, length)
            self.entry.insert(0, 'Finished downloading')
            print('Finished downloading')
        except Exception as e:
            print(f'Something went wrong: {e}')



app = App()
app.mainloop()