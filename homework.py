import os
import json


def clear_terminal():
    os.system('cls')  # This clears the terminal screen


def print_green(text):
    print("\033[32m" + text + "\033[0m")

def name_input():
    f_name = input("Please input your first name: ")
    last_name = input("Please input your last name: ")
    user_name = {}
    user_name["first_name"] = f_name
    user_name["last_name"] = last_name
    return user_name

def dump_json(data_dict):
    file_path = "user_name.json"    
    with open(file_path, "w") as json_file:
        json.dump(data_dict, json_file)    
    print_green(f"User data dumped into JSON file: {file_path}")    
    return file_path

def read_json(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    print_green(f"{file_path} contains following data")
    for key,value in data.items():
        print_green(f"{key} : {value}")
        

if __name__ =='__main__':
    clear_terminal()
    user_input = name_input()
    json_file = dump_json(user_input)
    read_json(json_file)