"""4

Revision ID: e9eeadbbc2d2
Revises: 10dddc58fd03
Create Date: 2023-11-20 01:51:48.854478

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e9eeadbbc2d2'
down_revision: Union[str, None] = '10dddc58fd03'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('driver')
    op.drop_table('vehicle')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vehicle',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('vehicle_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('model', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('year', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('license_plate', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('sitting_capacity', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('color', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='vehicle_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('driver',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('fname', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('mname', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('lname', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('phone_num', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('driving_license', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('registration_date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('vehicle_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='driver_user_id_fkey'),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicle.id'], name='driver_vehicle_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='driver_pkey')
    )
    # ### end Alembic commands ###
