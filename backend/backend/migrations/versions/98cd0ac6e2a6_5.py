"""5

Revision ID: 98cd0ac6e2a6
Revises: e9eeadbbc2d2
Create Date: 2023-11-20 01:59:51.220892

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98cd0ac6e2a6'
down_revision: Union[str, None] = 'e9eeadbbc2d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
