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

* `serve`: Serve the site locally and rebuild on changes
* `build`: Generate the static site
* `publish`: Publish via rsync over SSH

## `serve`

Serve the site locally and rebuild on changes

**Usage**:

```console
$ serve [OPTIONS] [DATA_FILE]
```

**Arguments**:

* `[DATA_FILE]`: [default: web-data.yaml]

**Options**:

* `--port INTEGER`: [default: 8000]
* `--help`: Show this message and exit.

## `build`

Generate the static site

**Usage**:

```console
$ build [OPTIONS] [DATA_FILE]
```

**Arguments**:

* `[DATA_FILE]`: [default: web-data.yaml]

**Options**:

* `--help`: Show this message and exit.

## `publish`

Publish via rsync over SSH

**Usage**:

```console
$ publish [OPTIONS] [DATA_FILE]
```

**Arguments**:

* `[DATA_FILE]`: [default: web-data.yaml]

**Options**:

* `--help`: Show this message and exit.

