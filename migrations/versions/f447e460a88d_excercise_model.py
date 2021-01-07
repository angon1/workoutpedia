"""excercise model

Revision ID: f447e460a88d
Revises: e714447e5a23
Create Date: 2020-11-11 15:34:19.803314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f447e460a88d"
down_revision = "e714447e5a23"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "excercise",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=64), nullable=True),
        sa.Column("description", sa.String(length=512), nullable=True),
        sa.Column("movieLink", sa.String(length=512), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("description"),
    )
    op.create_index(op.f("ix_excercise_name"), "excercise", ["name"], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_excercise_name"), table_name="excercise")
    op.drop_table("excercise")
    # ### end Alembic commands ###
