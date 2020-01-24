# my-nativefier-apps
Creating PWAs apps in your linux distribution automatically

Created by SuperNova Team.

# Index
+ [Installing dependencies](#installation)
+ [Installing my apps](#installing-my-nativefier-app)

## Dependencies
+ [Python 3](https://www.python.org/downloads/)
+ [Nodejs](https://nodejs.org/en/download/)
+ [Nativefier](https://github.com/jiahaog/nativefier)

## Installation
Using an Ubuntu based system you can just:

Installing python
```
  sudo apt-get install python3
```

Installing node
```
  sudo apt-get install curl
  curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
  sudo apt-get install nodejs
```

Installing Nativefier
```
  sudo npm i nativefier -g
```

## Installing my-nativefier-app
+ First clone this repository
```
  git clone https://github.com/hfabio/my-nativefier-apps.git
```

+ Now you can open the `apps.json` and configure the apps you want to install.
Follow this model for each app:
```
  {
    "name": "the name for your app",
    "url": "https://the-link-for-app.com/",
    "icon": "name-of-icon-in-icons-page"
  }
```
*note, the icon entry is optional, use it only if you want to change the default icon*
*if you really want to use a custom icon, dont forget to use the right name for the icon*

+ To run

Just use the terminal in this folder and run:
```
  python3 creator.py
```
*note: you will need to insert your sudo password to move the .desktop entries to /usr/share/applications folder*