"""
Utilities for loading, resizing and converting between PIL and WX image formats
"""

import sys
from PIL import Image  # type: ignore
import wx  # type: ignore

from GooeyEx.gui.three_to_four import bitmapFromBufferRGBA


def loadImage(img_path):
    return Image.open(img_path)


def resizeImage(im, targetHeight):
    im.thumbnail((sys.maxsize, targetHeight))
    return im


def wrapBitmap(im, parent):
    try:
        rgba = im.convert("RGBA").tobytes()
    except AttributeError:
        rgba = im.convert("RGBA").tostring()

    bitmapData = bitmapFromBufferRGBA(im, rgba)
    return wx.StaticBitmap(parent, bitmap=bitmapData)


if __name__ == "__main__":
    pass
