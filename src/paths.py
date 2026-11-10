"""
Centralização dos caminhos de diretórios e arquivos do projeto CampaignScore.

Este módulo define a estrutura de diretórios do projeto e disponibiliza
caminhos absolutos para leitura e escrita de dados, modelos, relatórios
e demais artefatos utilizados nas etapas de ingestão, preparação,
análise exploratória, engenharia de atributos e modelagem.

A definição centralizada dos caminhos garante consistência entre scripts
e notebooks, facilita a manutenção da estrutura do projeto e evita o uso
de caminhos fixos (hardcoded) ao longo do código.
"""

from pathlib import Path

# Raiz do projeto
BASE_PATH = Path(__file__).resolve().parents[1]

# Pastas principais
DATA_FOLDER = BASE_PATH / "data"
RAW_FOLDER = DATA_FOLDER / "raw"
PROCESSED_FOLDER = DATA_FOLDER / "processed"

MODELS_FOLDER = BASE_PATH / "models"
PREDICTIVE_FOLDER = MODELS_FOLDER / "predictive"
SEGMENTATION_FOLDER = MODELS_FOLDER / "segmentation"
REPORTS_FOLDER = BASE_PATH / "reports"

# data/raw
RAW_DATA = RAW_FOLDER / "customer_marketing_campaigns.csv"


# data/processed
PROCESSED_DATA = PROCESSED_FOLDER / "customer_data.parquet"
FEATURES_DATA = PROCESSED_FOLDER / "customer_features.parquet"
SEGMENTATION_DATA = PROCESSED_FOLDER / "customer_segmentation.parquet"
SEGMENT_ASSIGNMENTS = PROCESSED_FOLDER / "customer_segment_assignments.parquet"
PREDICTIVE_DATA = PROCESSED_FOLDER / "customer_predictive.parquet"
BUSINESS_PARAMETERS = PROCESSED_FOLDER / "business_parameters.json"

# reports
SEGMENT_PROFILE = REPORTS_FOLDER / "customer_segment_profile.csv"
