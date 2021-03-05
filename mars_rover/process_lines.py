from .validation import validation


def main(lines):
    # The first line is the plateau and every rover needs two lines, so the array must have odd length.
    validation.ensure_has_odd_lentgh(lines)
    if not lines[0]:
        raise ValueError("Missing data for the plateau")

    size_x, size_y = lines[0].split(" ")
    print(size_x, size_y)
