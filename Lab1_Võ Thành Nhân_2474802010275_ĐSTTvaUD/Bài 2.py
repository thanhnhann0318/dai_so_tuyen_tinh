from sympy import Symbol, solve
def main():
    x = Symbol('x')
    
    ptb2_1 = x**2 + 9*x + 8
    nghiem1 = solve(ptb2_1, dict=True)
    print("Nghiệm của phương trình x^2 + 9x + 8 = 0 (dạng dict):")
    print(nghiem1)
    
    ptb2_2 = x**2 + 1*x + 10
    nghiem2 = solve(ptb2_2, dict=True)
    print("\nNghiệm của phương trình x^2 + x + 10 = 0 (dạng dict):")
    print(nghiem2)

if __name__ == "__main__":
    main()
