import tkinter
import db_operation.analytical_operation as ao
import type.error_return_type as error_return_type
import tkinter.messagebox as tkMessageBox

class GameReportScreen():
    def __init__(self, analytical_report_screen_frame, master, setup_analytical_report_screen):
        self.analytical_report_screen_frame = analytical_report_screen_frame
        self.master = master
        self.setup_analytical_report_screen = setup_analytical_report_screen
        # This frame is the frame for this page
        self.game_report_screen_frame = tkinter.Frame(self.master)
        self.game_report_sortby_value = tkinter.StringVar()
        self.game_report_sortby_value.set("# of streamers playing")
        self.setup_game_report_screen()

    def _game_report_element_builder(self,delete_review_frame):
        pady = 5

        # Delete review frame title
        delete_review_title = tkinter.Label(delete_review_frame, text="Game report",bg="lightblue",)
        delete_review_title.pack(fill="both", expand=False, padx=10, pady=pady)


        # Sort by frame
        sort_by_frame = tkinter.Frame(delete_review_frame)
        sort_by_frame.pack(fill="both", expand=False, padx=10, pady=pady)

        # Sort by label
        sort_by_label = tkinter.Label(sort_by_frame, text="Sort by:",)
        sort_by_label.grid(row=0, column=0)
        # Sort by dropdown
        sort_by_dropdown = tkinter.OptionMenu(sort_by_frame, self.game_report_sortby_value, "# of streamers playing", "# of platform available", "Game sales",)
        sort_by_dropdown.grid(row=0, column=1)


        # Get sorted game report button
        get_sorted_game_report_button = tkinter.Button(delete_review_frame, text="Get sorted game report", bg="lightblue", command=lambda: self._get_report())
        get_sorted_game_report_button.pack(fill="both", expand=False, padx=10, pady=pady)

        # Creating a scrollbar
        scrollbar_game_report = tkinter.Scrollbar(delete_review_frame)
        scrollbar_game_report.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # Creating a listbox widget
        monospace_font = tkinter.font.Font(family="Courier", size=10)
        self.game_report_listbox = tkinter.Listbox(delete_review_frame, yscrollcommand=scrollbar_game_report.set, font=monospace_font)
        self.game_report_listbox.pack(fill="both", expand=True, padx=10, pady=pady)


        # Button : Go back to delete screen
        go_back_to_delete_screen_button = tkinter.Button(delete_review_frame, text="Go back to delete screen", fg="blue", command=lambda: self.go_back_to_main_screen())
        go_back_to_delete_screen_button.pack(fill="both", expand=False, padx=10, pady=pady)

    def setup_game_report_screen(self):
        self.analytical_report_screen_frame.pack_forget()

        self.game_report_screen_frame.pack(fill="both", expand=True)

        self._game_report_element_builder(self.game_report_screen_frame)
    
    def go_back_to_main_screen(self):
        self.game_report_screen_frame.pack_forget()
        self.analytical_report_screen_frame.pack_forget()
        self.setup_analytical_report_screen()

    def format_result(self, row, is_header=False):
        formatted_row = []

        for index, item in enumerate(row):
            if index == 0: # Game id
                formatted_item = f"{str(item):<20}"
            elif index == 1: # Title
                formatted_item = f"{str(item):<70}"
            elif index == 2 or index == 3: # # of streamers playing, # of platform available
                if is_header:
                    formatted_item = f"{str(item):<30}"
                else:
                    formatted_item = f"{item:<30}"
            elif index == 4: # Game sales
                if is_header:
                    formatted_item = f"{str(item):<50}"
                else:
                    formatted_item = f"{item:<50.2f}"
            formatted_row.append(formatted_item)

        return " ".join(formatted_row)

    def _get_report(self):
        sortby = self.game_report_sortby_value.get()
        
        result = ao.AnalyticalOperation().get_sorted_game_report(sort_by= sortby)

        self.game_report_listbox.delete(0, tkinter.END)

        if isinstance(result, error_return_type.ErrorReturnType):
            error_message = result.error_message
            tkMessageBox.showerror("Error", error_message)
            self.game_report_listbox.insert(tkinter.END, "Error occured")
            return
        
        for index,row in enumerate(result):
            if index == 0:
                formatted_row = self.format_result(row, is_header=True)
            else:
                formatted_row = self.format_result(row)
            self.game_report_listbox.insert(tkinter.END, formatted_row)
        

