from configparser import ConfigParser
import pathlib
from pathlib import Path, PurePath

def read_db_config(filename='config.ini',section='mysql'):
    # create parser and read ini configuration file
    parse = ConfigParser()
    parse.read(filename)
    
    
    # get section, default to mysql
    if parse.has_section(section):
        items = parse.items(section)
    else:
        raise Exception(f'{section} not found in {filename}')
    return dict(items)
if __name__ == "__main__":
    path = PurePath(__file__)
    # config_path = path.parent+
    db_config_path = path.parent/ 'config.ini'
    print(read_db_config(db_config_path))