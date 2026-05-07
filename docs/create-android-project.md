# `create-android-project`

Create a minimal Android Kotlin project structure from CLI.

**Usage**:

```console
$ create-android-project [OPTIONS] [PACKAGE_NAME] [PROJECT_NAME]
```

**Arguments**:

* `[PACKAGE_NAME]`: Android package name (e.g., com.example.app)
* `[PROJECT_NAME]`: Project display name

**Options**:

* `--release-store-file TEXT`: Path to release keystore file
* `--release-store-password TEXT`: Keystore password
* `--release-key-alias TEXT`: Key alias
* `--release-key-password TEXT`: Key password
* `--author-name TEXT`: Author name
* `--author-company TEXT`: Author company
* `--author-role TEXT`: Author role
* `--author-city TEXT`: Author city
* `--author-state TEXT`: Author state
* `--author-country TEXT`: Author country ISO code
* `--icon TEXT`: Launcher icon: &#x27;default&#x27; (generated), path to SVG file, or Material Icon ID
* `--icon-bg TEXT`: Launcher icon background color
* `--icon-fg TEXT`: Launcher icon foreground color
* `--help`: Show this message and exit.
