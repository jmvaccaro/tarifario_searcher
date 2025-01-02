import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pandas as pd

# Get df from tarifario_data
df = pd.read_csv("tarifario_data.csv")
cart = []

def get_amount():
    # Get the selected category, subcategory, and concept from the comboboxes
    category = combobox_category.get()
    subcategory = combobox_subcategory.get()
    concept = combobox_concept.get()

    if category and subcategory and concept:
        # Filter the data based on the selected category, subcategory, and concept
        result = df[(df['Category'] == category) & (df['Subcategory'] == subcategory) & (df['Concept'] == concept)]

        if not result.empty:
            # Get the amounts for each client
            client_a_amount = result['Client A'].values[0]
            client_b_amount = result['Client B'].values[0]
            client_c_amount = result['Client C'].values[0]

            # Format the amounts
            client_a_amount_formatted = f"${client_a_amount:,.0f}"
            client_b_amount_formatted = f"${client_b_amount:,.0f}"
            client_c_amount_formatted = f"${client_c_amount:,.0f}"

            def add_to_cart():
                # Add the selected concept and its amounts to the cart
                cart.append((concept, client_a_amount, client_b_amount, client_c_amount))
                update_cart()
                popup.destroy()

            def close_popup():
                popup.destroy()

            # Create a popup window to display the amounts
            popup = tk.Toplevel(window)
            popup.title("Amount Result")

            label = tk.Label(popup, text=f"Montos:\nCliente A: {client_a_amount_formatted}\n"
                                         f"Cliente B: {client_b_amount_formatted}\n"
                                         f"Cliente C: {client_c_amount_formatted}")
            label.pack(pady=10)

            add_button = tk.Button(popup, text="Agregar al carrito", command=add_to_cart)
            add_button.pack(side=tk.LEFT, padx=10, pady=10)

            accept_button = tk.Button(popup, text="Aceptar", command=close_popup)
            accept_button.pack(side=tk.LEFT, padx=10, pady=10)

        else:
            messagebox.showerror("Error", "No se encontraron coincidencias para la Categoría, Subcategoría o Concepto.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, seleccione todos los campos.")

def update_cart():
    # Update the cart view by removing old items and adding new ones
    for item in treeview_cart.get_children():
        treeview_cart.delete(item)

    total_client_a = 0
    total_client_b = 0
    total_client_c = 0

    for item in cart:
        concept, amount_a, amount_b, amount_c = item
        amount_a_formatted = f"${amount_a:,.0f}"
        amount_b_formatted = f"${amount_b:,.0f}"
        amount_c_formatted = f"${amount_c:,.0f}"

        # Insert the item into the Treeview (cart display)
        treeview_cart.insert("", "end", values=(concept, amount_a_formatted, amount_b_formatted, amount_c_formatted))

        total_client_a += amount_a
        total_client_b += amount_b
        total_client_c += amount_c

    # Insert the total values into the Treeview
    treeview_cart.insert("", "end", values=("Total", f"${total_client_a:,.0f}", f"${total_client_b:,.0f}", f"${total_client_c:,.0f}"))

def update_subcategories(event):
    # Update subcategory options based on selected category
    selected_category = combobox_category.get()
    valid_subcategories = df[df['Category'] == selected_category]['Subcategory'].unique().tolist()
    combobox_subcategory['values'] = valid_subcategories
    combobox_subcategory.set('')
    combobox_concept.set('')
    combobox_concept['values'] = []

def update_concepts(event):
    # Update concept options based on selected category and subcategory
    selected_category = combobox_category.get()
    selected_subcategory = combobox_subcategory.get()
    valid_concepts = df[(df['Category'] == selected_category) & (df['Subcategory'] == selected_subcategory)]['Concept'].unique().tolist()
    combobox_concept['values'] = valid_concepts
    combobox_concept.set('')

# Create the main window
window = tk.Tk()
window.title("Buscar monto y carrito")

# Labels and Comboboxes for selecting the category, subcategory, and concept
tk.Label(window, text="Categoría:").grid(row=0, column=0, padx=10, pady=5)
combobox_category = ttk.Combobox(window, values=df['Category'].unique().tolist())
combobox_category.grid(row=0, column=1, padx=10, pady=5)
combobox_category.bind("<<ComboboxSelected>>", update_subcategories)

tk.Label(window, text="Subcategoría:").grid(row=1, column=0, padx=10, pady=5)
combobox_subcategory = ttk.Combobox(window)
combobox_subcategory.grid(row=1, column=1, padx=10, pady=5)

combobox_subcategory.bind("<<ComboboxSelected>>", update_concepts)

tk.Label(window, text="Concepto:").grid(row=2, column=0, padx=10, pady=5)
combobox_concept = ttk.Combobox(window, width=80)  # Increase the width of the combobox
combobox_concept.grid(row=2, column=1, padx=10, pady=5)

# Button to search the amount
search_button = tk.Button(window, text="Buscar monto", command=get_amount)
search_button.grid(row=3, column=0, columnspan=2, pady=20)

# Cart area with Treeview
tk.Label(window, text="Carrito:").grid(row=4, column=0, padx=10, pady=5)

# Create a Treeview for the cart display
treeview_cart = ttk.Treeview(window, columns=("Concept", "Client A", "Client B", "Client C"), show="headings")
treeview_cart.grid(row=4, column=1, padx=10, pady=5)

# Configure column headers
treeview_cart.heading("Concept", text="Concepto")
treeview_cart.heading("Client A", text="Cliente A")
treeview_cart.heading("Client B", text="Cliente B")
treeview_cart.heading("Client C", text="Cliente C")

# Adjust column sizes
treeview_cart.column("Concept", width=200)
treeview_cart.column("Client A", width=100)
treeview_cart.column("Client B", width=100)
treeview_cart.column("Client C", width=100)

# Add scrollbars
scrollbar = ttk.Scrollbar(window, orient="vertical", command=treeview_cart.yview)
treeview_cart.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(row=4, column=2, sticky="ns")

# Run the application
window.mainloop()