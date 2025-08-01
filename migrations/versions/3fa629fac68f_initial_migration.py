"""Initial migration

Revision ID: 3fa629fac68f
Revises: 
Create Date: 2025-07-21 19:32:53.821973

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '3fa629fac68f'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('urls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('long_url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('short_url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_urls_id'), 'urls', ['id'], unique=False)
   
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    
    op.drop_index(op.f('ix_urls_id'), table_name='urls')
    op.drop_table('urls')
    # ### end Alembic commands ###
