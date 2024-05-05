from datetime import datetime

import kiss
import structlog

log = structlog.get_logger()

# Get current date and time
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

# Generate file name using current date and time
file_name = f"{formatted_datetime}.kissdump"


def kissdump(s):
    log.info("Dumping", file_name=file_name)

    with open(file_name, "ab") as file:
        file.write(s)


if __name__ == "__main__":
    _k = kiss.TCPKISS(host="localhost", port=8001)
    _k.start()
    _k.read(callback=kissdump)
