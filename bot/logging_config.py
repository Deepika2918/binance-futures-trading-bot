import logging
import os

# logs folder agar na ho to create kar do
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/trading.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)