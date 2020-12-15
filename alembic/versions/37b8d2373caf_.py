"""empty message

Revision ID: 37b8d2373caf
Revises: 
Create Date: 2020-12-15 12:40:43.103269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37b8d2373caf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('variantrecords',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cogid', sa.String(), nullable=True),
    sa.Column('position', sa.Integer(), nullable=True),
    sa.Column('ref', sa.String(), nullable=True),
    sa.Column('alt', sa.String(), nullable=True),
    sa.Column('is_indel', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_variantrecords_cogid'), 'variantrecords', ['cogid'], unique=False)
    op.create_index(op.f('ix_variantrecords_id'), 'variantrecords', ['id'], unique=False)
    op.create_index(op.f('ix_variantrecords_position'), 'variantrecords', ['position'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_variantrecords_position'), table_name='variantrecords')
    op.drop_index(op.f('ix_variantrecords_id'), table_name='variantrecords')
    op.drop_index(op.f('ix_variantrecords_cogid'), table_name='variantrecords')
    op.drop_table('variantrecords')
    # ### end Alembic commands ###
