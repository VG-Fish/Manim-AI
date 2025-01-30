# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "ipython>=8.31.0",
#     "latex>=0.7.0",
#     "libcst>=1.6.0",
#     "manim",
#     "requests",
# ]
# ///

import requests
import argparse
import subprocess
from typing import Dict, Any
from cst_parser import add_interactivity


def run_manim_code(code: str) -> None:
    with open("generated_code.py", "w") as f:
        f.write(code)
    add_interactivity()
    subprocess.run(["manim", "generated_code.py", "-p", "--renderer=opengl"])


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="A CLI tool for converting natural language to Manim animations."
    )
    parser.add_argument(
        "-p",
        "--prompt",
        help="What you want animated.",
        required=True,
    )
    args: argparse.Namespace = parser.parse_args()

    GEMINI_URL: str = f"""
    https://nova-motors-server.vercel.app/gemini?prompt=
Your sole purpose is to convert natural language into Manim (a Python library for creating mathematical animations) code. 
You will be given some text and must write Manim code to the best of your abilities. DO NOT OUTPUT MARKDOWN CODE, JUST PYTHON CODE.
AGAIN, DO NOT OUTPUT ANYTHING OTHER THAN VALID PYTHON + MANIM CODE. This is the prompt: {args.prompt}. Remember, DON'T code bugs.
"""

    print(
        "Calling Google Gemini now. Please note that since I'm hosting my Flask app on Vercel, there might be a cold start, so this may take a while.\n"
    )
    response: requests.Response | Dict[str, str] = requests.get(GEMINI_URL)

    if not response:
        print("Couldn't connect to the backend to generate the code.")
        return
    
    response = response.json()

    code: str = response["candidates"][0]["content"]["parts"][0]["text"]
    code = "\n".join(code.splitlines()[1:-1])

    run_manim_code(code)


if __name__ == "__main__":
    main()
