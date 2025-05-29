import numpy as np
def main():
    M1 = np.array([[9, 12],
                   [23, 30]])
    print("Ma trận M1:")
    print(M1)

    u = np.array([2, 1])
    print("\nVector u:")
    print(u)

    tichM1u = M1.dot(u)
    print("\nTích M1.dot(u):")
    print(tichM1u)
    print("Giải thích: M1 là ma trận 2x2, u là vector 2x1, kết quả là vector 2x1:\n"
          "[9*2 + 12*1, 23*2 + 30*1] = [30, 76]")

    tichuM1 = u.dot(M1)
    print("\nTích u.dot(M1):")
    print(tichuM1)
    print("Giải thích: u là vector 1x2, M1 là ma trận 2x2, kết quả là vector 1x2:\n"
          "[2*9 + 1*23, 2*12 + 1*30] = [41, 54]")
    print("\nTích np.dot(M1, u):")
    print(np.dot(M1, u))
    print("Giải thích: tương đương M1.dot(u), kết quả vector 2x1")

    print("\nTích np.dot(u, M1):")
    print(np.dot(u, M1))
    print("Giải thích: tương đương u.dot(M1), kết quả vector 1x2")
# Tạo ma trận zeros 5x5
    mat1 = np.zeros([5, 5])
    print("\nmat1 (zeros 5x5):")
    print(mat1)
# Tạo ma trận ones 5x5
    mat2 = np.ones([5, 5])
    print("\nmat2 (ones 5x5):")
    print(mat2)
# Tạo mat3 = mat1 + 2 * mat2
    mat3 = mat1 + 2 * mat2
    print("\nmat3 = mat1 + 2*mat2:")
    print(mat3)
# Gán mat4 = mat3 (tham chiếu)
    mat4 = mat3
# Thay đổi phần tử mat3[3][2]
    mat3[3][2] = 10
    print("\nSau khi mat3[3][2] = 10:")
    print("mat3:")
    print(mat3)
    print("mat4 (có thay đổi theo mat3 không?):")
    print(mat4)
    print("=> mat4 thay đổi cùng mat3 vì là tham chiếu")

# Tạo bản sao mat5 = copy của mat3
    mat5 = np.copy(mat3)
# Thay đổi mat3[3][2] tiếp
    mat3[3][2] = 20
    print("\nSau khi mat3[3][2] = 20:")
    print("mat3:")
    print(mat3)
    print("mat4 (tham chiếu):")
    print(mat4)
    print("mat5 (copy):")
    print(mat5)
    print("=> mat4 thay đổi cùng mat3, mat5 giữ nguyên giá trị cũ")
# Tạo ma trận empty 4x5
    mat6 = np.empty([4, 5])
    print("\nmat6 (empty 4x5) - giá trị rác trong bộ nhớ:")
    print(mat6)
# Tạo ma trận đơn vị 4x4
    mat7 = np.identity(4)
    print("\nmat7 (identity 4x4):")
    print(mat7)
# Tạo ma trận random 4x5
    try:
        mat8 = np.rand([4, 5])
    except AttributeError:
        mat8 = np.random.random([4, 5])
    print("\nmat8 (random 4x5):")
    print(mat8)

if __name__ == "__main__":
    main()
