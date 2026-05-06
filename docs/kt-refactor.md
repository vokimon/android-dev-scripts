# `kt-refactor.py`

A general Kotlin refactoring tool.

**Usage**:

```console
$ kt-refactor.py [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `move`: Moves kotlin artifacts between packages or...
* `noop`: Dummy command to force move to be a...

## `kt-refactor.py move`

Moves kotlin artifacts between packages or modules adapting imports.



Usage:

  File move:   kt-refactor move &lt;source_file&gt; &lt;target_dir&gt; 

  File rename: kt-refactor move &lt;source_file&gt; &lt;target_file.kt&gt; 

  Symbol only: kt-refactor move &lt;old_fully_qualified_name&gt; &lt;new_fully_qualified_name&gt;



Examples:

  kt-refactor move app/src/main/java/net/canvoki/carburoid/ui/settings/LinkPreference.kt app/src/main/java/net/canvoki/shared/component/preferences/ OtherSymbol ExtraSymbol

  kt-refactor move app/src/main/java/net/canvoki/carburoid/ui/settings/OldName.kt app/src/main/java/net/canvoki/shared/component/preferences/NewName.kt

  kt-refactor move net.canvoki.carburoid.ui.settings.LinkPreference net.canvoki.shared.component.preferences.LinkPreference

**Usage**:

```console
$ kt-refactor.py move [OPTIONS] SOURCE TARGET [SYMBOLS]...
```

**Arguments**:

* `SOURCE`: Source file path or old fully-qualified name  [required]
* `TARGET`: Target directory/file path or new fully-qualified name  [required]
* `[SYMBOLS]...`: Additional symbols to update besides the one named like the file

**Options**:

* `--help`: Show this message and exit.

## `kt-refactor.py noop`

Dummy command to force move to be a subcommand

**Usage**:

```console
$ kt-refactor.py noop [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.
