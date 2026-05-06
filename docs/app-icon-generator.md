# `app-icon-generator.py`

**Usage**:

```console
$ app-icon-generator.py [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `app-icon`: Generates svg app icon from material icon
* `launcher-icon`: Generates adaptative icons for Android...
* `splash`: Generate a simple featureGraphic.svg for...

## `app-icon-generator.py app-icon`

Generates svg app icon from material icon

**Usage**:

```console
$ app-icon-generator.py app-icon [OPTIONS] SVG_PATH
```

**Arguments**:

* `SVG_PATH`: Ruta al archivo SVG del ícono (foreground)  [required]

**Options**:

* `--bg TEXT`: Color de fondo (ej: &#x27;#d69999&#x27;)  [default: #d69999]
* `--fg TEXT`: Color del icono (ej: &#x27;#712b5e&#x27;)  [default: #712b5e]
* `--out,-o PATH`: Output svg file  [default: icon.svg]
* `-s,--size INTEGER`: Size in pixels  [default: 512]
* `--help`: Show this message and exit.

## `app-icon-generator.py launcher-icon`

Generates adaptative icons for Android from a material icon svg.

**Usage**:

```console
$ app-icon-generator.py launcher-icon [OPTIONS] SVG_PATH
```

**Arguments**:

* `SVG_PATH`: Ruta al archivo SVG del ícono (foreground)  [required]

**Options**:

* `--bg TEXT`: Color de fondo (ej: &#x27;#d69999&#x27;)  [default: #d69999]
* `--fg TEXT`: Color del icono (ej: &#x27;#712b5e&#x27;)  [default: #712b5e]
* `--out PATH`: Directorio de salida para recursos  [default: res]
* `--padding INTEGER`: Padding interno en píxeles  [default: 0]
* `--themed / --no-themed`: ¿Incluir ic_launcher_themed.xml para Android 12+?  [default: themed]
* `--minsdk INTEGER`: minSdkVersion de la app  [default: 24]
* `--help`: Show this message and exit.

## `app-icon-generator.py splash`

Generate a simple featureGraphic.svg for Google Play / F-Droid (1024x500)

**Usage**:

```console
$ app-icon-generator.py splash [OPTIONS] APP_NAME SVG_PATH
```

**Arguments**:

* `APP_NAME`: Application name  [required]
* `SVG_PATH`: Material icon svg file (foreground)  [required]

**Options**:

* `--bg TEXT`: Background color  [default: #d69999]
* `--fg TEXT`: Foreground color  [default: #712b5e]
* `--motto TEXT`: Motto under the name  [default: Fill up cheaper, closer]
* `--out PATH`: Output svg  [default: featureGraphic.svg]
* `--help`: Show this message and exit.
