## Installation Instructions

Dependencies: python3

### Building
I recommend setting up the harvester in a virtualenvironment to isolate it

Install VirtualEnv
```
pip3 install virtualenv
```

In the root of the project then run:
```
virtualenv venv
```

Activate the virtualenv (you'll need to do this each time you run the application too)
```
source venv/bin/activate
```

Install the pip dependencies
```
pip install -r requirements.txt
```

### Running

To search and travel backwards looking for every single tweet, run:

```
python harvester.py search
```

To subscribe to the new tweets stream as they come:

```
python harvester.py stream
```
