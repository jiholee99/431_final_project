import tkinter
import db_operation.fetch_operation as fo
import type.error_return_type as error_return_type

class FetchTopReviewedGamesScreen():
    def __init__(self, fetch_main_screen_frame, master, setup_fetch_screen):
        self.fetch_main_screen_frame = fetch_main_screen_frame
        self.master = master
        self.setup_fetch_screen = setup_fetch_screen
        # This frame is the frame for this page
        self.fetch_top_reviewed_games_screen_frame = tkinter.Frame(self.master)
        self.setup_fetch_top_reviewed_games_screen()
    
    def _fetch_top_reviewed_games_element_builder(self,fetch_top_reviewed_games_frame):
        pady = 5

        # Fetch function frame title
        fetch_top_reviewed_games_title = tkinter.Label(fetch_top_reviewed_games_frame, text="Fetching Functions",bg="lightblue",)
        fetch_top_reviewed_games_title.pack(fill="both", expand=False, padx=10, pady=pady)

        # Description for textfield
        description_label = tkinter.Label(fetch_top_reviewed_games_frame, text="Enter the amount of games you want to fetch below", bg="lightblue")
        description_label.pack(fill="both", expand=False, padx=10, pady=pady)

        # Textfield for amount of games to fetch
        amount_of_games_textfield = tkinter.Entry(fetch_top_reviewed_games_frame, width=30)
        amount_of_games_textfield.pack(fill="both", expand=False, padx=10, pady=pady)

        # Creating a scrollbar
        scrollbar = tkinter.Scrollbar(fetch_top_reviewed_games_frame)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # Creating a listbox widget
        monospace_font = tkinter.font.Font(family="Courier", size=10)
        self.result_listbox = tkinter.Listbox(fetch_top_reviewed_games_frame, yscrollcommand=scrollbar.set, font=monospace_font)
        self.result_listbox.pack(fill="both", expand=True, padx=10, pady=pady)

        # Attaching the listbox to the scrollbar
        scrollbar.config(command=self.result_listbox.yview)
        # Fetch button
        fetch_top_reviewed_games_button = tkinter.Button(fetch_top_reviewed_games_frame, text="Fetch", bg="lightblue", command=lambda: self._fetch_top_reviewed_games(amount_of_games_textfield))
        fetch_top_reviewed_games_button.pack(fill="both", expand=False, padx=10, pady=pady)
        

        # Button : Go back to fetch screen
        go_back_to_fetch_screen_button = tkinter.Button(fetch_top_reviewed_games_frame, text="Go back to fetch screen", bg="lightblue", command=self.go_back_to_fetch_screen)
        go_back_to_fetch_screen_button.pack(fill="both", expand=False, padx=10, pady=pady)

    def format_result(self, row, is_header=False):
        formatted_row = []
        for index, item in enumerate(row):
            if index == 0 or is_header:
                formatted_item = f"{str(item):<50}"
            elif index == 1 or index == 2:
                formatted_item = f"{item:<50.2f}"
            else :
                formatted_item = f"{item:<50}"
            formatted_row.append(formatted_item)
        return " ".join(formatted_row)
    
    def _fetch_top_reviewed_games(self, amount_of_games_textfield):
        # Clear result listbox
        self.result_listbox.delete(0, tkinter.END)
        # Get amount of games to fetch
        amount_of_games = amount_of_games_textfield.get()
        # Get result
        result = fo.FetchOperation().fetch_top_reviewed_games(amount_of_games)

        
        if (isinstance(result, error_return_type.ErrorReturnType)):
            self.result_listbox.insert(tkinter.END, result.get_error_message())
            return

        # Format result
        for index, row in enumerate(result):
            if (index == 0):
                formatted_row = self.format_result(row, True)
            else :
                formatted_row = self.format_result(row)
            self.result_listbox.insert(tkinter.END, formatted_row)

    def setup_fetch_top_reviewed_games_screen(self):
        # Clear existing content
        for widget in self.fetch_top_reviewed_games_screen_frame.winfo_children():
            widget.destroy()
        self.fetch_main_screen_frame.pack_forget()

        self.fetch_top_reviewed_games_screen_frame.pack(fill="both", expand=True)

        self._fetch_top_reviewed_games_element_builder(self.fetch_top_reviewed_games_screen_frame)
    
    def go_back_to_fetch_screen(self):
        self.fetch_top_reviewed_games_screen_frame.pack_forget()
        self.setup_fetch_screen()

