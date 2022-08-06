"""Graphic user interface (GUI)."""
# python
import tkinter as tk
import tkinter.ttk as ttk
import typing

# local
from app import constants
from app.backend import Backend


def clear_form() -> None:
    """Clear entry widgets."""
    title_text.set('')
    author_text.set('')
    year_text.set('')
    ISBN_text.set('')


def selected_values() -> typing.Optional[typing.List]:
    """
    Get values from current selected row.

    Returns
    -------
    list
        List with row values.
    """
    selections = list1.selection()
    if selections:
        selection = selections[0]
        values = list1.item(selection)['values']

        return values

    return None


def get_selected_row(*args):
    """Update entrys from current selected row."""
    values = selected_values()
    if values:
        e1.delete(0, tk.END)
        e1.insert(tk.END, values[1])

        e2.delete(0, tk.END)
        e2.insert(tk.END, values[2])

        e3.delete(0, tk.END)
        e3.insert(tk.END, values[3])

        e4.delete(0, tk.END)
        e4.insert(tk.END, values[4])


def view_command():
    """Show all registers."""
    clear_form()
    list1.delete(*list1.get_children())
    for row in backend.view():
        list1.insert('', tk.END, values=(row))


def search_command():
    """Show registers that match with searched values."""
    title = title_text.get()
    author = author_text.get()
    year = year_text.get()
    isbn = ISBN_text.get()
    list1.delete(*list1.get_children())
    for row in backend.search(title, author, year, isbn):
        list1.insert('', tk.END, values=(row))


def add_command():
    """Add a new registers from entry values."""
    title = title_text.get()
    author = author_text.get()
    year = year_text.get()
    isbn = ISBN_text.get()
    backend.insert(title, author, year, isbn)
    view_command()


def delete_command():
    """Delete current selected row."""
    values = selected_values()
    if values:
        backend.delete(values[0])
        view_command()


def update_command():
    """Update current selected row using current entry values."""
    values = selected_values()
    if values:
        idbook = values[0]
        title = title_text.get()
        author = author_text.get()
        year = year_text.get()
        isbn = ISBN_text.get()
        backend.update(idbook, title, author, year, isbn)
        view_command()


# database
backend = Backend(database_name=constants.DATABASE_NAME)

# interface
window = tk.Tk()
window.wm_title('The Book Store')

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)
window.columnconfigure(5, weight=1)
window.rowconfigure(2, weight=1)

l1 = ttk.Label(window, text='Title', anchor='center')
l1.grid(row=0, column=0, sticky='ew')

title_text = tk.StringVar()
e1 = ttk.Entry(window, textvariable=title_text)
e1.grid(row=0, column=1, columnspan=2, sticky='ew')

l2 = ttk.Label(window, text='Author', anchor='center')
l2.grid(row=0, column=3, sticky='ew')

author_text = tk.StringVar()
e2 = ttk.Entry(window, textvariable=author_text)
e2.grid(row=0, column=4, columnspan=2, sticky='ew')

l3 = ttk.Label(window, text='Year', anchor='center')
l3.grid(row=1, column=0, sticky='ew')

year_text = tk.StringVar()
e3 = ttk.Entry(window, textvariabl=year_text)
e3.grid(row=1, column=1, columnspan=2, sticky='ew')

l4 = ttk.Label(window, text='ISBN', anchor='center')
l4.grid(row=1, column=3, sticky='ew')

ISBN_text = tk.StringVar()
e4 = ttk.Entry(window, textvariable=ISBN_text)
e4.grid(row=1, column=4, columnspan=2, sticky='ew')

list1 = ttk.Treeview(window, columns=('id', 'title', 'author', 'year', 'isbn'))
list1.configure(show='headings')
list1.heading('id', text='Id')
list1.heading('title', text='Title')
list1.heading('author', text='Author')
list1.heading('year', text='Year')
list1.heading('isbn', text='ISBN')
list1.bind('<<TreeviewSelect>>', get_selected_row)
list1.grid(row=2, column=0, columnspan=6, sticky='nsew', pady=20)

sb1 = ttk.Scrollbar(window)
sb1.grid(row=2, column=6, sticky='ns', pady=20)

list1.config(yscrollcommand=sb1.set)
sb1.config(command=list1.yview)

eye_image = tk.PhotoImage(file=constants.EYE_IMAGE)
b1 = ttk.Button(window, text='View all', command=view_command)
b1.configure(image=eye_image, compound='left')
b1.grid(row=3, column=0, sticky='ew')

search_image = tk.PhotoImage(file=constants.SEARCH_IMAGE)
b2 = ttk.Button(window, text='Search', command=search_command)
b2.configure(image=search_image, compound='left')
b2.grid(row=3, column=1, sticky='ew')

add_image = tk.PhotoImage(file=constants.ADD_IMAGE)
b3 = ttk.Button(window, text='Add', command=add_command)
b3.configure(image=add_image, compound='left')
b3.grid(row=3, column=2, sticky='ew')

update_image = tk.PhotoImage(file=constants.UPDATE_IMAGE)
b4 = ttk.Button(window, text='Update', command=update_command)
b4.configure(image=update_image, compound='left')
b4.grid(row=3, column=3, sticky='ew')

delete_image = tk.PhotoImage(file=constants.DELETE_IMAGE)
b5 = ttk.Button(window, text='Delete', command=delete_command)
b5.configure(image=delete_image, compound='left')
b5.grid(row=3, column=4, sticky='ew')

close_image = tk.PhotoImage(file=constants.CLOSE_IMAGE)
b6 = ttk.Button(window, text='Close', command=window.destroy)
b6.configure(image=close_image, compound='left')
b6.grid(row=3, column=5, columnspan=2, sticky='ew')

# style
font = 'Georgia 16 normal'
style = ttk.Style()
style.theme_use('clam')

window.configure(background='#EFD3CD')
style.configure('.', background='#EFD3CD')

style.configure('TButton', background='#EBB6B3')
style.configure('Treeview', rowheight=40)
style.configure('Treeview.Heading', font=font)

style.configure('.', font=font)
for entry in (e1, e2, e3, e4):
    entry.configure(font=font)
