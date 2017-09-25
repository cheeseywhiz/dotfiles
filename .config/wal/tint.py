#!/usr/bin/env python3
"""Tint a grayscale image with a color."""
import argparse
import shlex
import sys
from PIL import Image
import numpy as np
import collect


class ImagePath(collect.path.Path):
    """A Path with Image loading and saving via PIL and numpy."""
    @property
    def array(self):
        """Return the numpy array from the image at this path."""
        with self.open('rb') as file:
            return np.asarray(Image.open(file))

    def save(self, array):
        """Save an array as an image to this path."""
        np.clip(array, 0, 255, array)
        array = np.asarray(array, dtype='uint8')

        with self.open('wb') as file:
            Image.fromarray(array).save(file, format='png')

        return self


def tint(grayscale_map, color):
    """Given a 2d numpy array height map, tint the map by the given color."""
    grayscale_rgb = np.ndarray((*grayscale_map.shape, 3))
    color_array = np.empty_like(grayscale_rgb)

    for i, row in enumerate(grayscale_map):
        for j, pixel in enumerate(row):
            for k, value in enumerate(color):
                color_array[i, j, k] = value
                grayscale_rgb[i, j, k] = pixel

    return color_array * grayscale_rgb / 127


def hex_to_rgb(hex_str):
    """Convert the given string to an RGB tuple. Preceeding # optional."""
    if hex_str[0] != '#':
        hex_str = '#' + hex_str

    return eval('(0x{1}{2}, 0x{3}{4}, 0x{5}{6})'.format(*hex_str))


class TintParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super().add_argument(
            'input', type=ImagePath,
            help='Input image path')
        super().add_argument(
            'output', type=ImagePath,
            help='Output image path')
        super().add_argument(
            'color', type=hex_to_rgb,
            help='The hex color to apply to the image. Preceeding # optional.')

    def parse_args(self, argv=None, *args, **kwargs):
        if argv is None:
            argv = sys.argv[1:]
        elif isinstance(argv, str):
            argv = shlex.split(argv)

        args = super().parse_args(argv, *args, **kwargs)
        args.output.save(tint(args.input.array, args.color))
        return args


def main(argv=None):
    TintParser(description=__doc__).parse_args(argv)


if __name__ == '__main__':
    main()
