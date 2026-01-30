import shutil
from datetime import datetime
from pathlib import Path


def create_backup(source_path, destination_path):
    source = Path(source_path)
    destination = Path(destination_path)

    if not source.exists():
        raise FileNotFoundError("Source folder does not exist")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_folder = destination / f"backup_{timestamp}"

    backup_folder.mkdir(parents=True, exist_ok=False)

    shutil.copytree(source, backup_folder / source.name)

    return backup_folder

