
from importlib.resources import path
import re
def welcoming_msg():
    print("""
    ***************************************************************
                        Welcome to madlibs!!
            To play, enter the file name of a madlibs file.
        You\'ll then be prompted for words. When done, you\'ll receive
                        your completed madlibs
                to quit from the game write "quit"
    ***************************************************************
    """)
welcoming_msg()



def read_template(path):
    try:
        f= open(path)
    except FileNotFoundError:
        print("enter a vaild file name")
    else:
        txt = f.read()
        f.close()
    finally:
        return txt

txt = read_template("assets/file.txt")

def parse_template(txt):
     
    parts_list = re.findall(r'\{.*?\}',txt)
    stripped = re.sub(r'\{.*?\}', '{}', txt)
    i=0
    for element in parts_list:
        element = element.strip('{}')
        parts_list[i]=element
        i=i+1
    parts_tuple=tuple(parts_list)
    return stripped ,parts_tuple

stripped=parse_template(txt)[0]
parts_tuple=parse_template(txt)[1]

def merge(stripped,parts_tuple):
        parts=[]
        parts_list=list(parts_tuple)
        for element in parts_list:
            element = element.strip('{}')
            user_input=input("enter a word >  ")
            if user_input=="quit":
                exit()
            else:
                parts.append(user_input)
        parts_tuple=tuple(parts)
        output=stripped.format(*parts_tuple)
        print(f' your madlib result:    {output}')
        f=open("assets/result.txt","w")
        content=f.write(output)
        return output

merge(stripped,parts_tuple)       
        


    
    
    
    

