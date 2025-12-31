import numpy as np

def cramer_solver(A, B):
    """
    Menyelesaikan sistem persamaan linear AX = B menggunakan metode Cramer
    
    Parameters:
    A : matriks koefisien (n x n)
    B : vektor konstanta (n x 1)
    
    Returns:
    X : solusi sistem persamaan
    """
    # Cek apakah matriks A persegi
    if A.shape[0] != A.shape[1]:
        print('Matriks A harus persegi!!')
    
    # Cek apakah dimensi A dan B sesuai
    if A.shape[0] != B.shape[0]:
        print('Dimensi matriks A dan vektor B tidak sesuai!!')
    
    n = A.shape[0]
    det_A = np.linalg.det(A)
    
    # Cek determinan tidak nol
    if abs(det_A) < 1e-10:
        print("Determinan matriks koefisien mendekati nol, metode Cramer tidak berlaku")
    
    # Hitung solusi untuk setiap variabel
    X = np.zeros(n)
    
    for i in range(n):
        # Buat matriks Ai dengan mengganti kolom ke-i dengan B
        Ai = A.copy()
        Ai[:, i] = B.flatten()
        
        # Hitung determinan matriks Ai
        det_Ai = np.linalg.det(Ai)
        
        # Hitung solusi xi
        X[i] = det_Ai / det_A
    
    return X

def main():
    '''Contoh penggunaan
        3w + x + 7y + 9z = 4
        w + x + 4y + 4z = 7
        -w - 2x + 0 - 3z = 0
        -2w - 1x - 4y - 6z = 6
                    '''
    matrix_A = np.array([[3, 1, 7, 9],
                         [1, 1, 4, 4],
                         [-1, -2, 0, -3],
                         [-2, -1, -4, -6]], dtype=float)
    
    vector_B = np.array([[4],
                         [7],
                         [0],
                         [6]], dtype=float)
    
    print("Matriks A:")
    print(matrix_A)
    print("\nVektor B:")
    print(vector_B)
    print()
    
    try:
        X = cramer_solver(matrix_A, vector_B)
        print("\nSolusi:")
        for i, sol in enumerate(X):
            print(f"x{i+1} = {sol:.4f}")
    except Exception as e:
        print(f"Error: {e}")

main()