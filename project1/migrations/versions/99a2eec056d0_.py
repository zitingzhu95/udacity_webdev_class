"""empty message

Revision ID: 99a2eec056d0
Revises: 18df22ecb37e
Create Date: 2022-05-30 04:36:12.705466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99a2eec056d0'
down_revision = '18df22ecb37e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('past_shows', sa.Text(), nullable=True))
    op.add_column('Venue', sa.Column('upcoming_shows', sa.Text(), nullable=True))
    op.add_column('Venue', sa.Column('past_shows_count', sa.Integer(), nullable=True))
    op.add_column('Venue', sa.Column('upcoming_shows_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'upcoming_shows_count')
    op.drop_column('Venue', 'past_shows_count')
    op.drop_column('Venue', 'upcoming_shows')
    op.drop_column('Venue', 'past_shows')
    # ### end Alembic commands ###
