#!/usr/bin/env python3
"""Build per-device www.js from the single source template.

Reads src/webserver/www.js (the shared source) and src/webserver/devices.json,
then generates docs/public/webserver/<slug>/www.js for each device by injecting
the device-specific configuration block.

Usage:
    python scripts/build_www.py           # write mode (default)
    python scripts/build_www.py --check   # exit 1 if any output is stale
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SOURCE = ROOT / "src" / "webserver" / "www.js"
DEVICES_JSON = ROOT / "src" / "webserver" / "devices.json"
OUTPUT_DIR = ROOT / "docs" / "public" / "webserver"

CONFIG_START = "__DEVICE_CONFIG_START__"
CONFIG_END = "__DEVICE_CONFIG_END__"


def load_devices():
    with open(DEVICES_JSON) as f:
        return json.load(f)


def build_config_block(slug, cfg):
    cfg_json = json.dumps(cfg, separators=(",", ":"))
    return (
        f'  var DEVICE_ID = "{slug}";\n'
        f"  var CFG = {cfg_json};\n"
    )


def replace_config(source_text, slug, cfg):
    pattern = re.compile(
        r"(^[^\n]*" + re.escape(CONFIG_START) + r"[^\n]*\n)"
        r"(.*?)"
        r"(^[^\n]*" + re.escape(CONFIG_END) + r"[^\n]*$)",
        re.MULTILINE | re.DOTALL,
    )
    m = pattern.search(source_text)
    if not m:
        raise ValueError(f"Config markers not found: {CONFIG_START} / {CONFIG_END}")
    return source_text[: m.start(2)] + build_config_block(slug, cfg) + source_text[m.start(3) :]


def build(check_only=False):
    devices = load_devices()
    source_text = SOURCE.read_text()
    dirty = []

    for slug, cfg in devices.items():
        output_path = OUTPUT_DIR / slug / "www.js"
        generated = replace_config(source_text, slug, cfg)

        if output_path.exists():
            current = output_path.read_text()
            if current == generated:
                continue

        dirty.append(slug)

        if not check_only:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(generated)
            print(f"  updated docs/public/webserver/{slug}/www.js")

    if check_only:
        if dirty:
            print("www.js outputs are out of date. Run 'python scripts/build_www.py' to fix:")
            for slug in dirty:
                print(f"  docs/public/webserver/{slug}/www.js")
            return 1
        print("All www.js outputs are up to date.")
        return 0

    if not dirty:
        print("All www.js outputs already up to date.")
    else:
        print(f"Built {len(dirty)} file(s).")
    return 0


if __name__ == "__main__":
    check = "--check" in sys.argv
    sys.exit(build(check_only=check))
