import numpy as np
# Bài 1.2.1
danhsach1 = np.array([1. , 3.])
danhsach2 = np.array([5. , 7.])

danhsach = danhsach1 + danhsach2
print("Danh sach:", danhsach)

danhsach_gapdoi = 2 * danhsach
print("Danh sach gap doi:", danhsach_gapdoi)

a = danhsach*2
print("Danh sach nhan 2:", a)

b = danhsach/2
print("Danh sach chia 2:", b)

# Ghép các danh sách bằng lệnh zip
mon_hoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinhCB"]
thu_tu = [2, 3, 4, 1]
diem_so = [10, 9, 8, 7] 
anh_xa = zip(thu_tu, mon_hoc, diem_so) 
anh_xa = list(zip(thu_tu,mon_hoc,diem_so))
tap_hop = set(anh_xa)
lay_TT, lay_monhoc, lay_diem = zip(*tap_hop)
print("danh sach:", anh_xa)
print("Danh sach tap hop", tap_hop)
print("danh sach mon hochoc:", lay_monhoc)

# Bài 1.2.2
a=b=c=0
mylist =[]
execfile('d:/thucthi1.py')

# Bài 2.1
from sympy import Symbol 
x = Symbol('x')
f = x + x + x + 2
print(f)
a = Symbol('Noi')
b = Symbol('Chim')
s=3*b + 7*a 
i = a.name
y = b.name
print(s)
print(i,y)
# Bài
from sympy import Symbol 
x = Symbol('x')
y = Symbol('y')
s = x*y + y*x
p = x*(x+2*x)
print(s,p)
# BàiBài
from sympy import Symbol 
x, y = Symbol('x y')
p = (x+2)*(y+3)
print(p)
# Bài
from sympy import Symbol
x, y = Symbol('x y') 
(x + 2)*(y + 3)
p = (x+2)*(y+3) + (x+2)*(x-3)
print(p)  
# BàiBài  
from sympy import Symbol 
x, y = Symbol('x y')
p = (x+2)*(y+3)
print(p.expand())
# bài 2.2.1
from sympy import symbols, factor

x, y = symbols('x y')
bieuthuc = x**3 - y**3
print(factor(bieuthuc))

from sympy import symbols, expand
x, y = symbols('x y')
bieuthuc = (x - y)*(x**2 + x*y + y**2)
print(expand(bieuthuc))
# Bài 2.2.2
from sympy import symbols, pprint

x, y = symbols('x y')
bieuthuc = x**2 - 2*x*y + y**2
pprint(bieuthuc)

from sympy import symbols, pprint, init_printing, factor

init_printing(order='rev-lex')

x, y = symbols('x y')
bieuthuc = x**2 - 2*x*y + y**2

pprint(bieuthuc)
bieuthuc1 = factor(bieuthuc)
pprint(bieuthuc1)
# Bài 2.2.3
from sympy import Symbol

x = Symbol('x')
y = Symbol('y')

bieuthuc = x**2 - x*y + y**2
print(bieuthuc)
giatri = bieuthuc.subs({x: 3, y: 2})
print(giatri)
# Sinh viên thực hành
# Thực hành 11
from sympy import symbols, pprint

x, y = symbols('x y')

bieuthuc = x**2 - x*y + y**2
print("Biểu thức ban đầu:")
pprint(bieuthuc)
print("\nTình huống 1: Thay x = 3, y = x")
giatri = bieuthuc.subs({x: 3, y: x})

print("Biểu thức sau khi thay thế:")
pprint(giatri)
print("Giá trị kết quả:", giatri)
#Thực hành 2
from sympy import symbols, pprint


x, y = symbols('x y')
bieuthuc = x**2 - x*y + y**2
print("Biểu thức ban đầu:")
pprint(bieuthuc)
print("\nTình huống 2: Thay x = y, y = 3")
giatri = bieuthuc.subs({x: y, y: 3})

print("Biểu thức sau khi thay thế:")
pprint(giatri)
print("Giá trị kết quả:", giatri)
#Thực hành 3
#1
from sympy import Symbol
x = Symbol('x')
y = Symbol('y')

bieuthuc = x**2 + y  
giatri = bieuthuc.subs({y: x}).subs({x: 3})
print(giatri)
#2
from sympy import Symbol, simplify

x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x - x*y + y*y
print(bieuthuc) 
bieuthuc_moi = bieuthuc.subs({x: 1 - y})
print(bieuthuc_moi)
#3 
from sympy import Symbol, sin, cos, simplify

x = Symbol('x')
y = Symbol('y')
bt = sin(x)*cos(y) + cos(x)*sin(y)
bt_moi = simplify(bt)
print(bt_moi)















