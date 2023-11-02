# File name: Assignement4b.py
# Author: Tamir Erdenebadrakh
# Description: Functional program that for memorizing game

# main program
def main():

    theList = ["horse", 14, 15.4] #the list

    for i in range(10):
        theList.append(i)

    while True:
        print("\n1. Search", "\n2. Add", "\n3. Remove",
              "\n4. Sort", "\n5. List all the elements", "\n6. Count",
              "\n7. Sum", "\n8. Exit")

        userInput = input("Enter the choice: ") #User input

        if userInput == '1':
            search_item(theList) #search
        elif userInput == '2':
            add_item(theList)   #add
        elif userInput == '3':  
            delete_item(theList)    #delete
        elif userInput == '4':
            sort_items(theList) #sort
        elif userInput == '5':
            list_items(theList) #list
        elif userInput == '6':
            count_items(theList)    #count
        elif userInput == '7':
            calculate_sum(theList) #Sum
        elif userInput == '8':
            print("Exiting the program.") #exit
            break
        else:
            print("Invalid choice. Please try again.")

def search_item(theList):   #Search option
    item = input("Enter the item to search for: ")
    if item in theList:
        print(f"{item} found in the list.")
    else:
        print(f"{item} not found in the list.")

def add_item(theList): #Add option
    item = input("Enter the item to add: ")
    theList.append(item)
    print(f"{item} added to the list.")

def delete_item(theList):   #Delete option
    item = input("Enter the item to delete: ")
    if item in theList:
        theList.remove(item)
        print(f"{item} deleted from the list.")
    else:
        print(f"{item} not found in the list.")

def sort_items(theList):    #Sort option
    theList.sort()
    print("List sorted in ascending order:", theList)

def list_items(theList): #List see option
    print("List contents:")
    for item in theList:
        print(item)

def count_items(theList): #count option
    count = len(theList)
    print(f"Total items in the list: {count}")

def calculate_sum(theList): #Sum calculater
    total = 0
    for item in theList:
        if isinstance(item, (int, float)):
            total += item
    print(f"Sum of numeric items in the list: {total}")

if __name__ == "__main__":
    main() 



