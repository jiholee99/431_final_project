import tkinter as tk

class UpdateScreen():
    def __init__(self, initial_frame, master, setup_main_screen):
        self.initial_frame = initial_frame
        self.master = master
        self.setup_main_screen = setup_main_screen
        # This frame is the frame for this page
        self.update_screen_frame = tk.Frame(self.master)
        self.setup_update_screen()
    
    def _update_function_element_builder(self,update_frame):
        pady = 5

        # Update function frame title
        update_function_title = tk.Label(update_frame, text="Updating Functions",bg="yellow",)
        update_function_title.pack(fill="both", expand=False, padx=10, pady=pady)

        # Button : Users can add sales data for each game such as the number of copies sold:
        add_sales_data_button = tk.Button(update_frame, text="Add sales data", bg="yellow",)
        add_sales_data_button.pack(fill="both", expand=False, padx=10, pady=pady)

        # Button : User can update game review scores:
        update_review_score_button = tk.Button(update_frame, text="Update review score", bg="yellow",)
        update_review_score_button.pack(fill="both", expand=False, padx=10, pady=pady)


        # Button : Users can edit any information about a game that is wrong
        edit_game_info_button = tk.Button(update_frame, text="Edit game information", bg="yellow",)
        edit_game_info_button.pack(fill="both", expand=False, padx=10, pady=pady)

        # Spacer
        spacer = tk.Label(update_frame, text="", bg="yellow",)
        spacer.pack(fill="both", expand=False, padx=10, pady=pady)

        # Button : Go back to main screen
        go_back_to_main_screen_button = tk.Button(update_frame, text="Go back to main screen", bg="yellow", command=self.go_back_to_main_screen)
        go_back_to_main_screen_button.pack(fill="both", expand=False, padx=10, pady=pady)
    
    def setup_update_screen(self):
        self.initial_frame.pack_forget()

        self.update_screen_frame.pack(fill="both", expand=True)

        self._update_function_element_builder(self.update_screen_frame)
    
    def go_back_to_main_screen(self):
        self.update_screen_frame.pack_forget()
        self.setup_main_screen()