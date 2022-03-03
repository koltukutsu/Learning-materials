import json
import os
from sys import exit as sys_exit

def main() -> None:
    def load_data(file_name:str) -> dict:
        with open(file_name, "r") as bought_file:
            bought = json.load(bought_file)
            return bought
        
        
    def save_data(data:dict, file_name:str) -> None:
        with open(file_name, "w") as json_file:
            json.dump(data, json_file) 


    def print_data(data:dict) -> None:
        print()
        if data:
            for class_name, amount in data.items():
                print(f"{class_name}: {amount}")
            print()
        else:
            print("No data is put yet!")
            
    def menu() -> int:
        menu_display: str
        choice: int
        
        menu_display = """
        1-Add new item
        2-Change the item condition
        3-Exit
        """
        print(menu_display)
        choice = int(input("Choice: "))
        
        return choice


    bought: dict
    file_name: str
    add_or_remove: int
    amount:int
    choice:int
    
    bought = None
    choice = 0    
    file_name = "./bought.json"    
    
    if not os.path.isfile(file_name):
        with open(file_name, "w") as json_file:
            json_file.write("{}") # puts {} so that when the file is read, an empty json is returned

    while choice != 3:
        bought = load_data(file_name)
        print_data(bought)
        
        choice = menu()
        if choice == 1:
                item = str(input("What is the item class to be initiated: "))
                if item in bought.keys():
                    print("The class is already initiated!")
                else:
                    try:
                        amount = int(input("How many is bought: "))
                    except ValueError:
                        print("You have to type a number")
                    else:
                        bought[item] = amount
        
        elif choice == 2:
                print_data(bought)
                item = str(input("What is the item class to be changed: "))
                if item in bought.keys():
                    print("1-Add or 2-Remove: ") 
                    add_or_remove = int(input())
                    try:
                        amount = int(input("Amount: "))
                    except ValueError:
                        print("You have to type a number")
                    else:
                        if add_or_remove == 1:
                            bought[item] += amount
                        elif add_or_remove ==2:
                            bought[item] -= amount
                else:
                    print("Invalid class")
        
        save_data(bought, file_name)
    sys_exit(0)
    
if __name__ == "__main__":
    main()