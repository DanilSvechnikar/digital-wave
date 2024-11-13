"""This is the main file for running the prediction by the model."""

from pathlib import Path

import cv2
from PIL import Image
from ultralytics import YOLO

from digital_wave import DATA_DIR, DEMO_DATA_DIR, MODELS_DIR
from digital_wave.bbox_utils import save_to_txt


def main() -> None:
    """Using the model."""
    output_image_dir = DATA_DIR / "Pred_images"
    output_image_dir.mkdir(exist_ok=True)

    output_txt_dir = DATA_DIR / "Pred_txt"
    output_txt_dir.mkdir(exist_ok=True)

    # Data should be in the path ./digital-wave/data/demo_data/
    model_fpath = MODELS_DIR / "yolov11n_best.pt"
    model = YOLO(model_fpath)

    result = model.predict(DEMO_DATA_DIR, verbose=False)
    for res in result:
        orig_image_fpath = Path(res.path)
        pred_image_fpath = output_image_dir / orig_image_fpath.name

        txt_fpath = orig_image_fpath.stem + ".txt"
        txt_fpath = output_txt_dir / txt_fpath

        img_with_boxes = cv2.cvtColor(res.plot(), cv2.COLOR_BGR2RGB)

        pil_img = Image.fromarray(img_with_boxes)
        pil_img.save(pred_image_fpath)

        classes = res.boxes.cls.numpy()
        bboxes = res.boxes.xyxy.numpy()

        save_to_txt(txt_fpath, bboxes, classes)


if __name__ == '__main__':
    main()
