#Spaces

Running this script updates the file names within the current working directory by replacing spaces with hyphens and uppercase characters with lowercase ones. To make this script executable and accessible globally, we must follow the following instructions.

> Note: we assume the use of Zsh. If you are using bash, the steps will be different. If this is the case, it will be beneficial to first understand the differences between the way OSX and Linux use the various bash shell config files.  I, personally, use [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh) (a Zsh configuration management framework) and these instructions appear to work just fine on both OSX (El Capitan) and Ubuntu (16.04 LTS).

###OSX and Linux (POSIX systems)

Navigate to the home directory (`/Users/{username}` on OSX, `/home/{username}` on Linux):

```bash
cd
```

If there is no `bin/` directory here, create one:

```bash
mkdir bin
```

We must now ensure that `bin/` is in the `$PATH` variable. Open the file `.zshrc` which is located in the home (~) directory. If it does not exist, simply create it. Then, add this line:

```bash
PATH=$PATH:$HOME/bin
```

If this is a newly-created file, you might need to refresh it by typing `source ~/.zshrc` or simply `. ~/.zshrc`

Now, simply drop a script into the `/bin` folder (with or without the `.py` extension) Finally, make this file executable by running:

```bash
chmod +x scriptname
```

The steps listed above were taken from suggestions [here](https://shapeshed.com/using-custom-shell-scripts-on-osx-or-linux/). After a bit of experimentation and research, it appears that there are a few *additional* steps we must carry out:

Determine where python resides (?):

```bash
which python
```

When I run this command, I see `/usr/bin/python`. This means that we must add the following line to the script in question:

```bash
#!/usr/bin/python
```

If every step is complete, we should be able to run the **spaces** program by simply typing the command `spaces` in the desired directory (given that our python file is named "spaces". If it were named "spaces.py", then we'd simply have to run "spaces.py").

###Additional Notes

The preceding steps instruct us to add our scripts into the root of the `bin/` directory. It might, however, be useful to add subdirectories here---each being individually and independently version-controlled. To carry this out, perhaps we must merely ensure that `/bin/{subdir}` is in the `$PATH` variable (as opposed to `bin/`), but I am unsure of this.

It might also be beneficial to create a `scripts/` directory for all scripts we intend to run in this way (independent of the directory devoted to web projects, if one exists), and then generate a symbolic link to the `bin/` subdirectory. If we did this, we'd be left with something like this:

1. `~/sites` for web development projects
2. `~/scripts` for globally-executable scripts
3. `~/bin/{subdir}` as the target of symbolic links stemming from (2)

There is some info on this [here](http://apple.stackexchange.com/questions/115646/how-can-i-create-a-symbolic-link-in-terminal), but again, I am unsure of this as well.
