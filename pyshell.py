import os, re
import os.path
import random
content = ""

settings ={

    "userName": "Daniel",
    "defaultBrowser": "firefox",
    "process": ["brave", "OUTLOOK", "firefox"],
    "automaticEmptyCdParam": "on"

}

folders = {
    "userName": "Daniel",
    "c": "C:\\",
    "d": "D:\\",
    "i": "I:\\",
    "desktop": "C:\\Users\\Daniel\\Desktop",
    "downloads": "C:\\Users\\Daniel\\Downloads",
    "documents": "C:\\Users\\Daniel\\Documents",
    "pictures": "C:\\Users\\Daniel\\Pictures",
    "sales": "I:\\Comercial\\02-Ventas\\01- Proyectos",
    "quotations": "I:\\Comercial\\01-Presupuestos\\01-Proyectos\\01-En Curso",
    "standards": "I:\\Documentacion Tecnica\\General\\SEGURIDAD\\01.NORMAS",
    "packinglist": "I:\\Comercial\\11-Packing List",
    "plates": "I:\\Documentacion Tecnica\\General\\Placa CE",
    "software": "I:\\Documentacion Tecnica\\Programas y software",
    "ppe": "I:\\Prevencion Riesgos Laborales"
}

user_name = settings["userName"]

# here list var for here functions
here_var =[]



# Command functions
# Remember, Python 3 Does not admit  function overload.

def ps(content_list):
    os.system("powershell.exe")

def show(content_list):

    if len(content_list) > 1:

        content_list.pop(0)
        os.system("dir "+content_list[0])

    elif len(content_list) <= 1:
        os.system("dir")

    else:
        pass


def go(match):
    content = os.listdir()
    state = False
    pattern = match  # HERE IS THE PROBLEM, MATCHING ONLY THE BEGINNING OF THE STRING
    for j in content:
        coincidence = re.search(pattern, j)
        if coincidence:
            print(f"moving to {j}")
            try:
                os.chdir(j)
            except NotADirectoryError:
                print("NotADirectoryError: That's not a directory!!")
            finally:
                state = True
                break

    if not state:
        print("No-matches...")


def cd(match):
    os.chdir(match)


def cdu():
    global user_name
    os.chdir("C:/Users/"+user_name)


def dir_fun(match):

    global folders
    print("moving to "+match)
    try:
        os.chdir(folders[match])
    except FileNotFoundError:
        print(f"FileNotFoundError: Route or file not found '{folders[match]}'")


def google(content_list):
    global settings
    browser = settings["defaultBrowser"]
    search_string = f"start {browser} www.google.com/search?q="

    if len(content_list) > 1:

        print(content_list)
        content_list.pop(0)
        print(content_list)

        for h in content_list:

            search_string = search_string+h+"+"

        try:
            os.system(search_string)

        except TypeError:

            print("this is a type error... please proceed")

    elif len(content_list) == 1:
        os.system(f"start {browser} www.google.com")

    else:
        pass


def search(match):
    directory = os.listdir()
    pattern = r'' + match  # Using search() will help. / also It accepts REGEX
    counter = 0
    print(f"Searching for: {pattern}")

    for j in directory:
        coincidence = re.search(pattern, j, flags=0)
        format_string = f"{counter}. {j} size: {os.path.getsize(j)} time: {os.path.getatime(j)} "
        if coincidence:
            if os.path.isdir(j):
                format_string= format_string + "type: Directory"
                print(format_string)
            else:
                format_string = format_string + "type: File"
                print(format_string)
        counter += 1


def sortedT():

    # Show a directory content according the time of each file or directory - from the oldest ones to the newest
    directory = os.listdir(os.getcwd())
    counter = 0
    sorted_time_list = []
    comp_dir = {}
    sorted_index = 0
    keys_list = []
    value_list = []

    # it lists the time of the different files and directories.

    for j in directory:
        comp_dir[j] = os.path.getatime(j)
        sorted_time_list.append(os.path.getatime(j))

    # Once get the time values of each file or directory, it sorts them and reverse to get from
    # the oldest ones to the newest ones.
    del directory
    sorted_time_list.sort()
    sorted_time_list.reverse()  # From the most recent values to the oldest ones.

    # It transforms the dictionary list of values and key into a common list.
    # The list derived from .values() .keys() methods are not compatible with common list methods.

    for i in comp_dir.values():
        value_list.append(i)
    for i in comp_dir.keys():
        keys_list.append(i)
    del comp_dir
    # It uses the index of the sorted time list (sorted_time_list) to compare them with the value list
    # and know exactly which key (file) it corresponds with.
    # sorted_index gets the corresponding position of time value in value_list (non-sorted list). The same index
    # is shared by the corresponding key in key_list, remember both list come from the same dictionary, comp_dir so
    # key order in key_list corresponds to value order in value_list. So identifying to index of the value in value_list
    # it is possible to know the index and position of the key that corresponds with.

    for j in sorted_time_list:
        sorted_index = value_list.index(j)
        format_string = f"{counter}. {keys_list[sorted_index]} size: {os.path.getsize(keys_list[sorted_index])} time: {j}"

        # it identifies if file or directory it is really a file or a directory...

        if os.path.isdir(keys_list[sorted_index]):
            format_string = format_string + "type: Directory"
            print(format_string)
        else:
            format_string = format_string + "type: File"
            print(format_string)
        counter += 1

        print("\n")


