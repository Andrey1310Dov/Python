import os
import datetime
import lxml.etree as ET

# Function for getting of time creating of a directory
def get_time_and_date_of_directory(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.utcfromtimestamp(t)

def create_xml_files(SORTS, SubTables):
    # Create a directory
    path = input("Write a name of a directory: ")
    name_dir = path.split('/')
    name_dir = name_dir[len(name_dir) - 1]
    try:
        os.makedirs(path)
    except OSError:
        print ("The directory %s has not been created" % path)
    else:
        print ("The directory %s has been created successfully" % path)
    # Get time of the creation of the directory
    d = get_time_and_date_of_directory(path).strftime("%Y-%m-%d %H:%M:%S")

    # Create xml file
    root = ET.Element(name_dir)
    root.set("Created", d)
    main_child = ET.SubElement(root, "Table_SORTS")
    sort_children = []
    counters = []
    n = - 1
    z = 0
    # Circle for sort_children
    for index in SORTS:
        sort_child = ET.SubElement(main_child, "SORT")
        for key, value in index.items():
            sort_child.set(key, value)
        sort_children.append(sort_child)
    # Circle for counters     
    for index in SubTables:
        n += 1
        keys = list(index.keys())
        length_values = len(index.get(keys[0]))
        for i in range(length_values):
            counter = ET.SubElement(sort_children[n], "Counter")
            for key, value in index.items():
                counter.set(key, value[i])
            counters.append(counter)
    # Write our file                                    
    filename = input("Write the file's name for writing in xml-format(point a path to the created directory): ")
    tree = ET.ElementTree(root)
    with open(filename, "wb") as my_file:
        my_file.write(ET.tostring(tree, pretty_print = True, encoding="UTF-8", standalone="yes"))
    return True

def reading_file(filename):
    # Check the exist of file for reading 
    try:
        lines = [line.rstrip() for line in open(filename)]
        lines.pop(len(lines) - 1)
    except:
        raise Exception("File's name is wrong or this file doesn't exist! Try again.")
    # Prepare dictionaries and lists for working
    SORT = {}
    list_SORTS = []
    SubTable = {}
    list_SubTables =[]
    list_Deno = []
    list_Pcs = []
    list_Amount = []
    list_Total = []
    amount_transactions = 0
    # We must create two lists of dictionaries.
    for line in lines:
        line = line.split()
        if "SORT" in line:
            SORT["Trans"] = line[len(line) - 1]
        elif "START" in line:
            SORT["START"] = line[len(line) - 2] + " " + line[len(line) - 1]
        elif "END" in line:
            SORT["END"] = line[len(line) - 2] + " " + line[len(line) - 1]
        elif "[No.]R" in line:
            SORT["No_R"] = line[len(line) - 1]
        elif "Amount" in line:
            SORT["Currency"] = line[0]
        elif len(line) == 1:
            amount_transactions += 1
            if list_Deno == [] and list_Pcs == [] and list_Amount == []:
                list_Deno.append(" ")
                SubTable["Deno"] = list_Deno
                list_Pcs.append(" ")
                SubTable["Pcs"] = list_Pcs
                list_Amount.append(" ")
                SubTable["Amount"] = list_Amount
        elif "Total" in line:
            SORT["Total_Pcs"] = line[len(line) - 2]
            SORT["Total_Amount"] = line[len(line) - 1]
            list_SORTS.append(SORT)
            list_SubTables.append(SubTable)
            SubTable = {}
            SORT = {}
            list_Deno = []
            list_Pcs = []
            list_Amount = []
            list_Total = []
        else:
            list_Deno.append(line[0])
            SubTable["Deno"] = list_Deno
            list_Pcs.append(line[1])
            SubTable["Pcs"] = list_Pcs
            list_Amount.append(line[2])
            SubTable["Amount"] = list_Amount
    # Create xml-file
    get_xml_file = create_xml_files(list_SORTS, list_SubTables)
    return True

# For check
reading_file(input("Write the file's name for reading: "))
