"""Modify schedule_time column type

Revision ID: 67612e82c79b
Revises: 
Create Date: 2024-06-07 07:41:20.827838

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '67612e82c79b'
down_revision: Union[str, None] = None
branch_labels = None
depends_on = None

def upgrade():
    # Modify the column type
    op.alter_column('event_schedule', 'schedule_time',
                    existing_type=sa.DateTime(),
                    type_=sa.Time())

def downgrade():
    # Reverse the modification if needed
    op.alter_column('event_schedule', 'schedule_time',
                    existing_type=sa.Time(),
                    type_=sa.DateTime())
