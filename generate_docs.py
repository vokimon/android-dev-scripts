#!/usr/bin/env python
"""Generate documentation for all CLI commands from pyproject.toml."""

import subprocess
from pathlib import Path

try:
    import tomllib
except ImportError:
    import tomli as tomllib

from consolemsg import step, success, warn, fail


def main():
    """Generate documentation for all CLI commands."""
    # Parse pyproject.toml
    pyproject = Path("pyproject.toml")
    if not pyproject.exists():
        fail(f"{pyproject} not found")

    with open(pyproject, "rb") as f:
        data = tomllib.load(f)

    scripts = data.get("project", {}).get("scripts", {})
    if not scripts:
        fail("No scripts found in [project.scripts]")

    # Create docs directory
    docs_dir = Path("docs")
    docs_dir.mkdir(exist_ok=True)

    step(f"Generating documentation in {docs_dir}/...")

    # Generate docs for each script
    for cmd_name, module_path in scripts.items():
        # Extract module:app from '"module.path:app"'
        if ":" not in module_path:
            warn(f"Skipping {cmd_name}: invalid module path '{module_path}'")
            continue

        # Extract module path (remove quotes and :startfunction suffix)
        module_app = module_path.strip().strip('"').strip("'")
        module_app = module_app.split(':')[0]

        output_file = docs_dir / f"{cmd_name}.md"

        step(f"→ Generating {output_file}...")

        # Call typer CLI to generate docs
        result = subprocess.run(
            ["typer", module_app, "utils", "docs",
             "--output", str(output_file),
             "--name", cmd_name],
            capture_output=False,
            text=True
        )

        if result.returncode == 0:
            success(f"Generated {output_file}")
        else:
            warn(f"Failed to generate docs for {cmd_name}")

    success(f"Documentation generation complete! See {docs_dir}/")


if __name__ == "__main__":
    main()
