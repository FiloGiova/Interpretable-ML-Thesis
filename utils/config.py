import time

# MAIN Absolute Path
main_path = "/<INSERT_FULL_PATH_TO_REPO_FOLDER>/tami/"
# Timestamp Execution
timeExec = "{}".format(time.strftime("%d%m_%H%M%S"))
# Database in use
database = "MalRadar" # or "CIC_2017"

# GLOBAL variables
AUTOTUNE, CHANNELS, IMG_DIM, VECTOR_DIM, CLASS_NAMES, BATCH_SIZE, DATA_REQ = None, None, None, None, None, None, None
