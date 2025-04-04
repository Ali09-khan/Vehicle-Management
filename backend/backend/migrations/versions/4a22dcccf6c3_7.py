"""7

Revision ID: 4a22dcccf6c3
Revises: fd8c22b7d9b1
Create Date: 2023-11-20 02:19:07.351699

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4a22dcccf6c3'
down_revision: Union[str, None] = 'fd8c22b7d9b1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("ALTER TABLE driver ALTER COLUMN registration_date TYPE date USING registration_date::date")
    # op.alter_column('driver', 'registration_date',
    #            existing_type=sa.VARCHAR(length=150),
    #            type_=sa.Date(),
    #            existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('driver', 'registration_date',
               existing_type=sa.Date(),
               type_=sa.VARCHAR(length=150),
               existing_nullable=False)
    # ### end Alembic commands ###
