import ast
import argparse
import imp
import inspect
import sys

import pkg_resources

try:
    imp.find_module('rgkit')
except ImportError:
    # force rgkit to appear as a module when run from current directory
    from os.path import dirname, abspath
    cdir = dirname(abspath(inspect.getfile(inspect.currentframe())))
    parentdir = dirname(cdir)
    sys.path.insert(0,parentdir)

from rgkit import game, render
from rgkit.settings import settings


parser = argparse.ArgumentParser(description="Robot game execution script.")
parser.add_argument("usercode1",
                    help="File containing first robot class definition.",
                    )
parser.add_argument("usercode2",
                    help="File containing second robot class definition.",
                    )
parser.add_argument("-m", "--map",
                    help="User-specified map file.",
                    type=argparse.FileType('r'),
                    default=pkg_resources.resource_filename('rgkit', 
                                                            'maps/default.py')
                    )
parser.add_argument("-H", "--headless", action="store_true",
                    default=False,
                    help="Disable rendering game output.")
args = parser.parse_args()

def make_player(fname):
    try:
        with open(fname) as f:
            return game.Player(f.read())
    except IOError, msg:
        if pkg_resources.resource_exists('rgkit', fname):
            with open(pkg_resources.resource_filename('rgkit', fname)) as f:
                return game.Player(f.read())
        raise IOError, msg


def main():

    map_data = ast.literal_eval(args.map.read())
    game.init_settings(map_data)

    players = [make_player(args.usercode1), make_player(args.usercode2)]
    g = game.Game(*players, record_turns=True)
    for i in range(settings.max_turns):
        print (' running turn %d ' % (g.turns + 1)).center(70, '-')
        g.run_turn()
    if not args.headless:
        render.Render(g, game.settings)
    print g.history

if __name__=="__main__":
    main()
