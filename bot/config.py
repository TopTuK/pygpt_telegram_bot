import os
import yaml
from dotenv import load_dotenv
from pathlib import Path
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

DEBUG = True

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load yaml config
with open(config_dir / "config.yml", 'r') as f:
    config_yaml = yaml.safe_load(f)

# load .env config
load_dotenv()

# config parameters
telegram_token = os.getenv('TELEGRAM_TOKEN') or 'wow_so_secret'
openai_api_key = os.getenv('OPEN_AI_KEY') or 'wow_so_secret'
if DEBUG:
    logger.info(f'TG_telegram_tokenTOKEN: {telegram_token} openai_api_key: {openai_api_key}')

# leave null to use default api base or you can put your own base url here
_api_base = os.getenv('OPEN_AI_API_BASE') or ''
openai_api_base = None if _api_base == '' else _api_base
if DEBUG:
    logger.info(f'openai_api_base: {openai_api_base}')

# new dialog starts after timeout (in seconds)
_dialog_timout = os.getenv('DIALOG_TIMEOUT')
new_dialog_timeout = int(_dialog_timout) if _dialog_timout else 600
if DEBUG:
    logger.info(f'new_dialog_timeout: {new_dialog_timeout}')

# if set, messages will be shown to user word-by-word
enable_message_streaming = True if os.getenv('ENABLE_MESSAGE_STREAMING') == 'True' else False
if DEBUG:
    logger.info(f'enable_message_streaming: {enable_message_streaming}')

_generated_images_count = os.getenv('GENERATE_IMAGES_COUNT')
return_n_generated_images = int(_generated_images_count) if _generated_images_count else 1
if DEBUG:
    logger.info(f'return_n_generated_images: {return_n_generated_images}')

# the image size for image generation. Generated images can have a size of 256x256, 512x512, or 1024x1024 pixels. Smaller sizes are faster to generate.
image_size = os.getenv('IMAGE_SIZE') or '512x512'
if DEBUG:
    logger.info(f'image_size: {image_size}')

_chat_modes_per_page = os.getenv('CHAT_MODE_PER_PAGE')
n_chat_modes_per_page = int(_chat_modes_per_page) if _chat_modes_per_page else 5
if DEBUG:
    logger.info(f'n_chat_modes_per_page: {n_chat_modes_per_page}')

mongodb_port = os.getenv('MONGODB_PORT') or '27017'
mongodb_uri = f"mongodb://mongo:{mongodb_port}"

allowed_telegram_usernames = []
tg_usernames = os.getenv('ALLOWED_TELEGRAM_USERNAMES') or None
if tg_usernames:
    allowed_telegram_usernames = tg_usernames.split(',')
if DEBUG:
    logger.info(f'allowed_telegram_usernames: {allowed_telegram_usernames}')
#allowed_telegram_usernames = config_yaml["allowed_telegram_usernames"]

# chat_modes
with open(config_dir / "chat_modes.yml", 'r') as f:
    chat_modes = yaml.safe_load(f)

# models
with open(config_dir / "models.yml", 'r') as f:
    models = yaml.safe_load(f)

# files
# TODO: help_group_chat_video_path = Path(__file__).parent.parent.resolve() / "static" / "help_group_chat.mp4"
