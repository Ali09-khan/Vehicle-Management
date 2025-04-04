"""17

Revision ID: 1bd69cdf84f9
Revises: d3d6837779be
Create Date: 2023-11-22 02:57:39.655939

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1bd69cdf84f9'
down_revision: Union[str, None] = 'd3d6837779be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('appointment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vehicle_id', sa.Integer(), nullable=False),
    sa.Column('license_plate', sa.String(length=150), nullable=False),
    sa.Column('date', sa.String(length=150), nullable=False),
    sa.Column('time', sa.String(length=150), nullable=False),
    sa.Column('maintainance_personnel_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['maintainance_personnel_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicle.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('appointment')
    # ### end Alembic commands ###
