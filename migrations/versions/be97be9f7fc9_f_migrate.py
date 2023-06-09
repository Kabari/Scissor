"""f migrate

Revision ID: be97be9f7fc9
Revises: 
Create Date: 2023-06-01 22:21:59.627234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be97be9f7fc9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(length=16), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password_hash', sa.Text(length=100), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('url',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(length=16), nullable=False),
    sa.Column('long_url', sa.String(length=2048), nullable=False),
    sa.Column('short_url', sa.String(length=6), nullable=False),
    sa.Column('custom_domain', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('qr_code', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('custom_domain'),
    sa.UniqueConstraint('short_url'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('click',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('ip_address', sa.String(length=50), nullable=True),
    sa.Column('user_agent', sa.String(length=255), nullable=True),
    sa.Column('referrer', sa.String(length=2048), nullable=True),
    sa.ForeignKeyConstraint(['url_id'], ['url.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('click')
    op.drop_table('url')
    op.drop_table('user')
    # ### end Alembic commands ###
