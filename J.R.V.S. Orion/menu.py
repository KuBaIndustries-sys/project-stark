import tkinter as tk


def create_menu(root, save_conversation, quit_app):
    """Tworzy menu aplikacji."""
    menu_bar = tk.Menu(root)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Zapisz historię", command=lambda: save_conversation())
    file_menu.add_separator()
    file_menu.add_command(label="Wyjście", command=quit_app)

    menu_bar.add_cascade(label="Plik", menu=file_menu)
    root.config(menu=menu_bar)
