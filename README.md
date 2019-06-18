### Automated ui tests with selenium for library-web-app 

library-web-app https://github.com/veffhz/library-web-app

##### install requirements

```pip3 install -r requirements.txt```

##### install chrome driver:

```
wget https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_linux64.zip

unzip chromedriver_linux64.zip

sudo mv chromedriver /usr/bin/chromedriver

sudo chown root:root /usr/bin/chromedriver

sudo chmod +x /usr/bin/chromedriver

```

##### run login test:
```pytest login_test.py```

##### run author test:
```pytest author_test.py```