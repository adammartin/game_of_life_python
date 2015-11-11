# Conway's Game of Life

This is a basic game of life implementation in python so that I can learn how to program in python.  This is not meant to show a master at work since I am an novice at python.  There are lots of improvements that could be done.  However this is my chance to explore python and alot of it's standard set up and limitations.

That said feel free to make appropriate fun of it ... it's how I learn!

## Usage

The project was configured and tested in python 3.4.

Navigate to the directory and run `pip install -r requirements.txt`

When completed execute `python game/game.py`

After you can post to the end point and recieve a response ...

```
$ curl http://127.0.0.1:5000/game -i -H "Content-Type: application/json" -X POST -d '[[0,1,0],[0,1,0],[0,1,0]]'

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 138
Server: Werkzeug/0.10.4 Python/3.4.3
Date: Wed, 11 Nov 2015 20:51:24 GMT

[
    [
        0,
        0,
        0
    ],
    [
        1,
        1,
        1
    ],
    [
        0,
        0,
        0
    ]
]
```