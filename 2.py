def add_item(list):
    item = input("please enter your item")
    shopping_list.append(item)

def remove_item(list):
    remove = input("Enter the item to remove")
    if remove in list:
            list.remove(remove)

def print_list(list):
    for index, item in enumerate(list, start=1):
        print(f"{index}. {item}")

shopping_list=[]
my_list = ["apple", "banana", "orange", "pear"]
print_list(my_list)