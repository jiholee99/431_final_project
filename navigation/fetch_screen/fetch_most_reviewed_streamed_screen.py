import tkinter as tk
import tkinter.font as tkFont
import db_operation.fetch_operation as fo
import type.error_return_type as error_return_type


class FetchMostReviewedStreamedScreen():
    def __init__(self, fetch_main_screen_frame, master, setup_fetch_screen):
        self.fetch_main_screen_frame = fetch_main_screen_frame
        self.master = master
        self.setup_fetch_screen = setup_fetch_screen
        self.fetch_most_reviewed_streamed_screen_frame = tk.Frame(self.master)
        self.setup_fetch_most_reviewed_streamed_screen()

    def _fetch_most_reviewed_streamed_element_builder(self, frame):
        pady = 5

        # Fetch most reviewed streamed function information
        information_label = tk.Label(frame, text="This function fetches the most reviewed and streamed games on each platform.\nFor each platform it first orders by number of reviews\nand then when it has a tie, it will use number of streamers to give proper ranking.", bg="lightblue")
        information_label.pack(fill="both", expand=False, padx=10, pady=pady)

        # Label result
        result_label = tk.Label(frame, text="Result: ", bg="lightblue")
        result_label.pack(fill="both", expand=False, padx=10, pady=pady)

        # Creating a scrollbar
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Creating a listbox widget
        monospace_font = tkFont.Font(family="Courier", size=10)
        self.result_listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, font=monospace_font)
        self.result_listbox.pack(fill="both", expand=True, padx=10, pady=pady)

        # Attaching the listbox to the scrollbar
        scrollbar.config(command=self.result_listbox.yview)

        # Fetch button
        fetch_button = tk.Button(frame, text="Fetch", bg="lightblue", command=self._fetch_most_reviewed_streamed)
        fetch_button.pack(fill="both", expand=False, padx=10, pady=pady)

        # Button : Go back to fetch screen
        go_back_button = tk.Button(frame, text="Go back to fetch screen", bg="lightblue", command=self.go_back_to_fetch_screen)
        go_back_button.pack(fill="both", expand=False, padx=10, pady=pady)

    def _fetch_most_reviewed_streamed(self):
        result = fo.FetchOperation().fetch_most_reviewed_streamed()  # Assuming this returns a list of items

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

    def setup_fetch_most_reviewed_streamed_screen(self):
        self.fetch_main_screen_frame.pack_forget()
        self.fetch_most_reviewed_streamed_screen_frame.pack(fill="both", expand=True)
        self._fetch_most_reviewed_streamed_element_builder(self.fetch_most_reviewed_streamed_screen_frame)

    def go_back_to_fetch_screen(self):
        self.fetch_most_reviewed_streamed_screen_frame.pack_forget()
        self.fetch_main_screen_frame.pack_forget()
        self.setup_fetch_screen()

    def format_result(self, row, is_header=False):
        formatted_row = []
        for index, item in enumerate(row):
            if is_header :
                if index == 0 or index == 1:
                    formatted_item = f"{str(item):<70}"
                elif index == 2 or index == 3:
                    formatted_item = f"{str(item):<20}"
                elif index == 4:
                    formatted_item = f"{str(item):<30}"
            elif index == 0 or index == 1:
                formatted_item = f"{item:<70}"
            elif index == 2 or index == 3:
                formatted_item = f"{item:<20}"
            elif index == 4:
                formatted_item = f"{item:<30}"
            formatted_row.append(formatted_item)
        return " ".join(formatted_row)
