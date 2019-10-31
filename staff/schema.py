"""
Data structures, used in project.

You may do changes in tables here, then execute
`alembic revision --message="Your text" --autogenerate`
and alembic would generate new migration for you
in staff/alembic/versions folder.
"""
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String


# For correct sorting in russian strings
RU_COLLATION = 'ru-RU-x-icu'

# Default naming convention for all indexes and constraints
# See why this is important and how it would save your time:
# https://alembic.sqlalchemy.org/en/latest/naming.html
convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),
    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(constraint_name)s',
    'fk': (
        'fk__%(table_name)s__%(all_column_names)s__'
        '%(referred_table_name)s'
    ),
    'pk': 'pk__%(table_name)s'
}

# Registry for all your tables
metadata = sqlalchemy.MetaData(naming_convention=convention)

# Your table, that is being used in project
users_table = Table(
    'users',
    metadata,
    Column('user_id', Integer, primary_key=True),
    Column('email', String(256), nullable=False, unique=True),
    Column('name', String(256, collation=RU_COLLATION), nullable=True),
    Column('surname', String(256, collation=RU_COLLATION), nullable=True)
)
