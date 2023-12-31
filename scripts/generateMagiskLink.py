#!/usr/bin/python3
#
# This file is part of MagiskOnWSALocal.
#
# MagiskOnWSALocal is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# MagiskOnWSALocal is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with MagiskOnWSALocal.  If not, see <https://www.gnu.org/licenses/>.
#
# Copyright (C) 2023 LSPosed Contributors
#

import sys

import json
import requests
from pathlib import Path

magisk_ver = sys.argv[1]
download_dir = Path.cwd().parent / "download" if sys.argv[2] == "" else Path(sys.argv[2])
tempScript = sys.argv[3]
print(f"Generating Magisk download link: release type={magisk_ver}", flush=True)
if not magisk_ver:
    magisk_ver = "stable"
if magisk_ver == "stable" or magisk_ver == "beta" or magisk_ver == "canary" or magisk_ver == "debug":
    try:
        magisk_link = json.loads(requests.get(
            f"https://github.com/topjohnwu/magisk-files/raw/master/{magisk_ver}.json").content)['magisk']['link']
    except Exception:
        print("Failed to fetch from GitHub API, fallbacking to jsdelivr...")
        magisk_link = json.loads(requests.get(
            f"https://fastly.jsdelivr.net/gh/topjohnwu/magisk-files@master/{magisk_ver}.json").content)['magisk']['link']

elif magisk_ver == "delta-stable":
    try:
        magisk_link = json.loads(requests.get(
            f"https://raw.githubusercontent.com/magojohnji/magisk-files-host/master/delta/stable.json").content)['magisk']['link']
    except Exception:
        print("Failed to fetch from GitHub API, fallbacking to jsdelivr...")
        magisk_link = json.loads(requests.get(
            f"https://fastly.jsdelivr.net/gh/magojohnji/magisk-files-host@master//delta/stable.json").content)['magisk']['link']

elif magisk_ver == "delta-beta":
    try:
        magisk_link = json.loads(requests.get(
            f"https://raw.githubusercontent.com/magojohnji/magisk-files-host/master/delta/beta.json").content)['magisk']['link']
    except Exception:
        print("Failed to fetch from GitHub API, fallbacking to jsdelivr...")
        magisk_link = json.loads(requests.get(
            f"https://fastly.jsdelivr.net/gh/magojohnji/magisk-files-host@master/delta/beta.json").content)['magisk']['link']

elif magisk_ver == "delta-canary":
    try:
        magisk_link = json.loads(requests.get(
            f"https://raw.githubusercontent.com/magojohnji/magisk-files-host/master/delta/canary.json").content)['magisk']['link']
    except Exception:
        print("Failed to fetch from GitHub API, fallbacking to jsdelivr...")
        magisk_link = json.loads(requests.get(
            f"https://fastly.jsdelivr.net/gh/magojohnji/magisk-files-host@master/delta/canary.json").content)['magisk']['link']

elif magisk_ver == "delta-debug":
    try:
        magisk_link = json.loads(requests.get(
            f"https://raw.githubusercontent.com/magojohnji/magisk-files-host/master/delta/debug.json").content)['magisk']['link']
    except Exception:
        print("Failed to fetch from GitHub API, fallbacking to jsdelivr...")
        magisk_link = json.loads(requests.get(
            f"https://fastly.jsdelivr.net/gh/magojohnji/magisk-files-host@master/delta/debug.json").content)['magisk']['link']

elif magisk_ver == "delta-lite-canary":
    try:
        magisk_link = json.loads(requests.get(
            f"https://raw.githubusercontent.com/magojohnji/magisk-files-host/master/delta_lite/canary.json").content)['magisk']['link']
    except Exception:
        print("Failed to fetch from GitHub API, fallbacking to jsdelivr...")
        magisk_link = json.loads(requests.get(
            f"https://fastly.jsdelivr.net/gh/magojohnji/magisk-files-host@master/delta_lite/canary.json").content)['magisk']['link']

elif magisk_ver == "delta-lite-debug":
    try:
        magisk_link = json.loads(requests.get(
            f"https://raw.githubusercontent.com/magojohnji/magisk-files-host/master/delta_lite/debug.json").content)['magisk']['link']
    except Exception:
        print("Failed to fetch from GitHub API, fallbacking to jsdelivr...")
        magisk_link = json.loads(requests.get(
            f"https://fastly.jsdelivr.net/gh/magojohnji/magisk-files-host@master/delta_lite/debug.json").content)['magisk']['link']

elif magisk_ver == "maru-canary":
    try:
        magisk_link = json.loads(requests.get(
            f"https://raw.githubusercontent.com/magojohnji/magisk-files-host/master/maru/canary.json").content)['magisk']['link']
    except Exception:
        print("Failed to fetch from GitHub API, fallbacking to jsdelivr...")
        magisk_link = json.loads(requests.get(
            f"https://fastly.jsdelivr.net/gh/magojohnji/magisk-files-host@master/maru/canary.json").content)['magisk']['link']

