"""created rental model

Revision ID: 104391cc0a9a
Revises: dccfc2070c6e
Create Date: 2021-11-10 18:11:11.128671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '104391cc0a9a'
down_revision = 'dccfc2070c6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rental', sa.Column('customer_id', sa.Integer(), nullable=True))
    op.add_column('rental', sa.Column('video_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'rental', 'customer', ['customer_id'], ['id'])
    op.create_foreign_key(None, 'rental', 'video', ['video_id'], ['id'])
    op.add_column('video', sa.Column('release_date', sa.DateTime(), nullable=False))
    op.add_column('video', sa.Column('title', sa.String(), nullable=False))
    op.add_column('video', sa.Column('total_inventory', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('video', 'total_inventory')
    op.drop_column('video', 'title')
    op.drop_column('video', 'release_date')
    op.drop_constraint(None, 'rental', type_='foreignkey')
    op.drop_constraint(None, 'rental', type_='foreignkey')
    op.drop_column('rental', 'video_id')
    op.drop_column('rental', 'customer_id')
    # ### end Alembic commands ###