import tkinter as tk
import tkinter.font as tkFont
import db_operation.insert_operation as io

class InsertStreamerDataScreen():
    def __init__(self, insert_main_screen_frame, master, setup_insert_screen):
        self.insert_main_screen_frame = insert_main_screen_frame
        self.master = master
        self.setup_insert_screen = setup_insert_screen
        # This frame is the frame for this page
        self.insert_streamer_info_screen_frame = tk.Frame(self.master)
        self.setup_insert_streamer_info_screen()
    
    def _insert_streamer_element_builder(self,insertStreamerFrame):
        pady = 5
        bgColor = "green"

        # Insert function frame title
        insert_streamer_title = tk.Label(insertStreamerFrame, text="Inserting Functions",)
        insert_streamer_title.pack(fill="both", expand=False, padx=10, pady=pady)

        # Description for textfield
        description_label = tk.Label(insertStreamerFrame, text="Enter Streamer Information, first box is uid, second box is username, and third box is number of subscribers", bg=bgColor)
        description_label.pack(fill="both", expand=False, padx=10, pady=pady)

        # Textfield for uid, username, and subscribers
        uid_textfield = tk.Entry(insertStreamerFrame, width=30)
        uid_textfield.pack(fill="both", expand=False, padx=10, pady=pady)

        username_textfield = tk.Entry(insertStreamerFrame, width=30)
        username_textfield.pack(fill="both", expand=False, padx=10, pady=pady)

        subscribers_textfield = tk.Entry(insertStreamerFrame, width=30)
        subscribers_textfield.pack(fill="both", expand=False, padx=10, pady=pady)

        # Creating a scrollbar
        scrollbar = tk.Scrollbar(insertStreamerFrame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Creating a listbox widget
        monospace_font = tkFont.Font(family="Courier", size=10)
        self.result_listbox = tk.Listbox(insertStreamerFrame, yscrollcommand=scrollbar.set, font=monospace_font)
        self.result_listbox.pack(fill="both", expand=True, padx=10, pady=pady)

        # Attaching the listbox to the scrollbar
        scrollbar.config(command=self.result_listbox.yview)
        # Insert button
        insert_streamer_info_button = tk.Button(insertStreamerFrame, text="Insert", bg=bgColor, command=lambda: self._insert_streamer(uid_textfield, username_textfield, subscribers_textfield))
        insert_streamer_info_button.pack(fill="both", expand=False, padx=10, pady=pady)


        # Button : Go back to insert screen
        go_back_to_insert_screen_button = tk.Button(insertStreamerFrame, text="Go back to insert screen", bg=bgColor, command=self.go_back_to_insert_screen)
        go_back_to_insert_screen_button.pack(fill="both", expand=False, padx=10, pady=pady)
    
    def format_result(self, row):
        formatted_row = []

        for index, item in enumerate(row):
            if index == 2:  # Assuming the third item should be formatted as a float
                if isinstance(item, float):
                    formatted_item = f"{item:<50.2f}"
                else:
                    formatted_item = f"{str(item):<50}"
            else:  # For other items (integers or strings)
                formatted_item = f"{str(item):<50}"

            formatted_row.append(formatted_item)

        return " ".join(formatted_row)

    def _insert_streamer(self, uid_textfield, username_textfield, subscribers_textfield):
        uid = uid_textfield.get()
        username = username_textfield.get()
        subscribers = subscribers_textfield.get()
        #insertStreamerInfo = io.InsertOperation().insertStreamerInfo(uid, username, subscribers)  # Assuming this inserts the streamer's information properly
        #io.InsertOperation().insertStreamerInfo(uid, username, subscribers)
        dataConfirmText = io.InsertOperation().insertStreamerInfo(uid, username, subscribers)
        if dataConfirmText == False:
            self.result_listbox.delete(0, tk.END)
            self.result_listbox.insert(tk.END, "Error, invalid input.")
        else:
            self.result_listbox.delete(0, tk.END)
            self.result_listbox.insert(tk.END, dataConfirmText)
        """
        if not result_items:
            self.result_listbox.delete(0, tk.END)
            self.result_listbox.insert(tk.END, "Error: No result found")
            return
        self.result_listbox.delete(0, tk.END)  # Clear the Listbox
        for row in result_items:
            formatted_row = self.format_result(row)
            self.result_listbox.insert(tk.END, formatted_row)
        """

    def setup_insert_streamer_info_screen(self):
        self.insert_main_screen_frame.pack_forget()

        self.insert_streamer_info_screen_frame.pack(fill="both", expand=True)

        self._insert_streamer_element_builder(self.insert_streamer_info_screen_frame)
    
    def go_back_to_insert_screen(self):
        self.insert_streamer_info_screen_frame.pack_forget()
        self.insert_main_screen_frame.pack_forget()
        self.setup_insert_screen()