

def read_lines(file_location):
    try:
        with open(file_location, 'r', encoding='utf-8') as file_handler:
            rows = file_handler.readlines()
            return rows
    except Exception as e:
        print(e)
        return []