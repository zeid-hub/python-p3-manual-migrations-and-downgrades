"""Renaming students to scholars

Revision ID: 93b589d33c32
Revises: 791279dd0760
Create Date: 2024-03-21 09:28:34.805303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93b589d33c32'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
