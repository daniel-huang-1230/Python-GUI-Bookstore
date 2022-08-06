import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(BASE_DIR, 'app')
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
DATABASE_NAME = os.path.join(SRC_DIR, 'books.db')
EYE_IMAGE = os.path.join(ASSETS_DIR, 'eye.png')
SEARCH_IMAGE = os.path.join(ASSETS_DIR, 'search.png')
ADD_IMAGE = os.path.join(ASSETS_DIR, 'add.png')
UPDATE_IMAGE = os.path.join(ASSETS_DIR, 'update.png')
DELETE_IMAGE = os.path.join(ASSETS_DIR, 'delete.png')
CLOSE_IMAGE = os.path.join(ASSETS_DIR, 'close.png')
