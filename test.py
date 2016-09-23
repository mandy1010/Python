
"""
Typing Game for Kids
Authur: Mandy H.
Date: 17 June 2016
"""

def open_file(filename):
    input_file = open(filename)
    content = input_file.read()
    #print(content)
    print("=" * 30)
    input_file.close()
    content = content.replace("\n", " ")
    print(content)
    content = list(content)
    return content

def main():
    open_file("source.txt")

main()
