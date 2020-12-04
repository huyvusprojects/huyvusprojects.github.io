import os
"""
def append(num):
    front = "				<img src=\"images/"
    back = ".jpg\" onContextMenu=\"return false;\"/>\n"
    string = front + str(num) + back
    return string

def autoload(num):
	mid = ""
	for i in range(1,num+1):
		mid += append(i)
	return mid
def count_files():
    return len([name for name in os.listdir('images') if os.path.isfile('images/' + name) and name != '.DS_Store'])
def main():
	filecount = count_files()
	with open('../front.txt') as f:
		start = f.readlines()
	start = "".join(start)
	with open('back.txt') as f:
		end = f.readlines()
	end = "".join(end)
	mid = autoload(filecount)
	return start + mid + end
file = open("CollectorsLGBT.html","w")
file.write(main())
file.close()"""
cur_path = os.path.dirname(__file__)
cur_path.chdir("..")
new_path = os.path.join(cur_path,'..\\front.txt')

