"""empty message

Revision ID: 409e2d083bd8
Revises: 27826b9594da
Create Date: 2013-12-04 16:55:29.987000

"""

# revision identifiers, used by Alembic.
revision = '409e2d083bd8'
down_revision = '27826b9594da'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('group_id', 'host')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index('group_id', 'host', [u'group_id'], unique=False)
    ### end Alembic commands ###
