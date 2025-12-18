import sqlite3
from pathlib import Path

# Create database directory if it doesn't exist
db_path = Path("data/amr_knowledgebase.db")
db_path.parent.mkdir(parents=True, exist_ok=True)

# Connect to SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Enable foreign key constraints
cursor.execute("PRAGMA foreign_keys = ON;")

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS organisms (
    organism_id INTEGER PRIMARY KEY AUTOINCREMENT,
    organism_name TEXT NOT NULL,
    taxonomy_id INTEGER,
    gram_type TEXT,
    notes TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS resistance_genes (
    gene_id INTEGER PRIMARY KEY AUTOINCREMENT,
    gene_name TEXT NOT NULL,
    gene_family TEXT,
    resistance_mechanism TEXT,
    description TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS antibiotics (
    antibiotic_id INTEGER PRIMARY KEY AUTOINCREMENT,
    antibioticotic_name TEXT NOT NULL,
    drug_class TEXT,
    target TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS evidence (
    evidence_id INTEGER PRIMARY KEY AUTOINCREMENT,
    evidence_type TEXT,
    source TEXT,
    reference_id TEXT,
    year INTEGER,
    geography TEXT,
    notes TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS organism_gene_mapping (
    mapping_id INTEGER PRIMARY KEY AUTOINCREMENT,
    organism_id INTEGER,
    gene_id INTEGER,
    FOREIGN KEY (organism_id) REFERENCES organisms (organism_id),
    FOREIGN KEY (gene_id) REFERENCES resistance_genes (gene_id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS gene_antibiotic_mapping (
    mapping_id INTEGER PRIMARY KEY AUTOINCREMENT,
    gene_id INTEGER,
    antibiotic_id INTEGER,
    FOREIGN KEY (gene_id) REFERENCES resistance_genes (gene_id),
    FOREIGN KEY (antibiotic_id) REFERENCES antibiotics (antibiotic_id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS gene_evidence_mapping (
    mapping_id INTEGER PRIMARY KEY AUTOINCREMENT,
    gene_id INTEGER,
    evidence_id INTEGER,
    FOREIGN KEY (gene_id) REFERENCES resistance_genes (gene_id),
    FOREIGN KEY (evidence_id) REFERENCES evidence (evidence_id)
);
""")

# Commit and close
conn.commit()
conn.close()

print("AMR KnowledgeBase database schema created successfully.")
