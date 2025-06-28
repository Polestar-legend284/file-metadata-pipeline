import os
from logger import log
from db_handler import insert_metadata

def process_file(path):
    name = os.path.basename(path)
    size = os.path.getsize(path)
    ftype = name.split('.')[-1] if '.' in name else ''
    log.info(f"[Processed] {name}, size={size}, type={ftype}")
    insert_metadata(name, size, ftype)