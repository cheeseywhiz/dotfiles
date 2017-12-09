#!/usr/bin/env python3
"""Tint a grayscale image with a color."""
import argparse
import os
import shlex
import sys
from PIL import Image
import numpy as np
import collect


class ImagePath(collect.Path):
    """A Path with image loading and saving via PIL and numpy."""
    @property
    def array(self):
        """Return the numpy array from the image at this path."""
        with self.open('rb') as file:
            return np.asarray(Image.open(file))

    def save(self, array):
        """Save an array as an image to this path."""
        array = np.clip(array, 0, 255)
        array = np.asarray(array, np.uint8)
        array = Image.fromarray(array)

        with open(self, 'wb') as file:
            array.save(file)

        return self

    def tint(self, color: (str, tuple), output: os.PathLike):
        """Tint the image at this path and save to the output path."""
        if isinstance(color, str):
            color = hex_to_rgb(color)

        ImagePath.save(output, tint_map(self.array, color))


def tint_map(grayscale_map, color):
    """Given a 2d numpy array height map, tint the map by the given RGB color
    tuple."""
    new_array = np.array([
        [color] * row.size
        for row in grayscale_map
    ]) * np.array([
        [[brightness] * 3
         for brightness in row]
        for row in grayscale_map
    ]) / np.mean(grayscale_map)
    return new_array


def hex_to_rgb(hex_str):
    """Convert the given string to an RGB tuple. Preceeding # optional."""
    return eval('(0x{0}{1}, 0x{2}{3}, 0x{4}{5})'.format(*hex_str.lstrip('#')))


class TintParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super().add_argument(
            'input', type=ImagePath, help='Input image path')
        super().add_argument(
            'color',
            help='The hex color to apply to the image. Preceeding # optional.')
        super().add_argument(
            'output', help='Output image path')

    def parse_args(self, argv=None, *args, **kwargs):
        if argv is None:
            argv = sys.argv[1:]
        elif isinstance(argv, str):
            argv = shlex.split(argv)

        args = super().parse_args(argv, *args, **kwargs)
        args.input.tint(args.color, args.output)
        return args


def main(argv=None):
    TintParser(description=__doc__).parse_args(argv)


if __name__ == '__main__':
    main()
