
def new_string (symbol, count):
    return symbol * count

print(new_string('!', 6))

def new_string (symbol, count = 3):
    return symbol * count

print(new_string(4))   # !!!!!!
#                 ('!')       !!!     
#                ('4')        12 

n = 10
def fib (n):
    if n in [1, 2]:
        return 1
    else:
        return fib( n - 1) + fib (n -2)

list = []
for i in range (1, n):
    list.append(fib(i))
print(list)