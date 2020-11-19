"""empty message

Revision ID: 3c1112ad225c
Revises: f447e460a88d
Create Date: 2020-11-19 13:32:31.244385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c1112ad225c'
down_revision = 'f447e460a88d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('discipline',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=512), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_discipline_name'), 'discipline', ['name'], unique=True)
    op.create_table('excercisetodiscipline',
    sa.Column('excercise_id', sa.Integer(), nullable=False),
    sa.Column('discipline_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['discipline_id'], ['discipline.id'], ),
    sa.ForeignKeyConstraint(['excercise_id'], ['excercise.id'], ),
    sa.PrimaryKeyConstraint('excercise_id', 'discipline_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('excercisetodiscipline')
    op.drop_index(op.f('ix_discipline_name'), table_name='discipline')
    op.drop_table('discipline')
    # ### end Alembic commands ###
