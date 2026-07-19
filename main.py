import download_docs

def main():
    json_docs, lua_sm = download_docs.download()
    print(json_docs, lua_sm)


if __name__ == "__main__":
    main()
