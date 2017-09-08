from tkinter import *
import re
import pyperclip


def main():
    print("Email and username is extracting on file wait a second...")
    match = re.findall(r'[\w.-]+@[\w-]+[.][\w]+', pyperclip.paste())
    p_match = re.findall(r"\+\d{3}\s?0?\d{6,10}", pyperclip.paste())

    def email():
        print("--------------------------------------")
        print("\t\tEmail address:")
        print("--------------------------------------")
        with open('email', 'a+') as f:
            for line in match:
                f.write(line+"\n")
                print(line)
    email()

    def phone():
        print("--------------------------------------")
        print("\t\tphone number:")
        print("--------------------------------------")
        with open('phone', 'a+') as f:
            for line in p_match:
                f.write(line+"\n")
                print(line)

    phone()


b = Button(text="Enter!!", command=main)
b.pack()
mainloop()
