import asyncio
import time
import reflex as rx
from ..ui.base import base_page
from rxconfig import config
from .. import navigation
from sqlmodel import Field
from datetime import datetime, timezone
import sqlalchemy
from .. import utils 


class ContactEntryModel(rx.Model, table=True):
    user_id: int = Field(nullable = True)
    first_name: str
    last_name: str = Field(nullable = True)
    email: str = Field(nullable = True)
    message: str
    created_at: datetime = Field(
        default_factory = utils.timing.get_utc_now,
        sa_type = sqlalchemy.DateTime(timezone = True),
        sa_column_kwargs = {
            "server_default" : sqlalchemy.func.now()
        },
        nullable = False
    )
