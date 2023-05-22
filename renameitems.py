import os

def rename_items(folder_path):
    items = os.listdir(folder_path)
    total_items = len(items)

    for i, item in enumerate(items, start=1):
        item_path = os.path.join(folder_path, item)
        item_name, item_extension = os.path.splitext(item)
        new_name = str(i) + item_extension
        new_item_path = os.path.join(folder_path, new_name)
        os.rename(item_path, new_item_path)
        print(f"Renamed {item} to {new_name}")

# Example usage
folder_path = "images"
rename_items(folder_path)
