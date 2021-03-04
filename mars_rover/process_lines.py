from validation import validation


def main(lines):
    # The first line is the plateau and every rover needs two lines, so the array must have odd length.
    validation.ensure_has_odd_lentgh(lines)
    print("I'm process_lines.main")
