import tkinter as tk
from tkinter import messagebox

def hitung_penjumlahan():
    try:
        x1 = float(entry_x1.get())
        y1 = float(entry_y1.get())
        z1 = float(entry_z1.get())

        x2 = float(entry_x2.get())
        y2 = float(entry_y2.get())
        z2 = float(entry_z2.get())

        hasil_x = x1 + x2
        hasil_y = y1 + y2
        hasil_z = z1 + z2

        label_hasil.config(text=f"Hasil: ({hasil_x}, {hasil_y}, {hasil_z})")

    except ValueError:
        messagebox.showerror("Error", "Semua input harus berupa angka!")

root = tk.Tk()
root.title("Penjumlahan Vektor 3 Dimensi")
root.geometry("380x330")

title = tk.Label(root, text="Anisa_027, Alfathkul_103, Nasywa_235", font=("Arial", 14, "bold"))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Vektor A").grid(row=0, column=0, columnspan=2)

tk.Label(frame, text="Ax :").grid(row=1, column=0, sticky="e")
entry_x1 = tk.Entry(frame)
entry_x1.grid(row=1, column=1)

tk.Label(frame, text="Ay :").grid(row=2, column=0, sticky="e")
entry_y1 = tk.Entry(frame)
entry_y1.grid(row=2, column=1)

tk.Label(frame, text="Az :").grid(row=3, column=0, sticky="e")
entry_z1 = tk.Entry(frame)
entry_z1.grid(row=3, column=1)

tk.Label(frame, text="Vektor B").grid(row=4, column=0, columnspan=2, pady=(10,0))

tk.Label(frame, text="Bx :").grid(row=5, column=0, sticky="e")
entry_x2 = tk.Entry(frame)
entry_x2.grid(row=5, column=1)

tk.Label(frame, text="By :").grid(row=6, column=0, sticky="e")
entry_y2 = tk.Entry(frame)
entry_y2.grid(row=6, column=1)

tk.Label(frame, text="Bz :").grid(row=7, column=0, sticky="e")
entry_z2 = tk.Entry(frame)
entry_z2.grid(row=7, column=1)

btn_hitung = tk.Button(root, text="Hitung Penjumlahan", command=hitung_penjumlahan)
btn_hitung.pack(pady=10)

label_hasil = tk.Label(root, text="Hasil: (  ,  ,  )", font=("Arial", 12))
label_hasil.pack()

root.mainloop()
