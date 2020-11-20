"""empty message

Revision ID: adcf436481cc
Revises: 3c1112ad225c
Create Date: 2020-11-19 20:58:59.171029

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adcf436481cc'
down_revision = '3c1112ad225c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_tag_name', table_name='tag')
    op.drop_table('tag')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), nullable=True),
    sa.Column('category', sa.VARCHAR(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_tag_name', 'tag', ['name'], unique=1)
    # ### end Alembic commands ###