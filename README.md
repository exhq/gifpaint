<h1>gifpaint</h1>
used for minecraft resourcepack creation<br><br><br>

how to use: <br>
`git clone https://github.com/exhq/gifpaint` <br>
`cd gifpaint` <br>
`pip install -r requirements.txt`<br>
`./main.py -(d, p | g ) {input file}` 

if -p is provided, the program takes in gif files and outputs png strips, however if -g is provided, the program takes in png strips and outputs gifs

the `-d` argument is optional, it changes how long every frame's duration is (example: -d 300 makes it so every frame is on screen for 300 miliseconds). if `-d` is not provided it will default to 50.

example usage: 

`./main.py -d 50 -g .png`

`./main.py -p ~/input.gif`
