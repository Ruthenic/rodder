function rodder -a job pack -d "Yet Another Fish package manager"
        rodder-setup
        switch $job
                case -S install
                        rodderInternalInstall $pack
                case -R remove uninstall
                        grep -i $pack ~/.config/fish/packs-installed-ever.txt|read packurl
                        string trim -c=: $packurl|read packurl
                        set pack $packurl
                        cd ~/.tmp/rodder
                        git clone $pack src
                        cd src
                        cd functions
                        set del (find ~/.tmp/rodder/src/functions -maxdepth 1 -type f -printf "%f\n")
                        rm ~/.config/fish/functions/$del
                        cd ~
                        rm -rf ~/.tmp/rodder/src
                        set pack (echo $pack| tr "/" -)
                        rm ~/.config/fish/packs/$pack.txt
                        echo "Done!"
                        fish
        end
end
function rodderSetup -d "Setup required directories
        if not test -d ~/.config/fish/packs
                mkdir ~/.config/fish/packs
        end
        if not test -d ~/.tmp/
                mkdir ~/.tmp/
        end
        if not test -d ~/.tmp/rodder
                mkdir ~/.tmp/rodder
        end
endfunction rodderInternalInstall -a pack -d "Install rodder functions (for internal use)"
        cd ~/.tmp/rodder
        git clone $pack src
        cd src
        cd functions
        cp *.fish ~/.config/fish/functions
        cd ~
        echo $pack >> ~/.config/fish/packs-installed-ever.txt
        echo $pack":"|read temp1
        echo (find ~/.tmp/rodder/src/functions -maxdepth 1 -type f -name "*.fish" -printf "%f\n")|read temp3
        echo "end pack"|read temp4
        set pack (echo $pack| tr "/" -)
        touch ~/.config/fish/packs/$pack.txt
        echo $temp1 >> ~/.config/fish/packs/$pack.txt
        echo $temp3 >> ~/.config/fish/packs/$pack.txt
        echo $temp4 >> ~/.config/fish/packs/$pack.txt
        rm -rf ~/.tmp/rodder/src
        echo "Done!"
end

function rodderInternalUpdate -d "Update rodder"
        function rodderInternalInstall -a pack -d "Install rodder functions (for internal use>
        cd ~/.tmp/rodder
        git clone https://github.com/Ruthenic/rodder src
        cd src
        cp *.fish ~/.config/fish/functions
        cd ~
        rm -rf ~/.tmp/rodder/src
        echo "Done!"
end
