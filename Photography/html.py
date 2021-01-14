import os
def write_html(link):
    positionLength = len(os.path.dirname(os.path.realpath(__file__)))
    links = link[positionLength:]
    index = links.count("/")
    html_text = ""
    html_text += get_text(os.path.dirname(os.path.realpath(__file__)) + "/front.txt", index + 1)
    """
    lines = get_title_text(link)
    if lines == None:
        pass
    else:
        html_text += "        <h2 class=\"notes\">"
        html_text += lines
        html_text += "</h2>\n"
    """
    html_text += array_wrapper(link)
    html_text += get_text(os.path.dirname(os.path.realpath(__file__)) + "/back.txt", index + 1)
    return html_text


"""
rip
def get_title_text(link):
    if os.path.isfile(link + "/title.txt"):
        title_text = ""
        file = open(link + "/title.txt")
        lines = file.readlines()
        for line in lines:
            title_text += line
        file.close()
        return title_text.replace("\n", "<br>")
    else:
        return None
"""


def get_text(link, value):
    # link: either front.txt or back.txt
    text = ""
    with open(link) as f:
        text = f.readlines()
    text = "".join(text)
    return text.replace("../../", "../" * value)


def get_image_array(link):
    # link: Address to the folder of the operation
    dir = link + "/images"
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
#print(get_text(os.path.dirname(os.path.realpath(__file__)) + "/front.txt"))
#print(os.path.dirname(os.path.realpath(__file__)))
#print(get_title_text(os.path.dirname(os.path.realpath(__file__)) + "\\Toaster"))
#print(write_html(os.path.dirname(os.path.realpath(__file__)) + "/"))
#print(write_html())
#print(get_image_count(os.path.dirname(os.path.realpath(__file__)) + "\\Potato\\Potatoe"))
