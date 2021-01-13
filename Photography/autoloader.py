import os
import html

def get_directories(link):
    all_directories = []
    to_check = []
    for address in os.listdir(link):
        if address == "images":
            all_directories.append(link)
        elif os.path.isdir(link + "\\" + address):
            to_check.append(link + "\\" + address)
    while len(to_check) > 0:
        link = to_check[0]
        to_check.pop(0)
        for address in os.listdir(link):
            if address == "images":
                all_directories.append(link)
            elif os.path.isdir(link + "\\" + address):
                to_check.append(link + "\\" + address)
    return all_directories
    #for os.path.dirname(os.path.realpath(__file__))

def main():
    array_list = []
    for folder in os.listdir("."):
        if os.path.isdir(folder) and folder != "__pycache__":
            array_list.append(folder)
    all_directories = []
    for address in array_list:
        directory = get_directories(os.path.dirname(os.path.realpath(__file__)) + "\\" + address)
        for dir in directory:
            all_directories.append(dir)
    for address in all_directories:
        file = open(address + "\\index.html", "w")
        file.write(html.write_html(address))
        file.close()

        #for index in directory:
    #get_directories(os.path.dirname(os.path.realpath(__file__)))
    #print(array_list)
#with open(os.path.dirname(os.path.realpath(__file__)) + "\\Potato\\Potatoe\\potato.txt") as f:
    #start = f.readlines()
#print(html.write_html(os.path.dirname(os.path.realpath(__file__)) + "\\Potato\\Potatoe"))
main()
