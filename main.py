import cv2
import os
import numpy as np
from models.object_detector import Detector
from models.denoiser import Denoiser
from models.depth_estimator import DepthEstimator
from utils.config import get_config
from utils.files import get_filelist
from models.image_handler import ImageHandler


def main():
    test = 1
    data_folder = r'D:\MnS\Projects\Algo\data'
    config_folder = r'D:\MnS\Projects\Algo\config'
    config = get_config(os.path.join(config_folder, "default.yaml"))
    filelist = get_filelist(data_folder)
    deno = Denoiser(blur=75)
    detector_config = config['detector']
    detector = Detector(**detector_config)
    estimator = DepthEstimator(model_type='DPT_Large')
    for image_file in filelist:
        image = ImageHandler.load_image(data_folder, image_file, flags=cv2.IMREAD_COLOR)
        removal_image = deno.removal_light(image)
        tensor = ImageHandler.convert_tensor(removal_image)
        detected_image, info, raw_boxes = detector(tensor)
        prediction = estimator(removal_image)
        save_image = prediction
        if info is not None:
            rois, means = ImageHandler.get_ROIs(info[0], prediction)
            depth_image = ImageHandler.draw_depth_info(prediction, info[0], means)
            save_image = depth_image
        cv2.imwrite(os.path.join(r'D:\MnS\Projects\Algo\outputs', image_file), save_image)


if __name__ == '__main__':
    main()
