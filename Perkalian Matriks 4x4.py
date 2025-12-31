import numpy as np
def baca_matriks(nama_matriks, baris, kolom):
    total_elemen = baris * kolom
    print(f"\nMasukkan {total_elemen} angka untuk matriks {nama_matriks} ({baris}x{kolom})")
    print("Tiap angka dipisah dengan spasi:")
    while True:
        try:
            data = list(map(float, input().split()))
            if len(data) == total_elemen:
                return np.array(data).reshape(baris, kolom)
            else:
                print(f"Error: harus tepat {total_elemen} angka! Silakan coba lagi.")
        except ValueError:
            print("Error: Masukkan angka yang valid (bilangan atau desimal).")
def dapatkan_dimensi():
    while True:
        try:
            print("\n--- Masukkan Dimensi Matriks A ---")
            baris_A = int(input("Jumlah baris matriks A: "))
            kolom_A = int(input("Jumlah kolom matriks A: "))
            print("\n--- Masukkan Dimensi Matriks B ---")
            baris_B = int(input("Jumlah baris matriks B: "))
            kolom_B = int(input("Jumlah kolom matriks B: "))
            if baris_A <= 0 or kolom_A <= 0 or baris_B <= 0 or kolom_B <= 0:
                print("\nError: Dimensi matriks harus bilangan bulat positif.")
                continue           
            if kolom_A != baris_B:
                print("\n========================================================")
                print("Error: Perkalian matriks tidak memungkinkan.")
                print(f"Jumlah kolom matriks A ({kolom_A}) harus sama dengan jumlah baris matriks B ({baris_B}).")
                print("========================================================")
                continue  
            return baris_A, kolom_A, baris_B, kolom_B
        except ValueError:
            print("\nError: Masukkan angka yang valid untuk dimensi.")
            continue        
def main():
    print("=== PROGRAM PERKALIAN MATRIKS (m x n) * (n x p) ===")  
    while True:
        baris_A, kolom_A, baris_B, kolom_B = dapatkan_dimensi()       
        A = baca_matriks("A", baris_A, kolom_A)
        B = baca_matriks("B", baris_B, kolom_B)
        C = np.dot(A, B)       
        print("\nMatriks A:")
        print(A)
        print("\nMatriks B:")
        print(B)
        print(f"\nHasil C = A × B (Ukuran: {C.shape[0]}x{C.shape[1]}):")
        print(C)        
        while True:
            ulang = input("\nApakah Anda ingin menghitung perkalian matriks lagi? (ya/tidak): ").lower()
            if ulang in ["ya", "tidak"]:
                break
            else:
                print("Input tidak valid. Mohon masukkan 'ya' atau 'tidak'.")
        
        if ulang == "tidak":
            print("Terima kasih telah menggunakan program ini!")
            break
if __name__ == "__main__":
    main()