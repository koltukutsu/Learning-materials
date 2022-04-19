import math
import numpy as np
from data_augmentation_yolo.image_transformer import SampleImgTransformer
import pytest

BG_COLOR = 255
BG_THRESH = 8


def test_median_noise(sample_image):
    image_modifier = SampleImgTransformer(
        image=sample_image, bg_color=BG_COLOR, bg_thresh=BG_THRESH
    )
    foregroundPix = np.where(image_modifier.mask_image == 0)

    total_pixel = np.size(foregroundPix) / 2
    percent_pixel = 0.3
    percent_salt = 0.4
    image_modifier.addMedianNoise(percentPixel=percent_pixel, percentSalt=percent_salt)

    count_pepper = np.count_nonzero(
        np.sum(image_modifier.modified_image[foregroundPix], -1) == 0
    )
    count_salt = np.count_nonzero(
        np.sum(image_modifier.modified_image[foregroundPix], -1) == 765
    )
    assert math.isclose(
        (count_salt + count_pepper), (percent_pixel * total_pixel), rel_tol=0.05
    )
    assert math.isclose(
        float(count_salt) / (count_salt + count_pepper), percent_salt, rel_tol=0.05
    )


def test_guassian_noise(sample_image):
    true_mean = 1
    true_variance = 2
    image_modifier = SampleImgTransformer(
        image=sample_image, bg_color=BG_COLOR, bg_thresh=BG_THRESH
    )
    image_modifier.addGaussianNoise(noiseMean=true_mean, noiseVariance=true_variance)
    indices = np.where(image_modifier.mask_image == 0)
    diff_pixels = image_modifier.modified_image[indices] - image_modifier.image[indices]
    actual_mean = np.mean(diff_pixels)
    actual_variance = np.var(diff_pixels)
    assert math.isclose(actual_mean, true_mean, rel_tol=0.05)

    assert math.isclose(actual_variance, true_variance, rel_tol=0.05)
