import time
import os

sh = 'zsh'
editor = "nvim"

os.system('setterm -foreground blue ')
print('Hello')

while True:
    cmd = input('neko ->> ')

    if cmd == 'system':
        sys = input('neko@system ->> ')

        os.system(sys)
    elif cmd == 'exit':
        break
    elif cmd == "edit":
        edit = input("neko@edit ->> ")

        os.system(editor + " " + edit)
    elif cmd == "config":
        os.system(editor + " project_neko.py")
        break
os.system(sh)
