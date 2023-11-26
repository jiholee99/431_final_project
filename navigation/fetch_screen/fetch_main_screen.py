import tkinter as tk

import navigation.fetch_screen.fetch_game_info_by_title_screen as fgibt

class FetchMainScreen():
    def __init__(self, initial_frame, master, setup_main_screen):
        self.initial_frame = initial_frame
        self.master = master
        self.setup_main_screen = setup_main_screen
        # This frame is the frame for this page
        self.fetch_screen_frame = tk.Frame(self.master)
        self.setup_fetch_screen()

    def _fetch_function_element_builder(self,fetch_frame):
        pady = 5

        # Fetch function frame title
        fetch_function_title = tk.Label(fetch_frame, text="Fetching Functions",bg="lightblue",)
        fetch_function_title.pack(fill="both", expand=False, padx=10, pady=pady)  # Make it expand horizontally

        # Button: Users can fetch information about a video game’s publisher, released platforms, and date of release for a given game title
        game_by_title_button = tk.Button(fetch_frame, text="See video game information by title", bg="lightblue", command= lambda: fgibt.FetchGameInfoByTitleScreen(fetch_frame, self.master, self.setup_fetch_screen))
        game_by_title_button.pack(fill="both", expand=False, padx=10, pady=pady)  # Make it expand horizontally

        # Button : Users can fetch information about the top selling game
        top_selling_item_button = tk.Button(fetch_frame, text="See top selling games", bg="lightblue",)
        top_selling_item_button.pack(fill="both", expand=False, padx=10, pady=pady)  # Make it expand horizontally

        # Button : Users can fetch information about the top reviewed game
        top_reviewed_game_button = tk.Button(fetch_frame, text="See top reviewed game", bg="lightblue",)
        top_reviewed_game_button.pack(fill="both", expand=False, padx=10, pady=pady)  # Make it expand horizontally

        # Button : Users can fetch games within their budget
        budget_game_button = tk.Button(fetch_frame, text="See games within your budget", bg="lightblue",)
        budget_game_button.pack(fill="both", expand=False, padx=10, pady=pady)  # Make it expand horizontally

        # Button : Users can fetch games that are popular among streamers by counting the number of streamers playing a certain game.
        popular_streamer_game_button = tk.Button(fetch_frame, text="See games that are popular among streamers", bg="lightblue",)
        popular_streamer_game_button.pack(fill="both", expand=False, padx=10, pady=pady)  # Make it expand horizontally

        # Button : Users can get the most reviewed and streamed games per platform which includes game company
        most_reviewed_streamed_game_button = tk.Button(fetch_frame, text="See most reviewed and streamed games per platform", bg="lightblue",)
        most_reviewed_streamed_game_button.pack(fill="both", expand=False, padx=10, pady=pady)  # Make it expand horizontally

        # Button : Go back to main screen
        go_back_to_main_screen_button = tk.Button(fetch_frame, text="Go back to main screen", bg="lightblue", command=self.go_back_to_main_screen)
        go_back_to_main_screen_button.pack(fill="both", expand=False, padx=10, pady=pady)

    def setup_fetch_screen(self):
        # Clear existing content
        for widget in self.fetch_screen_frame.winfo_children():
            widget.destroy()
        self.initial_frame.pack_forget()

        self.fetch_screen_frame.pack(fill="both", expand=True)

        self._fetch_function_element_builder(self.fetch_screen_frame)

    
    def go_back_to_main_screen(self):
        self.fetch_screen_frame.pack_forget()
        self.setup_main_screen()


        