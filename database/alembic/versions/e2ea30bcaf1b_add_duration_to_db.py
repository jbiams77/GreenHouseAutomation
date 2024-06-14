"""add duration to DB

Revision ID: e2ea30bcaf1b
Revises: 67612e82c79b
Create Date: 2024-06-11 07:35:15.754851

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e2ea30bcaf1b'
down_revision: Union[str, None] = '67612e82c79b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Add the 'duration' column to the 'event_schedule' table
    op.add_column('event_schedule', sa.Column('duration', sa.Integer(), nullable=True))

def downgrade():
    # Remove the 'duration' column from the 'event_schedule' table
    op.drop_column('event_schedule', 'duration')
