import subprocess,os,shutil
print("Welcome to rodder!")
if os.path.exists(os.getenv('HOME') + '/.config/rodder') == True or os.path.exists(os.getenv('HOME') + '~/.local/rodder') == True:
    isDeleteOldInstall = input(">< Previous install found! Would you like to remove it? [y/N] ")
    if isDeleteOldInstall.lower() == 'y':
        shutil.rmtree(os.getenv('HOME') + '/.local/rodder')
        shutil.rmtree(os.getenv('HOME') + '/.config/rodder')
        #shutil.rmtree(os.getenv('HOME') + '/.tmp/rodder')
    else:
        print(">< Cannot continue. Exiting :(...")
        exit()
isUserInstall = input(">< Would you like an install for this user only? [Y/n] ")
print(">< Cloning rodder git repo...")
print(subprocess.check_output('git clone https://github.com/ruthenic/rodder ' + os.getenv('HOME') + '/.tmp/rodder', shell=True))
print(">< Moving to installation directory...")
if isUserInstall.lower() == "y" or isUserInstall.lower() == "":
    path = '~/.local/rodder'
    shutil.move(os.getenv('HOME') + '/.tmp/rodder', os.getenv('HOME') + '/.local')
elif isUserInstall.lower() == "n":
    path = '/usr/local/rodder'
    print("Input your password to install to root (WARNING: NOT FULLY FUNCTIONAL, NOR FULLY TESTED.).")
    subprocess.call('sudo mv ~/.tmp/rodder /usr/local', shell=True)
else:
    print("Error: invalid selection! Exiting...")
    exit()
print(">< Creating config file...")
os.makedirs(os.getenv('HOME') + '/.config/rodder')
os.makedirs(os.getenv('HOME') + '/.config/rodder/repos')
with open(os.getenv('HOME') + '/.config/rodder/repos/master-repo-list.txt', 'w') as f:
    f.write('https://github.com/ruthenic/rodder-repo')
#shutil.rmtree(os.getenv('HOME') + '/.tmp/rodder')
subprocess.call('export PATH=' + os.getenv('HOME') + '/.local/rodder:$PATH', shell=True)
print("Done installing rodder!")
print("Be sure to add " + path + " to your path with " + '`export PATH=' + os.getenv('HOME') + '/.local/rodder:$PATH`')
