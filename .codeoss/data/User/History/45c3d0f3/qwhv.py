cat > ~/file-metadata-pipeline/watch_folder.py << 'EOF'
import time, os
from process_file import process_file

WATCH_DIR = "uploaded_files"
already_seen = set(os.listdir(WATCH_DIR))

print(f"Watching for new files in '{WATCH_DIR}'...")

while True:
cat > ~/file-metadata-pipeline/watch_folder.py << 'EOF'
import time, os
from process_file import process_file

WATCH_DIR = "uploaded_files"
already_seen = set(os.listdir(WATCH_DIR))

print(f"Watching for new files in '{WATCH_DIR}'...")

while True:
    current = set(os.listdir(WATCH_DIR))
    for fname in current - already_seen:
        process_file(os.path.join(WATCH_DIR, fname))
    already_seen = current
    time.sleep(2)
EOF
a    current = set(os.listdir(WATCH_DIR))
    new = current - already_seen
for fname in current - already_seen:
        process_file(os.path.join(WATCH_DIR, fname))
    already_seen = current
    time.sleep(2)
EOF
