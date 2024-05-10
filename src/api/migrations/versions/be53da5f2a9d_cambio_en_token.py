"""cambio en token

Revision ID: be53da5f2a9d
Revises: b7b02403f784
Create Date: 2024-05-08 22:59:48.914611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be53da5f2a9d'
down_revision = 'b7b02403f784'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('token',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('token',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)

    # ### end Alembic commands ###
