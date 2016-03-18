def main():
    minimum = int(input("Min: "))
    maximum = int(input("Max: "))
    print_table(minimum,maximum)


def print_table(a,b):
    print(format("C", ">5s"), format("F", ">8s"))
    print(format("", "=>6s"), format("", "=>8s"),sep='')
    current_temp = a
    while  current_temp <= b:
        c = 9/5*current_temp+32
        print_1_row(current_temp,c)
        current_temp += 1

def print_1_row(a,b):
    print(format(a, '5d'), format(b, '8.1f'))
    
main()
