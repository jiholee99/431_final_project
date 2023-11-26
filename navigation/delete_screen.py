import tkinter as tk

class DeleteScreen():
    def __init__(self, initial_frame, master, setup_main_screen):
        self.initial_frame = initial_frame
        self.master = master
        self.setup_main_screen = setup_main_screen
        # This frame is the frame for this page
        self.delete_screen_frame = tk.Frame(self.master)
        self.setup_delete_screen()

    def _delete_function_element_builder(self,delete_frame):
        pady = 5

        # Delete function frame title
        delete_function_title = tk.Label(delete_frame, text="Deleting Functions",bg="red",)
        delete_function_title.pack(fill="both", expand=False, padx=10, pady=pady)

        # Button : Go back to main screen
        go_back_to_main_screen_button = tk.Button(delete_frame, text="Go back to main screen", bg="red", command=self.go_back_to_main_screen)
        go_back_to_main_screen_button.pack(fill="both", expand=False, padx=10, pady=pady)
    
    def setup_delete_screen(self):
        self.initial_frame.pack_forget()

        self.delete_screen_frame.pack(fill="both", expand=True)

        self._delete_function_element_builder(self.delete_screen_frame)
    
    def go_back_to_main_screen(self):
        self.delete_screen_frame.pack_forget()
        self.setup_main_screen()
        