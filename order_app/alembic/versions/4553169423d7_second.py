"""second

Revision ID: 4553169423d7
Revises: 0b3911db7b8d
Create Date: 2023-12-06 22:30:47.318772

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4553169423d7'
down_revision: Union[str, None] = '0b3911db7b8d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
