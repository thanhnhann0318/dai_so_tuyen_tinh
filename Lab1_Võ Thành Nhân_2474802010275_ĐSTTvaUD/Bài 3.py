from sympy import Symbol, solve, pprint
def main():
    x = Symbol('x')
    a = Symbol('a')
    b = Symbol('b')
    c = Symbol('c')
    ptb2 = a*x**2 + b*x + c
    
    nghiem = solve(ptb2, x, dict=True)
    print("Nghiệm tổng quát của phương trình a*x^2 + b*x + c = 0:")
    for i, ngh in enumerate(nghiem, 1):
        print(f"Nghiệm thứ {i}:")
        pprint(ngh)  
    
if __name__ == "__main__":
    main()


