import tkinter as tk
import tkinter.font as tkFont

import navigation.fetch_screen.fetch_main_screen as fs
import navigation.insert_screen.insert_screen as inst
import navigation.update_screen.update_screen as upd
import navigation.delete_screen.delete_screen as dlt

class MainApp :
    def __init__(self, master) :
        self.master = master
         # Center the window
        window_width = 600
        window_height = 600
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.master.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.setup_main_screen()

    def _title_frame_element_builder(self, title_frame):
        # Title
        title_label = tk.Label(title_frame, text="Video Game Database Application", bg="pink")
        title_label.pack(pady=20)
        # Description
        description_label = tk.Label(title_frame, text="This application allows users to insert, update, and delete information about video games.", bg="pink")
        description_label.pack(pady=20)


    # Set up initial GUI
    def setup_main_screen(self):
        # Initial frame
        initial_frame = tk.Frame(self.master)
        initial_frame.pack(fill="both", expand=True)

        # Frame 0 : Title and description
        title_frame = tk.Frame(initial_frame)
        title_frame.configure(bg="pink")
        title_frame.pack(fill="both", expand=False, )  # Make it expand horizontally
        self._title_frame_element_builder(title_frame)
        
        # Frame 1 : Fetching functions
        fetch_function_parent_frame = tk.Frame(initial_frame)
        fetch_function_parent_frame.configure(bg="lightblue", height=100)
        fetch_function_parent_frame.pack(fill="both", expand=True)
        # Go to fetching function page
        go_to_fetch_screen_button = tk.Button(fetch_function_parent_frame, text="Go to fetching functions", command= lambda: fs.FetchMainScreen(initial_frame, self.master, self.setup_main_screen))
        go_to_fetch_screen_button.pack(pady=20, padx=20, expand=True)
        
        
        # Frame 2 : Inserting functions
        insert_function_parent_frame = tk.Frame(initial_frame)
        insert_function_parent_frame.configure(bg="green",)
        insert_function_parent_frame.pack(fill="both", expand=True)  # Make it expand horizontally
        # Go to inserting function page
        go_to_insert_screen_button = tk.Button(insert_function_parent_frame, text="Go to inserting functions", command= lambda: inst.InsertScreen(initial_frame, self.master, self.setup_main_screen))
        go_to_insert_screen_button.pack(pady=20, padx=20, expand=True)

        # Frame 3 : Updating functions
        update_function_parent_frame = tk.Frame(initial_frame)
        update_function_parent_frame.configure(bg="red",)
        update_function_parent_frame.pack(fill="both", expand=True)  # Make it expand horizontally
        # Go to updating function page
        go_to_update_screen_button = tk.Button(update_function_parent_frame, text="Go to updating functions", command= lambda: upd.UpdateScreen(initial_frame, self.master, self.setup_main_screen))
        go_to_update_screen_button.pack(pady=20, padx=20, expand=True)

        # Frame 4 : Deleting functions
        delete_function_parent_frame = tk.Frame(initial_frame)
        delete_function_parent_frame.configure(bg="yellow",)
        delete_function_parent_frame.pack(fill="both", expand=True)  # Make it expand horizontally
        # Go to deleting function page
        go_to_delete_screen_button = tk.Button(delete_function_parent_frame, text="Go to deleting functions", command= lambda: dlt.DeleteScreen(initial_frame, self.master, self.setup_main_screen))
        go_to_delete_screen_button.pack(pady=20, padx=20, expand=True)

if __name__ == "__main__" :
    root = tk.Tk()
    MainApp(root)
    root.mainloop()