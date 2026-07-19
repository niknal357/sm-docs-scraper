import download_docs
import make_ir
import render_docs


def main():
    json_docs, lua_docs = download_docs.download()
    ir = make_ir.make_ir(json_docs)
    ir_path = make_ir.write_ir(ir, json_docs.parent / "ir")
    markdown_path, html_path = render_docs.render_docs(
        ir,
        json_docs.parent / "markdown",
        json_docs.parent / "html",
    )
    print(f"Downloaded JSON docs to {json_docs}")
    print(f"Downloaded Lua docs to {lua_docs}")
    print(f"Wrote IR to {ir_path}")
    print(f"Wrote Markdown docs to {markdown_path}")
    print(f"Wrote HTML docs to {html_path}")


if __name__ == "__main__":
    main()
