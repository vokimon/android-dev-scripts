# `mastodon stuter`

CLI mastodon interaction

**Usage**:

```console
$ mastodon stuter [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `post`: Post a markdown thread to Mastodon with...
* `boost`: Boost and favorite a Mastodon post by URL...

## `mastodon stuter post`

Post a markdown thread to Mastodon with media, boosters, and metadata.

**Usage**:

```console
$ mastodon stuter post [OPTIONS] FILE POSTER
```

**Arguments**:

* `FILE`: Markdown file with thread or &#x27;-&#x27; for stdin  [required]
* `POSTER`: Poster account alias  [required]

**Options**:

* `--visibility TEXT`: Override visibility
* `--cw TEXT`: Override content warning
* `--language TEXT`: Override language
* `--sensitive / --no-sensitive`: Override sensitive flag
* `--boosters TEXT`: Optional list of boosters to override YAML
* `--help`: Show this message and exit.

## `mastodon stuter boost`

Boost and favorite a Mastodon post by URL using one or more accounts

**Usage**:

```console
$ mastodon stuter boost [OPTIONS] POST_URL BOOSTERS...
```

**Arguments**:

* `POST_URL`: Public URL of the post to boost/favorite  [required]
* `BOOSTERS...`: One or more account aliases that will boost/favorite  [required]

**Options**:

* `--help`: Show this message and exit.

