"""init

Revision ID: c7a4236131b6
Revises: 
Create Date: 2023-09-21 22:15:04.907150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7a4236131b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('user_id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('guruh', sa.String(length=20), nullable=True),
    sa.Column('number', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
