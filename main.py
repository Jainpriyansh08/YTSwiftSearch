# This is a sample Python script.
from swiftsearch import search_and_play


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
if __name__ == "__main__":
    # Get input from the user within theF notebook
    api_key = input("Enter your YouTube API key: ")
    query = input("Enter your search query: ")

    search_and_play(api_key, query)
