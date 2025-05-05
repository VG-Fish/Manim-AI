# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
#     "ipython>=8.31.0",
#     "latex>=0.7.0",
#     "libcst>=1.7.0",
#     "manim>=0.19.0",
# ]
# ///

from asyncio import create_subprocess_exec
from asyncio.subprocess import PIPE

from os import getcwd, walk
from os.path import join, dirname

from subprocess import CalledProcessError

from typing import Dict

from httpx import AsyncClient, RequestError, Response

from .cst_parser import add_interactivity

from shutil import which

async def run_manim_code(code: str, path: str = getcwd()) -> None:
    print("Adding interactivity...")
    add_interactivity(code, path)

    print("Running the scene...")
    manim_path = which("manim")
    if not manim_path:
        print("Manim executable not found.")
        return

    # Full path to the code file
    code_file = join(path, "generated_code.py")

    try:
        proc = await create_subprocess_exec(
            manim_path,
            "-ql",
            code_file,
            "--media_dir", f"{path}/output_media",
            stdout=PIPE,
            stderr=PIPE,
        )
        stdout, stderr = await proc.communicate()
        print("STDOUT:", stdout.decode())
        print("STDERR:", stderr.decode())

        code_dir = dirname(code_file)

        media_root = join(code_dir, "media", "videos")
        for root, _, files in walk(media_root):
            for file in files:
                if file.endswith(".mp4"):
                    video_path = join(root, file)
                    print(f"Opening video at: {video_path}")
                    await create_subprocess_exec("open", video_path)
                    return

        print("Video file not found in:", media_root)

    except Exception as e:
        print(f"Error while running Manim: {e}")

async def generate_video(prompt: str, path: str = getcwd()) -> None:
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

    async with AsyncClient() as client:
        try:
            response: Response = await client.post(GEMINI_URL, json={"prompt": PROMPT})
            response.raise_for_status()
        except RequestError as e:
            print(f"Error in getting the response: {e}")
            return

    if response.status_code != 200:
        print(f"Status Code Error: {response.status_code}")
        return

    json: Dict = response.json()

    if "error" in json:
        print(f"JSON Error: {json['error']}")
        return

    code: str = json["output"]
    code = "\n".join(code.splitlines()[1:-1])

    print("Creating the interactive scene...")
    await run_manim_code(code, path)
