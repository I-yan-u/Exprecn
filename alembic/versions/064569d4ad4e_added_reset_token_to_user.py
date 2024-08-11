"""Added reset token to user

Revision ID: 064569d4ad4e
Revises: d7dd393dd0a3
Create Date: 2024-08-11 02:01:05.781458

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '064569d4ad4e'
down_revision: Union[str, None] = 'd7dd393dd0a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('ResetToken', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'ResetToken')
    # ### end Alembic commands ###