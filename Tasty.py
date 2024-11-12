#!/usr/bin/env  python3

import sys
import json
import os

class Tasty:
    """
    Tasty class.
    :param tasks: the user tasks
    :param important_tasks: the important user tasks
    :param complete: the completed tasks
    :param unfinished: the unfinished tasks
    :param trash: the user trash
    :param version: the Tasty version
    :param save_file: the Tasty save file
    """

    # make sure to do an __init__ method

    def __init__(self):
        self.needs_saving = False
        self.save_file = "saved_data.json"
        self.tasks = {}
        self.complete = 0
        self.unfinished = 0
        # starting up
        self.clear()
        print('Welcome to Tasty. Loading your tasks...')
        self.load_tasks(self.save_file)
        self.display_tasks()

    def display_tasks(self):
        if self.tasks: 
            print('Tasks:')
            for task_name, status in self.tasks.items():
                print("- ", task_name, status)
            print(f"You have {self.complete} complete tasks. BUT You have {self.unfinished} unfinished tasks.")
        else:
            print("You have no tasks.")

    def remove_task(self, task_name):
        if task_name in self.tasks:
            del self.tasks[task_name]
            self.needs_saving = True
        else:
            print("Task not found.")

    def add_task(self, task_name):
        """
        Add a new task to the user tasks.
        """
        if task_name not in self.tasks:
            self.tasks[task_name] = "not yet"
            self.unfinished += 1
            self.needs_saving = True
        else:
            print("Task already added.")

    def prompt_user(self, prompt):
        line = input(prompt)
        #print(line)
        while not line:
            line = input(prompt)
        words = line.split()
        #print(words)
        command = words[0]
        #print(command)
        rest = words[1:]
        rest = " ".join(rest)
        #print(rest)
        return command, rest

    def save_tasks(self, filename):
        with open(filename, "w") as fp:
            dict_to_save = { "tasks": self.tasks}
            json.dump(dict_to_save,fp)
            self.needs_saving = False


    def load_tasks(self, filename):
        with open(filename) as json_file:
            loaded_dicts = json.load(json_file)
            self.tasks = loaded_dicts['tasks']
            self.update_counts()
            self.needs_saving = False

    def update_counts(self):
        for task_name, status in self.tasks.items():
            if status == 'not yet':
                self.unfinished += 1
            if status == 'completed':
                self.complete += 1
        
    def complete_task(self, task_name):
        if task_name in self.tasks:
            self.tasks[task_name] = 'completed'
            self.complete += 1
            self.unfinished -= 1
            self.needs_saving = True
        else:
            print("Task not found.")

    def unfinish_task(self, task_name):
        if task_name in self.tasks:
            self.tasks[task_name] = 'not yet'
            self.complete -= 1
            self.unfinished += 1
            self.needs_saving = True
        else:
            print("Task not found.")

    def help(self):
        """
        Display a help message.
        """
        print("Tasty Help ")
        print("============================================================================")
        print("help                     ->        display this message")
        print("tasks                    ->        display all your tasks")
        print("trash                    ->        display the content of the trash")
        print("new <task>               ->        add a new task")
        print("remove <task>            ->        add a task to the trash")
        print("complete <task>          ->        complete a task")
        print("unfinish <task>          ->        unfinish a task")
        print("recover <task>           ->        recover a removed task")
        print("destroy <task>           ->        remove a task from the trash")
        print("advancement              ->        see the tasks advancement")
        print("exit                     ->        exit Tasty")
        print("save                     ->        save your current tasks")
        print("load                     ->        load a save file")
        print("clear                    ->        clear the screen")
        
    def license(self):
        """
        Display the MIT License terms for Tasty.
        """
        print("""
Copyright (c) 2024 Tasty

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
        """)
       
    def exit_program(self):
        if self.needs_saving == True:
            self.save_tasks(self.save_file)
            print("*** Saving your work.")
        print('Bye, Felicia.')
        exit()

    def clear(self):
        os.system('clear')

if __name__ == "__main__":
    tasty = Tasty()
    # tasty.tasks == {}
    # tasty.help()
    print('Type "help" for commands')
    ## HACKY tests, used before we had a way to get the whole line
    ## split into two parts, Command and Rest (or task_name)
    # tasty.tasks["foo"] = "incomplete"
    # tasty.add_task("Buy Milk")
    #tasty.add_task("do something")

    #tasty.remove_task("Buy Milk")

    while True:
        command, task_name = tasty.prompt_user("Tasty> ")
        if command == "exit":
            tasty.exit_program() # exit the program, how would you do this?
            #break
            # or
            #exit()
        elif command == "help":
            tasty.help()
        elif command == "clear":
            tasty.clear()
        elif command == "license":
            tasty.license()
        elif command == "tasks":
            tasty.display_tasks()
        elif command == 'new':
            tasty.add_task(task_name)
        elif command == 'remove':
            tasty.remove_task(task_name)
        elif command == 'complete':
            tasty.complete_task(task_name)
        elif command == 'unfinish':
            tasty.unfinish_task(task_name)
        elif command == 'save':
            tasty.save_tasks(tasty.save_file)
        elif command == 'load':
            tasty.load_tasks(tasty.save_file)
        else:
            print("Unknown command:", command, ' : ', task_name)
    # exit()