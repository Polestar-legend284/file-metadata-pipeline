import logging, sys

logging.basicConfig(
  level=logging.INFO,
  format="%(asctime)s %(levelname)s | %(message)s",
  handlers=[
    logging.FileHandler("pipeline.log", mode="w"),
    logging.StreamHandler(sys.stdout)
  ]
)
log = logging.getLogger()