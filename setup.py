import subprocess,os,shutil
print("Welcome to rodder!")
if os.path.exists(os.getenv('HOME') + '/.config/rodder') == True or os.path.exists(os.getenv('HOME') + '~/.local/rodder') == True:
    isDeleteOldInstall = input(">< Previous install found! Would you like to remove it? [y/N] ")
    if isDeleteOldInstall.lower() == 'y':
        shutil.rmtree(os.getenv('HOME') + '/.local/rodder')
        shutil.rmtree(os.getenv('HOME') + '/.config/rodder')
        shutil.rmtree(os.getenv('HOME') + '/.tmp/rodder')
    else:
        print(">< Cannot continue. Exiting :(...")
        exit()
isUserInstall = input(">< Would you like an install for this user only? [Y/n] ")
print(">< Cloning rodder git repo...")
print(subprocess.check_output('git clone https://github.com/ruthenic/rodder ~/.tmp/rodder', shell=True))
print(">< Moving to installation directory...")
if isUserInstall.lower() == "y" or isUserInstall.lower() == "":
    path = '~/.local/rodder'
    subprocess.call('mv ~/.tmp/rodder ~/.local', shell=True)
elif isUserInstall.lower() == "n":
    path = '/usr/local/rodder'
    print("Input your password to install to root (WARNING: NOT FULLY FUNCTIONAL, NOR FULLY TESTED.).")
    subprocess.call('sudo mv ~/.tmp/rodder /usr/local', shell=True)
else:
    print("Error: invalid selection! Exiting...")
    exit()
print(">< Creating config file...")
subprocess.call('mkdir ~/.config/rodder && mkdir ~/.config/rodder/repos', shell=True)
subprocess.call('echo "https://github.com/ruthenic/rodder-repo" >> ~/.config/rodder/repos/master-repo-list.txt', shell=True)
subprocess.call('rm -rf ~/.tmp/rodder', shell=True)
subprocess.call('export PATH=' + os.getenv('HOME') + '/.local/rodder:$PATH', shell=True)
print("Done installing rodder!")
print("Be sure to add " + path + " to your path with " + '`export PATH=' + os.getenv('HOME') + '/.local/rodder:$PATH`')
