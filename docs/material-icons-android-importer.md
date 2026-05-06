# `material-icons-android-importer.py`

**Usage**:

```console
$ material-icons-android-importer.py [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `fetch-icon`: Fecth a material icon, converts to Vector...
* `import-icon`: Convert an svg icon to Vector Drawable...
* `download-icon`: Download a material icon as svg.
* `list`: Lists all Material Icon ids

## `material-icons-android-importer.py fetch-icon`

Fecth a material icon,
converts to Vector Drawable (Android&#x27;s format),
and place it into the proper path in the project,
so that they are available as &quot;@drawable/ic_{name}&quot;

**Usage**:

```console
$ material-icons-android-importer.py fetch-icon [OPTIONS] ICON_NAME [VARIANT]
```

**Arguments**:

* `ICON_NAME`: Material icon name (e.g., &#x27;settings&#x27;)  [required]
* `[VARIANT]`: Icon style variant  [default: baseline]

**Options**:

* `--flavor TEXT`: Android source set flavor  [default: main]
* `--project-root DIRECTORY`: Android project root directory  [default: .]
* `--help`: Show this message and exit.

## `material-icons-android-importer.py import-icon`

Convert an svg icon to Vector Drawable (Android&#x27;s format),
and place it into the proper path in the project,
so that they are available as &quot;@drawable/ic_{name}&quot;

**Usage**:

```console
$ material-icons-android-importer.py import-icon [OPTIONS] ICON_PATH
```

**Arguments**:

* `ICON_PATH`: Material icon svg file  [required]

**Options**:

* `--flavor TEXT`: Android source set flavor  [default: main]
* `--project-root DIRECTORY`: Android project root directory  [default: .]
* `--help`: Show this message and exit.

## `material-icons-android-importer.py download-icon`

Download a material icon as svg.

**Usage**:

```console
$ material-icons-android-importer.py download-icon [OPTIONS] ICON_NAME [VARIANT]
```

**Arguments**:

* `ICON_NAME`: Material icon name (e.g., &#x27;settings&#x27;)  [required]
* `[VARIANT]`: Icon style variant  [default: baseline]

**Options**:

* `-o, --output PATH`: Android project root directory
* `--help`: Show this message and exit.

## `material-icons-android-importer.py list`

Lists all Material Icon ids

**Usage**:

```console
$ material-icons-android-importer.py list [OPTIONS] [QUERY]
```

**Arguments**:

* `[QUERY]`: id search query for name, category or tags

**Options**:

* `--help`: Show this message and exit.
