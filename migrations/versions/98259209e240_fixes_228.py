"""Fixes 228

Revision ID: 98259209e240
Revises: 9ff01b7fcb5c
Create Date: 2024-02-26 15:02:54.486276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98259209e240'
down_revision = '9ff01b7fcb5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('ix_users_school_name')
        batch_op.create_index(batch_op.f('ix_users_school_name'), ['school_name'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_school_name'))
        batch_op.create_index('ix_users_school_name', ['school_name'], unique=True)

    # ### end Alembic commands ###
