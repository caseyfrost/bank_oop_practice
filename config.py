from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    # get section, default to postgresql
    db = {}
    params = parser.items(section)
    for param in params:
        db[param[0]] = param[1]

    return db


if __name__ == '__main__':
    print(config())
