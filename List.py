import random

# Initial list of words
initial_list = ["apple", "banana", "cherry", "date", "fig"]
target_list = ["grape", "kiwi", "lemon", "mango", "orange"]

def display_lists(current_list, target_list):
    print("\nCurrent List:", current_list)
    print("Target List:", target_list)

def check_lists(current_list, target_list):
    if current_list == target_list:
        print("Congratulations! You've transformed the list into the target list!")
        return True
    return False

def perform_operation(current_list):
    print("\nChoose an operation:")
    print("1. Append a word")
    print("2. Extend the list with another list")
    print("3. Concatenate two elements")
    print("4. Modify an element")
    print("5. Insert an element at a specific index")
    print("6. Pop an element")
    print("7. Remove a specific element")
    print("8. Sort the list (ascending)")
    print("9. Sort the list (descending)")
    print("10. View current list")
    print("0. Exit")

    choice = input("Enter the number of the operation: ")

    if choice == '1':
        word = input("Enter a word to append: ")
        current_list.append(word)
        print(f"Appended '{word}' to the list.")

    elif choice == '2':
        additional_list = input("Enter words to extend (comma separated): ").split(",")
        current_list.extend([word.strip() for word in additional_list])
        print(f"Extended list with {additional_list}.")

    elif choice == '3':
        index1 = int(input("Enter the first index to concatenate: "))
        index2 = int(input("Enter the second index to concatenate: "))
        if 0 <= index1 < len(current_list) and 0 <= index2 < len(current_list):
            concatenated_word = current_list[index1] + current_list[index2]
            current_list[index1] = concatenated_word
            current_list.pop(index2)  # Remove the second element after concatenation
            print(f"Concatenated '{current_list[index1]}' and removed the second element.")

    elif choice == '4':
        index = int(input("Enter the index of the element to modify: "))
        if 0 <= index < len(current_list):
            new_word = input("Enter the new word: ")
            current_list[index] = new_word
            print(f"Modified index {index} to '{new_word}'.")

    elif choice == '5':
        word = input("Enter the word to insert: ")
        index = int(input("Enter the index at which to insert: "))
        if 0 <= index <= len(current_list):
            current_list.insert(index, word)
            print(f"Inserted '{word}' at index {index}.")

    elif choice == '6':
        if current_list:
            popped_word = current_list.pop()
            print(f"Popped '{popped_word}' from the list.")
        else:
            print("The list is empty. Cannot pop.")

    elif choice == '7':
        word = input("Enter the word to remove: ")
        if word in current_list:
            current_list.remove(word)
            print(f"Removed '{word}' from the list.")
        else:
            print(f"'{word}' is not in the list.")

    elif choice == '8':
        current_list.sort()
        print("Sorted the list in ascending order.")

    elif choice == '9':
        current_list.sort(reverse=True)
        print("Sorted the list in descending order.")

    elif choice == '10':
        print("Current List:", current_list)

    elif choice == '0':
        print("Exiting the game.")
        return False

    else:
        print("Invalid choice. Please try again.")

    return True

def main():
    current_list = initial_list.copy()
    
    while True:
        display_lists(current_list, target_list)
        if check_lists(current_list, target_list):
            break
        if not perform_operation(current_list):
            break

if __name__ == "__main__":
    main()
