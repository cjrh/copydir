# copydir

Recursively copy a directory tree, with filters.

```batch
 usage: copydir.exe [-h] DIR TARGET_DIR [ignores [ignores ...]]

positional arguments:
  DIR
  TARGET_DIR
  ignores

optional arguments:
  -h, --help  show this help message and exit

```

## Why?

Sometimes you want to make backups of a directory tree which might also 
contain "output" folders with huge amounts of data that should _not_ be
backed up.  `copydir` will make the backup but skip those folders. This 
is quite easy to do on a POSIX-like system, but `copydir` also works on
Windows, which is where it was originally created.
