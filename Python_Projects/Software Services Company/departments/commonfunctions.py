import pickle

# Saving object list
def save_object(list, filename):
    try:
        with open(filename, "wb") as file:
            pickle.dump(list, file)
    except Exception as ex:
        print("Error during pickle object (Possibly unsupported):", ex)

# Loading file
def load_object(filename):
    loaded_list = []
    try:
        with open(filename, "rb") as file:
            loaded_list = pickle.load(file)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        loaded_list = None

    return loaded_list