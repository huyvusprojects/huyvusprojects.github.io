import os
def write_html(link):
    print(link)
    html_text = ""
    html_text += "".join(get_text("front.txt"))
    lines = get_title_text(link)
    if lines == None:
        pass
    else:
        html_text += "        <h2 class=\"notes\">"
        html_text += lines
        html_text += "</h2>\n"
    html_text += array_wrapper(link)
    html_text += "".join(get_text("back.txt"))
    return html_text


def get_title_text(link):
    if os.path.isfile(link + "\\title.txt"):
        title_text = ""
        file = open(link + "\\title.txt")
        lines = file.readlines()
        for line in lines:
            title_text += line
        file.close()

        return title_text[:-1].replace("\n", "<br>")
    else:
        return None

def get_text(link):
    # link: either front.txt or back.txt
    text = ""
    with open(link) as f:
        text = f.readlines()
    return text


def get_image_array(link):
    # link: Address to the folder of the operation
    dir = link + "\\images"
    return [name for name in os.listdir(dir) if name != '.DS_Store']


def array_wrapper(link):
    # link: Address to the folder of the operation
    arr = get_image_array(link)
    text = ""
    for image in arr:
        text += "        <img src=\"images/"
        text += image
        text += "\" onContextMenu=\"return false;\"/>\n"
    return text

#print(get_title_text(os.path.dirname(os.path.realpath(__file__)) + "\\Toaster"))
#print(write_html(os.path.dirname(os.path.realpath(__file__)) + "\\Potato\\Potatoe"))
#print(write_html())
#print(get_image_count(os.path.dirname(os.path.realpath(__file__)) + "\\Potato\\Potatoe"))
