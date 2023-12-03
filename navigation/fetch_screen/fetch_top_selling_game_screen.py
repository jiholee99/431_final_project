import tkinter as tk
import tkinter.font as tkFont
import db_operation.fetch_operation as fo

class FetchTopSellingGameScreen():
    def __init__(self, fetch_main_screen_frame, master, setup_fetch_screen):
        self.fetch_main_screen_frame = fetch_main_screen_frame
        self.master = master
        self.setup_fetch_screen = setup_fetch_screen
        # This frame is the frame for this page
        self.fetch_top_selling_game_screen_frame = tk.Frame(self.master)
        self.setup_fetch_top_selling_game_screen()
    
    def _fetch_top_selling_game_element_builder(self,fetch_top_selling_game_frame):
        pady = 5

        # Fetch function frame title
        fetch_top_selling_game_title = tk.Label(fetch_top_selling_game_frame, text="Fetching Functions",bg="lightblue",)
        fetch_top_selling_game_title.pack(fill="both", expand=False, padx=10, pady=pady)

        # Label in case user enters empty string
        empty_string_label = tk.Label(fetch_top_selling_game_frame, text="Empty string will return 100 games by default", bg="lightblue")
        empty_string_label.pack(fill="both", expand=False, padx=10, pady=pady)

        # Description for textfield
        description_label = tk.Label(fetch_top_selling_game_frame, text="Enter the amount of games you want to fetch below", bg="lightblue")
        description_label.pack(fill="both", expand=False, padx=10, pady=pady)

        # Textfield for amount of games to fetch
        amount_of_games_textfield = tk.Entry(fetch_top_selling_game_frame, width=30)
        amount_of_games_textfield.pack(fill="both", expand=False, padx=10, pady=pady)

        # Creating a scrollbar
        scrollbar = tk.Scrollbar(fetch_top_selling_game_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Creating a listbox widget
        monospace_font = tkFont.Font(family="Courier", size=10)
        self.result_listbox = tk.Listbox(fetch_top_selling_game_frame, yscrollcommand=scrollbar.set, font=monospace_font)
        self.result_listbox.pack(fill="both", expand=True, padx=10, pady=pady)

        # Attaching the listbox to the scrollbar
        scrollbar.config(command=self.result_listbox.yview)

        # Fetch button
        fetch_top_selling_game_button = tk.Button(fetch_top_selling_game_frame, text="Fetch", bg="lightblue", command=lambda: self._fetch_top_selling_game(amount_of_games_textfield))
        fetch_top_selling_game_button.pack(fill="both", expand=False, padx=10, pady=pady)
        
        # Button : Go back to fetch screen
        go_back_to_fetch_screen_button = tk.Button(fetch_top_selling_game_frame, text="Go back to fetch screen", bg="lightblue", command=self.go_back_to_fetch_screen)
        go_back_to_fetch_screen_button.pack(fill="both", expand=False, padx=10, pady=pady)

    def format_result(self, row):
        formatted_row = []

        for index, item in enumerate(row):
            if isinstance(item, float):
                formatted_item = f"{item:<50.2f}"
            else:
                formatted_item = f"{str(item):<50}"

            formatted_row.append(formatted_item)

        return " ".join(formatted_row)
    
    def _fetch_top_selling_game(self, amount_of_games_textfield):
        amount_of_games = amount_of_games_textfield.get()
        fo_instance = fo.FetchOperation()
        myresult = fo_instance.fetch_top_selling_game(amount_of_games)
        if (myresult == False):
            self.result_listbox.delete(0, tk.END)
            self.result_listbox.insert(tk.END, "Please enter a valid number")
            return
        self.result_listbox.delete(0, tk.END)
        for row in myresult:
            self.result_listbox.insert(tk.END, self.format_result(row))
    
    def setup_fetch_top_selling_game_screen(self):
        # Clear existing content
        for widget in self.fetch_top_selling_game_screen_frame.winfo_children():
            widget.destroy()
        self.fetch_main_screen_frame.pack_forget()

        self.fetch_top_selling_game_screen_frame.pack(fill="both", expand=True)

        self._fetch_top_selling_game_element_builder(self.fetch_top_selling_game_screen_frame)

    def go_back_to_fetch_screen(self):
        self.fetch_top_selling_game_screen_frame.pack_forget()
        self.setup_fetch_screen()
    