import re


def read_template(path):
    """
    This function takes a path for txt file and returns a string of the content inside the file 
    """
    try:
        file = open(path, 'r')
        content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError('please enter a vaild file path')


def welcome_messege():
    """
    this function shows a welcome massege 
    """
    print("""
    *********************************************
    Welcometo the malib game 
    you will be asked to inter some random words 
    finally you will see the result
    *********************************************
    """)


def parse_template(txt):
    """
    This function takes a template(string) and extract all the
    phrases within any curly brackets {}
    """
    parts_list = re.findall(r'\{.*?\}',txt)
    stripped = re.sub(r'\{.*?\}', '{}', txt)
    i=0
    for element in parts_list:
        element = element.strip('{}')
        parts_list[i]=element
        i=i+1
    parts_tuple=tuple(parts_list)
    return stripped ,parts_tuple


def merge(stripped, parts_tuple):
    """
    this function merges the user input with the text file in order 
    """
    txt = open('assets/result.txt', 'w')
    txt.write(stripped.format(*parts_tuple))

    return stripped.format(*parts_tuple)


def play():
    """this function to start the game in the terminal"""
    welcome_messege()
    template = read_template('./assets/file.txt')
    stripped, parts_tuple = parse_template(template)
    inputs = [input(f"\nwrite a/an {i}: ") for i in parts_tuple]
    txt= open("assets/result.txt","r")
    result= txt.read()
    print(result)

    return merge(stripped, inputs)


if __name__ == "__main__":
    play()




