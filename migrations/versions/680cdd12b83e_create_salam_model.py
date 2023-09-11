"""Create salam model

Revision ID: 680cdd12b83e
Revises: 7ba33fbe6d31
Create Date: 2023-09-11 19:39:58.770497

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '680cdd12b83e'
down_revision: Union[str, None] = '7ba33fbe6d31'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
