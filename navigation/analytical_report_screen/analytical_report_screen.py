import tkinter as tk

import navigation.analytical_report_screen.game_report_screen as drs

class AnalyticalReportScreen():
    def __init__(self, initial_frame, master, setup_main_screen):
        self.initial_frame = initial_frame
        self.master = master
        self.setup_main_screen = setup_main_screen
        # This frame is the frame for this page
        self.analytical_report_screen_frame = tk.Frame(self.master)
        self.setup_analytical_report_screen()

    def _analytical_report_function_element_builder(self,admin_frame):
        pady = 5

        # Admin function frame title
        admin_function_title = tk.Label(admin_frame, text="Analytical report Functions",bg="yellow",)
        admin_function_title.pack(fill="both", expand=False, padx=10, pady=pady)

        # Button : Users can delete a review
        delete_review_button = tk.Button(admin_frame, text="Get a game report", bg="yellow", command= lambda: drs.GameReportScreen(admin_frame, self.master, self.setup_analytical_report_screen))
        delete_review_button.pack(fill="both", expand=False, padx=10, pady=pady)

        # Button : Go back to main screen
        go_back_to_main_screen_button = tk.Button(admin_frame, text="Go back to main screen", fg="blue", command=self.go_back_to_main_screen)
        go_back_to_main_screen_button.pack(fill="both", expand=False, padx=10, pady=pady)
    
    def setup_analytical_report_screen(self):
        for widget in self.analytical_report_screen_frame.winfo_children():
            widget.destroy()

        self.initial_frame.pack_forget()

        self.analytical_report_screen_frame.pack(fill="both", expand=True)

        self._analytical_report_function_element_builder(self.analytical_report_screen_frame)

    def go_back_to_main_screen(self):
        self.analytical_report_screen_frame.pack_forget()
        self.setup_main_screen()
    
