# demasker
Tries to reverse a mask overlay operation as best as possible.

## Requirements

Python 3.x

PIL (Python Imaging Library)

## How to use

Example usage: demasker("maskedimage.png", "mask.png"). 

Output will be spit out at "demask.png", unless a different location is specified.

If an image isn't fully masked, you can manually set an alpha. If the mask is shifted a little, you may have to determine the correct offsets, and change that.

## Future Developments

The current build appears to not have major issues. There may possibly be problems with negative offsets, so try to stick to the positive ones if possible.

Some possible future investigations include:

* Determining offsets/alpha automatically

* Generate additional mask pictures (for those who use new types of masks) given the masked and unmasked images - may require several samples to compute
