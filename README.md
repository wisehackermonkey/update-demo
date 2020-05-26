# update-demo
 demo app learn how to update using pyupdate


# run docker files server for testing
```bash
sudo docker run --rm -it -p 8888:8080 --name simple -v /root/public:/var/www:ro trinitronx/python-simplehttpserver
or
sudo docker run -d -p 8888:8080 --name simple -v /root/public:/var/www:ro trinitronx/python-simplehttpserver

```

##### [Docker hub for trinitronx/python-simplehttpserver](https://hub.docker.com/r/trinitronx/python-simplehttpserver)

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
- ## [how to use pyupdater](https://www.pyupdater.org/usage-cli/)



# Scratch pad
```
pyinstaller --onefile --hidden-import="pkg_resources.py2_warn"  main.py
```