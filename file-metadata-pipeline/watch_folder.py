import time, os
from process_file import process_file
from logger import log

WATCH_DIR = "uploaded_files"
seen = set(os.listdir(WATCH_DIR))
log.info(f"Watching '{WATCH_DIR}' for new files…")

while True:
    current = set(os.listdir(WATCH_DIR))
    for fn in current - seen:
        process_file(os.path.join(WATCH_DIR, fn))
    seen = current
    time.sleep(1)