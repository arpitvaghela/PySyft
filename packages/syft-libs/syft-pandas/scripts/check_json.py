import json
import os
from pathlib import Path


def get_unique():
    root_dir = Path(os.path.dirname(__file__)).parent
    PKG_SUPPORT = os.path.join(root_dir, "src", "syft_pandas", "package-support.json")

    with open(PKG_SUPPORT, "r") as f:
        data = json.load(f)

    methods: tuple[str, str] = data["methods"]
    with open("scripts/required_other_types", "w") as f:
        for r in set([return_type for _, return_type in methods]):
            if not r.startswith("pandas"):
                f.write(f"{r}\n")


if __name__ == "__main__":
    get_unique()
