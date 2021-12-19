"""Properties parser."""

from configparser import ConfigParser
from io import StringIO
from tempfile import NamedTemporaryFile
from typing import Any, IO, Iterable, Union, Optional


__all__ = ['PropertiesParser']


SECTION = 'properties'


class _ConfigParser(ConfigParser):
    """Modified Configparser for reading server.properties."""

    def _read(self, fp: IO, fpname: str) -> None:
        """Reads a single file."""
        return super()._read(StringIO(f'[{SECTION}]\n{fp.read()}'), fpname)


class PropertiesParser:
    """Parse Java properties files."""

    def __init__(self):
        self.parser = _ConfigParser()

    def __getitem__(self, key: str) -> str:
        return self.parser[SECTION][key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.parser[SECTION][key] = value

    def get(self, key: str, **kwargs) -> str:
        """Returns the value of the respective key."""
        return self.parser.get(SECTION, key, **kwargs)

    def getint(self, key: str, **kwargs) -> int:
        """Returns an integer value."""
        return self.parser.getint(SECTION, key, **kwargs)

    def getfloat(self, key: str, **kwargs) -> float:
        """Returns an float value."""
        return self.parser.getfloat(SECTION, key, **kwargs)

    def getboolean(self, key: str, **kwargs) -> bool:
        """Returns an boolean value."""
        return self.parser.getboolean(SECTION, key, **kwargs)

    def set(self, key: str, value: Optional[Any] = None) -> None:
        """Sets a value."""
        return self.parser.set(SECTION, key, value)

    def read(self, filenames: Union[str, Iterable[str]],
             encoding: Optional[str] = None) -> list[str]:
        """Reads files."""
        return self.parser.read(filenames, encoding=encoding)

    def write(self, filename: str) -> None:
        """Writes to the given file."""
        with NamedTemporaryFile('w+') as tmp:
            self.parser.write(tmp, space_around_delimiters=False)
            tmp.flush()
            tmp.seek(0)

            with open(filename, 'w', encoding='utf-8') as file:
                for index, line in enumerate(tmp):
                    if index > 0:   # Skip section header.
                        file.write(line)
