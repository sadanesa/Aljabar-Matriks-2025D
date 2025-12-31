#Fungsi input
def determinan(A):
    n = len(A)
    # ukuran matriks
    # Determinan 1x1
    if n == 1:
        return A[0][0]

    # Determinan 2x2: ad - bc
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]

    # Determinan 3x3: Metode Sarrus
    if n == 3:
        # metode sarrus: (aek + bfg + cdh) - (ceg + bdi + afh)
        a, b, c = A[0]
        d, e, f = A[1]
        g, h, i = A[2]

        diagonal_utama = a*e*i + b*f*g + c*d*h
        diagonal_samping = c*e*g + b*d*i + a*f*h

        return diagonal_utama - diagonal_samping

    # ordo tidak lebih dari 3
    raise ValueError("Hanya mendukung matriks 1x1, 2x2, dan 3x3.")


def minor(A, i, j):
    # Menghilangkan baris i dan kolom j dari A
    return [row[:j] + row[j + 1:] for idx, row in enumerate(A) if idx != i]


def cofaktor(A):
    # Membuat matriks kofaktor menggunakan tanda (+/-)
    return [[(-1) ** (i + j) * determinan(minor(A, i, j))
             for j in range(len(A))]
            for i in range(len(A))]


def transpose(A):
    # Menukar baris menjadi kolom
    return [list(r) for r in zip(*A)]


def inverse(A):
    # Hitung determinan
    det = determinan(A)

    # Jika determinan nol maka matriks tidak punya invers
    if det == 0:
        return None

    # Menggunakan rumus: A^-1 = (1/det) * adjoint(A)
    adj = transpose(cofaktor(A))
    return [[elem / det for elem in row] for row in adj]


#Output

print("Invers Matriks (Metode Adjoin)")

n = int(input("Masukkan ordo matriks (2 atau 3): "))
A = []

print("Masukkan elemen matriks:")
for i in range(n):
    # Input satu baris matriks dalam bentuk angka float
    A.append(list(map(float, input(f"Baris {i + 1}: ").split())))

invA = inverse(A)

print("\nMatriks A:")
for r in A:
    print(r)

if invA:
    print("\nInvers A:")
    for r in invA:
        print(r)
else:
    print("\nMatriks tidak memiliki invers, karena det = 0")

input("\nTekan ENTER untuk keluar...")

