import tkinter as tk
import tkinter.messagebox as tkMessageBox
import db_operation.update_operation as uo
import type.error_return_type as err
import re

class UpdateReviewScreen():
    def __init__(self, update_main_screen_frame, master, setup_update_main_screen):
        self.update_main_screen_frame = update_main_screen_frame
        self.master = master
        self.setup_update_main_screen = setup_update_main_screen
        # This frame is the frame for this page
        self.update_review_frame = tk.Frame(self.master)
        self.setup_update_review()

    def _update_review_element_builder(self, update_review_frame ):
        pady = 5

        # Update function frame title
        update_review_title = tk.Label(update_review_frame, text="Update Review",bg="yellow",)
        update_review_title.pack(fill="both", expand=False, padx=10, pady=pady)

        # Listbox for fetching all the reviews. This will be populated by the fetch_review_button
        # Users will select the review_id from this listbox
        fetch_review_button = tk.Button(update_review_frame, text="See the list of reviews", bg="yellow" , command=lambda: self.fetch_reviews())
        fetch_review_button.pack(fill="both", expand=False, padx=10, pady=pady)
        # Creating a scrollbar
        fetch_review_scrollbar = tk.Scrollbar(update_review_frame)
        fetch_review_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # Creating a listbox widget
        monospace_font = tk.font.Font(family="Courier", size=10)
        self.fetch_review_listbox = tk.Listbox(update_review_frame, yscrollcommand=fetch_review_scrollbar.set, font=monospace_font)
        self.fetch_review_listbox.pack(fill="both", expand=True, padx=10, pady=pady)

        # Textfield section to update review score
        # You need game_id, reviewer_id and post_id and score.

        # Warning label
        warning_label = tk.Label(update_review_frame, text="Warning: Please make sure you have the correct fields below before pushing the button", fg="red")
        warning_label.pack(fill="both", expand=False, padx=10, pady=pady)

        # Description for game_id textfield description
        game_id_textfield_description = tk.Label(update_review_frame, text="Enter the game_id you want to change review score",)
        game_id_textfield_description.pack(fill="both", expand=False, padx=10, pady=pady)
        # Textfield for game_id
        game_id_textfield = tk.Entry(update_review_frame, width=30)
        game_id_textfield.pack(fill="both", expand=False, padx=10, pady=pady)

        # Description for reviewer_id textfield description
        reviewer_id_textfield_description = tk.Label(update_review_frame, text="Enter the reviewer_id you want to change review score",)
        reviewer_id_textfield_description.pack(fill="both", expand=False, padx=10, pady=pady)
        # Textfield for reviewer_id
        reviewer_id_textfield = tk.Entry(update_review_frame, width=30)
        reviewer_id_textfield.pack(fill="both", expand=False, padx=10, pady=pady)

        # Description for post_id textfield description
        post_id_textfield_description = tk.Label(update_review_frame, text="Enter the post_id you want to change review score",)
        post_id_textfield_description.pack(fill="both", expand=False, padx=10, pady=pady)
        # Textfield for post_id
        post_id_textfield = tk.Entry(update_review_frame, width=30)
        post_id_textfield.pack(fill="both", expand=False, padx=10, pady=pady)

        # Description for score textfield description
        score_textfield_description = tk.Label(update_review_frame, text="Enter the score you want to change review score",)
        score_textfield_description.pack(fill="both", expand=False, padx=10, pady=pady)
        # Textfield for score
        score_textfield = tk.Entry(update_review_frame, width=30)
        score_textfield.pack(fill="both", expand=False, padx=10, pady=pady)

        # Button : Update review score
        update_review_score_button = tk.Button(update_review_frame, text="Update review score", bg="yellow", command=lambda: self.update_review_score(game_id_textfield, reviewer_id_textfield, post_id_textfield, score_textfield))
        update_review_score_button.pack(fill="both", expand=False, padx=10, pady=pady)

        # Description for listbox
        update_review_description = tk.Label(update_review_frame, text="If your request was successful, the table below will show an upadted review value",)
        update_review_description.pack(fill="both", expand=False, padx=10, pady=pady)

        # Creating a scrollbar
        update_review_scrollbar = tk.Scrollbar(update_review_frame)
        update_review_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Creating a listbox widget
        monospace_font = tk.font.Font(family="Courier", size=10)
        self.update_review_listbox = tk.Listbox(update_review_frame, yscrollcommand=update_review_scrollbar.set, font=monospace_font)
        self.update_review_listbox.pack(fill="both", expand=True, padx=10, pady=pady)
    
        # Go back Button
        go_back_button = tk.Button(update_review_frame, text="Go back to update main screen", bg="yellow", command=lambda: self.go_back_to_update_main_screen())
        go_back_button.pack(fill="both", expand=False, padx=10, pady=pady)
    
    def setup_update_review(self):
        self.update_main_screen_frame.pack_forget()
        self.update_review_frame.pack(fill="both", expand=True)
        self._update_review_element_builder(self.update_review_frame)

    def format_reviews_result(self, row):
        formatted_row = []

        for index, item in enumerate(row):
            if isinstance(item, float):
                    formatted_item = f"{item:<50.2f}"
            else:
                formatted_item = f"{str(item):<50}"

            formatted_row.append(formatted_item)

        return " ".join(formatted_row)

    def fetch_reviews(self):
        result = uo.UpdateOperation().fetch_reviews()

        # Clear the listbox
        self.fetch_review_listbox.delete(0, tk.END)

        for row in result:
            formatted_row = self.format_reviews_result(row)
            self.fetch_review_listbox.insert(tk.END, formatted_row)

    def update_review_score(self, game_id_textfield, reviewer_id_textfield, post_id_textfield, score_textfield):
        game_id = game_id_textfield.get()
        reviewer_id = reviewer_id_textfield.get()
        post_id = post_id_textfield.get()
        score = score_textfield.get()

        if game_id == "" or reviewer_id == "" or post_id == "" or score == "":
            tkMessageBox.showerror("Error", "One or more of your field is empty. Please fill in all the fields")
            return
        if not(game_id.isdigit()) or not(reviewer_id.isdigit()) or not(post_id.isdigit()) or not(score.isdigit()):
            tkMessageBox.showerror("Error", "One or more of your field contains non digit string. Please enter a valid number")
            return
        
        result = uo.UpdateOperation().update_review_score(game_id, reviewer_id, post_id, score)

        if (isinstance(result, err.ErrorReturnType)):
            tkMessageBox.showerror("Error", result.error_message)
            return
        
        # Clear the listbox
        self.update_review_listbox.delete(0, tk.END)
        
        for row in result:
            formatted_row = self.format_reviews_result(row)
            self.update_review_listbox.insert(tk.END, formatted_row)
        

    def go_back_to_update_main_screen(self):
        self.update_review_frame.pack_forget()
        self.update_main_screen_frame.pack_forget()
        self.setup_update_main_screen()
    
