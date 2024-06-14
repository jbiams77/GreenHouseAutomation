"""verify duration column addition

Revision ID: df25d9ee9258
Revises: e2ea30bcaf1b
Create Date: 2024-06-11 07:46:32.928485

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision: str = 'df25d9ee9258'
down_revision: Union[str, None] = 'e2ea30bcaf1b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Bind the current connection
    bind = op.get_bind()
    inspector = Inspector.from_engine(bind)
    
    # Check if the column already exists
    columns = [column['name'] for column in inspector.get_columns('event_schedule')]
    if 'duration' not in columns:
        # Add the 'duration' column to the 'event_schedule' table
        op.add_column('event_schedule', sa.Column('duration', sa.Integer(), nullable=True))

def downgrade():
    # Bind the current connection
    bind = op.get_bind()
    inspector = Inspector.from_engine(bind)
    
    # Check if the column exists
    columns = [column['name'] for column in inspector.get_columns('event_schedule')]
    if 'duration' in columns:
        # Remove the 'duration' column from the 'event_schedule' table
        op.drop_column('event_schedule', 'duration')
