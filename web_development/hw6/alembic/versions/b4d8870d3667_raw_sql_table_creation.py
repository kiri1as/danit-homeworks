"""Raw SQL table creation

Revision ID: b4d8870d3667
Revises: 
Create Date: 2024-12-18 21:18:32.415867

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'b4d8870d3667'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with open('sql/init_tables.sql', 'r') as script:
        sql_execution = script.read()
    op.execute(sql_execution)


def downgrade() -> None:
    with open('sql/init_tables_restore.sql', 'r') as script:
        sql_execution = script.read()
    op.execute(sql_execution)
