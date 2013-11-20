# rgkit -- Testing kit for [robot game](http://robotgame.org) [![Build Status](https://travis-ci.org/brandonhsiao/rgkit.png?branch=master)](https://travis-ci.org/brandonhsiao/rgkit) #

Additional information can be found at this [link](http://robotgame.org/kit).

## Package Installation

__pip__

The easiest way to install the kit is with `[pip](http://www.pip-installer.org/en/latest/)`. From the terminal, run:

`pip install git+https://travis-ci.org/brandonhsiao/rgkit`

__Note:__ *This will install rgkit system-wide. It is recommended to use [virtualenv](http://www.virtualenv.org/en/latest/) to manage development environments.*

__virtualenv__

Installing with `virtualenv` requires the following steps:

```
mkdir my_robot
cd my_robot
virtualenv env
source env/bin/activate
pip install git+https://travis-ci.org/brandonhsiao/rgkit
```

__setup.py__

You can also manually install directly from the source folder. Make a local copy of the git repository or download the source files. Then, using the terminal, run the following from the root directory of the source code:

`python setup.py install`

__Note:__ *This will install rgkit system-wide. It is recommended to use [virtualenv](http://www.virtualenv.org/en/latest/) to manage development environments.*

__Running the game__

After installing the package, the script is executable from the command line (if you're using virtualenv, remember to activate the environment). There are two entry points provided: `run` and `mapeditor`. The general usage of run is:

```
usage: run [-h] [-m MAP] [-H] usercode1 usercode2

Robot game execution script.

positional arguments:
  usercode1          File containing first robot class definition.
  usercode2          File containing second robot class definition.

optional arguments:
  -h, --help         show this help message and exit
  -m MAP, --map MAP  User-specified map file.
  -H, --headless     Disable rendering game output.
```

So, from a directory containing your_robot.py, you can run a game against the default robot and suppress GUI output with the following command:

`run -H your_robot.py defaultrobots.py`

## Developing in the source directory:

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

__Running the game__

To run the game with the source configured this way, use the terminal and execute the following from the inner `rgkit` folder (i.e., in the same directory as `run.py`):

`python run.py your_robot.py defaultrobots.py`

## Importing:

Once installed, you should only need the `rg` module (which is itself optional) to develop your own robots. The package can be imported like any other module, i.e.,

```
import rg

class Robot:
    def act(self):
        return ['guard']

```