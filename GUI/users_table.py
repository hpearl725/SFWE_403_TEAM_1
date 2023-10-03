from tkinter import ttk


def create_users_table(frame):
    """
    This function creates a Users table using a Treeview widget.

    :param frame: The parent frame to which the Users table will be added.
    :type frame: tk.Frame
    :return: The created Users table.
    :rtype: ttk.Treeview
    """
    users_tree = ttk.Treeview(frame, columns=("Username", "Role"), show="headings")

    users_tree.heading("Username", text="Username")
    users_tree.heading("Role", text="Role")

    users_tree.insert("", "end", values=("user1", "Admin"))
    users_tree.insert("", "end", values=("user2", "User"))
    users_tree.insert("", "end", values=("user3", "User"))

    return users_tree


def show_users_table(users_tree):
    """
    This function shows the Users table.

    :param users_tree: The Users table to be shown.
    :type users_tree: ttk.Treeview
    """
    users_tree.pack()


def hide_users_table(users_tree):
    """
    This function hides the Users table.

    :param users_tree: The Users table to be hidden.
    :type users_tree: ttk.Treeview
    """
    users_tree.pack_forget()
