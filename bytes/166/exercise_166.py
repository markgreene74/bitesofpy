# https://codechalleng.es/bites/166/
# https://docs.python.org/3/library/configparser.html
import configparser


class ToxIniParser:
    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = configparser.ConfigParser()
        self.config.read(ini_file)

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
        New to properties? -> https://pybit.es/property-decorator.html
        """
        return len(self.config.sections())

    @property
    def environments(self):
        """Return a list of environments
        (= "envlist" attribute of [tox] section)"""
        _env_str = self.config["tox"]["envlist"].replace(",", " ")
        return [i.strip() for i in _env_str.split()]

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        return set(
            self.config[i][j]
            for i in self.config.sections()
            for j in self.config[i]
            if j == "basepython"
        )
