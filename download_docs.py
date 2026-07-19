import shutil
from pathlib import Path
from zipfile import ZipFile

from download_file import download_file


def download():
    temp = Path("temp/")
    temp.mkdir(parents=True, exist_ok=True)
    shutil.rmtree(temp)
    temp.mkdir(parents=True, exist_ok=True)

    json_zip = temp / "json.zip"
    lua_zip = temp / "lua.zip"

    download_file("https://scrapmechanic.com/api/json.zip", json_zip)
    download_file("https://scrapmechanic.com/api/lua.zip", lua_zip)
    with ZipFile(json_zip, "r") as archive:
        archive.extractall(temp)
    with ZipFile(lua_zip, "r") as archive:
        archive.extractall(temp)

    return temp / "json/", temp / "sm.lua"
