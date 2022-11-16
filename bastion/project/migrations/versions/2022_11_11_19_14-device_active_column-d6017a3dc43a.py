"""device active column

Revision ID: d6017a3dc43a
Revises: 86428e1abada
Create Date: 2022-11-11 19:14:04.676937

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "d6017a3dc43a"
down_revision = "86428e1abada"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("device", sa.Column("active", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("device", "active")
    # ### end Alembic commands ###
