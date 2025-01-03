import requests
from bs4 import BeautifulSoup
import tkinter as tk
import random


# ️ Scrape words from Wikipedia
def get_words_from_wikipedia():
    url = "https://en.wikipedia.org/wiki/List_of_English_words_of_Latin_origin"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    words = [word.text.strip() for word in soup.find_all("li")]

    # Filter to include only alphabetical words
    return [word for word in words if word.isalpha()]


# Create the GUI window
def create_gui(words):
    if not words:
        print("No words found. Exiting.")
        return

    root = tk.Tk()
    root.title("Word Generator")
    root.geometry("800x400")
    root.configure(bg="white")

    word_label = tk.Label(root, text="", font=("Helvetica", 64), fg="black", bg="white")
    word_label.pack(expand=True)

    timer_label = tk.Label(root, text="10", font=("Helvetica", 32), fg="gray", bg="white")
    timer_label.pack()

    def update_word():
        word = random.choice(words)
        word_label.config(text=word)
        countdown(10)

    def countdown(seconds):
        if seconds > 0:
            timer_label.config(text=f"{seconds} seconds")
            root.after(1000, countdown, seconds - 1)
        else:
            update_word()

    update_word()
    root.mainloop()


# Main Program
words = get_words_from_wikipedia()
create_gui(words)
