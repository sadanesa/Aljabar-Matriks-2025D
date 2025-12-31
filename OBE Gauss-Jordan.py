# dibuat oleh kelompok Tim Nas
#nama : dicky alviano 
#nim : 25031554227




A = [
    [1,  2, -1, 3],
    [2, -1,  3, 1],
    [-1, 1,  2, 4]
]


def print_matrix(M):
    for baris in M:
        baris_1 = []
        for x in baris:
            if float(x).is_integer():
                baris_1.append(f"{int(x):7}")
            else:
                baris_1.append(f"{x:7.3f}")
        print(baris_1)
    print()

def gauss_jordan(mat):
    n = len(mat)

    for i in range(n):

        if mat[i][i] == 0:
            for k in range(i+1, n):
                if mat[k][i] != 0:
                    mat[i], mat[k] = mat[k], mat[i]
                    break

        pivot = mat[i][i]
        for j in range(i, n+1):
            mat[i][j] /= pivot

        for k in range(n):
            if k != i:
                faktor = mat[k][i]
                for j in range(i, n+1):
                    mat[k][j] -= faktor * mat[i][j]

    return mat

hasil = gauss_jordan(A)
print_matrix(hasil)

x = hasil[0][3]
y = hasil [1][3]
z = hasil [2][3]

print ("x = ", int(x))
print ("y =", int(y))
print ("z = ", int(z))

