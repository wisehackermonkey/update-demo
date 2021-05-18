# from pyupdater.client import Client, AppUpdate, LibUpdate
# from client_config import ClientConfig
# import __init__
# APP_NAME = 'update-demo'
# APP_VERSION = __init__.__version__


# def print_status_info(info):
#     total = info.get(u'total')
#     downloaded = info.get(u'downloaded')
#     status = info.get(u'status')
#     print(downloaded, total, status)

# client = Client(ClientConfig(), refresh=True,
#                         progress_hooks=[print_status_info])

# app_update = client.update_check(APP_NAME, APP_VERSION)
# if app_update is not None:
#     app_update.download()
#     if app_update.is_downloaded():
#         app_update.extract_overwrite()
# # if app_update.is_downloaded():
# #     app_update.extract_restart()


import logging

logging.basicConfig(level=logging.DEBUG)

from client_config import ClientConfig
from pyupdater.client import Client, AppUpdate, LibUpdate


def check_for_update():
    client = Client(ClientConfig(), refresh=True)
    app_update = client.update_check(ClientConfig.APP_NAME, ClientConfig.APP_VERSION)

    if app_update is not None:  # is there a new update
        if app_update.download():  # the update download is made here
            if isinstance(app_update, AppUpdate):  # you should freeze it
                app_update.extract_restart()
                return True
            else:
                app_update.extract()
                return True
    return False
if __name__ == "__main__":
    print('Current version is ', ClientConfig.APP_VERSION)
    if check_for_update():
        print('there\'s a new update :D')   