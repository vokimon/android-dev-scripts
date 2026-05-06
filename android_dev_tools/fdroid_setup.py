#!/usr/bin/env python
"""Sets up or starts a local F-Droid build environment."""

import os
import sys
import subprocess
from pathlib import Path
from dotenv import load_dotenv
from consolemsg import step, warn, fail, error, success
import typer

app = typer.Typer(help=__doc__)

FROID_BUILD_SCRIPT = """\
# Should be run inside
# docker run --rm -itu vagrant --entrypoint /bin/bash   -v $(pwd):/build:z   -v $HOME/Documents/godot/fdroidserver:/home/vagrant/fdroidserver:Z   registry.gitlab.com/fdroid/fdroidserver:buildserver
APP_ID={app_id}
run() {{
    echo -e "\\033[34;1m== $*\\033[0m"
    "$@"
}}

df -h
. /etc/profile
export serverwebroot=$(pwd)/build
run echo $serverwebroot
export PATH="$fdroidserver:$PATH" PYTHONPATH="$fdroidserver"
export JAVA_HOME=$(java -XshowSettings:properties -version 2>&1 > /dev/null | grep 'java.home' | awk -F'=' '{{print $2}}' | tr -d ' ')
run sudo bash /home/vagrant/fdroidserver/buildserver/provision-gradle
run sdkmanager --install "platform-tools" "build-tools;36.0.0" "platforms;android-36" "cmdline-tools;latest" "cmake;3.10.2.4988404" "ndk;23.2.8568313"
#run sudo apt-get update -y
#run sudo apt-get install -y pkgconf clang scons imagemagick python3-pip python-is-python3 apksigner
cd /build
run fdroid readmeta -v
run fdroid rewritemeta -v $APP_ID
run fdroid lint -v $APP_ID
run fdroid checkupdates -v --auto --allow-dirty $APP_ID
run fdroid build -vl $APP_ID
"""

def run(*args, **kwargs):
    step(' '.join(args))
    result = subprocess.run(args, capture_output=False, text=True, **kwargs)
    if result.returncode != 0:
        fail(f"Command failed with return code {result.returncode}")
    return True

def try_run(*args, **kwargs):
    step(' '.join(args))
    result = subprocess.run(args, capture_output=False, text=True, **kwargs)
    return result.returncode == 0

@app.command()
def main(
    yaml_file: Path = typer.Argument(..., exists=True, resolve_path=True, help="Path to app.yml metadata file"),
    gitlab_user: str = typer.Argument(None, help="GitLab username (overrides .env)"),
):
    """Sets up or starts a local F-Droid build environment."""
    base_dir = yaml_file.parent
    fdroid_server_path = base_dir / "fdroid-server"
    fdroid_data_path = base_dir / "fdroid-data"
    app_id = yaml_file.stem  # basename without .yml

    if Path(".env").exists():
        load_dotenv()

    # Fallback gitlab_user to environment or fail
    if not gitlab_user:
        gitlab_user = os.environ.get("GITLAB_USER", "")

    if not gitlab_user:
        fail(
            "GITLAB_USER not defined. "
            "Provide as argument, set environment variable, or add to .env (cwd)"
        )

    # Check/install docker
    if not try_run("which", "docker"):
        step("Installing docker...")
        run("sudo", "sh", "-c", "apt-get update && apt-get install -y docker.io")

    os.chdir(base_dir)

    # Clone fdroid-server if needed
    if not fdroid_server_path.exists():
        run("git", "clone", "--depth=1", "https://gitlab.com/fdroid/fdroidserver", str(fdroid_server_path))

    # Clone fdroiddata if needed
    if not fdroid_data_path.exists():
        run("git", "clone", "--depth=100", f"git@gitlab.com:{gitlab_user}/fdroiddata.git", str(fdroid_data_path))
        os.chdir(fdroid_data_path)
        run("git", "remote", "set-branches", "origin", app_id)
        if not try_run("git", "fetch", "origin", app_id) or not try_run("git", "checkout", app_id):
            run("git", "checkout", "-b", app_id)
        os.chdir(base_dir)

    # Remove old files
    for f in [fdroid_data_path / "fdroid-build.sh", fdroid_data_path / "metadata" / f"{app_id}.yml"]:
        if f.exists() or f.is_symlink():
            f.unlink()

    # Generate fdroid-build.sh
    build_script = fdroid_data_path / "fdroid-build.sh"
    build_script.write_text(FROID_BUILD_SCRIPT.format(app_id=app_id))
    build_script.chmod(0o755)
    success(f"Generated {build_script}")

    # Hard link the YAML file
    metadata_dir = fdroid_data_path / "metadata"
    metadata_dir.mkdir(exist_ok=True)
    hardlink_target = metadata_dir / f"{app_id}.yml"
    if hardlink_target.exists():
        hardlink_target.unlink()
    os.link(yaml_file, hardlink_target)
    success(f"Hard linked {yaml_file} -> {hardlink_target}")

    # Set ownership
    for path in [fdroid_data_path, fdroid_server_path]:
        run("sudo", "chown", "-R", "1000:1000", str(path))

    step("Inside the docker you usually run build/fdroid-build.sh or any part of it")

    # Run docker
    try_run(
        "docker", "run", "--rm",
        "-itu", "vagrant",
        "--entrypoint", "/bin/bash",
        "-v", f"{fdroid_data_path}:/build:z",
        "-v", f"{fdroid_server_path}:/home/vagrant/fdroidserver:Z",
        "registry.gitlab.com/fdroid/fdroidserver:buildserver",
    )

    # Restore ownership
    run("sudo", "chown", "-R", f"{os.getuid()}:{os.getgid()}", str(fdroid_data_path), str(fdroid_server_path))
    success("F-Droid setup complete")

if __name__ == "__main__":
    app()
