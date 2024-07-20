def is_sublist(sublist, main_list):
    # Get the length of the sublist
    sublist_length = len(sublist)
    
    # Iterate over the main list
    for i in range(len(main_list) - sublist_length + 1):
        # Check if the current sublist matches the given sublist
        if main_list[i:i+sublist_length] == sublist:
            return True
    
    return False

# Example usage
main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sublist1 = [4, 5, 6]
sublist2 = [6, 7, 8, 9, 10]

print("Main List:", main_list)

print("Sublist 1:", sublist1)
print("Is Sublist 1 a sublist of Main List?", is_sublist(sublist1, main_list))

print("Sublist 2:", sublist2)
print("Is Sublist 2 a sublist of Main List?", is_sublist(sublist2, main_list))



#or 

# Example usage
main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sublist1 = [4, 5, 6]
sublist2 = [6, 7, 8, 9, 10]

print("Main List:", main_list)

# Check if sublist1 is a sublist of main_list
is_sublist1 = False
sublist1_length = len(sublist1)
for i in range(len(main_list) - sublist1_length + 1):
    if main_list[i:i+sublist1_length] == sublist1:
        is_sublist1 = True
        break

print("Sublist 1:", sublist1)
print("Is Sublist 1 a sublist of Main List?", is_sublist1)

# Check if sublist2 is a sublist of main_list
is_sublist2 = False
sublist2_length = len(sublist2)
for i in range(len(main_list) - sublist2_length + 1):
    if main_list[i:i+sublist2_length] == sublist2:
        is_sublist2 = True
        break

print("Sublist 2:", sublist2)
print("Is Sublist 2 a sublist of Main List?", is_sublist2)

