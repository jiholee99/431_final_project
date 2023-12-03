import tkinter as tk
import tkinter.font as tkFont
import db_operation.fetch_operation as fo

class FetchGameInfoByTitleScreen():
    def __init__(self, fetch_main_screen_frame, master, setup_fetch_screen):
        self.fetch_main_screen_frame = fetch_main_screen_frame
        self.master = master
        self.setup_fetch_screen = setup_fetch_screen
        # This frame is the frame for this page
        self.fetch_game_info_by_title_screen_frame = tk.Frame(self.master)
        self.setup_fetch_game_info_by_title_screen()
    
    def _fetch_game_info_by_title_element_builder(self,fetch_game_info_by_title_frame):
        pady = 5

        # Fetch function frame title
        fetch_game_info_by_title_title = tk.Label(fetch_game_info_by_title_frame, text="Fetching Functions",bg="lightblue",)
        fetch_game_info_by_title_title.pack(fill="both", expand=False, padx=10, pady=pady)

        # Description for textfield
        description_label = tk.Label(fetch_game_info_by_title_frame, text="Enter the game title below", bg="lightblue")
        description_label.pack(fill="both", expand=False, padx=10, pady=pady)

        # Textfield for game title
        game_title_textfield = tk.Entry(fetch_game_info_by_title_frame, width=30)
        game_title_textfield.pack(fill="both", expand=False, padx=10, pady=pady)

        # Creating a scrollbar
        scrollbar = tk.Scrollbar(fetch_game_info_by_title_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Creating a listbox widget
        monospace_font = tkFont.Font(family="Courier", size=10)
        self.result_listbox = tk.Listbox(fetch_game_info_by_title_frame, yscrollcommand=scrollbar.set, font=monospace_font)
        self.result_listbox.pack(fill="both", expand=True, padx=10, pady=pady)

        # Attaching the listbox to the scrollbar
        scrollbar.config(command=self.result_listbox.yview)
        # Fetch button
        fetch_game_info_by_title_button = tk.Button(fetch_game_info_by_title_frame, text="Fetch", bg="lightblue", command=lambda: self._fetch_game_info_by_title(game_title_textfield))
        fetch_game_info_by_title_button.pack(fill="both", expand=False, padx=10, pady=pady)


        # Button : Go back to fetch screen
        go_back_to_fetch_screen_button = tk.Button(fetch_game_info_by_title_frame, text="Go back to fetch screen", bg="lightblue", command=self.go_back_to_fetch_screen)
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

    def _fetch_game_info_by_title(self, game_title_textfield):
        game_title = game_title_textfield.get()
        result_items = fo.FetchOperation().fetch_game_info_by_title(game_title)  # Assuming this returns a list of items
        if not result_items:
            self.result_listbox.delete(0, tk.END)
            self.result_listbox.insert(tk.END, "Error: No result found")
            return
        self.result_listbox.delete(0, tk.END)  # Clear the Listbox
        for row in result_items:
            formatted_row = self.format_result(row)
            self.result_listbox.insert(tk.END, formatted_row)


    def setup_fetch_game_info_by_title_screen(self):
        self.fetch_main_screen_frame.pack_forget()

        self.fetch_game_info_by_title_screen_frame.pack(fill="both", expand=True)

        self._fetch_game_info_by_title_element_builder(self.fetch_game_info_by_title_screen_frame)
    
    def go_back_to_fetch_screen(self):
        self.fetch_game_info_by_title_screen_frame.pack_forget()
        self.fetch_main_screen_frame.pack_forget()
        self.setup_fetch_screen()