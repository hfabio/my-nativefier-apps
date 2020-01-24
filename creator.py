#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: hfabio
'''
import json
import threading
import os
pwas_path = '~/PWAs/'

exists = os.path.isdir(os.path.expanduser(pwas_path))
if not exists:
    os.mkdir(os.path.expanduser(pwas_path))

with open('./apps.json', 'r') as f:
    data = json.load(f)

apps = data['apps']


def writeDesktopEntry(name):
    with open('{}.desktop'.format(name), 'w') as desktop:
        desktop.write('[Desktop Entry]\n')
        desktop.write('Terminal=false\n')
        desktop.write('Name={}\n'.format(name))
        desktop.write(
            'Exec={}{}-linux-x64/{}\n'.format(os.path.expanduser(pwas_path), name, name))
        desktop.write('Type=Application\n')
        desktop.write(
            'Icon={}{}-linux-x64/resources/app/icon.png\n'.format(os.path.expanduser(pwas_path), name))
        desktop.write('Categories=Network;')
        desktop.close()


def createApp(url, name, icon):
    print('Installing {}'.format(name))
    if icon != '':
        os.system(
            'nativefier "{}" --name "{}" --icon "icons/{}" ~/PWAs'.format(url, name, icon))
    else:
        os.system('nativefier "{}" --name "{}" ~/PWAs'.format(url, name))
    writeDesktopEntry(name)


def create(app):
    if 'icon' in app:
        createApp(app['url'], app['name'], app['icon'])
    else:
        createApp(app['url'], app['name'], '')


for app in apps:
    create(app)
print('\n'*50)
print('please, insert your sudo password to move all .desktop and create access')
os.system('sudo mv *.desktop /usr/share/applications/')


'''
threads = [threading.Thread(target=create, args=(app,)) for app in apps]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
'''
