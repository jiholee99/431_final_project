import tkinter as tk
import tkinter.font as tkFont
import db_operation.fetch_operation as fo
import type.error_return_type as ert

class FetchGameWithinBudget():
    def __init__(self, fetch_main_screen_frame, master, setup_fetch_screen):
        self.fetch_main_screen_frame = fetch_main_screen_frame
        self.master = master
        self.setup_fetch_screen = setup_fetch_screen
        # This frame is the frame for this page
        self.fetch_game_within_budget_screen_frame = tk.Frame(self.master)
        self.setup_fetch_game_within_budget_screen()
    
    def _fetch_game_within_budget_element_builder(self,fetch_game_within_budget_frame):
        pady = 5

        # Fetch function frame title
        fetch_game_within_budget_title = tk.Label(fetch_game_within_budget_frame, text="Fetching Functions",bg="lightblue",)
        fetch_game_within_budget_title.pack(fill="both", expand=False, padx=10, pady=pady)

        # Description for textfield
        description_label = tk.Label(fetch_game_within_budget_frame, text="Enter your budget below", bg="lightblue")
        description_label.pack(fill="both", expand=False, padx=10, pady=pady)

        # Textfield for budget
        budget_textfield = tk.Entry(fetch_game_within_budget_frame, width=30)
        budget_textfield.pack(fill="both", expand=False, padx=10, pady=pady)

        # Creating a scrollbar
        scrollbar = tk.Scrollbar(fetch_game_within_budget_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Creating a listbox widget
        monospace_font = tkFont.Font(family="Courier", size=10)
        self.result_listbox = tk.Listbox(fetch_game_within_budget_frame, yscrollcommand=scrollbar.set, font=monospace_font)
        self.result_listbox.pack(fill="both", expand=True, padx=10, pady=pady)

        # Attaching the listbox to the scrollbar
        scrollbar.config(command=self.result_listbox.yview)
        # Fetch button
        fetch_game_within_budget_button = tk.Button(fetch_game_within_budget_frame, text="Fetch", bg="lightblue", command=lambda: self._fetch_game_within_budget(budget_textfield))
        fetch_game_within_budget_button.pack(fill="both", expand=False, padx=10, pady=pady)


        # Button : Go back to fetch screen
        go_back_to_fetch_screen_button = tk.Button(fetch_game_within_budget_frame, text="Go back to fetch screen", bg="lightblue", command=self.go_back_to_fetch_screen)
        go_back_to_fetch_screen_button.pack(fill="both", expand=False, padx=10, pady=pady)

    def format_result(self, row, is_header=False):
        formatted_row = []
        print(f"Row : {row}")
        for index, item in enumerate(row):
            if index == 0 or is_header:
                formatted_item = f"{str(item):<50}"
            else:
                formatted_item = f"{item:<50.2f}"
            formatted_row.append(formatted_item)
        return " ".join(formatted_row)
    
    def _fetch_game_within_budget(self, budget_textfield):
        # Clear result listbox
        self.result_listbox.delete(0, tk.END)

        # Get user input
        budget = budget_textfield.get()
        print(f"budget entered is {budget}")

        # Fetch data
        result = fo.FetchOperation().fetch_game_within_budget(budget)
        print(f"is result error : {isinstance(result, ert.ErrorReturnType)}")
        if (isinstance(result, ert.ErrorReturnType)):
            self.result_listbox.insert(tk.END, result.get_error_message())
            return

        # Display result
        for index, row in enumerate(result):
            if (index == 0):
                formatted_row = self.format_result(row, True)
            else :
                formatted_row = self.format_result(row)
            self.result_listbox.insert(tk.END, formatted_row)
    
    def setup_fetch_game_within_budget_screen(self):
        # Clear existing content
        for widget in self.fetch_game_within_budget_screen_frame.winfo_children():
            widget.destroy()
        self.fetch_main_screen_frame.pack_forget()

        self.fetch_game_within_budget_screen_frame.pack(fill="both", expand=True)

        self._fetch_game_within_budget_element_builder(self.fetch_game_within_budget_screen_frame)

    def go_back_to_fetch_screen(self):
        self.fetch_game_within_budget_screen_frame.pack_forget()
        self.setup_fetch_screen()

