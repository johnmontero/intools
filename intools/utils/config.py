import confuse

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

def read_config():
    return confuse.Configuration('intools', loader=Loader)