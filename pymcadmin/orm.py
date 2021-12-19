"""Object-relational mappings."""

from peewee import AutoField, Model, ForeignKeyField

from peeweeplus import Argon2Field, MySQLDatabase, RestrictedCharField

from pymcadmin.constants import EMAIL_REGEX, NAME_REGEX


__all__ = ['DATABASE', 'User', 'Server']


DATABASE = MySQLDatabase('pymcadmin')


class BaseModel(Model):
    """Base model for the database."""

    class Meta:     # pylint: disable=C0115,R0903
        database = DATABASE
        schema = database.database


class User(BaseModel):
    """User information."""

    id = AutoField()
    name = RestrictedCharField(NAME_REGEX)
    email = RestrictedCharField(EMAIL_REGEX)
    passwd = Argon2Field()


class Server(BaseModel):
    """A Minecraft server."""

    id = AutoField()
    owner = ForeignKeyField(User, column_name='user', on_delete='CASCADE')
