import tkinter

class DeleteReviewScreen():
    def __init__(self, initial_frame, master, setup_main_screen):
        self.initial_frame = initial_frame
        self.master = master
        self.setup_main_screen = setup_main_screen
        # This frame is the frame for this page
        self.delete_review_screen_frame = tkinter.Frame(self.master)
        self.setup_delete_review_screen()

    def _delete_review_element_builder(self,delete_review_frame):
        pady = 5

        # Delete review frame title
        delete_review_title = tkinter.Label(delete_review_frame, text="Delete Review",bg="lightblue",)
        delete_review_title.pack(fill="both", expand=False, padx=10, pady=pady)

        # Description for textfield
        description_label = tkinter.Label(delete_review_frame, text="Enter the review ID of the review you want to delete", bg="lightblue")
        description_label.pack(fill="both", expand=False, padx=10, pady=pady)

        # Textfield for review ID
        review_id_textfield = tkinter.Entry(delete_review_frame, width=30)
        review_id_textfield.pack(fill="both", expand=False, padx=10, pady=pady)

        # Delete button
        delete_review_button = tkinter.Button(delete_review_frame, text="Delete", bg="lightblue", command=lambda: self._delete_review(review_id_textfield))
        delete_review_button.pack(fill="both", expand=False, padx=10, pady=pady)


        # Button : Go back to delete screen
        go_back_to_delete_screen_button = tkinter.Button(delete_review_frame, text="Go back to delete screen", bg="lightblue", command=self.go_back_to_delete_screen)
        go_back_to_delete_screen_button.pack(fill="both", expand=False, padx=10, pady=pady)

    def setup_delete_review_screen(self):
        self.initial_frame.pack_forget()

        self.delete_review_screen_frame.pack(fill="both", expand=True)

        self._delete_review_element_builder(self.delete_review_screen_frame)
    
    def go_back_to_main_screen(self):
        self.delete_review_screen_frame.pack_forget()
        self.setup_main_screen()

    def _delete_review(self, review_id_textfield):
        pass