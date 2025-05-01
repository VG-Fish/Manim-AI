# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "ipython>=8.31.0",
#     "latex>=0.7.0",
#     "libcst>=1.7.0",
#     "manim>=0.19.0",
#     "requests",
# ]
# ///

from requests import post, Response
from argparse import ArgumentParser, Namespace
from subprocess import run
from typing import Dict
from .cst_parser import add_interactivity


def run_manim_code(code: str) -> None:
    with open("generated_code.py", "w") as f:
        f.write(code)

    print("Adding interactivity...")
    add_interactivity()

    print("Running the scene...")
    try:
        run(["manim", "-pql", "generated_code.py", "--renderer=opengl"])
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

    PROMPT: str = f"""Your sole purpose is to convert natural language into Manim code. 
You will be given some text and must write valid Manim code to the best of your abilities.
DON'T code bugs and SOLELY OUTPUT PYTHON CODE. Import ALL the necessary libraries.
Define ALL constants. After you generate your code, check to make sure that it can run.
Ensure all the generated manim code is compatible with manim 0.19.0. DO NOT USE
DEPRECATED CLASSES, such as "ParametricSurface." Ensure EVERY element in the scene is visually distinctive. 
Define EVERY function you use. Write text at the top to explain what you're doing.
REMEMBER, YOU MUST OUTPUT CODE THAT DOESN'T CAUSE BUGS. ASSUME YOUR CODE IS BUGGY, AND RECODE IT AGAIN.
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

def generate_video(prompt: str) -> None:
    GEMINI_URL: str = "https://gemini-wrapper-nine.vercel.app/gemini"

    print("Getting response...")

    PROMPT: str = f"""Your sole purpose is to convert natural language into Manim code. 
You will be given some text and must write valid Manim code to the best of your abilities.
DON'T code bugs and SOLELY OUTPUT PYTHON CODE. Import ALL the necessary libraries.
Define ALL constants. After you generate your code, check to make sure that it can run.
Ensure all the generated manim code is compatible with manim 0.19.0. DO NOT USE
DEPRECATED CLASSES, such as "ParametricSurface." Ensure EVERY element in the scene is visually distinctive. 
Define EVERY function you use. Write text at the top to explain what you're doing.
REMEMBER, YOU MUST OUTPUT CODE THAT DOESN'T CAUSE BUGS. ASSUME YOUR CODE IS BUGGY, AND RECODE IT AGAIN.
The prompt: {prompt}"""

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