"""salam model

Revision ID: 43b2b9a51b6d
Revises: 680cdd12b83e
Create Date: 2023-09-11 19:40:41.245543

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '43b2b9a51b6d'
down_revision: Union[str, None] = '680cdd12b83e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('myrat', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'myrat')
    # ### end Alembic commands ###