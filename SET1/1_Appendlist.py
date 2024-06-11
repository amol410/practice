my_list=[]

def append_to_list(element):
    my_list.append(element)
    print(f"element '{element}'has been added to the list ")
    print(f"Current list: {my_list}" )

def main():
    while True:
        element = input("Enter element you want to append :- ")
        if element.lower() == 'exit':
            print("exiting the program")
            break
        append_to_list(element)

main() 


# Simple Way 
list = []

while True:
    element = input("enter the element :- ")
    if element.lower() == 'exit':
        break
    int(element)

    list.append(element)

    print(list)  