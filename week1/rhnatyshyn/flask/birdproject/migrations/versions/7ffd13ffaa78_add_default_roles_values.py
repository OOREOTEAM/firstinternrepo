"""Add default roles values

Revision ID: 7ffd13ffaa78
Revises: cba185ae2591
Create Date: 2025-09-27 10:00:15.883318

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ffd13ffaa78'
down_revision = 'cba185ae2591'
branch_labels = None
depends_on = None

#Added separete migtation to pupulate Member and Admin values

def upgrade():
    role_table = sa.table('role',
                           sa.column('role_id', sa.Integer),
                           sa.column('name', sa.String))

    op.bulk_insert(role_table,
                   [
                       {'name': 'Admin'},
                       {'name': 'Member'}
                   ]
    )


def downgrade():
    op.execute("DELETE FROM role WHERE name IN ('Admin', 'Member')")
