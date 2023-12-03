import tkinter as tk
import tkinter.messagebox as tkMessageBox
import db_operation.update_operation as uo
import type.error_return_type as err
import re

class UpdateGameSalesDataScreen():
    def __init__(self, update_main_screen_frame, master, setup_update_main_screen):
        self.update_main_screen_frame = update_main_screen_frame
        self.master = master
        self.setup_update_main_screen = setup_update_main_screen
        # This frame is the frame for this page
        self.update_game_sales_data_frame = tk.Frame(self.master)
        self.setup_update_game_sales_data()

    def _update_game_sales_data_element_builder(self, update_game_sales_data_frame ):
        pady = 5

        # Update function frame title
        update_game_sales_data_title = tk.Label(update_game_sales_data_frame, text="Update Game Sales Data",bg="yellow",)
        update_game_sales_data_title.pack(fill="both", expand=False, padx=10, pady=pady)

        # Listbox for game_id. This will be populated by the fetch_game_id_button
        # Users will select the game_id from this listbox

        # Button : Fetch game_id
        fetch_game_id_button = tk.Button(update_game_sales_data_frame, text="See the list of games for game_id", bg="yellow", command=lambda: self.fetch_game_ids())
        fetch_game_id_button.pack(fill="both", expand=False, padx=10, pady=pady)

        # Creating a scrollbar
        scrollbar_gameid = tk.Scrollbar(update_game_sales_data_frame)
        scrollbar_gameid.pack(side=tk.RIGHT, fill=tk.Y)

        # Creating a listbox widget
        monospace_font = tk.font.Font(family="Courier", size=10)
        self.gameid_result_listbox = tk.Listbox(update_game_sales_data_frame, yscrollcommand=scrollbar_gameid.set, font=monospace_font)
        self.gameid_result_listbox.pack(fill="both", expand=True, padx=10, pady=pady)

        # 2 Textfield game_id and number of copies sold

        # Warning label
        warning_label = tk.Label(update_game_sales_data_frame, text="Warning: Please make sure you have the correct game_id before proceeding", fg="red")
        warning_label.pack(fill="both", expand=False, padx=10, pady=pady)

        # Description for game_id textfield description
        game_id_textfield_description = tk.Label(update_game_sales_data_frame, text="Enter the game_id you want to change sales data",)
        game_id_textfield_description.pack(fill="both", expand=False, padx=10, pady=pady)
        # Textfield for game_id
        game_id_textfield = tk.Entry(update_game_sales_data_frame, width=30)
        game_id_textfield.pack(fill="both", expand=False, padx=10, pady=pady)


        # number of copies sold textfield description
        num_of_copies_sold_description = tk.Label(update_game_sales_data_frame, text="Enter the number of copies sold below",)
        num_of_copies_sold_description.pack(fill="both", expand=False, padx=10, pady=pady)
        # Textfield for number of copies sold
        number_of_copies_sold_textfield = tk.Entry(update_game_sales_data_frame, width=30)
        number_of_copies_sold_textfield.pack(fill="both", expand=False, padx=10, pady=pady)


        # Button : Update game sales data
        update_game_sales_data_button = tk.Button(update_game_sales_data_frame, text="Update game sales data", bg="yellow", command=lambda: self.update_game_sales_data(game_id_textfield, number_of_copies_sold_textfield))
        update_game_sales_data_button.pack(fill="both", expand=False, padx=10, pady=pady)

        # Description for result listbox
        result_listbox_label = tk.Label(update_game_sales_data_frame, text="If your request was successful, the table below will show an upadted value")
        result_listbox_label.pack(fill="both", expand=False, padx=10, pady=pady)

        # Creating a scrollbar
        scrollbar_number_of_copies_sold = tk.Scrollbar(update_game_sales_data_frame)
        scrollbar_number_of_copies_sold.pack(side=tk.RIGHT, fill=tk.Y)

        # Creating a listbox widget
        monospace_font = tk.font.Font(family="Courier", size=10)
        self.number_of_copies_sold_result_listbox = tk.Listbox(update_game_sales_data_frame, yscrollcommand=scrollbar_number_of_copies_sold.set, font=monospace_font)
        self.number_of_copies_sold_result_listbox.pack(fill="both", expand=True, padx=10, pady=pady)

        
        # Button : Go back to update screen
        go_back_to_update_screen_button = tk.Button(update_game_sales_data_frame, text="Go back to update screen", fg="blue", command=self.go_back_to_update_screen)
        go_back_to_update_screen_button.pack(fill="both", expand=False, padx=10, pady=pady)

    def format_game_id_result(self, row, is_header=False):
        formatted_row = []

        for index, item in enumerate(row):
            if isinstance(item, float):
                    formatted_item = f"{item:<50.2f}"
            else:
                formatted_item = f"{str(item):<50}"

            formatted_row.append(formatted_item)

        return " ".join(formatted_row)

    def fetch_game_ids(self):
        result = uo.UpdateOperation().fetch_game_by_gameid()

        for row in result:
            formatted_row = self.format_game_id_result(row)
            self.gameid_result_listbox.insert(tk.END, formatted_row)

    def is_decimal(self, string):
        pattern = r"^\d+(\.\d{1,2})?$"
        return bool(re.match(pattern, string))

    def update_game_sales_data(self, game_id_textfield, number_of_copies_sold_textfield):
        game_id = game_id_textfield.get()
        number_of_copies_sold = number_of_copies_sold_textfield.get()

        # Check if game_id field is correct
        if (game_id == "") or (game_id.isdigit() == False):
            tkMessageBox.showerror("Error", "Please enter a valid game_id")
            return
        elif (number_of_copies_sold == "") or (self.is_decimal(number_of_copies_sold) == False):
            tkMessageBox.showerror("Error", "Please enter a valid number of copies sold. Currently only supports up to 2 decimal places")
            return
        
        result = uo.UpdateOperation().update_game_sales_data(game_id, number_of_copies_sold)

        if (isinstance(result, err.ErrorReturnType)):
            tkMessageBox.showerror("Database Error", result.message)
            return
        
        # Clear the listbox
        self.number_of_copies_sold_result_listbox.delete(0, tk.END)
        
        for row in result:
            formatted_row = self.format_game_id_result(row)
            self.number_of_copies_sold_result_listbox.insert(tk.END, formatted_row)

    def setup_update_game_sales_data(self):
        self.update_main_screen_frame.pack_forget()

        self.update_game_sales_data_frame.pack(fill="both", expand=True)

        self._update_game_sales_data_element_builder(self.update_game_sales_data_frame)

    def go_back_to_update_screen(self):
        self.update_game_sales_data_frame.pack_forget()
        self.update_main_screen_frame.pack_forget()
        self.setup_update_main_screen()
    
