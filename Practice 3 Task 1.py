#Practice 3 Task 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
def NumberChecking(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

def ListChecking(list):
    result=[]
    for i in my_list:
        if NumberChecking(i):
            result.append(i)
    return result

my_str=input("Enter your list. Use the whitespace to separate elements.: ")
my_list=my_str.split()
result=ListChecking(my_list)
if len(result)!=0:
    print(f"The entered list contains the following numbers: {ListChecking(my_list)}")
else:
    print("The entered list doesn't contain numbers!")
