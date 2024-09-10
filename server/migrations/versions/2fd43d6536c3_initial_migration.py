"""initial migration

Revision ID: 2fd43d6536c3
Revises: 684173af23d5
Create Date: 2024-09-10 10:11:59.835664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fd43d6536c3'
down_revision = '684173af23d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.add_column('reviews', sa.Column('rating', sa.Integer(), nullable=True))
    # op.alter_column('reviews', 'customer_id',
            #    existing_type=sa.INTEGER(),
            #    nullable=True)
   
   

    def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
        op.alter_column('reviews', 'item_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # op.alter_column('reviews', 'customer_id',
            #    existing_type=sa.INTEGER(),
            #    nullable=False)
        op.drop_column('reviews', 'rating')
    # ### end Alembic commands ###
