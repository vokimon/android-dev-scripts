# `generate-web`

**Usage**:

```console
$ generate-web [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `serve`: Serve the site locally and rebuild on changes
* `build`: Generate the static site
* `publish`: Publish via rsync over SSH

## `generate-web serve`

Serve the site locally and rebuild on changes

**Usage**:

```console
$ generate-web serve [OPTIONS] [DATA_FILE]
```

**Arguments**:

* `[DATA_FILE]`: [default: web-data.yaml]

**Options**:

* `--port INTEGER`: [default: 8000]
* `--help`: Show this message and exit.

## `generate-web build`

Generate the static site

**Usage**:

```console
$ generate-web build [OPTIONS] [DATA_FILE]
```

**Arguments**:

* `[DATA_FILE]`: [default: web-data.yaml]

**Options**:

* `--help`: Show this message and exit.

## `generate-web publish`

Publish via rsync over SSH

**Usage**:

```console
$ generate-web publish [OPTIONS] [DATA_FILE]
```

**Arguments**:

* `[DATA_FILE]`: [default: web-data.yaml]

**Options**:

* `--help`: Show this message and exit.
