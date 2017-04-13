To install in a virual environment

```
virtualenv env
source env/bin/activate
pip install -U setuptools
pip install -r requirements.txt 
```

Then
```
cd src
```

edit config.py to change user/password for WLC and AP

```
./AP_troubleshoot.py -w <WLC_IP>
```

