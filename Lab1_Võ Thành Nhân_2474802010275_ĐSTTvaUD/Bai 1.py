from sympy import Symbol, solve
def main():
    x = Symbol('x')
    
    bieuthuc1 = x + 3 - 5
    nghiem1 = solve(bieuthuc1)
    print("Nghiệm phương trình x + 3 = 5:")
    print(nghiem1)       
    print("Nghiệm đầu tiên:", nghiem1[0])  

    bieuthuc2 = x**2 + 3 - 5
    nghiem2 = solve(bieuthuc2)
    print("\nNghiệm phương trình x^2 + 3 = 5:")
    print(nghiem2)
    print("Nghiệm thứ nhất:", nghiem2[0])
    print("Nghiệm thứ hai:", nghiem2[1])

if __name__ == "__main__":
    main()
