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

from requests import get, Response
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
        print("Creating the interactive scene failed!")


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

    # The multiline quote is unindented to provide more space to write.
    GEMINI_URL: str = (
        f"""
https://nova-motors-server.vercel.app/gemini?prompt=
Your sole purpose is to convert natural language into Manim (a Python library for creating mathematical animations) code. 
You will be given some text and must write valid Manim code to the best of your abilities. 
This is the prompt: \"{args.prompt}\" Remember, DON'T code bugs and SOLELY OUTPUT PYTHON CODE--NOT PLAINTEXT OR MARKDOWN.
    """
    )

    print("Getting response...")
    response: Response | Dict[str, str] = get(GEMINI_URL)

    if not response:
        print("Couldn't connect to the backend to generate the code.")
        return

    response = response.json()

    code: str = response["candidates"][0]["content"]["parts"][0]["text"]
    code = "\n".join(code.splitlines()[1:-1])

    print("Creating the interactive scene...")
    run_manim_code(code)


if __name__ == "__main__":
    main()
