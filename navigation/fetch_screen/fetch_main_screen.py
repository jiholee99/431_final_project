import tkinter as tk

import navigation.fetch_screen.fetch_game_info_by_title_screen as fgibt
import navigation.fetch_screen.fetch_top_selling_game_screen as ftsgs
import navigation.fetch_screen.fetch_game_within_budget_screen as fgwbs
import navigation.fetch_screen.fetch_top_reviewed_games_screen as ftrgs
import navigation.fetch_screen.fetch_popular_among_streamer_screen as fpas
import navigation.fetch_screen.fetch_most_reviewed_streamed_screen as fmrss

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
        fetch_function_title.pack(fill="both", expand=False, padx=10, pady=pady)  

        # Button: Users can fetch information about a video game’s publisher, released platforms, and date of release for a given game title
        game_by_title_button = tk.Button(fetch_frame, text="See video game information by title", bg="lightblue", command= lambda: fgibt.FetchGameInfoByTitleScreen(fetch_frame, self.master, self.setup_fetch_screen))
        game_by_title_button.pack(fill="both", expand=False, padx=10, pady=pady)  

        # Button : Users can fetch information about the top selling game
        top_selling_item_button = tk.Button(fetch_frame, text="See top selling games", bg="lightblue", command= lambda:  ftsgs.FetchTopSellingGameScreen(fetch_frame, self.master, self.setup_fetch_screen))
        top_selling_item_button.pack(fill="both", expand=False, padx=10, pady=pady)  

        # Button : Users can fetch information about the top reviewed game
        top_reviewed_game_button = tk.Button(fetch_frame, text="See top reviewed game", bg="lightblue", command= lambda: ftrgs.FetchTopReviewedGamesScreen(fetch_frame, self.master, self.setup_fetch_screen))
        top_reviewed_game_button.pack(fill="both", expand=False, padx=10, pady=pady)  

        # Button : Users can fetch games within their budget
        budget_game_button = tk.Button(fetch_frame, text="See games within your budget", bg="lightblue", command= lambda: fgwbs.FetchGameWithinBudget(fetch_frame, self.master, self.setup_fetch_screen))
        budget_game_button.pack(fill="both", expand=False, padx=10, pady=pady) 

        # Button : Users can fetch games that are popular among streamers by counting the number of streamers playing a certain game.
        popular_streamer_game_button = tk.Button(fetch_frame, text="See games that are popular among streamers", bg="lightblue", command= lambda: fpas.FetchPopularAmongStreamerScreen(fetch_frame, self.master, self.setup_fetch_screen))
        popular_streamer_game_button.pack(fill="both", expand=False, padx=10, pady=pady)  

        # Button : Users can get the most reviewed and streamed games per platform which includes game company
        most_reviewed_streamed_game_button = tk.Button(fetch_frame, text="See most reviewed and streamed games per platform", bg="lightblue", command= lambda: fmrss.FetchMostReviewedStreamedScreen(fetch_frame, self.master, self.setup_fetch_screen))
        most_reviewed_streamed_game_button.pack(fill="both", expand=False, padx=10, pady=pady)  

        # Button : Go back to main screen
        go_back_to_main_screen_button = tk.Button(fetch_frame, text="Go back to main screen", fg="blue", command=self.go_back_to_main_screen)
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


        