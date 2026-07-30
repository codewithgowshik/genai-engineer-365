import logging

logging.basicConfig(
    level=logging.INFO,# Show messages of INFO level and above(INFO, WARNING, ERROR and CRITICAL will be displayed)

    format="%(asctime)s - %(levelname)s - %(message)s"   # %(asctime)s    -> Current date and time
                                                         # %(levelname)s  -> Type of message (INFO, ERROR, etc.)
                                                         # %(message)s    -> Actual message written by the developer
)

# Third-party libraries log every HTTP call at INFO, which drowns
# out the agent UI. Keep them at WARNING and above.
for noisy in ("httpx", "httpcore", "google_genai", "google.genai"):
    logging.getLogger(noisy).setLevel(logging.WARNING)

# Create a logger object for the current file
logger = logging.getLogger("__name__") # __name__ is automatically replaced with the module name
