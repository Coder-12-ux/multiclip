# added a new comment
import json
import clipboard
import sys
# from os import system as cmd

# if key or value string has a space in them then enclose them in double quotes
# for loading an item in clipboard, type the key<space>value
# for getting an item from clipboard use "~" in front of item's key

try:
    cliplib = json.loads(open("cplib.json").read())
except FileNotFoundError:
    open("cplib.json", "a").write("{}")
    cliplib = json.loads(open("cplib.json").read())


def get(key):
    try:
        return cliplib[key]
    except KeyError:
        return "INVALID KEY"


def save(key=None, value=None):
    if (key != None) and (value != None):
        cliplib[key] = value

    json.dump(cliplib, open("cplib.json", "w"))


args = sys.argv[1:]

if len(args) == 0:
    exit("NO ARGUMENTS")

key = args[0][1:]


if len(args) > 2:
    exit("INVALID NUMBER OF ARGUMENTS")

elif (len(args) == 1) and (args[0] == "lib"):
    exit(cliplib)

elif (len(args) == 1) and (args[0] == "help"):
    print(
        "--------------------\n",
        "MULTICLIP aka \"mlcp\"\n",
        "--------------------\n",
        "  A utility that can store more than one\n",
        "  clipboard items at a time\n\n",
        "  Every clipboard item has a key associated\n",
        "  with it, which is then use to access the\n",
        "  clip from the library\n",
        "HOW TO USE:\n",
        "  add ~(tilde) sign infront of the item's\n",
        "  key you want to get on your clipboard\n",
        "syntax = mlcp ~<key>\n\n",
        "  for adding a new item in the library\n",
        "  type the key value as arguments\n",
        "  if the either key or value has space\n",
        "  then enclose them in DOUBLE QUOTES\n",
        "syntax = mlcp <key> <value>\n\n",
        "  for seeing the library, type mlcp lib\n\n",
        "  for deleting an item from library, type\n",
        "syntax = mlcp -<key>\n\n",
        "  for seeing an specific item from a key,\n",
        "syntax = mlcp ><key>\n\n",
        "  for saving the current item from clipboard, \n",
        "syntax = mlcp +<key>",
        sep="")

elif "~" in args[0]:
    clipboard.copy(get(key))
    # print("getting")

elif "?" in args[0]:
    exit(get(key))

elif len(args) == 2:
    key, value = args[0], args[1]
    save(key,value)

elif "+" in args[0]:
    save(key, clipboard.paste())

elif "-" in args[0]:
    exit(f"\"{cliplib.pop(key)}\" deleted")

