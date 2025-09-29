"""Add default roles data

Revision ID: 9d608e9a075a
Revises: 
Create Date: 2025-09-29 15:50:25.412878

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d608e9a075a'
down_revision = None
branch_labels = None
depends_on = None


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
