"""19

Revision ID: 551ea9e14548
Revises: cdb0bc0b5901
Create Date: 2023-11-22 03:42:18.581535

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '551ea9e14548'
down_revision: Union[str, None] = 'cdb0bc0b5901'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fueling_record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vehicle_id', sa.Integer(), nullable=False),
    sa.Column('driver_id', sa.Integer(), nullable=False),
    sa.Column('car_plate_info', sa.String(length=150), nullable=False),
    sa.Column('date_and_time', sa.String(length=150), nullable=False),
    sa.Column('amount_of_fuel', sa.Integer(), nullable=False),
    sa.Column('fuel_type', sa.String(length=150), nullable=False),
    sa.Column('cost', sa.Integer(), nullable=False),
    sa.Column('gas_station_name', sa.String(length=150), nullable=False),
    sa.Column('fueling_personnel_id', sa.Integer(), nullable=False),
    sa.Column('driver_image', sa.String(length=150), nullable=False),
    sa.Column('fuel_levels_before', sa.Integer(), nullable=False),
    sa.Column('fuel_levels_after', sa.Integer(), nullable=False),
    sa.Column('milage', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['driver_id'], ['driver.id'], ),
    sa.ForeignKeyConstraint(['fueling_personnel_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicle.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fueling_record')
    # ### end Alembic commands ###
