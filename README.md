# rodder
A distro-independent (or distro-agonistic if you wanna be fancy), non-system package manager with custom repos, similar to Homebrew

# FAQ

## Why "rodder"?
Because a fishing rod grabs fish, similar to how a package manager grabs packages.

# Notes

## PyPI CLI Interface

If you want to run the command line app from the PyPI installer, please use the command
```python -m rodder.rodder [command]```
I've no fucking idea how to fix this, so deal with it I guess.

## PyPI Library

Similarly (although less bad), if you want to import the package and use it, I recommend using
```import rodder.rodder as rodder```
so you can do `rodder.help()`, `rodder.install('package')`, etc. etc.

I'll have some docs up on the library soonish, but it's pretty simple, just look at the code
