import argparse
import os

from bemani.format import IFS


def main() -> None:
    parser = argparse.ArgumentParser(description="A utility to extract IFS files.")
    parser.add_argument(
        "file",
        help="IFS file to extract.",
        type=str,
    )
    parser.add_argument(
        "-d",
        "--directory",
        help="Directory to extract to. Defaults to current directroy.",
        default="."
    )
    parser.add_argument(
        "--convert-xml-files",
        help="Convert xml files that are in binary.",
        action="store_true",
    )
    parser.add_argument(
        "--convert-texture-files",
        help="Convert texture files that are in game-format.",
        action="store_true",
    )
    args = parser.parse_args()

    root = args.directory
    if root[-1] != '/':
        root = root + '/'
    root = os.path.realpath(root)

    fp = open(args.file, 'rb')
    data = fp.read()
    fp.close()

    ifs = IFS(data, args.convert_xml_files, args.convert_texture_files)
    for fn in ifs.filenames:
        print('Extracting {} to disk...'.format(fn))
        realfn = os.path.join(root, fn)
        dirof = os.path.dirname(realfn)
        os.makedirs(dirof, exist_ok=True)
        with open(realfn, 'wb') as fp:
            fp.write(ifs.read_file(fn))


if __name__ == '__main__':
    main()
