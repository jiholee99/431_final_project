import tkinter as tk
import db_operation.fetch_operation as fo
import type.error_return_type as error_return_type


class FetchPopularAmongStreamerScreen():
    def __init__(self, fetch_main_screen_frame, master, setup_fetch_screen):
        self.fetch_main_screen_frame = fetch_main_screen_frame
        self.master = master
        self.setup_fetch_screen = setup_fetch_screen
        # This frame is the frame for this page
        self.popular_among_streamer_frame = tk.Frame(self.master)
        self.setup_popular_among_streamer_screen()

    def _fetch_popular_among_streamer_element_builder(self, fetch_popular_among_streamer_frame):
        # Fetch function frame title
        fetch_popular_among_streamer_title = tk.Label(fetch_popular_among_streamer_frame, text="Fetches game that are popular among streamers",bg="lightblue",)
        fetch_popular_among_streamer_title.pack(fill="both", expand=False, padx=10, pady=10)

        #  Empty string warning
        empty_string_label = tk.Label(fetch_popular_among_streamer_frame, text="Empty string will return 100 games by default", fg="red")
        empty_string_label.pack(fill="both", expand=False, padx=10, pady=10)

        # Amount of games to fetch
        amount_of_games_label = tk.Label(fetch_popular_among_streamer_frame, text="Amount of games to fetch: ")
        amount_of_games_label.pack(fill="both", expand=False, padx=10, pady=10)

        
        # Textfield for amount of games to fetch
        amount_of_games_textfield = tk.Entry(fetch_popular_among_streamer_frame)
        amount_of_games_textfield.pack(fill="both", expand=False, padx=10, pady=10)

        # Result listbox
        result_listbox_label = tk.Label(fetch_popular_among_streamer_frame, text="Result: ")
        result_listbox_label.pack(fill="both", expand=False, padx=10, pady=10)

        monospace_font = tk.font.Font(family="Courier", size=10)
        self.result_listbox = tk.Listbox(fetch_popular_among_streamer_frame, font=monospace_font)
        self.result_listbox.pack(fill="both", expand=True, padx=10, pady=10)

        # Attaching the listbox to the scrollbar
        scrollbar = tk.Scrollbar(self.result_listbox)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.result_listbox.config(yscrollcommand=scrollbar.set)

        # Fetch button
        fetch_popular_among_streamer_button = tk.Button(fetch_popular_among_streamer_frame, text="Fetch", bg="lightblue", command=lambda: self._fetch_popular_among_streamer(amount_of_games_textfield))
        fetch_popular_among_streamer_button.pack(fill="both", expand=False, padx=10, pady=10)

        # Button : Go back to fetch screen
        go_back_to_fetch_screen_button = tk.Button(fetch_popular_among_streamer_frame, text="Go back to fetch screen", bg="lightblue", command=self.go_back_to_fetch_screen)
        go_back_to_fetch_screen_button.pack(fill="both", expand=False, padx=10, pady=10)

    def format_result(self, row, is_header=False):
        formatted_row = []
        for index, item in enumerate(row):
            if index == 0 or is_header:
                formatted_item = f"{str(item):<50}"
            else :
                formatted_item = f"{item:<50}"
            formatted_row.append(formatted_item)
        return " ".join(formatted_row)

    def _fetch_popular_among_streamer(self, amount_of_games_textfield):
        # Clear result listbox
        self.result_listbox.delete(0, tk.END)

        # Fetch amount of games
        amount_of_games = amount_of_games_textfield.get()

        # Fetch result from database
        result = fo.FetchOperation().fetch_popular_among_streamer(amount_of_games)

        if (isinstance(result, error_return_type.ErrorReturnType)):
            self.result_listbox.insert(tk.END, result.get_error_message())
            return

        # Display result in listbox
        for index, row in enumerate(result):
            if (index == 0):
                formatted_row = self.format_result(row, True)
            else :
                formatted_row = self.format_result(row)
            self.result_listbox.insert(tk.END, formatted_row)
    
    def setup_popular_among_streamer_screen(self):
        for widget in self.popular_among_streamer_frame.winfo_children():
            widget.destroy()
        self.fetch_main_screen_frame.pack_forget()
        self.popular_among_streamer_frame.pack(fill="both", expand=True)
        self._fetch_popular_among_streamer_element_builder(self.popular_among_streamer_frame)


    def go_back_to_fetch_screen(self):
        self.popular_among_streamer_frame.forget()
        self.setup_fetch_screen()