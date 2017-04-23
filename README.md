# demasker
Tries to reverse a mask overlay operation as best as possible.

## Motivation

https://www.reddit.com/r/picturegame is a fun subreddit that everyone should play. The basic gist is that you want to identify things in pictures, in order to answer questions (which may be as straightforward as "what is this thing?"). However, the advent of things like reverse image searching [RIS] (Google, Tineye, Bing, Yandex, etc. etc.) has often made it rather trivial to do identification. This is where masks come in, which when overlaid seem to successfully fool these engines.

Unfortunately this also means that such rounds are often less well constructed, and honestly rounds without masking are usually more elegant. (and less of an eyesore to humans, even if they are readable with the masking(kind of like a Captcha)) Thus, this was born.

Granted, many other round types immune to RIS are also relatively cookie-cutter, such as:

* name the subreddit by banner (only sometimes RISable)

* Youtube snippets (usually not RISable if a good screenshot is made)

* Google Maps screenshots (sometimes RISable)

* Wikipedia screenshots (usually not RISable)

* low-quality puzzles, and partly because very few players will get the high-quality ones without a large dosage of hints\* (The idea behind the puzzles are surely immune to RIS, but for instance almost all ciphers and encodings can be broken in rather straightforward ways)

\* the author appreciates puzzles and wishes that more rounds were puzzly rather than identification

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
