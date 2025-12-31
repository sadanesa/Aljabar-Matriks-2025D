import tkinter as tk
from tkinter import messagebox

def hitung_dot():
    try:
        x1 = float(entry_x1.get())
        y1 = float(entry_y1.get())
        x2 = float(entry_x2.get())
        y2 = float(entry_y2.get())

        dot = x1*x2 + y1*y2
        hasil_var.set(f"Dot Product = {dot}")

    except ValueError:
        messagebox.showerror("Error", "Input harus berupa angka!")

root = tk.Tk()
root.title("Perkalian Vektor 2 Dimensi")
root.geometry("370x300")

judul = tk.Label(root, text="Anisa_027, Alfathkul_103, Nasywa_235", font=("Arial", 12, "bold"))
judul.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Vektor A").grid(row=0, column=0, columnspan=2, pady=5)
tk.Label(frame, text="x₁:").grid(row=1, column=0)
entry_x1 = tk.Entry(frame)
entry_x1.grid(row=1, column=1)

tk.Label(frame, text="y₁:").grid(row=2, column=0)
entry_y1 = tk.Entry(frame)
entry_y1.grid(row=2, column=1)

tk.Label(frame, text="Vektor B").grid(row=3, column=0, columnspan=2, pady=5)
tk.Label(frame, text="x₂:").grid(row=4, column=0)
entry_x2 = tk.Entry(frame)
entry_x2.grid(row=4, column=1)

tk.Label(frame, text="y₂:").grid(row=5, column=0)
entry_y2 = tk.Entry(frame)
entry_y2.grid(row=5, column=1)

tombol = tk.Button(root, text="Hitung Menggunakan Metode Dot Product", command=hitung_dot)
tombol.pack(pady=10)

hasil_var = tk.StringVar()
hasil_label = tk.Label(root, textvariable=hasil_var, font=("Arial", 11, "bold"))
hasil_label.pack(pady=5)

root.mainloop()
