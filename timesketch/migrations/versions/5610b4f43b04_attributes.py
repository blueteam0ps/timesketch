"""attributes

Revision ID: 5610b4f43b04
Revises: None
Create Date: 2020-10-23 10:09:30.817613

"""

# revision identifiers, used by Alembic.
revision = '5610b4f43b04'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('attribute_status')
    op.drop_table('attribute_label')
    op.drop_table('attribute_comment')
    op.add_column('attribute', sa.Column('attributecontainer_id', sa.Integer(), nullable=True))
    op.add_column('attribute', sa.Column('ontology', sa.UnicodeText(), nullable=True))
    op.add_column('attribute', sa.Column('value', sa.UnicodeText(), nullable=True))
    op.drop_constraint('attribute_sketch_id_fkey', 'attribute', type_='foreignkey')
    op.create_foreign_key(None, 'attribute', 'attributecontainer', ['attributecontainer_id'], ['id'])
    op.drop_column('attribute', 'sketch_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('attribute', sa.Column('sketch_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'attribute', type_='foreignkey')
    op.create_foreign_key('attribute_sketch_id_fkey', 'attribute', 'sketch', ['sketch_id'], ['id'])
    op.drop_column('attribute', 'value')
    op.drop_column('attribute', 'ontology')
    op.drop_column('attribute', 'attributecontainer_id')
    op.create_table('attribute_comment',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('comment', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('parent_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['attribute.id'], name='attribute_comment_parent_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='attribute_comment_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='attribute_comment_pkey')
    )
    op.create_table('attribute_label',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('label', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('parent_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['attribute.id'], name='attribute_label_parent_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='attribute_label_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='attribute_label_pkey')
    )
    op.create_table('attribute_status',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('parent_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['attribute.id'], name='attribute_status_parent_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='attribute_status_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='attribute_status_pkey')
    )
    # ### end Alembic commands ###