def sortedt():

    # Show a directory content according the time of each file or directory - from the newest ones to the oldest

    directory = os.listdir(os.getcwd())
    counter = 0
    sorted_time_list = []
    comp_dir = {}
    sorted_index = 0
    keys_list = []
    value_list = []

    # it lists the time of the different files and directories.

    for j in directory:
        comp_dir[j] = os.path.getatime(j)
        sorted_time_list.append(os.path.getatime(j))

    # Once get the time values of each file or directory, it sorts them and reverse to get from
    # the oldest ones to the newest ones.
    del directory
    sorted_time_list.sort()

    # It transforms the dictionary list of values and key into a common list.
    # The list derived from .values() .keys() methods are not compatible with common list methods.

    for i in comp_dir.values():
        value_list.append(i)
    for i in comp_dir.keys():
        keys_list.append(i)
    del comp_dir
    # It uses the index of the sorted time list (sorted_time_list) to compare them with the value list
    # and know exactly which key (file) it corresponds with.
    # sorted_index gets the corresponding position of time value in value_list (non-sorted list). The same index
    # is shared by the corresponding key in key_list, remember both list come from the same dictionary, comp_dir so
    # key order in key_list corresponds to value order in value_list. So identifying to index of the value in value_list
    # it is possible to know the index and position of the key that corresponds with.

    for j in sorted_time_list:
        sorted_index = value_list.index(j)
        format_string = f"{counter}. {keys_list[sorted_index]} size: {os.path.getsize(keys_list[sorted_index])} time: {j}"

        # it identifies if file or directory it is really a file or a directory...

        if os.path.isdir(keys_list[sorted_index]):
            format_string = format_string + "type: Directory"
            print(format_string)
        else:
            format_string = format_string + "type: File"
            print(format_string)
        counter += 1

    print("\n")


def sorteds():

    # Show a directory content according the size of each file or directory - from the smallest ones to the biggest

    directory = os.listdir(os.getcwd())
    counter = 0
    sorted_size_key_list = []
    comp_dir = {}
    value_list = []
    key_list = []
    final_value_list = []
    final_key_list = []
    discard_key_list = []

    # it lists the size of the different files and directories.

    for j in directory:
        comp_dir[j] = os.path.getsize(j)

    # dictionary lists of values and keys
    del directory
    value_list = comp_dir.values()
    key_list = comp_dir.keys()

    # Due to dictionary list of methods .values() and .key() are not 100% compatible with list properties and methods.
    # this loops transform dictionary list into common lists.

    for i in value_list:
        final_value_list.append(i)
    for i in key_list:
        final_key_list.append(i)

    del value_list
    del key_list

    # it sorts the value list...
    final_value_list.sort()  # numerical

    # It sorts the files or directory keys in a list according the file size order.

    for h in final_value_list:
        for i in final_key_list:
            if comp_dir[i] == h:
                sorted_size_key_list.append(i)

    del final_value_list
    del final_key_list

    # It discards the repeated files or directory
    final_sorted_size_key_list = []

    for i in sorted_size_key_list:
        for j in sorted_size_key_list:

            if i in discard_key_list:
                pass

            else:

                if i == j:
                    final_sorted_size_key_list.append(i)
                    discard_key_list.append(i)

    counter = 0
    for i in final_sorted_size_key_list:
        print(f"{counter}. {final_sorted_size_key_list[counter]} size: {os.path.getsize(final_sorted_size_key_list[counter])} time: {os.path.getatime(final_sorted_size_key_list[counter])}")
        counter += 1

    print("\n")


def sortedS():
    # Show a directory content according the size of each file or directory - from the smallest ones to the biggest

    directory = os.listdir(os.getcwd())
    counter = 0
    sorted_size_key_list = []
    comp_dir = {}
    value_list = []
    key_list = []
    final_value_list = []
    final_key_list = []
    discard_key_list = []

    # it lists the size of the different files and directories.

    for j in directory:
        comp_dir[j] = os.path.getsize(j)

    # dictionary lists of values and keys
    del directory
    value_list = comp_dir.values()
    key_list = comp_dir.keys()

    # Due to dictionary list of methods .values() and .key() are not 100% compatible with list properties and methods.
    # this loops transform dictionary list into common lists.

    for i in value_list:
        final_value_list.append(i)
    for i in key_list:
        final_key_list.append(i)

    del value_list
    del key_list

    # it sorts the value list...
    final_value_list.sort()  # numerical
    final_value_list.reverse()

    # It sorts the files or directory keys in a list according the file size order.

    for h in final_value_list:
        for i in final_key_list:
            if comp_dir[i] == h:
                sorted_size_key_list.append(i)

    del final_value_list
    del final_key_list

    # It discards the repeated files or directory
    final_sorted_size_key_list = []

    for i in sorted_size_key_list:
        for j in sorted_size_key_list:

            if i in discard_key_list:
                pass

            else:

                if i == j:
                    final_sorted_size_key_list.append(i)
                    discard_key_list.append(i)

    counter = 0
    for i in final_sorted_size_key_list:
        print(
            f"{counter}. {final_sorted_size_key_list[counter]} size: {os.path.getsize(final_sorted_size_key_list[counter])} time: {os.path.getatime(final_sorted_size_key_list[counter])}")
        counter += 1

    print("\n")

