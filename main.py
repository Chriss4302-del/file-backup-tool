import argparse
import sys

from backup import create_backup
from logger import setup_logger.


def main():
    parser = argparse.ArgumentParser(description="Simple folder backup tool")
    parser.add_argument("-s", "--source", required=True)
    parser.add_argument("-d", "--destination", required=True)
    args = parser.parse_args()

    logger = setup_logger()

    try:
        backup_folder = create_backup(args.source, args.destination)
        logger.info(f"Backup created at {backup_folder}")
    except Exception as e:
        logger.error(f"Backup failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
