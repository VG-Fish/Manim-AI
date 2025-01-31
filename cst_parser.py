# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "libcst",
# ]
# ///

import libcst as cst
import libcst.matchers as m
from libcst.display import dump

from os.path import exists

from typing import Dict, Tuple
from typing import Self

import wave


def get_audio_file_duration(file_path: str) -> float:
    with wave.open(file_path, "r") as f:
        frames: int = f.getnframes()
        rate: int = f.getframerate()
        duration = frames / rate
        return round(duration, 2)


class GeminiTransformer(cst.CSTTransformer):
    """
    A class to add code to a Gemini generated code file.
    """

    def __init__(
        self: Self,
        sound_indicator_nodes: Dict[str, Tuple[str, float]],
        debug: bool = False,
        debug_file_path: str = "",
        debug_num_new_lines: int = 1,
    ) -> None:
        """
        This function initializes the class.
        """
        self.sound_indicator_nodes: Dict[str, Tuple[str, float]] = sound_indicator_nodes

        # Debug variables.
        self.debug: bool = debug
        self.debug_file_path: str = debug_file_path
        self.debug_num_new_lines: int = debug_num_new_lines

        # Clear the debug file if it exists.
        if exists(self.debug_file_path):
            with open(self.debug_file_path, "w") as f:
                f.close()

    def leave_FunctionDef(
        self: Self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        """
        This function adds `self.interactive_embed()` to the end of the construct function.
        """
        if original_node.name.value != "construct":
            return super().leave_FunctionDef(original_node, updated_node)

        interactive_code: cst.SimpleStatementLine = cst.parse_statement(
            "self.interactive_embed()"
        )
        new_body: cst.IndentedBlock = cst.IndentedBlock(
            body=[*updated_node.body.body, interactive_code]
        )
        return updated_node.with_changes(body=new_body)

    def visit_SimpleStatementLine(self, node: cst.SimpleStatementLine) -> bool | None:
        """
        This function writes the CST nodes to the debug file.
        """
        if not self.debug:
            return

        with open(self.debug_file_path, "a") as f:
            for child in node.children:
                f.write(dump(child))
                f.write("\n" * self.debug_num_new_lines)

    def leave_SimpleStatementLine(
        self: Self,
        original_node: cst.SimpleStatementLine,
        updated_node: cst.SimpleStatementLine,
    ) -> cst.SimpleStatementLine:
        """
        This function adds `self.add_sound(...)` after certain Manim function calls, such as `Create()` or `FadeOut()`.
        """
        for child in original_node.children:
            # This for loop matches specific nodes to add `self.add_sound(...)` after lines containing certain Manim function calls.
            for node, (
                sound_file_path,
                intensity,
            ) in self.sound_indicator_nodes.items():
                # First type of function call to match for.
                if m.matches(
                    child,
                    m.Expr(
                        value=m.Call(
                            args=[
                                m.ZeroOrMore(m.Arg()),
                                m.Arg(value=m.Call(func=m.Name(value=node))),
                                m.ZeroOrMore(m.Arg()),
                            ],
                        )
                    ),
                ):
                    run_time_arg = cst.Arg(
                        value=cst.Float(
                            value=str(get_audio_file_duration(sound_file_path))
                        ),
                        keyword=cst.Name(value="run_time"),
                    )
                    updated_args = updated_node.body[0].value.args + (run_time_arg,)
                    updated_call = updated_node.body[0].value.with_changes(
                        args=updated_args
                    )
                    updated_body = [
                        updated_node.body[0].with_changes(value=updated_call)
                    ] + list(updated_node.body[1:])
                    updated_node = updated_node.with_changes(body=updated_body)

                    sound_code: cst.SimpleStatementLine = cst.parse_statement(
                        f"self.add_sound('{sound_file_path}', {intensity})"
                    )
                    return cst.FlattenSentinel([sound_code, updated_node])

        return super().leave_SimpleStatementLine(original_node, updated_node)


def add_interactivity() -> None:
    """
    Adds interactivity to the generated Gemini code.
    """
    with open("generated_code.py", "r") as f:
        code: str = f.read()
    code: cst.Module = cst.parse_module(code)

    debug: bool = True
    if debug:
        with open("code_debug.txt", "w") as f:
            f.write(dump(code))

    sound_indicator_nodes: Dict[str, str] = {
        "Create": ("click.wav", 1),
        "Rotate": ("click.wav", 1),
        "FadeOut": ("click.wav", 1),
    }
    updated_cst: cst.Module = code.visit(
        GeminiTransformer(
            sound_indicator_nodes,
            debug,
            "parser_debug.txt",
            3,
        )
    )

    with open("generated_code.py", "w") as f:
        f.write(updated_cst.code)


if __name__ == "__main__":
    add_interactivity()
