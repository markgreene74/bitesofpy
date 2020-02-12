# https://codechalleng.es/bites/233/
# # https://docs.python.org/3/library/zipfile.html
from datetime import datetime
from pathlib import Path, PosixPath
from zipfile import ZipFile
from glob import glob
from os import path

TMP = Path("/tmp")
LOG_DIR = TMP / "logs"
ZIP_FILE = "logs.zip"


def zip_last_n_files(
    directory: PosixPath = LOG_DIR, zip_file: str = ZIP_FILE, n: int = 3
):
    log_files = glob(directory.joinpath("*.log").as_posix())
    sorted_log_files = sorted(log_files, key=path.getmtime)
    with ZipFile(zip_file, "w") as myzip:
        for i in sorted_log_files[-n:]:
            file_mtime = datetime.fromtimestamp(path.getmtime(i)).date()
            old_filename = Path(i).name.split(".")[0]
            new_filename = old_filename + f"_{str(file_mtime)}.log"
            myzip.write(i, new_filename)

