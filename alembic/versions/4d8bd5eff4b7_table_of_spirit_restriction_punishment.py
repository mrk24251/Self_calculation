"""table of spirit , restriction & punishment

Revision ID: 4d8bd5eff4b7
Revises: 
Create Date: 2020-10-04 16:23:18.971158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d8bd5eff4b7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "spirit",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("text", sa.String(500)),
    )

    op.create_table(
        "punish",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("task", sa.String(100)),
        sa.Column("value", sa.Integer),
    )

    op.create_table(
        "restriction",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("reason", sa.String(300)),
        sa.Column("endingWith", sa.String(500)),
        sa.Column("myRestriction", sa.String(300)),
        sa.Column("created_date", sa.Date),
    )


def downgrade():
    pass
