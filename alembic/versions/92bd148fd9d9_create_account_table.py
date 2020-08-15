"""create account table

Revision ID: 92bd148fd9d9
Revises: 
Create Date: 2020-08-15 12:39:25.893296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92bd148fd9d9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "punish",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("task",sa.String(100)),
        sa.Column("value", sa.Integer),
    )

def downgrade():
    op.drop_table("punish")
