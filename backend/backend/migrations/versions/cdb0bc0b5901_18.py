"""18

Revision ID: cdb0bc0b5901
Revises: 1bd69cdf84f9
Create Date: 2023-11-22 03:26:56.474395

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cdb0bc0b5901'
down_revision: Union[str, None] = '1bd69cdf84f9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('maintenance_record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vehicle_id', sa.Integer(), nullable=False),
    sa.Column('mainteneance_personnel_id', sa.Integer(), nullable=False),
    sa.Column('maintenance_description', sa.String(length=150), nullable=False),
    sa.Column('milage', sa.Integer(), nullable=False),
    sa.Column('date_and_time', sa.String(length=150), nullable=False),
    sa.Column('status', sa.String(length=150), nullable=False),
    sa.Column('part_numbers', sa.Integer(), nullable=False),
    sa.Column('photo', sa.String(length=150), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['mainteneance_personnel_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicle.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('maintenance_record')
    # ### end Alembic commands ###
