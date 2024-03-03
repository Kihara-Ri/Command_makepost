# Command_makepost
This is a python script which I'm going to create a markdown file that appends 'Post Front-matter' so that I won't spend more time on this.

This is a script you can execute in command line anywhere you are in, you just need to set the shebang 

```python
#!/usr/bin/env python3
```

to tell the interpreter to execute the python file.

And then you copy the `makepost.py` to the directory `/usr/local/bin` to ensure the global accessable:

```bash
sudo cp makepost.py /usr/local/bin
sudo chmod +x /usr/local/bin/makepost
```

And now you can execute the command like this:

```bash
makepost post <--path optional>
```

Also you are supposed to set the `_post` directory as your own default post directory.