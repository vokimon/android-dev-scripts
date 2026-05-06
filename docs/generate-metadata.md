# `generate-metadata.py`

Generates metadata for packaging and distributing in different platforms
using standard files as single source of truth.

Required project files:


- meta/overrides.yaml: Main configuration and overrides (project name, URLs, categories, motto...)

- README.md: Source for project name (first header) and description (remaining or until &lt;!-- end-of-description --&gt;)

- CHANGES.md: Takes takes the current version and the release notes

- LICENSE: License file (auto-detected via SPDX)

- .git/ for repository info
- meta/translations/*.yaml translated metadata (but en.yaml)

- app/src/main/AndroidManifest.xml OR app/build.gradle(.kts): For package name

- .env: Signing credentials (for F-Droid fingerprint)

- icon.png application icon

- media/*png screenshots (by default extract names as their description)

- media/*md screenshot captions matching screenshot names (if missing use png file names)

- media/promo/*.svg promotional images with place holders for metadata text (banner, splash)



General outputs:



- version.properties with proper version

- meta/translations/en.yaml with updated metadata to translate

- .github/ISSUE_TEMPLATE/bug_report.yml with updated version list

- media/promo/*.svg text updated with metadata by ids (name, description, motto, version...)

- media/promo/*.png from SVG templates



F-Droid outputs:



- Full fastlane structure (descriptions, changelogs, screenshots, icons, featured images)

- meta/&lt;app_id&gt;.yml for F-Droid compilation



Flatpak outputs:



- tools/flatpak/&lt;app_id&gt;.metainfo.xml

- tools/flatpak/&lt;app_id&gt;.desktop



Godot outputs:



- export_presets.cfg

**Usage**:

```console
$ generate-metadata.py [OPTIONS]
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