elif magisk_ver == "maru-debug":
    try:
        magisk_link = json.loads(requests.get(
            f"https://raw.githubusercontent.com/magojohnji/magisk-files-host/master/maru/debug.json").content)['magisk']['link']
    except Exception:
        print("Failed to fetch from GitHub API, fallbacking to jsdelivr...")
        magisk_link = json.loads(requests.get(
            f"https://fastly.jsdelivr.net/gh/magojohnji/magisk-files-host@master/maru/debug.json").content)['magisk']['link']

elif magisk_ver == "maru-debug":
    try:
        magisk_link = json.loads(requests.get(
            f"https://raw.githubusercontent.com/magojohnji/magisk-files-host/master/maru/debug.json").content)['magisk']['link']
    except Exception:
        print("Failed to fetch from GitHub API, fallbacking to jsdelivr...")
        magisk_link = json.loads(requests.get(
            f"https://fastly.jsdelivr.net/gh/magojohnji/magisk-files-host@master/maru/debug.json").content)['magisk']['link']

elif magisk_ver == "cygisk-canary":
    try:
        magisk_link = json.loads(requests.get(
            f"https://raw.githubusercontent.com/magojohnji/magisk-files-host/master/cygisk/canary.json").content)['magisk']['link']
    except Exception:
        print("Failed to fetch from GitHub API, fallbacking to jsdelivr...")
        magisk_link = json.loads(requests.get(
            f"https://fastly.jsdelivr.net/gh/magojohnji/magisk-files-host@master/cygisk/canary.json").content)['magisk']['link']

elif magisk_ver == "cygisk-debug":
    try:
        magisk_link = json.loads(requests.get(
            f"https://raw.githubusercontent.com/magojohnji/magisk-files-host/master/cygisk/debug.json").content)['magisk']['link']
    except Exception:
        print("Failed to fetch from GitHub API, fallbacking to jsdelivr...")
        magisk_link = json.loads(requests.get(
            f"https://fastly.jsdelivr.net/gh/magojohnji/magisk-files-host@master/cygisk/debug.json").content)['magisk']['link']

elif magisk_ver == "monet-stable":
    try:
        magisk_link = json.loads(requests.get(
            f"https://raw.githubusercontent.com/magojohnji/magisk-files-host/master/monet/stable.json").content)['magisk']['link']
    except Exception:
        print("Failed to fetch from GitHub API, fallbacking to jsdelivr...")
        magisk_link = json.loads(requests.get(
            f"https://fastly.jsdelivr.net/gh/magojohnji/magisk-files-host@master/monet/stable.json").content)['magisk']['link']

elif magisk_ver == "monet-beta":
    try:
        magisk_link = json.loads(requests.get(
            f"https://raw.githubusercontent.com/magojohnji/magisk-files-host/master/monet/beta.json").content)['magisk']['link']
    except Exception:
        print("Failed to fetch from GitHub API, fallbacking to jsdelivr...")
        magisk_link = json.loads(requests.get(
            f"https://fastly.jsdelivr.net/gh/magojohnji/magisk-files-host@master/monet/beta.json").content)['magisk']['link']

elif magisk_ver == "monet-canary":
    try:
        magisk_link = json.loads(requests.get(
            f"https://raw.githubusercontent.com/magojohnji/magisk-files-host/master/monet/canary.json").content)['magisk']['link']
    except Exception:
        print("Failed to fetch from GitHub API, fallbacking to jsdelivr...")
        magisk_link = json.loads(requests.get(
            f"https://fastly.jsdelivr.net/gh/magojohnji/magisk-files-host@master/monet/canary.json").content)['magisk']['link']

elif magisk_ver == "monet-debug":
    try:
        magisk_link = json.loads(requests.get(
            f"https://raw.githubusercontent.com/magojohnji/magisk-files-host/master/moent/debug.json").content)['magisk']['link']
    except Exception:
        print("Failed to fetch from GitHub API, fallbacking to jsdelivr...")
        magisk_link = json.loads(requests.get(
            f"https://fastly.jsdelivr.net/gh/magojohnji/magisk-files-host@master/monet/debug.json").content)['magisk']['link']

elif magisk_ver == "alpha":
    try:
        magisk_link = json.loads(requests.get(
            f"https://raw.githubusercontent.com/vvb2060/magisk_files/alpha/alpha.json").content)['magisk']['link']
    except Exception:
        print("Failed to fetch from GitHub API, fallbacking to jsdelivr...")
        magisk_link = json.loads(requests.get(
            f"https://fastly.jsdelivr.net/gh/vvb2060/magisk_files/alpha.json").content)['magisk']['link']

elif magisk_ver == "lite":
    try:
        magisk_link = json.loads(requests.get(
            f"https://raw.githubusercontent.com/magojohnji/magisk-files-host/master/lite/lite.json").content)['magisk']['link']
    except Exception:
        print("Failed to fetch from GitHub API, fallbacking to jsdelivr...")
        magisk_link = json.loads(requests.get(
            f"https://fastly.jsdelivr.net/gh/magojohnji/magisk-files-host@master/lite/lite.json").content)['magisk']['link']

print(f"download link: {magisk_link}", flush=True)

with open(download_dir/tempScript, 'a') as f:
    f.writelines(f'{magisk_link}\n')
    f.writelines(f'  dir={download_dir}\n')
    f.writelines(f'  out=magisk-{magisk_ver}.zip\n')
