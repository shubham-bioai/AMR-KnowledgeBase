1️⃣ organisms table

Stores standardized organism information.

| Column Name   | Data Type    | Description                              |
| ------------- | ------------ | ---------------------------------------- |
| organism_id   | INTEGER (PK) | Unique organism identifier               |
| organism_name | TEXT         | Scientific name (e.g., Escherichia coli) |
| taxonomy_id   | INTEGER      | NCBI taxonomy ID                         |
| gram_type     | TEXT         | Gram-positive / Gram-negative            |
| notes         | TEXT         | Optional remarks                         |





2️⃣ resistance_genes table

Stores AMR gene details.

| Column Name          | Data Type    | Description                         |
| -------------------- | ------------ | ----------------------------------- |
| gene_id              | INTEGER (PK) | Unique gene identifier              |
| gene_name            | TEXT         | Gene symbol (e.g., blaTEM, mecA)    |
| gene_family          | TEXT         | Gene family (e.g., bla, tet)        |
| resistance_mechanism | TEXT         | Enzymatic degradation, efflux, etc. |
| description          | TEXT         | Functional description              |





3️⃣ antibiotics table

Stores antibiotic and drug class information.

| Column Name     | Data Type    | Description                             |
| --------------- | ------------ | --------------------------------------- |
| antibiotic_id   | INTEGER (PK) | Unique antibiotic identifier            |
| antibiotic_name | TEXT         | Drug name (e.g., Ampicillin)            |
| drug_class      | TEXT         | Beta-lactam, Aminoglycoside, etc.       |
| target          | TEXT         | Target site (cell wall, ribosome, etc.) |





4️⃣ evidence table

Stores supporting evidence for resistance.

| Column Name   | Data Type    | Description                       |
| ------------- | ------------ | --------------------------------- |
| evidence_id   | INTEGER (PK) | Unique evidence identifier        |
| evidence_type | TEXT         | Genomic / Phenotypic / Literature |
| source        | TEXT         | NCBI / CARD / WHO / PubMed        |
| reference_id  | TEXT         | Accession ID / DOI / PMID         |
| year          | INTEGER      | Year of publication               |
| geography     | TEXT         | Country / region                  |
| notes         | TEXT         | Additional details                |





5️⃣ organism_gene_mapping table

Maps organisms to resistance genes.

| Column Name | Data Type    | Description                 |
| ----------- | ------------ | --------------------------- |
| mapping_id  | INTEGER (PK) | Unique mapping identifier   |
| organism_id | INTEGER (FK) | References organisms        |
| gene_id     | INTEGER (FK) | References resistance_genes |





6️⃣ gene_antibiotic_mapping table

Maps resistance genes to affected antibiotics.

| Column Name   | Data Type    | Description                 |
| ------------- | ------------ | --------------------------- |
| mapping_id    | INTEGER (PK) | Unique mapping identifier   |
| gene_id       | INTEGER (FK) | References resistance_genes |
| antibiotic_id | INTEGER (FK) | References antibiotics      |





7️⃣ gene_evidence_mapping table

Links genes with supporting evidence.

| Column Name | Data Type    | Description                 |
| ----------- | ------------ | --------------------------- |
| mapping_id  | INTEGER (PK) | Unique mapping identifier   |
| gene_id     | INTEGER (FK) | References resistance_genes |
| evidence_id | INTEGER (FK) | References evidence         |
