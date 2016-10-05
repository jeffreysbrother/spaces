#Spaces

To make this script executable and accessible globally we must follow these instructions:

###OSX and Linux (POSIX systems)

Navigate to the home directory:

```bash
cd
```

If there is no `bin/` directory here, create one:

```bash
mkdir bin
```

Ensure that `bin/` is in the `$PATH` variable. Open the file `.bash_profile` (located in the home directory) and add this line, if necessary:

```bash
PATH=$PATH:$HOME/bin
```

Reload your profile by typing this:

```bash
source ~/.bash_profile
```

Now, simply drop a script into the `/bin` folder (it does not need to have the `.py` extension) Finally, make this file executable by running:

```bash
chmod +x scriptname.py
```

The steps listed above were taken from suggestions [here](https://shapeshed.com/using-custom-shell-scripts-on-osx-or-linux/). After a bit of experimentation and research, it appears that there are a few more things we must do:

Determine where python resides:

```bash
which python
```

When I run this command, I see `/usr/bin/python`. This means that we must add the following line to the script in question:

```bash
#!/usr/bin/python
```

If every step is complete, we should be able to run the **spaces** program by simply running the command `spaces` in the desired directory (given that our python file is named "spaces". If it were named "spaces.py", then we'd simply have to run "spaces.py").

###Additional Notes

The preceding steps instruct us to add our scripts into the root of the `bin/` directory. It might, however, be useful to add subdirectories here---each being individually and independently version controlled. To carry this out, it might be the case that we must merely ensure that `/bin/{subdir}` is in the `$PATH` variable (as opposed to `bin/`), but I am unsure of this.

It might also be beneficial to create a `scripts/` directory for all scripts we intend to run in this way (independent of the directory devoted to web projects, if one exists), and then generate a symbolic link to the `bin/` subdirectory. There is some info on this [here](http://apple.stackexchange.com/questions/115646/how-can-i-create-a-symbolic-link-in-terminal), but again, I am unsure of this as well.
