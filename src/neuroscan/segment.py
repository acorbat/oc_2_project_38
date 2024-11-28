from cellpose import models
from cellpose.io import logger_setup
from skimage.exposure import equalize_adapthist
from skimage.morphology import ball, erosion, remove_small_objects
from skimage.filters import gaussian
from skimage.util import apply_parallel
import numpy as np

logger_setup()


def segment_nuclei(image: np.ndarray, scale: tuple) -> np.ndarray:
    """Segments nuclei from the image. spacing is the pixel size in micrometers (Z, Y, X)."""
    smoothed_img = gaussian(image, sigma=(1/scale["Z"], 0.5/scale["Y"], 0.5/scale["X"]))

    model = models.Cellpose(model_type="cyto3")

    anisotropy = scale["Z"] / scale["X"]
    diameter = 10 / scale["X"]

    masks, flows, styles, diams = model.eval(
        [smoothed_img],
        batch_size=8,
        diameter=diameter,
        z_axis=0,
        do_3D=True,
        channels=[0, 0],
        # stitch_threshold=0.5,
        normalize=True,
        flow_threshold=0.2,
        cellprob_threshold=4.0,
        anisotropy=anisotropy,
    )

    voxel_size = scale["X"] * scale["Y"] * scale["Z"]
    minimum_nuclei_volume = 2000 * voxel_size

    label = apply_parallel(erosion, masks[0], chunks=(1, masks[0].shape[1], masks[0].shape[2]), compute=True, extra_keywords={"footprint": ball(4)}, dtype="uint16")
    label = remove_small_objects(label, minimum_nuclei_volume / voxel_size)
    return label


def segment_motor_neuron(image: np.ndarray, scale: tuple) -> np.ndarray:
    """Segments motor neurons from the iamge. spacing is the pixel size in micrometers (Z, Y, X)."""
    smooth = gaussian(image, (1.714 / scale["Z"], 0.514 / scale["Y"], 0.514 / scale["X"]))

    model = models.Cellpose(model_type="cyto3")

    anisotropy = scale["Z"] / scale["X"]
    diameter = 10 / scale["X"]

    masks, flows, styles, diams = model.eval(
        [smooth],
        batch_size=8,
        diameter=diameter,
        z_axis=0,
        do_3D=True,
        channels=[0, 0],
        # stitch_threshold=0.5,
        normalize=True,
        anisotropy=anisotropy,
        flow_threshold=-0.1,
        cellprob_threshold=6.0,
        compute_masks=True,
    )

    voxel_size = scale["X"] * scale["Y"] * scale["Z"]
    minimum_nuclei_volume = 2000 * voxel_size

    label = remove_small_objects(masks[0], minimum_nuclei_volume / voxel_size)
    return label
