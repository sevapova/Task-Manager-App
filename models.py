from sqlalchemy import (
    Table, 
    Column, 
    Integer, 
    String,
    Text,
    ForeignKey,
)
from database import metadata


users = Table(
    'users',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(64), unique=True, nullable=False),
    Column("fullname", String(128), nullable=False),
)

tasks = Table(
    'tasks',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(128), unique=True, nullable=False),
    Column("description", Text, nullable=False, default=''),
    Column("user_id", ForeignKey('users.id')),
)

