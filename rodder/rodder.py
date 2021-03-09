#!/usr/bin/python
import sys,subprocess,os,shutil,pygit2
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
                #print(subprocess.check_output('git clone ' + line.replace('\n', '') + ' ' + os.getenv('HOME') + '/.tmp/rodder/' + line.rsplit('/', 1)[-1], shell=True))
                try:
                    shutil.rmtree(os.getenv('HOME') + '/.tmp/rodder/' + line.rsplit('/', 1)[-1].replace('\n', ''))
                except Exception as e:
                    #print(os.getenv('HOME') + '/.tmp/rodder/' + line.rsplit('/', 1)[-1].replace('\n', ''))
                    #print('error: couldn\'t delete old tmp dir')
                    pass
                pygit2.clone_repository(line.replace('\n', ''), os.getenv('HOME') + '/.tmp/rodder/' + line.rsplit('/', 1)[-1].replace('\n', ''))
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
    #ugh, i wish i knew of a way to do this by returning things, but that would require a huge overhaul
    #also for installation and stuff it doesn't really matter
    #package = sys.argv[2] #rodder install template; sys.argv[2] == template
    tmp = os.listdir(os.getenv('HOME') + '/.config/rodder/repos/')
    for i in tmp:
        if os.path.isdir(os.getenv('HOME') + '/.config/rodder/repos/' + i) == False and i != 'master-repo-list.txt':
            with open(os.getenv('HOME') + '/.config/rodder/repos/' + i) as f:
                for line in f:
                    if line.split(';')[0] == package: #checks if "template" == line (in this case, template;install.py;uninstall.py) split by the semicolons, and the first thing in the array is what it is compared against
                        exec(open(os.getenv('HOME') + '/.config/rodder/repos/' + line.split(';')[1].replace('\n', '')).read())
                        isPackageInstalled = True
                        #exit() #uh, this shouldn't cause any problems? right? maybe?
                        #Narrator: It did.
                        #this like, double breaks packages with the same name in multiple repos, but that would probably require a complete rework of this code anyway, so ¯\_(ツ)_/¯
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
                        #exit() #see install code for my comments on this exit()
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
    ret_list = []
    for i in tmp:
        if os.path.isdir(os.getenv('HOME') + '/.config/rodder/repos/' + i) == False and i != 'master-repo-list.txt' and i.endswith('.desc.txt'):
            with open(os.getenv('HOME') + '/.config/rodder/repos/' + i) as f:
                print("Packages in " + i.split('.')[0] + ":") #TODO?: make dict, so we can return repos and packages? would make harder to parse though
                for line in f:
                    ret_list.append(line.split(';')[0])
                    print(line.split(';')[0]) #i mean, there is no reason for not printing as long as we still return something
    return ret_list
def get_package_metadata(pkg):
    tmp = os.listdir(os.getenv('HOME') + '/.config/rodder/repos/')
    for i in tmp:
        if os.path.isdir(os.getenv('HOME') + '/.config/rodder/repos/' + i) == False and i != 'master-repo-list.txt':
            with open(os.getenv('HOME') + '/.config/rodder/repos/' + i) as f:
                for line in f:
                    if line.split(';')[0] == pkg:
                        metadata = {}
                        with open(os.getenv('HOME') + '/.config/rodder/repos/' + line.split(';')[3].replace('\n', '')) as f:
                            for line in f:
                                line = line.strip()
                                try:
                                    metadata[line.split(':')[0].strip()] = line.split(':')[1].strip()
                                except:
                                    pass #DAMN YOU TRAILING NEWLINES
    return metadata

class repo():
    def list():
        ret_list = []
        with open(os.getenv('HOME') + '/.config/rodder/repos/master-repo-list.txt') as f:
            for line in f:
                ret_list.append(line.split('/')[len(line.split('/'))-1])
        return ret_list
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
            f.write('\n' + str(repo))
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
    ret_package = ''
    for i in tmp:
        if os.path.isdir(os.getenv('HOME') + '/.config/rodder/repos/' + i) == False and i != 'master-repo-list.txt':
            with open(os.getenv('HOME') + '/.config/rodder/repos/' + i) as f:
                for line in f:
                    if package in line:
                        print('{} - {}'.format(line.split(';')[0], i.split('.')[0]))
                        ret_package = line.split(';')[0]
                        break #idk if this makes a difference
    return ret_package

#start cli tool (which is unable to be used correctly for some reason)
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
        print(">< Installing {}...\n\n".format(sys.argv[2]))
        while True:
            metadata = get_package_metadata(sys.argv[2])
            package = sys.argv[2]
            confirm = input("Are you sure you want to install {}:{}? [y/n] ".format(sys.argv[2],metadata['version']))
            confirm = confirm.strip()
            if confirm.lower() == 'y':
                install(package) #rodder install template; sys.argv[2] == template
                break
            elif confirm.lower() == 'n':
                print(">< Exiting...")
                exit()
            else:
                print(">< Invalid input!")
    elif sys.argv[1] == "remove":
        print(">< Removing {}...\n\n".format(sys.argv[2]))
        while True:
            metadata = get_package_metadata(sys.argv[2])
            package = sys.argv[2]
            confirm = input("Are you sure you want to remove {}:{}? [y/n] ".format(sys.argv[2],metadata['version']))
            confirm = confirm.strip()
            if confirm.lower() == 'y':
                remove(package) #rodder install template; sys.argv[2] == template
                break
            elif confirm.lower() == 'n':
                print(">< Exiting...")
                exit()
            else:
                print(">< Invalid input!")
    elif sys.argv[1] == 'list':
        list() #once again, we don't need the for list because we return, as well as print now
        #for i in list():
            #print(i)
    elif sys.argv[1] == 'repo': #here is where the code for managing repos starts
        if sys.argv[2] == 'list':
            for i in repo.list():
                print(i)
        elif sys.argv[2] == 'add':
            repo.add(sys.argv[3])
        elif sys.argv[2] == 'reset':
            repo.reset()
        elif sys.argv[2] == 'remove':
            repo.remove(sys.argv[3])
    elif sys.argv[1] == 'search':
        print(search())
