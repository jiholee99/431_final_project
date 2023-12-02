class UtilOperation():
    def __init__(self):
        return

    # This function will format the result from the database into a list of strings
    # that can be displayed in the listbox
    def format_result(self, row):
        formatted_row = []

        for index, item in enumerate(row):
            formatted_item = f"{str(item):<50}"
            formatted_row.append(formatted_item)

        return formatted_row