"""create restriction table

Revision ID: d7f2744a91d8
Revises: 28332ddf91d4
Create Date: 2020-09-22 10:49:09.960990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7f2744a91d8'
down_revision = '28332ddf91d4'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        "restriction",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("reason",sa.String(100)),
        sa.Column("endingWith", sa.String(100)),
        sa.Column("myRestriction", sa.String(100)),
        sa.Column("created_date", sa.Date),
    )

def downgrade():
    op.drop_table("restriction")
