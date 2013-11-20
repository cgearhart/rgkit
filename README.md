# rgkit -- Testing kit for [robot game](http://robotgame.org) [![Build Status](https://travis-ci.org/brandonhsiao/rgkit.png?branch=master)](https://travis-ci.org/brandonhsiao/rgkit) #

Please see this [link](http://robotgame.org/kit) for the instructions.

## PIP/VirtualEnv Installation

The easiest way to install the kit is with [pip](http://www.pip-installer.org/en/latest/). From the terminal, run:

`pip install git+https://travis-ci.org/brandonhsiao/rgkit`

__Note:__ *This will install rgkit system-wide. We recommend using [virtualenv](http://www.virtualenv.org/en/latest/) to avoid namespace collisions.*

Virtualenv adds the following steps:

```
mkdir my_robot
cd my_robot
virtualenv env
source env/bin/activate
pip install git+https://travis-ci.org/brandonhsiao/rgkit
```

## Installation via Setup.py

Make a local copy of the git repository or download the source files. Using the terminal, run the following from the root directory of the source code:

`python setup.py install`

__Note:__ *This will install rgkit system-wide. We recommend using [virtualenv](http://www.virtualenv.org/en/latest/) to avoid namespace collisions.*

After downloading the source files and writing your own robot file. From the terminal, run:

`python run.py your_robot.py defaultrobots.py`

## From Source:

`rgkit` is packaged as a module, so you *can* co-locate the module directory with your own source code and import/run as usual. 
```
- rgkit
|--- rgkit
|    |--- __init__.py
|    |--- game.py
|    |--- run.py
|    |--- ...
|    |--- your_robot.py
|--- setup.py
...
```

To run the game, use the terminal and execute the following from the inner `rgkit` folder (i.e., in the same directory as `run.py`):

`python run.py your_robot.py defaultrobots.py`


## Use:

Once installed, the package can be imported like any other module, i.e.,

```
import rg

class Robot:
    def act(self):
        return ['guard']

```