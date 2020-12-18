import subprocess
print("Welcome to rodder!")
isUserInstall = input(">< Would you like an install for this user only? [Y/n] ")
print(">< Cloning rodder git repo...")
print(subprocess.check_output('git clone https://github.com/ruthenic/rodder ~/.tmp/rodder', shell=True))
print(">< Moving to installation directory...")
if isUserInstall.lower() == "y" or isUserInstall.lower() == "":
    path = '~/.local/rodder'
    subprocess.call('mv ~/.tmp/rodder ~/.local/rodder', shell=True)
elif isUserInstall.lower() == "n":
    path = '/usr/local/rodder'
    print("Input your password to install to root.")
    subprocess.call('sudo mv ~/.tmp/rodder /usr/local', shell=True)
else:
    print("Error: invalid selection! Exiting...")
    exit()
subprocess.call('rm -rf ~/.tmp/rodder', shell=True)
print("Done installing rodder!")
print("Be sure to add " + path + " to your path!")
