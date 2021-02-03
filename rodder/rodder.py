#!/usr/bin/python
import sys,subprocess,os,shutil
def check():
    print(">< Checking printing abilities...")
    print(">< Test successful! Exiting...")
    exit()
if os.path.exists(os.getenv('HOME') + '/.config/rodder') == False:
    os.makedirs(os.getenv('HOME') + '/.config/rodder')
if os.path.exists(os.getenv('HOME') + '/.config/rodder/repos') == False:
    os.makedirs(os.getenv('HOME') + '/.config/rodder/repos')
if os.path.exists(os.getenv('HOME') + '/.config/rodder/repos/master-repo-list.txt') == False:
    with open(os.getenv('HOME') + '/.config/rodder/repos/master-repo-list.txt', 'w') as f:
        f.write('https://github.com/ruthenic/rodder-repo')
if os.path.exists(os.getenv('HOME') + '/.local/bin') == False:
    os.makedirs(os.getenv('HOME') + '/.local/bin') #have to throw this in here to fix docker systems
def help():
    print("rodder is a package management system\n")
    print("rodder install - installs program from current repos")
    print("rodder update - pulls newest version of repo file")
    print("rodder remove - uninstall program") #god this needs an update, but guess who can't be fucked
    #exit() #why did i even put exits in places lmao, the original version would've functioned without them
def update():
    try:
        with open(os.getenv('HOME') + '/.config/rodder/repos/master-repo-list.txt') as f:
            for line in f:
                print(">< Updating " + line.rsplit('/', 1)[-1] + '...')
                tmp = os.listdir(os.getenv('HOME') + '/.config/rodder/repos/')
                for i in tmp:
                    if os.path.isdir(os.getenv('HOME') + '/.config/rodder/repos/' + i) == False and i != 'master-repo-list.txt' and i != 'LICENSE' and os.path.exists(os.getenv('HOME') + '/.config/rodder/repos/' + i):
                        with open(os.getenv('HOME') + '/.config/rodder/repos/' + i) as f2:
                                for line2 in f2:
                                    if os.path.isdir(os.getenv('HOME') + '/.config/rodder/repos/' + line2.split(';')[0].replace('\n', '')) == True:
                                        shutil.rmtree(os.getenv('HOME') + '/.config/rodder/repos/' + line2.split(';')[0].replace('\n', ''))
                print(subprocess.check_output('git clone ' + line.replace('\n', '') + ' ' + os.getenv('HOME') + '/.tmp/rodder/' + line.rsplit('/', 1)[-1], shell=True))
            for i in os.listdir(os.getenv('HOME') + '/.tmp/rodder/' + line.rsplit('/', 1)[-1].replace('\n', '')):
                try:
                    os.remove(os.getenv('HOME') + '/.config/rodder/repos/'  + i)
                except:
                    try:
                        shutil.rmtree(os.getenv('HOME') + '/.config/rodder/repos' + '/' + i)
                    except:
                        pass
                shutil.move(os.getenv('HOME') + '/.tmp/rodder/' + line.rsplit('/', 1)[-1].replace('\n', '') + '/' + i, os.getenv('HOME') + '/.config/rodder/repos')
            subprocess.call('rm -rf ' + os.getenv('HOME') + '/.tmp/rodder/' + line.rsplit('/', 1)[-1].replace('\n', ''), shell=True)
            os.remove(os.getenv('HOME') + '/.config/rodder/repos/LICENSE')
    except Exception as e:
        print("ERROR: UPDATE FAILED")
        print(str(e))
def install(package):
    #package = sys.argv[2] #rodder install template; sys.argv[2] == template
    tmp = os.listdir(os.getenv('HOME') + '/.config/rodder/repos/')
    for i in tmp:
        if os.path.isdir(os.getenv('HOME') + '/.config/rodder/repos/' + i) == False and i != 'master-repo-list.txt':
            with open(os.getenv('HOME') + '/.config/rodder/repos/' + i) as f:
                for line in f:
                    if line.split(';')[0] == package: #checks if "template" == line (in this case, template;install.py;uninstall.py) split by the semicolons, and the first thing in the array is what it is compared against
                        exec(open(os.getenv('HOME') + '/.config/rodder/repos/' + line.split(';')[1].replace('\n', '')).read())
                        isPackageInstalled = True
                        break
                    else:
                        isPackageInstalled = False
    try:
        if isPackageInstalled == False:
            print('>< Cannot find package ' + package + '... Exiting')
    except:
        print(">< Installation failed for unknown reason, try running `rodder update`!")
def remove(package):
    #package = sys.argv[2]
    tmp = os.listdir(os.getenv('HOME') + '/.config/rodder/repos/')
    for i in tmp:
        if os.path.isdir(os.getenv('HOME') + '/.config/rodder/repos/' + i) == False and i != 'master-repo-list.txt':
            with open(os.getenv('HOME') + '/.config/rodder/repos/' + i) as f:
                for line in f:
                    if line.split(';')[0] == package:
                        exec(open(os.getenv('HOME') + '/.config/rodder/repos/' + line.split(';')[2].replace('\n', '')).read())
                        isPackageInstalled = True
                        break
                    else:
                        isPackageInstalled = False
    try:
        if isPackageInstalled == False:
            print('>< Cannot find package ' + package + '... Exiting')
    except:
        print(">< Installation failed for unknown reason, try running `rodder update`!")
