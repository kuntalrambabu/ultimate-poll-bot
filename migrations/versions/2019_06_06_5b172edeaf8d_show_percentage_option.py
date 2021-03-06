"""Show percentage option

Revision ID: 5b172edeaf8d
Revises: 841eba11c02b
Create Date: 2019-06-06 09:37:49.688539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b172edeaf8d'
down_revision = '841eba11c02b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('poll', sa.Column('show_percentage', sa.Boolean(), server_default='true', nullable=False))
    op.alter_column(
        'poll', 'results_visible',
        existing_type=sa.BOOLEAN(),
        server_default=None,
        existing_nullable=False
    )
    op.create_unique_constraint('one_vote_per_option_and_user', 'vote', ['user_id', 'poll_id', 'poll_option_id'])
    op.drop_constraint('vote_user_id_poll_id_poll_option_id_key', 'vote', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('vote_user_id_poll_id_poll_option_id_key', 'vote', ['user_id', 'poll_id', 'poll_option_id'])
    op.drop_constraint('one_vote_per_option_and_user', 'vote', type_='unique')
    op.alter_column(
        'poll', 'results_visible',
        existing_type=sa.BOOLEAN(),
        server_default=sa.text('true'),
        existing_nullable=False
    )
    op.drop_column('poll', 'show_percentage')
    # ### end Alembic commands ###
