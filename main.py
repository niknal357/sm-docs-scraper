import argparse
from pathlib import Path

import download_docs
import make_ir
import render_docs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path)
    args = parser.parse_args()

    if args.source_root is None:
        source = download_docs.download()
    else:
        source = download_docs.load_downloaded(args.source_root)

    ir = make_ir.make_ir(source.json_docs)
    ir_path = make_ir.write_ir(ir, source.json_docs.parent / "ir")
    markdown_path, html_path = render_docs.render_docs(
        ir,
        Path("dist/markdown"),
        Path("dist/html"),
    )
    source_hash_path = download_docs.write_source_digest(
        html_path,
        source.source_digest,
    )

    print(f"Downloaded JSON docs at {source.json_docs}")
    print(f"Downloaded Lua docs at {source.lua_docs}")
    print(f"Wrote IR to {ir_path}")
    print(f"Wrote Markdown docs to {markdown_path}")
    print(f"Wrote HTML docs to {html_path}")
    print(f"Wrote API source digest to {source_hash_path}")


if __name__ == "__main__":
    main()
