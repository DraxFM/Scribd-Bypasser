import os
import sys

version = "1.0"

requirements = ["requests"]

os.system(f"title Scribd Bypasser v{version} - Made by github.com/DraxFM")

def get_python_found():
    path_env = os.environ.get("PATH")
    path_dirs = path_env.split(os.pathsep)
    python_dir = os.path.dirname(sys.executable)
    return any(python_dir in path for path in path_dirs)
    
try:
    if get_python_found() == False:
        print("Python is not added to PATH or could not be found!")
        print("Please add Python to PATH or make sure it is correctly installed.")
        print("Press Enter to exit.")
        input()
        os._exit(1)
except:
    print("An unexpected error occured. If this keeps happening please contact the developer!")
    print("Press Enter to exit.")
    input()
    os._exit(1)
    
for obj in requirements:
    os.system(f"pip install {obj}")
    
os.system("cls")

import requests

def check_blank(input):
    if not input or input.isspace():
        res = None
    else:
        res = True
    return res
    
def exit(errorMsg):
    print(f"Error: {errorMsg}")
    print("Press Enter to exit.")
    input()
    os._exit(1)
    
def validate_request(rload):
    try:
        with requests.get(rload) as r:
            if r.status_code == 200:
                return True
            else:
                return False
    except BaseException:
        return False

print("-- Scribd Bypasser made by draxfm --")
print()
print("This Script lets you bypass the free preview of Scribd without needing an account or anything.")
print("This only works with documents uploaded on Scribd in the normal type.")
print("You need the full URL to the document for this.")
print("The bypassed document will be locally saved on the location of this script file.")
print()
print("Github: www.github.com/DraxFM")
print("Discord Invite: https://discord.gg/sEXECdC3Et")
print("Discord: draxfm")
print()
fileName = input("Local Bypassed Document Name: ")
fileURL = input("URL to Scribd Document: ")
print()
print("Checking Validity...")

if check_blank(fileName) == None:
    exit("Document Name Empty or invalid!")

if os.path.isfile(f"./{fileName}.html") == True:
    exit("Name of Bypassed Document conflicts with already existing file!")
    
if check_blank(fileURL) == None:
    exit("URL seems to be empty!")

if not "scribd.com" in fileURL:
    exit("URL seems not to be from Scribd!")
    
if validate_request(fileURL) == False:
    exit("URL is invalid or not reachable!")
    
print("Bypass validated.")
print("Requesting URL...")
    
try:
    r = requests.get(fileURL)
    src = r.text
    print("URL obtained.")
    print("Writing to local file...")
    with open(f"{fileName}.html", "w", encoding="utf-8") as f:
        f.write(str(src))
        f.close()
        print("Source code copied over to local file.")
except requests.exceptions.RequestException as e:
    exit(f"INTERNAL: {e}")
    
print("Checking for Blur...")

with open(f"{fileName}.html", "r", encoding="utf-8") as f:
    s = f.read()
    if '<div class="outer_page only_ie6_border blurred_page"' in s:
        print("Blur found.")
        print("Bypassing Document...")
        f.close()
        with open(f"{fileName}.html", "w", encoding="utf-8") as f:
            s = s.replace('<div class="outer_page only_ie6_border blurred_page"', '<div class="outer_page only_ie6_border"')
            f.write(s)
            f.close()

print("Document Bypassed.")
print("Press Enter to open the document and close this window.")
input()
os.system(f"start {fileName}.html")
os._exit(1)
    