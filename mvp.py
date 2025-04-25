# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "ipython>=8.31.0",
#     "latex>=0.7.0",
#     "libcst>=1.6.0",
#     "manim",
#     "pygame>=2.6.1",
#     "requests",
# ]
# ///

from requests import post, Response
from argparse import ArgumentParser, Namespace
from subprocess import run
from typing import Dict
from cst_parser import add_interactivity


def run_manim_code(code: str) -> None:
    with open("generated_code.py", "w") as f:
        f.write(code)

    print("Adding interactivity...")
    add_interactivity()

    print("Running the scene...")
    try:
        run(["manim", "generated_code.py", "-p", "--renderer=opengl"])
    except FileNotFoundError:
        print("Could not find the generated code file.")


def main() -> None:
    parser: ArgumentParser = ArgumentParser(
        description="A CLI tool for converting natural language to Manim animations."
    )
    parser.add_argument(
        "-p",
        "--prompt",
        help="What you want animated.",
        required=True,
    )
    args: Namespace = parser.parse_args()

    GEMINI_URL: str = "https://gemini-wrapper-nine.vercel.app/gemini"

    print("Getting response...")

    PROMPT = f"""Your sole purpose is to convert natural language into Manim code. 
You will be given some text and must write valid Manim code to the best of your abilities.
DON'T code bugs and SOLELY OUTPUT PYTHON CODE.
The prompt: {args.prompt}"""

    response: Response | Dict[str, str] = post(GEMINI_URL, json={"prompt": PROMPT})

    if not response:
        print("Couldn't connect to the backend to generate the code.")
        return

    json: Dict = response.json()

    if "error" in json:
        print(json["error"])
        return

    code: str = json["output"]
    code = "\n".join(code.splitlines()[1:-1])

    print("Creating the interactive scene...")
    run_manim_code(code)


if __name__ == "__main__":
    main()
