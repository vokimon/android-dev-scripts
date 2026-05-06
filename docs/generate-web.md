# `generate-web.py`

**Usage**:

```console
$ generate-web.py [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `serve`: Serve the site locally and rebuild on changes
* `build`: Generate the static site
* `publish`: Publish via rsync over SSH

## `generate-web.py serve`

Serve the site locally and rebuild on changes

**Usage**:

```console
$ generate-web.py serve [OPTIONS] [DATA_FILE]
```

**Arguments**:

* `[DATA_FILE]`: [default: web-data.yaml]

**Options**:

* `--port INTEGER`: [default: 8000]
* `--help`: Show this message and exit.

## `generate-web.py build`

Generate the static site

**Usage**:

```console
$ generate-web.py build [OPTIONS] [DATA_FILE]
```

**Arguments**:

* `[DATA_FILE]`: [default: web-data.yaml]

**Options**:

* `--help`: Show this message and exit.

## `generate-web.py publish`

Publish via rsync over SSH

**Usage**:

```console
$ generate-web.py publish [OPTIONS] [DATA_FILE]
```

**Arguments**:

* `[DATA_FILE]`: [default: web-data.yaml]

**Options**:

* `--help`: Show this message and exit.
