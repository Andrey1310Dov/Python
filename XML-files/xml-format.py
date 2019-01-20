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

    # Create SORTS
    sorts_child_1 = ET.SubElement(main_child, "SORT", attrib=SORTS[0])
    sorts_child_2 = ET.SubElement(main_child, "SORT", attrib=SORTS[1])
    sorts_child_3 = ET.SubElement(main_child, "SORT", attrib=SORTS[2])
    sorts_child_4 = ET.SubElement(main_child, "SORT", attrib=SORTS[3])

    # Create subtables and its attributes
    dict_child_1 = SubTables[0]
    dict_child_2 = SubTables[1]
    dict_child_3 = SubTables[2]
    dict_child_4 = SubTables[3]
    
    dict_child_1_1 = {}
    for key, value in dict_child_1.items():
        if key == "Total":
            dict_child_1_1["Total_Pcs"] = value[0]
            dict_child_1_1["Total_Amount"] = value[1]
        else:
            dict_child_1_1[key] = value[0]

    dict_child_1_2 = {}
    for key, value in dict_child_1.items():
        if key == "Total":
            dict_child_1_2["Total_Pcs"] = value[0]
            dict_child_1_2["Total_Amount"] = value[1]
        else:
            dict_child_1_2[key] = value[1]

    dict_child_2_1 = {}
    for key, value in dict_child_2.items():
        if key == "Total":
            dict_child_2_1["Total_Pcs"] = value[0]
            dict_child_2_1["Total_Amount"] = value[1]
        else:
            dict_child_2_1[key] = value[0]

    dict_child_2_2 = {}
    for key, value in dict_child_2.items():
        if key == "Total":
            dict_child_2_2["Total_Pcs"] = value[0]
            dict_child_2_2["Total_Amount"] = value[1]
        else:
            dict_child_2_2[key] = value[1]
            
    dict_child_3_1 = {}
    for key, value in dict_child_3.items():
        if key == "Total":
            dict_child_3_1["Total_Pcs"] = value[0]
            dict_child_3_1["Total_Amount"] = value[1]
        else:
            dict_child_3_1[key] = value[0]
            
    dict_child_3_2 = {}
    for key, value in dict_child_3.items():
        if key == "Total":
            dict_child_3_2["Total_Pcs"] = value[0]
            dict_child_3_2["Total_Amount"] = value[1]
        else:
            dict_child_3_2[key] = value[1]

    dict_child_3_3 = {}
    for key, value in dict_child_3.items():
        if key == "Total":
            dict_child_3_3["Total_Pcs"] = value[0]
            dict_child_3_3["Total_Amount"] = value[1]
        else:
            dict_child_3_3[key] = value[2]
            
    dict_child_4_1 = {}
    for key, value in dict_child_4.items():
        if key == "Total":
            dict_child_4_1["Total_Pcs"] = value[0]
            dict_child_4_1["Total_Amount"] = value[1]
    dict_child_4_1["Deno"] = ""
    dict_child_4_1["Pcs"] = ""
    dict_child_4_1["Amount"] = ""
            
    counter_1 = ET.SubElement(sorts_child_1, "Counter", attrib=dict_child_1_1)
    counter_1 = ET.SubElement(sorts_child_1, "Counter", attrib=dict_child_1_2)
    counter_2 = ET.SubElement(sorts_child_2, "Counter", attrib=dict_child_2_1)
    counter_2 = ET.SubElement(sorts_child_2, "Counter", attrib=dict_child_2_2)
    counter_3 = ET.SubElement(sorts_child_3, "Counter", attrib=dict_child_3_1)
    counter_3 = ET.SubElement(sorts_child_3, "Counter", attrib=dict_child_3_2)
    counter_3 = ET.SubElement(sorts_child_3, "Counter", attrib=dict_child_3_3)
    counter_4 = ET.SubElement(sorts_child_4, "Counter", attrib=dict_child_4_1)

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
        elif "Total" in line:
            list_Total.append(line[len(line) - 2])
            list_Total.append(line[len(line) - 1])
            SubTable["Total"] = list_Total
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
