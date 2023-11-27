import tkinter as tk

class AdminScreen():
    def __init__(self, initial_frame, master, setup_main_screen):
        self.initial_frame = initial_frame
        self.master = master
        self.setup_main_screen = setup_main_screen
        # This frame is the frame for this page
        self.admin_screen_frame = tk.Frame(self.master)
        self.setup_admin_screen()

    def _admin_function_element_builder(self,admin_frame):
        pady = 5

        # Admin function frame title
        admin_function_title = tk.Label(admin_frame, text="Admin Functions",bg="yellow",)
        admin_function_title.pack(fill="both", expand=False, padx=10, pady=pady)

        # Button : Go back to main screen
        go_back_to_main_screen_button = tk.Button(admin_frame, text="Go back to main screen", bg="yellow", command=self.go_back_to_main_screen)
        go_back_to_main_screen_button.pack(fill="both", expand=False, padx=10, pady=pady)
    
    def setup_admin_screen(self):
        self.initial_frame.pack_forget()

        self.admin_screen_frame.pack(fill="both", expand=True)

        self._admin_function_element_builder(self.admin_screen_frame)

    def go_back_to_main_screen(self):
        self.admin_screen_frame.pack_forget()
        self.setup_main_screen()
    
    