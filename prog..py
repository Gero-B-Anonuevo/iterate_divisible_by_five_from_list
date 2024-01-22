#pseudocode

#accept numbers
list_of_numbers = [60, 43, 75, 44, 53, 90]
#def function or for loop range
def divisible_by_5(numberlist):
    print("Given list: ", numberlist)
    print("Divisible by 5")
    for divisible in range(numberlist):
        if divisible%5 == 0:
            print(divisible)
#print results
print (divisible_by_5(list_of_numbers))