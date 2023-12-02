import tkinter as tk


class FetchPopularAmongStreamerScreen():
    def __init__(self, fetch_main_screen_frame, master, setup_fetch_screen):
        self.fetch_main_screen_frame = fetch_main_screen_frame
        self.master = master
        self.setup_fetch_screen = setup_fetch_screen
        # This frame is the frame for this page
        self.popular_among_streamer_frame = tk.Frame(self.master)
        self.setup_popular_among_streamer_screen()

    def _fetch_popular_among_streamer_element_builder(self, fetch_popular_among_streamer_frame):
        # Amount of games to fetch
        amount_of_games_label = tk.Label(fetch_popular_among_streamer_frame, text="Amount of games to fetch: ")
        amount_of_games_label.pack(fill="both", expand=False, padx=10, pady=10)

        amount_of_games_textfield = tk.Entry(fetch_popular_among_streamer_frame)
        amount_of_games_textfield.pack(fill="both", expand=False, padx=10, pady=10)

        # Result listbox
        result_listbox_label = tk.Label(fetch_popular_among_streamer_frame, text="Result: ")
        result_listbox_label.pack(fill="both", expand=False, padx=10, pady=10)

        result_listbox = tk.Listbox(fetch_popular_among_streamer_frame)
        result_listbox.pack(fill="both", expand=True, padx=10, pady=10)

        # Attaching the listbox to the scrollbar
        scrollbar = tk.Scrollbar(result_listbox)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        result_listbox.config(yscrollcommand=scrollbar.set)

        # Fetch button
        fetch_popular_among_streamer_button = tk.Button(fetch_popular_among_streamer_frame, text="Fetch", bg="lightblue", command=lambda: self._fetch_popular_among_streamer(amount_of_games_textfield, result_listbox))
        fetch_popular_among_streamer_button.pack(fill="both", expand=False, padx=10, pady=10)

        # Button : Go back to fetch screen
        go_back_to_fetch_screen_button = tk.Button(fetch_popular_among_streamer_frame, text="Go back to fetch screen", bg="lightblue", command=self.go_back_to_fetch_screen)
        go_back_to_fetch_screen_button.pack(fill="both", expand=False, padx=10, pady=10)

    def _fetch_popular_among_streamer(self, amount_of_games_textfield, result_listbox):
        # Clear result listbox
        result_listbox.delete(0, tk.END)

        # Fetch amount of games
        amount_of_games = amount_of_games_textfield.get()

        # Fetch result from database
        result = self.fetch_popular_among_streamer_screen.fetch_popular_among_streamer(amount_of_games)

        # Display result in listbox
        for row in result:
            result_listbox.insert(tk.END, self.fetch_popular_among_streamer_screen.format_result(row))
    
    def setup_popular_among_streamer_screen(self):
        for widget in self.popular_among_streamer_frame.winfo_children():
            widget.destroy()
        self.fetch_main_screen_frame.pack_forget()
        self.popular_among_streamer_frame.pack(fill="both", expand=True)
        self._fetch_popular_among_streamer_element_builder(self.popular_among_streamer_frame)


    def go_back_to_fetch_screen(self):
        self.popular_among_streamer_frame.forget()
        self.setup_fetch_screen()