def list():
    tmp = os.listdir(os.getenv('HOME') + '/.config/rodder/repos/')
    for i in tmp:
        if os.path.isdir(os.getenv('HOME') + '/.config/rodder/repos/' + i) == False and i != 'master-repo-list.txt':
            with open(os.getenv('HOME') + '/.config/rodder/repos/' + i) as f:
                print("Packages in " + i.split('.')[0] + ":")
                for line in f:
                    print(line.split(';')[0])
                    
class repo():
    def list():
        with open(os.getenv('HOME') + '/.config/rodder/repos/master-repo-list.txt') as f:
            for line in f:
                print(line.split('/')[len(line.split('/'))-1])
    def add(repo):
        #repo = sys.argv[3]
        if not repo.startswith('https://'):
            repo = 'https://github.com/' + repo
        with open(os.getenv('HOME') + '/.config/rodder/repos/master-repo-list.txt') as f:
            for line in f:
                if line.replace('\n', '').lower() == repo.lower():
                    print(">< Repo already in config file! Exiting...")
                    exit()
        with open(os.getenv('HOME') + '/.config/rodder/repos/master-repo-list.txt', 'a') as f:
            f.write('\n' + repo)
    def reset():
        wantsReset = input("Are you sure you want to reset the config file to the default? [y/N] ")
        if wantsReset.lower() == 'y':
            with open(os.getenv('HOME') + '/.config/rodder/repos/master-repo-list.txt', 'w') as f:
                    f.write('https://github.com/ruthenic/rodder-repo')
        elif wantsReset.lower() == 'n' or wantsReset.lower() == '':
            pass #time to find all the exit calls, oh boy
    def remove(repo):
        #repo = sys.argv[3]
        if not repo.startswith('https://'):
            repo = 'https://github.com/' + repo
        lines = []
        with open(os.getenv('HOME') + '/.config/rodder/repos/master-repo-list.txt') as f:
            for line in f:
                if not line.replace('\n', '').lower() == repo.lower():
                    lines.append(line)
        with open(os.getenv('HOME') + '/.config/rodder/repos/master-repo-list.txt', 'w') as f:
            for l in lines:
                f.write(l + '/n')
def search(package):
    tmp = os.listdir(os.getenv('HOME') + '/.config/rodder/repos/')
    tmp2 = open('{}/.tmp/rodder/search.txt'.format(os.getenv('HOME')), 'w+')
    for i in tmp:
        if os.path.isdir(os.getenv('HOME') + '/.config/rodder/repos/' + i) == False and i != 'master-repo-list.txt':
            with open(os.getenv('HOME') + '/.config/rodder/repos/' + i) as f:
                for line in f:
                    if package in line:
                        print('{} - {}'.format(line.split(';')[0], i.split('.')[0]))
                        tmp2.write(line.split(';')[0] + '\n')


if __name__ == "__main__":
    debug = False
    def interpreter(debug):
        if debug == True:
            while True:
                grhgghqahugsoauigigifjioifajoijfaojosjiojigrijoojiafofoajfojifaiojf = input('>>> ') #i swear to god if anyone names a variable this
                try:
                    exec(grhgghqahugsoauigigifjioifajoijfaojosjiojigrijoojiafofoajfojifaiojf)
                except Exception as e:
                    print(str(e))
        else:
            pass
    if sys.argv[1] == "check":
        check()
    if os.path.exists(os.getenv('HOME') + '/.config/rodder') == False: #eh, i'll keep this check for dirs in the actual wrapper for now
        os.makedirs(os.getenv('HOME') + '/.config/rodder')
    if os.path.exists(os.getenv('HOME') + '/.config/rodder/repos') == False:
        os.makedirs(os.getenv('HOME') + '/.config/rodder/repos')
    if os.path.exists(os.getenv('HOME') + '/.config/rodder/repos/master-repo-list.txt') == False:
        with open(os.getenv('HOME') + '/.config/rodder/repos/master-repo-list.txt', 'w') as f:
            f.write('https://github.com/ruthenic/rodder-repo')
    if os.path.exists(os.getenv('HOME') + '/.local/bin') == False:
        os.makedirs(os.getenv('HOME') + '/.local/bin') #have to throw this in here to fix docker systems
    if sys.argv[1] == "help" or sys.argv[1] == "":
        print("rodder is a package management system\n")
        print("rodder install - installs program from current repos")
        print("rodder update - pulls newest version of repo file")
        print("rodder remove - uninstall program") #god this needs an update, but guess who can't be fucked
        exit()
    elif sys.argv[1] == "update":
        update()
    elif sys.argv[1] == "install":
        install(sys.argv[2]) #rodder install template; sys.argv[2] == template
    elif sys.argv[1] == "remove":
        remove(sys.argv[2])
    elif sys.argv[1] == 'list':
        list()
    elif sys.argv[1] == 'repo': #here is where the code for managing repos starts
        if sys.argv[2] == 'list':
            repo.list
        elif sys.argv[2] == 'add':
            repo.add(sys.argv[3])
            with open(os.getenv('HOME') + '/.config/rodder/repos/master-repo-list.txt', 'a') as f:
                f.write('\n' + repo)
        elif sys.argv[2] == 'reset':
            repo.reset()
        elif sys.argv[2] == 'remove':
            repo.remove(sys.argv[3])
    elif sys.argv[1] == 'search':
        search()
