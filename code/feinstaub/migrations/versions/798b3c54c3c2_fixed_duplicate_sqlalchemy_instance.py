"""Fixed duplicate SQLAlchemy instance

Revision ID: 798b3c54c3c2
Revises: 
Create Date: 2025-03-26 10:01:29.951310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '798b3c54c3c2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('location',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('loc', sa.Integer(), nullable=False),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lon', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('loc')
    )
    op.create_table('sensor',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('location_id', sa.Integer(), nullable=False),
    sa.Column('sensor_type', sa.String(), nullable=False),
    sa.Column('sensor_name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('sensor_name')
    )
    op.create_table('dust_measurement',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('sensor_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.String(), nullable=False),
    sa.Column('p1', sa.Float(), nullable=True),
    sa.Column('p2', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['sensor_id'], ['sensor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('weather_measurement',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('sensor_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.String(), nullable=False),
    sa.Column('pressure', sa.Float(), nullable=True),
    sa.Column('temperature', sa.Float(), nullable=True),
    sa.Column('humidity', sa.Float(), nullable=True),
    sa.Column('altitude', sa.Float(), nullable=True),
    sa.Column('pressure_sealevel', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['sensor_id'], ['sensor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('weather_measurement')
    op.drop_table('dust_measurement')
    op.drop_table('sensor')
    op.drop_table('location')
    # ### end Alembic commands ###
