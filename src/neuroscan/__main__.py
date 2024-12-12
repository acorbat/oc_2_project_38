from argparse import ArgumentParser
import logging
from pathlib import Path
from tqdm import tqdm

from neuroscan.io import load_image, get_scale, save_labels
from neuroscan.segment import segment_nuclei, segment_motor_neuron

logger = logging.getLogger(__name__)


def main():
    logger.setLevel(logging.INFO)
    parser = ArgumentParser()
    parser.add_argument(
        "command",
        type=str,
        choices=["segment", "quantify"],
        help="Command to run. You can choose between segment "
        + "and quantify.",
    )
    parser.add_argument(
        "path",
        type=Path,
        help="Path to file or folder to process",
    )
    args = parser.parse_args()

    is_folder = args.path.is_dir()

    if args.command == "segment":
        if is_folder:
            segment_folder(
                folderpath=args.path,
            )
        else:
            segment_file(
                filepath=args.path,
            )
    elif args.command == "quantify":
        print("Not Implemented")
        # quantify_folder(folderpath=args.path)


def segment_file(
    filepath: Path,
) -> None:
    """Segments an image file and saves it."""
    logger.info("Loading image %s" % str(filepath))
    scale = get_scale(filepath)

    for channel in ["motor", "nuclei"]:
        savepath = filepath.with_name(filepath.stem + f"_{channel}.tiff")
        if savepath.exists():
            logger.info(f"Skipping {channel} channel, already segmented")
            continue
        logger.info(f"Segmenting {channel} channel")
        image = load_image(filepath, channel=channel)
        if channel == "motor":
            labeled = segment_motor_neuron(image, scale=scale)
        elif channel == "nuclei":
            labeled = segment_nuclei(image, scale=scale)
        save_labels(savepath, labeled)


def segment_folder(
    folderpath: Path,
) -> None:
    """Runs segment file for a whole folder and subfolders."""
    filepaths = list(folderpath.rglob("*.czi"))

    logger.info(f"{len(filepaths)} images were found.")
    for filepath in tqdm(filepaths):
        logger.info(f"Segmenting image {filepath.stem}")
        segment_file(filepath=filepath)
        

if __name__ == "__main__":
    main()