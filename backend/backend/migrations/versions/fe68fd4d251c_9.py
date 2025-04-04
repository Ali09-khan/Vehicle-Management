"""9

Revision ID: fe68fd4d251c
Revises: 4a22dcccf6c3
Create Date: 2023-11-20 02:27:26.257177

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fe68fd4d251c'
down_revision: Union[str, None] = '4a22dcccf6c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('driver', 'registration_date',
               existing_type=sa.DATE(),
               type_=sa.String(length=150),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('driver', 'registration_date',
               existing_type=sa.String(length=150),
               type_=sa.DATE(),
               existing_nullable=False)
    # ### end Alembic commands ###
