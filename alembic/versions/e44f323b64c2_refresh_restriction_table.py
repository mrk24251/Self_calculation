"""refresh restriction table

Revision ID: e44f323b64c2
Revises: d7f2744a91d8
Create Date: 2020-09-24 16:38:02.097314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e44f323b64c2'
down_revision = 'd7f2744a91d8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "restriction",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("reason",sa.String(300)),
        sa.Column("endingWith", sa.String(500)),
        sa.Column("myRestriction", sa.String(300)),
        sa.Column("created_date", sa.Date),
    )

def downgrade():
    op.drop_table("restriction")
