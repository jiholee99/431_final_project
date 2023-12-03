import tkinter as tk
import tkinter.messagebox as tkMessageBox
import db_operation.update_operation as uo
import type.error_return_type as err

class UpdateGameCompanyInfo():
    def __init__(self, update_main_screen_frame, master, setup_update_main_screen):
        self.update_main_screen_frame = update_main_screen_frame
        self.master = master
        self.setup_update_main_screen = setup_update_main_screen
        # This frame is the frame for this page
        self.update_game_company_info_frame = tk.Frame(self.master)
        self.setup_update_game_company_info()

    def _update_game_company_info_element_builder(self, update_game_company_info_frame ):
        pady = 5

        # Update function frame title
        update_game_company_info_title = tk.Label(update_game_company_info_frame, text="Update Game Company Info")
        update_game_company_info_title.pack(fill="both", expand=False, padx=10, pady=pady)

        # Listbox for game_id. This will be populated by the fetch_game_id_button
        # Users will select the game_id from this listbox

        # Button : Fetch game_id
        fetch_game_company_button = tk.Button(update_game_company_info_frame, text="See the list of all game companies", command=lambda: self.fetch_game_companies())
        fetch_game_company_button.pack(fill="both", expand=False, padx=10, pady=pady)

        # Creating a scrollbar
        fetch_game_company_scrollbar = tk.Scrollbar(update_game_company_info_frame)
        fetch_game_company_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Creating a listbox widget
        monospace_font = tk.font.Font(family="Courier", size=10)
        self.fetch_game_company_listbox = tk.Listbox(update_game_company_info_frame, yscrollcommand=fetch_game_company_scrollbar.set, font=monospace_font)
        self.fetch_game_company_listbox.pack(fill="both", expand=True, padx=10, pady=pady)


        # Warning label
        warning_label = tk.Label(update_game_company_info_frame, text="Warning: Please make sure you have the correct game_id before proceeding", fg="red")
        warning_label.pack(fill="both", expand=False, padx=10, pady=pady)

        # 3 Textfield needed : company_name, num_employees, foundation_year
        
        # Description for company_name textfield description
        company_name_textfield_description = tk.Label(update_game_company_info_frame, text="Enter the new company name you want to change",)
        company_name_textfield_description.pack(fill="both", expand=False, padx=10, pady=pady)
        # Textfield for company_name
        company_name_textfield = tk.Entry(update_game_company_info_frame, width=30)
        company_name_textfield.pack(fill="both", expand=False, padx=10, pady=pady)

        # Description for num_employees textfield description
        num_employees_textfield_description = tk.Label(update_game_company_info_frame, text="Enter the new number of employees you want to add",)
        num_employees_textfield_description.pack(fill="both", expand=False, padx=10, pady=pady)
        # Textfield for num_employees
        num_employees_textfield = tk.Entry(update_game_company_info_frame, width=30)
        num_employees_textfield.pack(fill="both", expand=False, padx=10, pady=pady)

        # Description for foundation_year textfield description
        foundation_year_textfield_description = tk.Label(update_game_company_info_frame, text="Enter the new year of foundation you want to add",)
        foundation_year_textfield_description.pack(fill="both", expand=False, padx=10, pady=pady)
        # Textfield for foundation_year
        foundation_year_textfield = tk.Entry(update_game_company_info_frame, width=30)
        foundation_year_textfield.pack(fill="both", expand=False, padx=10, pady=pady)

        # Button : Update game company info
        update_game_company_info_button = tk.Button(update_game_company_info_frame, text="Update game company info", command=lambda: self.update_game_company_info(company_name_textfield, num_employees_textfield, foundation_year_textfield))
        update_game_company_info_button.pack(fill="both", expand=False, padx=10, pady=pady)

        # Creating a scrollbar
        update_game_company_info_scrollbar = tk.Scrollbar(update_game_company_info_frame)
        update_game_company_info_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Creating a listbox widget
        monospace_font = tk.font.Font(family="Courier", size=10)
        self.update_game_company_info_listbox = tk.Listbox(update_game_company_info_frame, yscrollcommand=update_game_company_info_scrollbar.set, font=monospace_font)
        self.update_game_company_info_listbox.pack(fill="both", expand=True, padx=10, pady=pady)
        
        
        # BUtton : Go back to update main screen
        go_back_to_update_main_screen_button = tk.Button(update_game_company_info_frame, text="Go back to update main screen", command=self.go_back_to_update_main_screen, fg="blue")
        go_back_to_update_main_screen_button.pack(fill="both", expand=False, padx=10, pady=pady)

    def setup_update_game_company_info(self):
        self.update_main_screen_frame.pack_forget()

        self.update_game_company_info_frame.pack(fill="both", expand=True)

        self._update_game_company_info_element_builder(self.update_game_company_info_frame)

    def format_game_company_info_result(self, row):
        formatted_row = []

        for index, item in enumerate(row):
            if isinstance(item, float):
                    formatted_item = f"{item:<50.2f}"
            else:
                formatted_item = f"{str(item):<80}"

            formatted_row.append(formatted_item)

        return " ".join(formatted_row)

    def fetch_game_companies(self):
        result = uo.UpdateOperation().fetch_game_companies()
        if (isinstance(result, err.ErrorReturnType)):
            tkMessageBox.showerror("Error", result.error_message)
        else:
            self.fetch_game_company_listbox.delete(0, tk.END)
            for row in result:
                formatted_row = self.format_game_company_info_result(row)
                self.fetch_game_company_listbox.insert(tk.END, formatted_row)

    def update_game_company_info(self, company_name_textfield, num_employees_textfield, foundation_year_textfield):
        company_name = company_name_textfield.get()
        num_employees = num_employees_textfield.get()
        foundation_year = foundation_year_textfield.get()

        result = uo.UpdateOperation().update_game_company_info(company_name, num_employees, foundation_year)
        if (isinstance(result, err.ErrorReturnType)):
            tkMessageBox.showerror("Error", result.error_message)
        else:
            self.update_game_company_info_listbox.delete(0, tk.END)
            for row in result:
                formatted_row = self.format_game_company_info_result(row)
                self.update_game_company_info_listbox.insert(tk.END, formatted_row)
    

    def go_back_to_update_main_screen(self):
        self.update_game_company_info_frame.pack_forget()
        self.update_main_screen_frame.pack_forget()
        self.setup_update_main_screen()                                    
