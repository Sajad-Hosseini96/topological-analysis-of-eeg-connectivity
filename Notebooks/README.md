# Notebooks

This directory contains the Jupyter notebook and supporting Python modules used for the analysis and classification procedures.

## Main Notebook

### `Feature Extraction & Classification.ipynb`

The main notebook implements three complementary classification approaches:

1. **Multivariate Pattern Analysis (MVPA)** using preprocessed EEG data.
2. **Functional connectivity matrix classification** using the entries of the connectivity matrices directly as input features.
3. **Topological Data Analysis (TDA)** applied to functional connectivity matrices, followed by classification using extracted topological features.

The notebook also includes the feature extraction, machine-learning, and evaluation procedures associated with these analyses.

## Supporting Files

### `path.py`

Provides functions for loading the input EEG data and functional connectivity matrices from local directories.

The required datasets are not included in this repository. The paths defined in this file should therefore be modified according to the local location of the data.

### `TFE/`

Contains feature-extraction code used by the main notebook.

Parts of this implementation were derived from software originally developed by **Samir Moustafa** and distributed under the MIT License. The original copyright notice and license terms are retained.

Further information regarding the third-party implementation and its license is provided in:

```text
TFE/README.md
```

## Data Processing

The preprocessing of the EEG recordings and the estimation of functional connectivity matrices were performed in MATLAB. The corresponding MATLAB source code is not included in this repository.

The Python notebook starts from:

* preprocessed EEG data for the MVPA analysis; and
* precomputed functional connectivity matrices for the direct matrix-classification and TDA analyses.

The functional connectivity measures considered include:

* Pearson correlation
* Spearman correlation
* Phase Locking Value (PLV)
* Phase Lag Index (PLI)

For the TDA analysis, the connectivity matrices are subsequently transformed into topological representations and used for topological feature extraction and classification.

