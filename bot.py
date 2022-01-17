from vk_search import PeopleSearch
from service import Application
from config import *

if __name__ == '__main__':
    app = Application(GROUP_TOKEN)
    app.run()
