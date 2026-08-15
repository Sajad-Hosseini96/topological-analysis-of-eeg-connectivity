# Topological Analysis of EEG Functional Connectivity

This repository contains the Python implementation of the analysis and classification procedures used in our study of EEG functional connectivity and topological data analysis (TDA).

The analysis compares three complementary classification approaches:

1. **Multivariate Pattern Analysis (MVPA)** using preprocessed EEG signals.
2. **Functional connectivity matrix classification** using the entries of the connectivity matrices directly as input features.
3. **Topological Data Analysis (TDA)** applied to functional connectivity matrices, followed by classification using extracted topological features.

The repository is intended to provide the computational implementation of the Python-based analyses associated with the study.

---

## Analysis Overview

The overall analysis consists of three classification pathways:

```text
                         EEG recordings
                              │
                              ▼
                     MATLAB preprocessing
                              │
                      Preprocessed EEG
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
               MVPA                Functional Connectivity
                 │                         │
                 │                 MATLAB connectivity analysis
                 │                         │
                 │                  Connectivity Matrices
                 │                         │
                 │                 ┌───────┴─────────────┐
                 │                 │                     │
                 │                 ▼                     ▼
                 │            Matrix-entry              TDA
                 │                 |                     │
                 │                 |                     ▼
                 │                 |           Topological features
                 │                 │                     │
                  ─────────────────|─────────────────────
                                   ▼                     
                             Classification
```

### 1. MVPA

MVPA is performed using **preprocessed EEG data**.

The EEG preprocessing procedure was performed in MATLAB and is not included in this repository. The Python notebook contains the subsequent analysis and classification procedures.

### 2. Functional Connectivity Matrix Classification

Functional connectivity matrices were generated from the preprocessed EEG data using MATLAB.

In this analysis, the individual entries of the connectivity matrices are used directly as classification features, without applying topological transformations.

The connectivity measures considered include:

* Pearson correlation
* Spearman correlation
* Phase Locking Value (PLV)
* Phase Lag Index (PLI)

### 3. Topological Data Analysis

For the TDA-based approach, the precomputed functional connectivity matrices are treated as the input representation of the functional brain network.

Topological features are extracted through persistent homology using Vietoris–Rips persistence. The resulting persistence information is subsequently transformed into feature representations for machine-learning classification.

The implemented topological representations include:

* Persistence diagrams
* Persistence landscapes
* Betti curves
* Persistence entropy

The extracted topological features are subsequently used for classification.

---

## Repository Structure

```text
topological-analysis-of-eeg-connectivity/
│
├── Notebooks/
│   │
│   ├── TFE/
│   │   ├── base.py
│   │   ├── common_routines.py
│   │   ├── __init__.py
│   │   └── README.md
│   │
│   ├── Feature Extraction & Classification.ipynb
│   ├── path.py
│   └── README.md
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

### `Notebooks/Feature Extraction & Classification.ipynb`

This is the main analysis notebook and contains the Python implementation of the classification and feature-extraction procedures.

The notebook covers the three analysis pathways:

* MVPA using preprocessed EEG data
* Direct classification using connectivity matrix entries
* TDA-based feature extraction and classification

### `Notebooks/TFE/`

This directory contains third-party feature-extraction code used as part of the analysis.

The applicable copyright notice and MIT License associated with the original implementation are retained. See `Notebooks/TFE/README.md` for attribution and licensing information.

---


## Methods

The analysis incorporates the following computational methods:

### EEG and Functional Connectivity

* EEG preprocessing
* Pearson correlation
* Spearman correlation
* Phase Locking Value (PLV)
* Phase Lag Index (PLI)

The EEG preprocessing and connectivity estimation were performed in MATLAB.

### Topological Data Analysis

* Vietoris–Rips persistence
* Persistence diagrams
* Persistence landscapes
* Betti curves
* Persistence entropy
* Persistence amplitudes

### Machine Learning

The repository includes the machine-learning procedures used for classification and evaluation, including feature selection, dimensionality reduction, and classification methods implemented using scikit-learn.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Sajad-Hosseini96/topological-analysis-of-eeg-connectivity.git

cd topological-analysis-of-eeg-connectivity
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

The exact package versions used in the analysis are specified in `requirements.txt`.

---

## Running the Analysis

After installing the required dependencies:

1. Obtain the required EEG data and/or functional connectivity matrices from the corresponding data source.
2. Modify the data path in `Notebooks/path.py` according to the local data location.
3. Open:

```text
Notebooks/Feature Extraction & Classification.ipynb
```

4. Run the notebook sections corresponding to the desired analysis:

   * MVPA
   * Functional connectivity matrix classification
   * TDA-based classification

The MATLAB preprocessing and connectivity-estimation stages must be completed separately before running the corresponding Python analyses.

---


## License

The source code developed for this repository is distributed under the terms specified in `LICENSE`.

Third-party components included in the repository remain subject to their original licenses and copyright notices.

---

## Citation

If you use this repository or the methods implemented here, please cite the corresponding publication:

> Citation information will be added following publication.
