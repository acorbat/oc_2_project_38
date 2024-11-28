from czifile import CziFile
from pathlib import Path
import numpy as np
from typing import Literal
from tifffile import imwrite


def load_image(filepath: Path, channel: Literal['motor', 'nuclei']) -> np.ndarray:
    """Loads an image from a CZI file."""
    image_handle = CziFile(filepath)
    if channel == 'motor':
        channel = 1
    elif channel == 'nuclei':
        channel = 2
    else:
        raise ValueError("Invalid channel")
    return np.squeeze(image_handle.asarray())[channel]


def get_scale(filepath: Path) -> tuple:
    """Gets the pixel size from a CZI file."""
    image_handle = CziFile(filepath)
    scale = {
    values_dict["Id"]: values_dict["Value"] * 10**6
    for values_dict in image_handle.metadata(raw=False)["ImageDocument"]["Metadata"][
        "Scaling"
    ]["Items"]["Distance"]
    }
    return scale


def save_labels(filepath: Path, image: np.ndarray) -> None:
    """Saves a label image to a tiff file."""
    imwrite(filepath, data=image, imagej=True, dtype="uint16")
