#!/usr/bin/bash
#note: this only works on my machine, but i should be the only one running it anyways
cd ~/Coding/Etc/rodder-aur/rodder-git
makepkg
makepkg --printsrcinfo > .SRCINFO
git add PKGBUILD .SRCINFO
git commit
git push
