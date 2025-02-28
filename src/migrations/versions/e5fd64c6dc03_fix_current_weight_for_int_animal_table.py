"""fix current_weight for int animal table

Revision ID: e5fd64c6dc03
Revises: b10d94c4c8a7
Create Date: 2025-02-28 16:05:10.660257

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# Revision identifiers, used by Alembic.
revision: str = 'e5fd64c6dc03'
down_revision: Union[str, None] = 'b10d94c4c8a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Apagar a tabela nova se já existir (evita erro se migração for rodada várias vezes)
    op.execute("DROP TABLE IF EXISTS animal_new")

    # Criar nova tabela com todas as colunas corretamente configuradas
    op.create_table(
        'animal_new',
        sa.Column('id', sa.String, primary_key=True, unique=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('breed', sa.String, nullable=True),
        sa.Column('age', sa.Integer, nullable=True),
        sa.Column('gender', sa.String, nullable=False),
        sa.Column('health_condition', sa.String, nullable=True),
        sa.Column('current_weight', sa.Integer, nullable=False),  # Alterado para INTEGER corretamente
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.utcnow),
        sa.Column('updated_at', sa.DateTime, nullable=False, default=datetime.utcnow),
        sa.Column('farm_id', sa.String, sa.ForeignKey("farm.id"), nullable=False),
    )

    # Copiar os dados da tabela antiga para a nova (apenas colunas existentes)
    op.execute('''
        INSERT INTO animal_new (id, name, breed, age, gender, health_condition, current_weight, created_at, updated_at, farm_id)
        SELECT id, name, breed, age, gender, health_condition, current_weight, created_at, updated_at, farm_id FROM animal
    ''')

    # Remover a tabela antiga
    op.drop_table('animal')

    # Renomear a nova tabela para substituir a antiga
    op.rename_table('animal_new', 'animal')


def downgrade() -> None:
    """Implementar reversão da migração, se necessário"""
    pass
