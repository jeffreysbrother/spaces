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

###Symbolic links

In the previous steps, I suggest adding our scripts to the root of the `bin/` directory. This would, in most cases, require us to *move* or *copy* a file that was created elsewhere (in some development directory, perhaps). To avoid duplication, we can create a symlink from a dedicated project folder to our `bin/` directory by running this in the command line:

```bash
ln -s /path/to/original /path/to/symlink
```
