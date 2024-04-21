"""Se comenta segunda tabla chef

Revision ID: 51769d592660
Revises: 953b5b301df1
Create Date: 2024-04-18 23:22:47.330030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51769d592660'
down_revision = '953b5b301df1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('chef')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=80), nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('chef',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=80), nullable=False),
    sa.Column('descripcion', sa.VARCHAR(length=200), nullable=False),
    sa.Column('imagen', sa.VARCHAR(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('descripcion'),
    sa.UniqueConstraint('imagen'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###
