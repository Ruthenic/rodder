import subprocess,os,shutil,requests,json,zipfile
print("Welcome to rodder!")
if os.path.exists(os.getenv('HOME') + '/.config/rodder') == True or os.path.exists(os.getenv('HOME') + '/.local/rodder') == True:
    isDeleteOldInstall = input(">< Previous install found! Would you like to remove it? [y/N] ")
    if isDeleteOldInstall.lower() == 'y':
        try:
            shutil.rmtree(os.getenv('HOME') + '/.local/rodder')
        except:
            pass
        try:
            shutil.rmtree(os.getenv('HOME') + '/.config/rodder')
        except:
            pass
        shutil.rmtree(os.getenv('HOME') + '/.tmp/rodder')
    else:
        print(">< Cannot continue. Exiting :(...")
        exit()
isUserInstall = input(">< Would you like an install for this user only? [Y/n] ")
#wantsReleaseVersion = input(">< Would you like the latest release, or the master branch? [RELEASE/master] ") #removing this for now because tbh its really dumb (still keeping the supporting code though)
wantsReleaseVersion = 'master'
#print(">< Cloning rodder git repo/downloading latest release...")
if wantsReleaseVersion.lower() == "master":
    print(">< Cloning rodder git repo...")
    print(subprocess.check_output('git clone https://github.com/ruthenic/rodder ' + os.getenv('HOME') + '/.tmp/rodder', shell=True))
elif wantsReleaseVersion.lower() == "release":
    print(">< Downloading latest rodder release...")
    dlurl = 'https://api.github.com/repos/Ruthenic/rodder/zipball/v0.1'
    file = requests.get(dlurl)
    os.makedirs(os.getenv('HOME') + '/.tmp/rodder', exist_ok=True)
    print(">< Extracting latest rodder release...")
    with open(os.getenv('HOME') + '/.tmp/rodder/rodder-v0.1.zip', 'wb') as f:
        f.write(file.content)
    with zipfile.ZipFile(os.getenv('HOME') + '/.tmp/rodder/rodder-v0.1.zip') as f:
        f.extractall(os.getenv('HOME') + '/.tmp/rodder')
print(">< Moving to installation directory...")
if isUserInstall.lower() == "y" or isUserInstall.lower() == "":
    path = '~/.local/rodder'
    if wantsReleaseVersion.lower() == "master":
        shutil.move(os.getenv('HOME') + '/.tmp/rodder', os.getenv('HOME') + '/.local')
    else:
        shutil.move(os.getenv('HOME') + '/.tmp/rodder/Ruthenic-rodder-8bb63e2', os.getenv('HOME') + '/.local')
        os.rename(os.getenv('HOME') + '/.local/Ruthenic-rodder-8bb63e2', os.getenv('HOME') + '/.local/rodder')
elif isUserInstall.lower() == "n":
    path = '/usr/local/rodder'
    print("Input your password to install to root (WARNING: NOT FULLY FUNCTIONAL, NOR FULLY TESTED.).")
    subprocess.call('sudo mv ~/.tmp/rodder /usr/local', shell=True)
else:
    print("Error: invalid selection! Exiting...")
    exit()
print('>< Moving librodder to python lib directory...') #AAAAAAAAAAAHHHHHHHH GOD THIS IS SO BAD
#shutil.move('{}/.local/rodder/','{}/.local/lib/Python3.9/site-packages')
print(">< Creating config file...")
os.makedirs(os.getenv('HOME') + '/.config/rodder')
os.makedirs(os.getenv('HOME') + '/.config/rodder/repos')
with open(os.getenv('HOME') + '/.config/rodder/repos/master-repo-list.txt', 'w') as f:
    f.write('https://github.com/ruthenic/rodder-repo')
if wantsReleaseVersion.lower() == "master":
    f = open(os.getenv('HOME') + '/.config/rodder/.usingmaster', 'wb'); f.close() #there has to be a better way to create files
#shutil.rmtree(os.getenv('HOME') + '/.tmp/rodder')
subprocess.call('export PATH=' + os.getenv('HOME') + '/.local/rodder:$PATH', shell=True)
print("Done installing rodder!")
print("Be sure to add " + path + " to your path with " + '`export PATH=' + os.getenv('HOME') + '/.local/rodder:$PATH`')
