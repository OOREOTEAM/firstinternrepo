"""Add default admins

Revision ID: 3a1c826c344d
Revises: 9d608e9a075a
Create Date: 2025-09-29 15:59:23.440022

"""
from alembic import op
import sqlalchemy as sa
from werkzeug.security import generate_password_hash
import os
from dotenv import load_dotenv

load_dotenv()

# revision identifiers, used by Alembic.
revision = '3a1c826c344d'
down_revision = '9d608e9a075a'
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