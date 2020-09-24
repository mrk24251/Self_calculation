"""create spirit Table

Revision ID: 28332ddf91d4
Revises: bc791ceeea73
Create Date: 2020-09-15 13:26:11.285253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28332ddf91d4'
down_revision = 'bc791ceeea73'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "spirit",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("text",sa.String(300)),
    )

def downgrade():
    op.drop_table("spirit")
