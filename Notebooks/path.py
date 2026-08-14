from pathlib import Path
import scipy.io


# Set this to the local directory containing the EEG dataset.
# Example:
# DATA_DIR = Path(r"E:/TDA_Implementation/SubjectData/Data")
DATA_DIR = Path("data")


def load_data(sub, type):
    """Load EEG data, labels, and channel labels for a subject."""
    data1 = scipy.io.loadmat(
        DATA_DIR / "Whole" / "DataLabel" / f"sub{sub}_data1.mat"
    )["data1"]

    label1 = scipy.io.loadmat(
        DATA_DIR / "Whole" / "DataLabel" / f"sub{sub}_label1.mat"
    )["label1"][0]

    label_ch1 = scipy.io.loadmat(
        DATA_DIR / "channel_label.mat"
    )["channel_label"]

    return data1, label1, label_ch1


def load_matrix(sub, method):
    """Load the functional connectivity matrix for a subject and method."""
    matrix_path = (
        DATA_DIR
        / "Whole"
        / "Matrix"
        / method
        / f"Subject{sub}.mat"
    )

    return scipy.io.loadmat(matrix_path)
