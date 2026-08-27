"""
MIT License

Copyright (c) 2026 sphericosprey

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from argparse import ArgumentParser
from pathlib import Path


PATCHES = [
    (
        "Patch 1",
        bytes.fromhex("8b 15 b8 ff 63 00 8d 45 fc 50 8d 4d f4 68 24 95 69 00 51 6a 00 52 8b 45 f8 50 ff d3"),
        bytes.fromhex("c7 05 24 95 69 00 00 00 00 00 66 90 66 90 66 90 66 90 66 90 66 90 66 90 66 90 66 90"),
    ),
    (
        "Patch 2",
        bytes.fromhex("89 1d 24 95 69 00"),
        bytes.fromhex("89 15 24 95 69 00"),
    ),
]


def apply_patch(inpath: Path, outpath: Path):
    data = inpath.read_bytes()

    for name, old, new in PATCHES:
        if len(old) != len(new):
            raise SystemExit(f"{name}: old/new length mismatch")
        count = data.count(old)
        if count != 1:
            raise SystemExit(f"{name}: expected 1 match, found {count}")
        data = data.replace(old, new)

    outpath.write_bytes(data)


def parse_args():
    parser = ArgumentParser(
        description="Heroes of Might and Magic 3 Skip Intro Patch",
    )

    parser.add_argument(
        "-i", "--input",
        default="Heroes3.exe",
        type=Path,
        help="Path to the HoMM3 executable",
    )
    
    parser.add_argument(
        "-o", "--output",
        default="Heroes3_skip_intro.exe", 
        type=Path,
        help="Path to the output executable",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    if not args.input.is_file():
        raise SystemExit(f"missing input file: {args.input}")

    apply_patch(args.input, args.output)

    print("Success!")
