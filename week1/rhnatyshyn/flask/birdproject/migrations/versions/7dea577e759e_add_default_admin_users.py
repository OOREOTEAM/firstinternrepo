"""Add default admin users

Revision ID: 7dea577e759e
Revises: 7ffd13ffaa78
Create Date: 2025-09-27 10:37:54.499854

"""
from alembic import op
import sqlalchemy as sa
from werkzeug.security import generate_password_hash
import os
from dotenv import load_dotenv

load_dotenv()

# revision identifiers, used by Alembic.
revision = '7dea577e759e'
down_revision = '7ffd13ffaa78'
branch_labels = None
depends_on = None


def upgrade():

    users_table = sa.table('user',
                    sa.column('username', sa.String),
                    sa.column('password', sa.String),
                    sa.column('role_id', sa.Integer)                  
                    )
    admin_pass= os.environ.get('ADMIN_PASSWORD')
    hashed_password = generate_password_hash(admin_pass) 

    op.bulk_insert(users_table,
                   [
                       {
                           'username': 'admin_larysa',
                           'password': hashed_password,
                           'role_id': 1
                       },
                        
                       {
                           'username': 'admin_rostyslav',
                           'password': hashed_password,
                           'role_id': 1
                       },

                       {
                           'username': 'admin_andrii',
                           'password': hashed_password,
                           'role_id': 1
                       },

                       {
                           'username': 'admin_oleksandr',
                           'password': hashed_password,
                           'role_id': 1
                       },
                   ]
                )

def downgrade():
    op.execute("DELETE FROM \"user\" WHERE role_id=1")
