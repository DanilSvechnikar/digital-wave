"""This file contains functions related to bbox."""

from pathlib import Path

import numpy as np


def save_to_txt(
    label_file: Path,
    bboxes: list[np.float64],
    class_labels: list[int],
) -> None:
    """Saves label and bbox to a txt file."""
    with open(label_file, "w") as file:
        for bbox, class_label in zip(bboxes, class_labels):
            name_label = "person" if class_label == 0 else "tractor"
            file.write(f"{name_label} {bbox[0]} {bbox[1]} {bbox[2]} {bbox[3]}\n")
