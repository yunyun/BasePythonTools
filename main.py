import argparse
import logging
import time

from app.controller.MainController import MainController
from lib.base import beginLogsStart

if __name__ == "__main__":
    beginLogsStart()
    print("run is running.")
    logging.info("run is running.")
    start = time.time()
    # begin someting

    mainCon = MainController()
    mainCon.Main()

    # end someting
    end = time.time()
    totalTime = end - start
    print(f"Finished in {totalTime}")
    logging.info(f"Finished in {totalTime}")

