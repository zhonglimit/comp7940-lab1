def print_factor(x):
    factorys = []
    for i in range(1,x+1):
        if x % i == 0 : factorys.append(i)
    # print(factorys)
    return factorys

def print_factors(num_list):
    factorysKeyValue = {}
    for i in num_list:
        factorys = print_factor(i)
        factorysKeyValue[i] = factorys
        
    # print(factorys)
    return factorysKeyValue

def main():

    print("Hello World")
    x = 52633
    factory = print_factor(x)
    print(factory)
    l = [52633, 8137, 1024, 999]
    factorys = print_factors(l)
    print(factorys)


if __name__ == '__main__':
    main()