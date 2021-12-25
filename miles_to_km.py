from tkinter import ttk
from tkinter import *


def miles_to_km():
    miles = float(entry.get())
    km = miles * 1.609
    result.config(text=f"{km:.3f}")


# instantiate main window
window = Tk()
window.title("Miles to Km Converter")
window.config(padx=10, pady=10)

# instantiate necessary widgets
frame = ttk.Frame(window, borderwidth=5, relief="solid", padding=(5, 10))
entry = ttk.Entry(frame, width=10, justify="right", font=("Arial", 16))

miles_label = ttk.Label(
    frame, text="Miles", font=("Arial", 16), justify="center", padding=(10, 0)
)

is_equal_label = ttk.Label(
    frame, text="is equal to:", font=("Arial", 16), padding=(10, 0)
)

result = ttk.Label(frame, text="0", justify="center", font=("Arial", 16))

km_label = ttk.Label(
    frame, text="Km", font=("Arial", 16), justify="center", padding=(10, 0)
)

calculate_btn = ttk.Button(frame, text="Calculate", command=miles_to_km)

# place widgets in grid system
frame.grid(row=0, column=0, columnspan=3)
entry.grid(row=0, column=1)
miles_label.grid(row=0, column=2)
is_equal_label.grid(row=1, column=0)
result.grid(row=1, column=1)
km_label.grid(row=1, column=2)
calculate_btn.grid(row=2, column=1)

# window mainloop
window.mainloop()
