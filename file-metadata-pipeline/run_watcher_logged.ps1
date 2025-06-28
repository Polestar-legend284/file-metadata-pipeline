$env:PYTHONUNBUFFERED = "1"
python watch_folder.py 2>&1 | Tee-Object -FilePath "watcher_output.log"