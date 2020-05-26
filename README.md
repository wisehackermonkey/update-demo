# update-demo
## demo app learn how to update using pyupdate
```bash
by oran collins
github.com/wisehackermonkey
oranbusiness@gmail.com
20200526
```
![Screenshot_1](/assets/Screenshot_1.jpg)
![Screenshot_2](/assets/Screenshot_2.jpg)



# how to install app
### Go to http://64.227.84.118:8888/ 
- Download the latest `update-demo-win-X.X.X.zip`
- Unzip to folder, and run exe, ignore windows permissions stuff.


# Development: Install
### prerequisites
- docker enabled web accessible server:  `im using digital ocean server 64.227.84.118:8888`
- local machine with python 3.7+ installed
## Steps
### on local dev machine
```
git clone 
cd /path/to/repo
pip install -r requirements.txt
pyupdater init
pyupdater settings --plugin scp
```
### on web accessible server
```
sudo docker run -d -p 8888:8080 --name simple -v /root/public:/var/www:ro trinitronx/python-simplehttpserver
```
### on local dev machine
```
python main.py
```

# DONE


# Important files to look at
- main.py - gui program with button `update`
- update.py - files handle updates using pyupdater
- client_config.py - location for config of app

##### Take note of location `/root/public` is where the update files will be accessible 


# description of how 'update' button works

- when the update button is pressed
- tk calls a function located in update.py called "check_for_update()"
- which 
- looks for the latest version of the app at this static file bucket http://64.227.84.118:8888/ 
- downloads the latest version to C:\Users\<PC - NAME>\AppData\Local\wisehackermonkey\update-demo folder in windows
- then replaces extracts and replaces the exe with the new version
- kills the app and restarts it grabbing the overwritten exe

# how pushing new app version works

- new feature is added like a new button
- ![](/assets/Screenshot_3.jpg) 
- the package version is updated in client_config.py
- the exe is built by issuing `pyupdater build --onefile --hidden-import="pkg_resources.py2_warn"  --app-version=1.2.6 main.py` 
 - which builds the exe into one file with '--onefile' argument 
 - and "--hidden-import="pkg_resources.py2_warn" fixes an 'pyinstaller' error with pkg_resources.py2_warn giving stopping app from launching, anonying!
- the exe must be cryptographically signed by issuing `pyupdater pkg --sign`
- then uploaded the the docker static file server  (trinitronx/python-simplehttpserver) running at 64.227.84.118:8888
 - the file is pushed to the server by using 'scp' with login credentals to the server
 - the files are uploaded to the directory '/root/public' 
 - NOTE: to authorize scp `pyupdater settings --plugin scp`
   - Username: <required>
   - Password: <required>
   - Server IP: <required>
   - Path to .zip file storage: (my case it was) '/root/public' 
   - path to "keypack.pyu" file on server


# run docker files server for testing
```bash
sudo docker run --rm -it -p 8888:8080 --name simple -v /root/public:/var/www:ro trinitronx/python-simplehttpserver
or
sudo docker run -d -p 8888:8080 --name simple -v /root/public:/var/www:ro trinitronx/python-simplehttpserver

```

### [Link to docker image used](https://hub.docker.com/r/trinitronx/python-simplehttpserver)

# Scp upload 
```
pyupdater settings --service scp

pyupdater upload --service scp
```

# build
```
pyupdater build --onefile --app-version=1.0.1 main.py
pyupdater pkg --process
pyupdater pkg --sign

NOTE: requires setup
pyupdater upload --service scp

```
# build with fixed errors
```
pyupdater build --onefile --hidden-import="pkg_resources.py2_warn"  --app-version=1.0.6 main.py
```
#### in one command
```
pyupdater build --app-version=1.0.2 main.py;pyupdater pkg --process;pyupdater pkg --sign;pyupdater upload --service scp
```

# run update
```
python update.py
```
# Resouces
- #### [ pyupdater cli docs](https://www.pyupdater.org/usage-cli/)



# ~~Scratch pad~~
```
pyinstaller --onefile --hidden-import="pkg_resources.py2_warn"  main.py
```