```markdown
# File Metadata Pipeline

An end-to-end, local-first file metadata tracking system for Windows.  
Monitors a directory for file events, extracts metadata, stores it in SQLite, and exposes a Flask-powered dashboard and REST API.  
Originally designed for GCP, this version runs entirely on your local machine with a single click via `run.bat`.

## Table of Contents
1. Key Features  
2. Tech Stack  
3. Prerequisites  
4. Installation & Setup  
5. Usage  
6. Project Structure  
7. Script and Module Overview  
8. Configuration  
9. Contributing  

## 1. Key Features
- Directory watcher that monitors a target folder for create/modify/delete events  
- Metadata extraction: size, extension, timestamps, and custom tags  
- Persistent storage in SQLite, managed via `db_handler.py` and verified by `verify_db.py`  
- RESTful API and HTML dashboard served by Flask (`app.py`)  
- Centralized logging through `logger.py`, with output in `pipeline.log` and `watcher_output.log`  
- One-click startup of server and watcher via `run.bat`  

## 2. Tech Stack

| Layer            | Technology                                      |
|------------------|-------------------------------------------------|
| Watcher          | Python (`watch_folder.py`) + PowerShell wrapper (`run_watcher_logged.ps1`) |
| Metadata Process | Python (`process_file.py`)                      |
| Database         | SQLite (`db_handler.py`, `verify_db.py`, `show_db.py`) |
| Backend API      | Python 3.8+ + Flask (`app.py`)                  |
| Frontend         | HTML5, CSS3, JavaScript (`templates/index.html`)|
| Orchestration    | Windows Batch (`run.bat`)                       |
| Logging          | Python Logging module (`logger.py`)             |

## 3. Prerequisites
- Windows 10 or 11  
- PowerShell v5.1 or newer  
- Python 3.8 or newer  
- Git (for cloning the repository)  
- Port 5000 available (configurable in `app.py`)  

## 4. Installation & Setup
1. Clone the repository  
   ```powershell
   git clone https://github.com/Polestar-Legend284/file-metadata-pipeline.git
   cd file-metadata-pipeline
   ```
2. (Optional) Create and activate a virtual environment  
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install Python dependencies  
   ```powershell
   pip install -r requirements.txt
   ```
4. Initialize or verify the database schema  
   ```powershell
   python verify_db.py
   ```
5. Configure the watch folder  
   - Open `run_watcher_logged.ps1` or `watch_folder.py`  
   - Set the watch path variable to your target directory, for example:  
     ```powershell
     $WatchPath = 'C:\Users\dhruv\Downloads\watchme'
     ```

## 5. Usage
1. Start the pipeline  
   ```powershell
   .\run.bat
   ```
   This launches two windows:
   - A PowerShell window running `run_watcher_logged.ps1` and logging to `watcher_output.log`  
   - A Python window running `app.py` in debug mode  
2. Open the dashboard in your browser  
   ```
   http://localhost:5000
   ```
3. API endpoints  
   - `GET /files` — list all file metadata records  
   - `GET /files/<id>` — retrieve metadata for a single record by ID  
4. To stop the pipeline, close both terminal windows or press Ctrl+C in each.

## 6. Project Structure
```
file-metadata-pipeline/
├── app.py
├── db_handler.py
├── logger.py
├── metadata.db
├── process_file.py
├── run.bat
├── run_watcher_logged.ps1
├── show_db.py
├── verify_db.py
├── watch_folder.py
├── watcher_output.log
├── pipeline.log
├── templates/
│   └── index.html
├── uploaded_files/
└── venv/
```

## 7. Script and Module Overview
- **app.py**: Defines Flask routes, renders the HTML dashboard, and serves JSON endpoints.  
- **db_handler.py**: Contains functions to create the `file_metadata` table and perform insert/query operations.  
- **process_file.py**: Extracts file metadata (size, extension, timestamps) and inserts it into the database.  
- **watch_folder.py**: Monitors the configured directory for file events and triggers `process_file.py`.  
- **logger.py**: Sets up the logging configuration to write to `pipeline.log`.  
- **verify_db.py**: Ensures the database schema exists or migrates it if necessary.  
- **show_db.py**: CLI tool to print the contents of `metadata.db` to the console.  
- **run_watcher_logged.ps1**: PowerShell wrapper that runs `watch_folder.py` and logs output to `watcher_output.log`.  
- **run.bat**: Batch script that starts both the Flask server and the PowerShell watcher.

## 8. Configuration
- **Server port**: Edit the `app.run(port=…)` call in `app.py`.  
- **Watch folder path**: Modify the `$WatchPath` variable in `run_watcher_logged.ps1` or directly in `watch_folder.py`.  
- **Database file**: Change the `DB` variable in `app.py` and `db_handler.py` if you want to use a different file or location.  
- **Logging level**: Adjust the level (`DEBUG`, `INFO`, `WARNING`, `ERROR`) in `logger.py`.

## 9. Contributing
If you’d like to contribute improvements or fixes:
1. Fork the repository, then clone your fork.  
2. Create a feature branch:  
   ```bash
   git checkout -b feature/my-feature
   ```
3. Make your changes and test locally.  
4. Commit with a clear message:  
   ```bash
   git commit -m "Add feature: custom metadata tags"
   ```
5. Push your branch and open a pull request. Describe your changes and motivation.

Your feedback and contributions are welcome!
``