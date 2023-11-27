import tkinter as tk

class InsertScreen() :
    def __init__(self, initial_frame, master, setup_main_screen):
        self.initial_frame = initial_frame
        self.master = master
        self.setup_main_screen = setup_main_screen
        # This frame is the frame for this page
        self.insert_screen_frame = tk.Frame(self.master)
        self.setup_insert_screen()
    
    def _insert_function_element_builder(self,insert_frame):
        pady = 5

        # Insert function frame title
        insert_function_title = tk.Label(insert_frame, text="Inserting Functions",bg="green",)
        insert_function_title.pack(fill="both", expand=False, padx=10, pady=pady)

        # Button : Go back to main screen
        go_back_to_main_screen_button = tk.Button(insert_frame, text="Go back to main screen", bg="green", command=self.go_back_to_main_screen)
        go_back_to_main_screen_button.pack(fill="both", expand=False, padx=10, pady=pady)

    def setup_insert_screen(self):
        self.initial_frame.pack_forget()

        self.insert_screen_frame.pack(fill="both", expand=True)

        self._insert_function_element_builder(self.insert_screen_frame)

    def go_back_to_main_screen(self):
        self.insert_screen_frame.pack_forget()
        self.setup_main_screen()