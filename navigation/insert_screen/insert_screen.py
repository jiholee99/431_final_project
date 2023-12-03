import tkinter as tk

import navigation.insert_screen.insert_streamer_data as isd
import navigation.insert_screen.insert_streamer_platform as isp

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
        insert_function_title = tk.Label(insert_frame, text="Inserting Functions",)
        insert_function_title.pack(fill="both", expand=False, padx=10, pady=pady)

        # Button: Users can add information about a Streamer
        streamer_info_button = tk.Button(insert_frame, text="Enter information about a streamer", bg="green", command= lambda: isd.InsertStreamerDataScreen(insert_frame, self.master, self.setup_insert_screen))
        streamer_info_button.pack(fill="both", expand=False, padx=10, pady=pady)  # Make it expand horizontally

        # Button: Users can add information about what platforms a Streamer streams
        #platform_button = tk.Button(insert_frame, text="Enter information about a platform that a streamer streams", bg="green", command= lambda: isp.InsertStreamerPlatformScreen(insert_frame, self.master, self.setup_insert_screen))
        #platform_button.pack(fill="both", expand=False, padx=10, pady=pady)  # Make it expand horizontally

        # Button : Go back to main screen
        go_back_to_main_screen_button = tk.Button(insert_frame, text="Go back to main screen", fg="blue", command=self.go_back_to_main_screen)
        go_back_to_main_screen_button.pack(fill="both", expand=False, padx=10, pady=pady)

    def setup_insert_screen(self):        
        # Clear existing content
        for widget in self.insert_screen_frame.winfo_children():
            widget.destroy()        
        self.initial_frame.pack_forget()

        self.insert_screen_frame.pack(fill="both", expand=True)

        self._insert_function_element_builder(self.insert_screen_frame)

    def go_back_to_main_screen(self):
        self.insert_screen_frame.pack_forget()
        self.setup_main_screen()