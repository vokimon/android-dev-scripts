# `yaml-translations.py`

Management tools for YAML translation files.

YAML translations are stored as individual files for each language,
(ie, ru.yaml for russian), inside a directory for a single module or component.

Usually one of the languages is considered the reference one, usually &#x27;en&#x27;.

YAML&#x27;s contain a dictionary where keys are the ids to refer them.
Nested dictionaries are interpreted as namespaces.

A different multilingual yaml format is often used for transfers.
It contains structures ID-&gt;lang-&gt;text.

**Usage**:

```console
$ yaml-translations.py [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `extract`: Extract translations from per-language...
* `distribute`: Distribute translations from a...
* `sync`: Align translation files with the reference...
* `rename`: Renames a text id in all the translation...
* `move`: Move translation keys or namespaces from...
* `andaluh`: Generate Andalûh (&#x27;and&#x27;) translations from...
* `to-json`: Convert YAML translation files to JSON.
* `from-json`: Convert JSON translation files to YAML.
* `blockify`: Format multiline values as block style.
* `flowify`: Convert strings in YAML to flow style,...
* `find`: Find usages of translation IDs in source...

## `yaml-translations.py extract`

Extract translations from per-language YAMLs into a multilingual YAML.

Output format: id -&gt; lang -&gt; text (flattened keys).

**Usage**:

```console
$ yaml-translations.py extract [OPTIONS] INPUT_DIR [IDS]... OUTPUT_YAML
```

**Arguments**:

* `INPUT_DIR`: Directory with per-language YAML files  [required]
* `[IDS]...`: IDs or prefixes to extract (all if omitted)
* `OUTPUT_YAML`: Output YAML file for extracted translations  [required]

**Options**:

* `--help`: Show this message and exit.

## `yaml-translations.py distribute`

Distribute translations from a multilingual YAML into per-language files.

Input format: id -&gt; lang -&gt; text (flattened keys).

**Usage**:

```console
$ yaml-translations.py distribute [OPTIONS] INPUT_YAML OUTPUT_DIR
```

**Arguments**:

* `INPUT_YAML`: YAML with id -&gt; lang -&gt; translation  [required]
* `OUTPUT_DIR`: Directory with per language YAML translation files  [required]

**Options**:

* `--help`: Show this message and exit.

## `yaml-translations.py sync`

Align translation files with the reference language.

- Orders keys like the reference

- Uses yaml text formating used in reference language file

- Reports or optionally adds/remove missing and extra keys



Each file uses the reference language from its own directory.

**Usage**:

```console
$ yaml-translations.py sync [OPTIONS] YAMLS...
```

**Arguments**:

* `YAMLS...`: Directory containing translation yamls or specific yamls to process  [required]

**Options**:

* `--ref TEXT`: Reference language  [default: en]
* `--add-missing`: Add missing ids from reference language with an empty string ready to fill
* `--remove-extra`: Remove ids not in the reference language
* `--help`: Show this message and exit.

## `yaml-translations.py rename`

Renames a text id in all the translation files

**Usage**:

```console
$ yaml-translations.py rename [OPTIONS] PATH OLD_ID NEW_ID
```

**Arguments**:

* `PATH`: Directory with YAML files  [required]
* `OLD_ID`: Old translation key  [required]
* `NEW_ID`: New translation key  [required]

**Options**:

* `--help`: Show this message and exit.

## `yaml-translations.py move`

Move translation keys or namespaces from source to destination module.

**Usage**:

```console
$ yaml-translations.py move [OPTIONS] SRC_DIR DST_DIR IDS...
```

**Arguments**:

* `SRC_DIR`: Source translation directory  [required]
* `DST_DIR`: Destination translation directory  [required]
* `IDS...`: IDs or namespaces to move  [required]

**Options**:

* `--help`: Show this message and exit.

## `yaml-translations.py andaluh`

Generate Andalûh (&#x27;and&#x27;) translations from Spanish (&#x27;es&#x27;) file.

The use of &#x27;and&#x27; code is an abuse of a seldomly used code for
Papuan Anzu language until Andalûh gets its own.

**Usage**:

```console
$ yaml-translations.py andaluh [OPTIONS] PATH
```

**Arguments**:

* `PATH`: Directory with translation YAML files  [required]

**Options**:

* `--overwrite`: Overwrite existing translations in destination language
* `--help`: Show this message and exit.

## `yaml-translations.py to-json`

Convert YAML translation files to JSON.

**Usage**:

```console
$ yaml-translations.py to-json [OPTIONS] PATHS...
```

**Arguments**:

* `PATHS...`: YAML files or directories  [required]

**Options**:

* `--help`: Show this message and exit.

## `yaml-translations.py from-json`

Convert JSON translation files to YAML.

**Usage**:

```console
$ yaml-translations.py from-json [OPTIONS] PATHS...
```

**Arguments**:

* `PATHS...`: JSON files or directories  [required]

**Options**:

* `--help`: Show this message and exit.

## `yaml-translations.py blockify`

Format multiline values as block style. Single line are kept unless forced.

**Usage**:

```console
$ yaml-translations.py blockify [OPTIONS] PATH [IDS]...
```

**Arguments**:

* `PATH`: YAML file or directory  [required]
* `[IDS]...`: IDs or namespaces to process (all if omitted)

**Options**:

* `--force`: Convert also single-line strings
* `--help`: Show this message and exit.

## `yaml-translations.py flowify`

Convert strings in YAML to flow style, Multiline are kept unless forced.

**Usage**:

```console
$ yaml-translations.py flowify [OPTIONS] PATH [IDS]...
```

**Arguments**:

* `PATH`: YAML file or directory  [required]
* `[IDS]...`: IDs or namespaces to process (all if omitted)

**Options**:

* `--force`: Convert also multi-line
* `--help`: Show this message and exit.

## `yaml-translations.py find`

Find usages of translation IDs in source files.

**Usage**:

```console
$ yaml-translations.py find [OPTIONS] PATH [IDS]...
```

**Arguments**:

* `PATH`: Directory with translations or a specific YAML file  [required]
* `[IDS]...`: IDs to search (all if omitted)

**Options**:

* `--ref TEXT`: Reference language  [default: en]
* `-x TEXT`: Directories to exclude
* `-s TEXT`: File suffixes to include
* `--only-missing`: Show only IDs with no occurrences
* `--help`: Show this message and exit.
