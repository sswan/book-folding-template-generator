# book-folding-template-generator
Python script to generate templates for book folding.

You will need to have a black and white template where what is white
will be folded and black will not be folded. You will also need to
measure your book, I suggest using mm as it's easier to do fractions.
All of the user inputs are at the top of `generate_template.py` and
are documented.

The generator is set up to make a heart using `template.jpg' using
the book "Scientific Computing: An Introductory Survey" by Michael
T. Heath. A picture of the folded book is in `example.jpg`.

An example of the usage and output is given below.

```
$ python3 generate_template.py | head -n 30

===== Image Dimensions
Width pixels: 5068
Height pixels: 5000

===== Get data to check that the image was read correctly.
  left column with data is 477/5068
  right column with data is 4591/5068
  top row with data is 765/5000
  bottom row with data is 4533/5000

===== Art dimensions
  Art width: 292.2mm (art_arc_span)
  Art height: 267.6mm (art_img_height_mm)

=====> MEASURE FROM THE TOP OF THE PAGE <=====

pg:  29  edges: |   44.6mm    71.3mm   |
pg:  30  edges: |   39.1mm    76.8mm   |
pg:  31  edges: |   35.2mm    80.6mm   |
pg:  32  edges: |   31.8mm    84.0mm   |
pg:  33  edges: |   29.0mm    86.9mm   |
pg:  34  edges: |   26.6mm    89.4mm   |
pg:  35  edges: |   24.2mm    92.1mm   |
pg:  36  edges: |   22.2mm    94.3mm   |
pg:  37  edges: |   20.2mm    96.6mm   |
pg:  38  edges: |   18.5mm    98.6mm   |

pg:  39  edges: |   16.9mm   100.5mm   |
pg:  40  edges: |   15.3mm   102.6mm   |
```
