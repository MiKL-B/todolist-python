import os
import sys
from sys import platform
import time
import pickle
from rich.table import Table
from rich.console import Console

import task


class App:
    def __init__(self):
        self._task_list = []


    def main(self):
        self.display_menu()


    def display_title(self):
        os.system('title Todolist-Python')
        print("Welcome in the Todolist-Python")


    # functions menu

    def display_menu(self):
        self.clear_console()
        self.display_title()
        self._task_list = self.load()
        print()
        self.display_task_list()
        print()
        print("Command for the tasks:")

        if len(self._task_list) > 0:
            print("1 Create")
            print("2 Read")
            print("3 Update")
            print("4 Delete")
            print("5 Quit")
        else:
            print("1 Create")
            print("2 Quit")
        print()
        self.choice_menu()


    def choice_menu(self):
        choice = input("Input a command: ")
        if len(self._task_list) > 0:
            if choice == "1":
                self.create()
            elif choice == "2":
                self.read()
            elif choice == "3":
                self.update()
            elif choice == "4":
                self.delete()
            elif choice == "5":
                self.quit()
            else:
                self.display_menu()
        else:
            if choice == "1":
                self.create()
            elif choice == "2":
                self.quit()
            else:
                self.display_menu()


    # functions miscellaneous

    def clear_console(self):
        if platform == "linux":  # Linux
            os.system("clear")
        elif platform == "darwin":  # Mac
            os.system("clear")
        elif platform == "win32":  # Windows
            os.system("cls")


    def quit(self):
        sys.exit()


    # functions tasks

    def display_task_list(self):
        if len(self._task_list) > 0:
            table = Table(title="Task list")
            table.add_column("index")
            table.add_column("name")
            table.add_column("description")
            table.add_column("status")
            for index, item in enumerate(self._task_list):
                table.add_row(str(item._index),item._name,item._description,item._status)

            console = Console()
            console.print(table)
        else:
            print("Task list empty!")


    def create(self):
        i_index = 0
        for index, item in enumerate(self._task_list):
            i_index = item._index
        new_task = task.Task(i_index+1)
        self._task_list.append(new_task)
        self.save(self._task_list)
        print("Task created!")
        time.sleep(2)
        self.display_menu()


    def read(self):
        self.clear_console()
        self.display_task_list()
        print("Which one do you want to read?")
        print("R return")
        choice = input("Choose a task: ").lower()
        for index, item in enumerate(self._task_list):
            if choice == str(item._index):
                self.display_task(item)
            elif choice == "r":
                self.display_menu()
        else:
            self.read()


    def display_task(self,item):
        self.clear_console()
        print(item._index)
        print(item._name)
        print()
        print("R Return")
        print()
        choice = input("Input a command: ").lower()
        if choice == "r":
            self.display_menu()
        else:
            self.display_task(item)


    def update(self):
        self.clear_console()
        self.display_task_list()
        print("Which one do you want to update?")
        print("R return")
        choice = input("Choose a task: ").lower()
        for index, item in enumerate(self._task_list):
            if choice == str(item._index):
                self.update_task(item)
            elif choice == "r":
                self.display_menu()
        else:
            self.update()


    def update_task(self,item):
        self.clear_console()
        choice_name = input(f"Choose a new name for {item._name}: ")
        item._name = choice_name
        print("Name changed!")
        time.sleep(2)

        choice_description = input(f"Choose a new description for {item._description}: ")
        item._description = choice_description
        print("Description changed!")
        time.sleep(2)

        print()
        print("1 Todo")
        print("2 In progress")
        print("3 Finished")
        choice_status = input(f"Choose a new status: ")
        if choice_status == "1":
            status = "Todo"
        elif choice_status == "2":
            status = "In progress"
        elif choice_status == "3":
            status = "Finished"
        else:
            status = ""

        item._status = status
        print("Status changed!")
        self.save(self._task_list)


    def delete(self):
        self.clear_console()
        self.display_task_list()
        print("Which one do you want to delete?")
        print("R return")
        choice = input("Choose a task: ").lower()
        for index, item in enumerate(self._task_list):
            if choice == str(item._index):
                self.delete_task(item)
            elif choice == "r":
                self.display_menu()
        else:
            self.delete()


    def delete_task(self,item):
        self.clear_console()
        self._task_list.remove(item)
        self.save(self._task_list)
        print("Task removed!")
        time.sleep(2)
        self.display_menu()


    # functions data

    def save(self,data):
        pickle.dump(data, open("save/SaveFile","wb"))


    def load(self):
        if self.is_any_data():
            data = pickle.load(open("save/SaveFile","rb"))
        else:
            data = []
        return data


    def is_any_data(self):
        path = "save/SaveFile"
        is_data_exist = os.path.exists(path)
        return is_data_exist
