from sympy import Symbol, solve
def main():
    x = Symbol('x')
    y = Symbol('y')
    pt1 = 2*x + 3*y - 12
    pt2 = 3*x - 2*y - 5

    nghiem_list = solve((pt1, pt2), dict=True)
    print("Nghiệm của hệ phương trình:")
    print(nghiem_list)
    nghiem = nghiem_list[0]
    val_pt1 = pt1.subs({x: nghiem[x], y: nghiem[y]})
    val_pt2 = pt2.subs({x: nghiem[x], y: nghiem[y]})

    print("\nGiá trị biểu thức pt1 sau khi thay nghiệm:", val_pt1)
    print("Giá trị biểu thức pt2 sau khi thay nghiệm:", val_pt2)

if __name__ == "__main__":
    main()
