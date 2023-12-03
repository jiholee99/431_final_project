import tkinter as tk
import db_operation.delete_operation as do
import type.error_return_type as err
import tkinter.messagebox as tkMessageBox

class DeleteReviewerAndReviewsScreen():
    def __init__(self, delete_screen_frame, master, setup_delete_screen):
        self.delete_screen_frame = delete_screen_frame
        self.master = master
        self.setup_delete_screen = setup_delete_screen
        # This frame is the frame for this page
        self.delete_reviewer_and_reviews_frame = tk.Frame(self.master)
        self.setup_delete_reviewer_and_reviews()

    def _delete_reviewer_and_reviews_element_builder(self,delete_review_frame):
        pady = 5

        # Delete review frame title
        delete_review_title = tk.Label(delete_review_frame, text="Delete reviewer and reviews",bg="lightblue",)
        delete_review_title.pack(fill="both", expand=False, padx=10, pady=pady)

        # Reviewer ID frame
        reviewer_id_frame = tk.Frame(delete_review_frame)
        reviewer_id_frame.pack(fill="both", expand=False, padx=10, pady=pady)

        # Reviewer ID label
        reviewer_id_label = tk.Label(reviewer_id_frame, text="Type in the reviewer ID to delete:",)
        reviewer_id_label.grid(row=0, column=0)
        # Reviewer ID entry
        self.reviewer_id_entry = tk.Entry(reviewer_id_frame,)
        self.reviewer_id_entry.grid(row=0, column=1)

        # Delete reviewer and reviews button
        delete_reviewer_and_reviews_button = tk.Button(delete_review_frame, text="Delete reviewer and reviews", bg="lightblue", command=lambda: self.delete_reviewer_and_reviews(self.reviewer_id_entry))
        delete_reviewer_and_reviews_button.pack(fill="both", expand=False, padx=10, pady=pady)

        # Button : See updated reviewer and reviews
        see_updated_reviewer_and_reviews_button = tk.Button(delete_review_frame, text="See updated reviewer and reviews", bg="lightblue", command=lambda: self._see_updated_reviewer_and_reviews())
        see_updated_reviewer_and_reviews_button.pack(fill="both", expand=False, padx=10, pady=pady)

        # Description for reviewer
        reviewer_description = tk.Label(delete_review_frame, text="Reviewer table",)
        reviewer_description.pack(fill="both", expand=False, padx=10, pady=pady)
        # Scrollbar for reviewer
        scrollbar_reviewer = tk.Scrollbar(delete_review_frame)
        scrollbar_reviewer.pack(side=tk.RIGHT, fill=tk.Y)

        # Listbox for reviewer
        monospace_font = tk.font.Font(family="Courier", size=10)
        self.reviewer_listbox = tk.Listbox(delete_review_frame, yscrollcommand=scrollbar_reviewer.set, font=monospace_font)
        self.reviewer_listbox.pack(fill="both", expand=True, padx=10, pady=pady)

        # Description for reviews
        reviews_description = tk.Label(delete_review_frame, text="Reviews table. Contains all information about reviewer reviews a game.",)
        reviews_description.pack(fill="both", expand=False, padx=10, pady=pady)
        # Scrollbar for reviews
        scrollbar_reviews = tk.Scrollbar(delete_review_frame)
        scrollbar_reviews.pack(side=tk.RIGHT, fill=tk.Y)
        # Listbox for reviews
        monospace_font = tk.font.Font(family="Courier", size=10)
        self.reviews_listbox = tk.Listbox(delete_review_frame, yscrollcommand=scrollbar_reviews.set, font=monospace_font)
        self.reviews_listbox.pack(fill="both", expand=True, padx=10, pady=pady)

        
        # Button : Go back to delete screen
        go_back_to_delete_screen_button = tk.Button(delete_review_frame, text="Go back to delete screen", fg="blue", command=lambda: self.go_back_to_delete_screen())
        go_back_to_delete_screen_button.pack(fill="both", expand=False, padx=10, pady=pady)
    
    def setup_delete_reviewer_and_reviews(self):
        self.delete_screen_frame.pack_forget()

        self.delete_reviewer_and_reviews_frame.pack(fill="both", expand=True)

        self._delete_reviewer_and_reviews_element_builder(self.delete_reviewer_and_reviews_frame)

    def go_back_to_delete_screen(self):
        self.delete_reviewer_and_reviews_frame.pack_forget()
        self.delete_screen_frame.pack(fill="both", expand=True)

    def format_result(self, row):
        formatted_row = []

        for index, item in enumerate(row):
            if isinstance(item, float):
                    formatted_item = f"{item:<50.2f}"
            else:
                formatted_item = f"{str(item):<30}"

            formatted_row.append(formatted_item)

        return " ".join(formatted_row)

    def delete_reviewer_and_reviews(self, reviewer_textfield):
        reviewer_id = reviewer_textfield.get()
        if reviewer_id == "":
            return
        print(reviewer_id)

        remove_result = do.DeleteOperation().delete_reviewer_and_reviews(reviewer_id)

        if (isinstance(remove_result, err.ErrorReturnType)):
            tkMessageBox.showerror("Error", remove_result.error_message)
            return

        tkMessageBox.showinfo("Success", "Successfully deleted reviewer and reviews")
        

    def _see_updated_reviewer_and_reviews(self):
        # Update reviewer listbox
        reviewer_result = do.DeleteOperation().fetch_reviewer()
        
        if (isinstance(reviewer_result, err.ErrorReturnType)):
            tkMessageBox.showerror("Error", reviewer_result.error_message)
            return
        
        self.reviewer_listbox.delete(0, tk.END)
        for row in reviewer_result:
            formatted_row = self.format_result(row)
            self.reviewer_listbox.insert(tk.END, formatted_row)

        # Update reviews listbox
        reviews_result = do.DeleteOperation().fetch_reviews()

        if (isinstance(reviews_result, err.ErrorReturnType)):
            tkMessageBox.showerror("Error", reviews_result.error_message)
            return
        
        self.reviews_listbox.delete(0, tk.END)
        for row in reviews_result:
            formatted_row = self.format_result(row)
            self.reviews_listbox.insert(tk.END, formatted_row)