def here():

    global here_var
    here_var.append(os.getcwd())


def showhere():
    global here_var
    counter=0
    for i in here_var:
        print(f"{counter}.{here_var[counter]}")
        counter=counter+1


def gohere(match):
    global here_var
    os.chdir(here_var[match])


def py(content_list):

    format_string = f"python -c"
    content_list.pop[0]

    for i in content_list:
        format_string = format_string+" "+i

    os.system(format_string)



def exit_breaking():
    return False

# AUXILIARY FUNCTIONS for character correction:

def fix_slide_bar(string_sample):
    string_sample = string_sample.replace("/", "\\")
    return string_sample

def fix_slide_bar_list(sample_list):
    counter=0
    for i in sample_list:
        memory=i
        sample_list.pop(counter)
        fix_slide_bar(memory)
        sample_list.insert(counter, memory)
        counter+=1


def reverse_slide_bar(string_sample):
    string_sample = string_sample.replace("\\","/")
    return string_sample


def fix_capital(string_sample):
    if string_sample.count("c:") > 0:

        final_string = string_sample.replace("c:", "C:")

        return final_string

    elif string_sample.count("d:") > 0:

        final_string = string_sample.replace("d:", "D:")

        return final_string

    else:
        return string_sample




helpdic_en = {

    "exit": "Close the console...",
    "show": "show / show <directory> : shows in the console the directory content  // Similar commands: DIR, ls, Get-ChildItem.",
    "go": "go() command transfers the pointer to the first directory match in the current directory. i.e: You are in 'C:/Users' and you want to move to MyUser -- go My or go MyU and then moves to C:/Users/MyUser  ",
    "search": "It searches the corresponding element that match with the parameter. i.e: search hello.py -- Look for all files and folder that match with 'hello.py'",
    "google": "It googles what you want in your selected browser, i.e: google White horses , the it googles White horses :D",
}

# MAIN FUNCTION

continuity = True

while continuity:
    location = os.getcwd()
    content = input(f"PyS>{location}>")
    #content = fix_slide_bar(content)

    parted_content = content.split(" ")

    # Command analysis and execution

    if parted_content[0] == "exit":
        continuity = exit_breaking()

    else:

        # Insert all reamining commands:

        if parted_content[0] == "show":
            fix_slide_bar_list(parted_content)
            show(parted_content)

        elif parted_content[0] == "go":
            fix_slide_bar_list(parted_content)
            try:
                go(parted_content[1])
            except IndexError:
                print("IndexError: Required parameter for go() command")

        elif parted_content[0] == "cd":
            fix_slide_bar_list(parted_content)
            try:
                cd(parted_content[1])
            except IndexError:
                if settings["automaticEmptyCdParam"] == "off":
                    print("IndexError: Required parameter for cd() command")
                else:
                    cdu()
            except OSError:
                if settings["automaticEmptyCdParam"] == "off":
                    print("IndexError: Required parameter for cd() command")
                else:
                    cdu()

        elif parted_content[0] == "ps":
            ps(parted_content)

        elif parted_content[0] == "py":
            py(parted_content)

        elif parted_content[0] == "google":
            fix_slide_bar_list(parted_content)
            google(parted_content)

        elif parted_content[0] == "search":
            fix_slide_bar_list(parted_content)
            try:
                search(parted_content[1])

            except IndexError:
                print("IndexError: Required parameter for search command")

        elif parted_content[0] == "sortedT":
            sortedT()

        elif parted_content[0] == "sortedt":
            sortedt()

        elif parted_content[0] == "sorteds":
            sorteds()

        elif parted_content[0] == "sortedS":
            sortedS()

        elif parted_content[0] == "here":
            here()

        elif parted_content[0] == "gohere":
            fix_slide_bar_list(parted_content)
            try:
                gohere(int(parted_content[1]))
            except IndexError:
                print("IndexError: Required parameter for gohere() command")
            except TypeError:
                print("")


        elif parted_content[0] == "showhere":
            showhere()


        else:
            command_execution = True

            for h in folders:
                if parted_content[0] == h:
                    #os.chdir(folders[h])
                    dir_fun(h)
                    command_execution = False
                    break

            #REQUIRED TESTING ALL CMD COMMANDS AND CONSOLE SCRIPTS . Use "\" instead "/"
            if command_execution:
                command_string = ""
                for i in parted_content:
                    if command_string == "":
                        command_string = command_string + i
                    else:
                        command_string = command_string + " " + i

                print(command_string)
                os.system(f"{command_string}")

