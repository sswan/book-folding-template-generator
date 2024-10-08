#!/usr/bin/env python3
from PIL import Image
import numpy as np
import sys


# ========================================================= USER INPUTS

# Total number of pages in the book
unnumbered_pre_pages = 24
unnumbered_post_pages = 4
total_pages = 408

# How many pages you want to leave undisturbed at the front and back?
pre_post_buffer = 52


# How tall you want the text to be?
page_height_mm = 233.0
page_width_mm = 186.0

# File name of the black and white image.
template = "template.jpg"

# ===================================================== END USER INPUTS


if unnumbered_pre_pages > pre_post_buffer:
    raise Exception("the pre_post_buffer must be >= unnumbered_pre_pages")
if unnumbered_post_pages > pre_post_buffer:
    raise Exception("the pre_post_buffer must be >= unnumbered_post_pages")

pre_buffer = pre_post_buffer - unnumbered_pre_pages
post_buffer = pre_post_buffer - unnumbered_post_pages

# Read in the file, convert to grayscale, get image size.
im_frame = Image.open(template)
np_frame = np.array(im_frame)
data = np.sum(np_frame[:, :, :3], axis=2) < (255 / 2.0)
img_pix_h, img_pix_w = data.shape

print("\n===== Image Dimensions")
print(f"Width pixels: {img_pix_w}")
print(f"Height pixels: {img_pix_h}")

# Figure out how many columns and rows are blank around the border.
print("\n===== Get data to check that the image was read correctly.")
for left_col in range(img_pix_w):
    if any(data[:, left_col]):
        print(f"  left column with data is {left_col}/{img_pix_w}")
        break

for right_col in reversed(range(img_pix_w)):
    if any(data[:, right_col]):
        print(f"  right column with data is {right_col}/{img_pix_w}")
        break

for top_row in range(img_pix_h):
    if any(data[top_row, :]):
        print(f"  top row with data is {top_row}/{img_pix_h}")
        break

for bottom_row in reversed(range(img_pix_h)):
    if any(data[bottom_row, :]):
        print(f"  bottom row with data is {bottom_row}/{img_pix_h}")
        break

# Figure out the size of the image, assume book opens 90 degrees.
art_arc_span_mm = page_width_mm * np.pi / 2.0
art_aspect_ratio = (bottom_row - top_row) / (right_col - left_col)
art_img_height_mm = art_arc_span_mm * art_aspect_ratio
print("\n===== Art dimensions")
print(f"  Art width: {art_arc_span_mm:.1f}mm (art_arc_span)")
print(f"  Art height: {art_img_height_mm:.1f}mm (art_img_height_mm)")

print("\n=====> MEASURE FROM THE TOP OF THE PAGE <=====\n")
page_break_cntr = 0
for cur_page in range(1 + pre_buffer, total_pages + 1 - post_buffer):
    x_frac = (cur_page - pre_buffer) / (total_pages - pre_buffer - post_buffer)

    img_col = round(left_col + x_frac * (right_col - left_col))

    changes_indicies = np.argwhere(np.diff(data[:, img_col])).flatten()

    # plus 1 and (-0.5) because np.diff.
    changes_fracs = (changes_indicies - top_row + 1) / (bottom_row - top_row)
    changes_mm = (changes_fracs - 0.5) * art_img_height_mm + page_height_mm / 2.0

    if len(changes_mm) % 2 != 0:
        raise Exception(f"len(changes_mm) must be even! got {len(changes_mm)}")

    changes_txt = "  ".join(
        [
            f"{_: 6.1f}mm" + ("   |" if idx % 2 == 1 else "")
            for idx, _ in enumerate(changes_mm)
        ]
    )

    print(f"pg:{cur_page: 4d}  edges: | {changes_txt}")
    page_break_cntr += 1
    if page_break_cntr == 10:
        print("")
        page_break_cntr = 0
