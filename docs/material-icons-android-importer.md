# CLI

**Usage**:

```console
$ [OPTIONS] COMMAND [ARGS]...
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

## `fetch-icon`

Fecth a material icon,
converts to Vector Drawable (Android&#x27;s format),
and place it into the proper path in the project,
so that they are available as &quot;@drawable/ic_{name}&quot;

**Usage**:

```console
$ fetch-icon [OPTIONS] ICON_NAME [VARIANT]
```

**Arguments**:

* `ICON_NAME`: Material icon name (e.g., &#x27;settings&#x27;)  [required]
* `[VARIANT]`: Icon style variant  [default: baseline]

**Options**:

* `--flavor TEXT`: Android source set flavor  [default: main]
* `--project-root DIRECTORY`: Android project root directory  [default: .]
* `--help`: Show this message and exit.

## `import-icon`

Convert an svg icon to Vector Drawable (Android&#x27;s format),
and place it into the proper path in the project,
so that they are available as &quot;@drawable/ic_{name}&quot;

**Usage**:

```console
$ import-icon [OPTIONS] ICON_PATH
```

**Arguments**:

* `ICON_PATH`: Material icon svg file  [required]

**Options**:

* `--flavor TEXT`: Android source set flavor  [default: main]
* `--project-root DIRECTORY`: Android project root directory  [default: .]
* `--help`: Show this message and exit.

## `download-icon`

Download a material icon as svg.

**Usage**:

```console
$ download-icon [OPTIONS] ICON_NAME [VARIANT]
```

**Arguments**:

* `ICON_NAME`: Material icon name (e.g., &#x27;settings&#x27;)  [required]
* `[VARIANT]`: Icon style variant  [default: baseline]

**Options**:

* `-o, --output PATH`: Android project root directory
* `--help`: Show this message and exit.

## `list`

Lists all Material Icon ids

**Usage**:

```console
$ list [OPTIONS] [QUERY]
```

**Arguments**:

* `[QUERY]`: id search query for name, category or tags

**Options**:

* `--help`: Show this message and exit.

