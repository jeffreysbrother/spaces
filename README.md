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
