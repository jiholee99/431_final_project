import tkinter as tk
import navigation.delete_screen.delete_reviewer_and_reviews_screen as drrs
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as tkMessageBox

class DeleteScreen():
    def __init__(self, initial_frame, master, setup_main_screen):
        self.initial_frame = initial_frame
        self.master = master
        self.setup_main_screen = setup_main_screen
        # This frame is the frame for this page
        self.delete_screen_frame = tk.Frame(self.master)
        self.setup_delete_screen()

    def _delete_function_element_builder(self,delete_frame):
        pady = 5

        # Delete function frame title
        delete_function_title = tk.Label(delete_frame, text="Deleting Functions",bg="red",)
        delete_function_title.pack(fill="both", expand=False, padx=10, pady=pady)

        # Button : Admin can delete a reviewer and all of their reviews
        delete_reviewer_and_reviews_button = tk.Button(delete_frame, text="Delete reviewer and reviews(ADMIN ONLY)", bg="red", command= lambda: self.type_in_admin_password(delete_frame=self.delete_screen_frame))
        delete_reviewer_and_reviews_button.pack(fill="both", expand=False, padx=10, pady=pady)

        # Button : Go back to main screen
        go_back_to_main_screen_button = tk.Button(delete_frame, text="Go back to main screen", fg="blue", command= self.go_back_to_main_screen)
        go_back_to_main_screen_button.pack(fill="both", expand=False, padx=10, pady=pady)

    def type_in_admin_password(self, delete_frame):
        # admin password dialog
        
        result = simpledialog.askstring("Admin password", "Please type in the admin password", parent=self.master)
        if result == "admin":
            drrs.DeleteReviewerAndReviewsScreen(delete_frame, self.master, self.setup_delete_screen)
        else:
            tkMessageBox.showerror("Error", "Incorrect password")
    
    def setup_delete_screen(self):
        for widget in self.delete_screen_frame.winfo_children():
            widget.destroy()

        self.initial_frame.pack_forget()

        self.delete_screen_frame.pack(fill="both", expand=True)

        self._delete_function_element_builder(self.delete_screen_frame)
    
    def go_back_to_main_screen(self):
        self.delete_screen_frame.pack_forget()
        self.setup_main_screen()
        