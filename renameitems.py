import os
import tkinter as tk
from tkinter import filedialog, ttk
from threading import Thread
import time

def rename_items(folder_path, progress_var, result_label):
    items = os.listdir(folder_path)
    total_items = len(items)

    for i, item in enumerate(items, start=1):
        item_path = os.path.join(folder_path, item)
        item_name, item_extension = os.path.splitext(item)
        new_name = str(i) + item_extension
        new_item_path = os.path.join(folder_path, new_name)

        # Check if the new name already exists and generate a unique name if needed
        while os.path.exists(new_item_path):
            i += 1
            new_name = str(i) + item_extension
            new_item_path = os.path.join(folder_path, new_name)

        os.rename(item_path, new_item_path)
        time.sleep(0.1)  # Simulate some work
        progress_var.set((i / total_items) * 100)
        result_label.config(text=f"Renaming {item} to {new_name}")

    result_label.config(text="Renaming completed!")


def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_label.config(text=f"Selected Folder: {folder_path}")
        start_button.config(state=tk.NORMAL)

def start_renaming():
    selected_folder = folder_label.cget("text")[16:].strip()  # Remove leading/trailing spaces
    if selected_folder:
        progress_var.set(0)
        result_label.config(text="Renaming in progress...")
        start_button.config(state=tk.DISABLED)

        thread = Thread(target=rename_items, args=(selected_folder, progress_var, result_label))
        thread.start()


# Create the main window
root = tk.Tk()
root.title("Batch Rename Tool")

# Create and configure widgets
label = tk.Label(root, text="Select a folder to batch rename:")
label.pack(pady=10)

browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.pack(pady=10)

folder_label = tk.Label(root, text="Selected Folder: ")
folder_label.pack(pady=10)

start_button = tk.Button(root, text="Start Renaming", command=start_renaming, state=tk.DISABLED)
start_button.pack(pady=10)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the main event loop
root.mainloop()
