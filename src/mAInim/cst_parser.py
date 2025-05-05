# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "libcst",
# ]
# ///

import libcst as cst
import libcst.matchers as m
from libcst.display import dump
from libcst import RemoveFromParent

from typing import Dict, Tuple, Self, Union
import wave as w
from os import getcwd


def get_audio_file_duration(sound_file_path: str) -> float:
    """
    Returns the length of the given .wav sound file path.
    """
    with w.open(sound_file_path, "r") as f:
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
    ) -> None:
        self.sound_indicator_nodes: Dict[str, Tuple[str, float]] = sound_indicator_nodes

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

    def leave_SimpleStatementLine(
        self: Self,
        original_node: cst.SimpleStatementLine,
        updated_node: cst.SimpleStatementLine,
    ) -> Union[cst.SimpleStatementLine, cst.FlattenSentinel]:
        """
        This function adds `self.add_sound(...)` after certain Manim function calls, such as `Create()` or `FadeOut()`.
        """
        # for child in original_node.children:
        #     # This for loop matches specific nodes to add `self.add_sound(...)` after lines containing
        #     # certain Manim function calls.
        #     for node, (
        #         sound_file_path,
        #         intensity,
        #     ) in self.sound_indicator_nodes.items():
        #         # First type of function call to match for.
        #         if m.matches(
        #             child,
        #             m.Expr(
        #                 value=m.Call(
        #                     func=m.Attribute(
        #                         value=m.Name(
        #                             value="self",
        #                         ),
        #                         attr=m.Name(
        #                             value="play",
        #                         ),
        #                     ),
        #                     args=[
        #                         m.ZeroOrMore(m.Arg()),
        #                         m.Arg(value=m.Call(func=m.Name(value=node))),
        #                         m.ZeroOrMore(m.Arg()),
        #                     ],
        #                 )
        #             ),
        #         ):
        #             run_time_arg = cst.Arg(
        #                 value=cst.Float(
        #                     value=str(get_audio_file_duration(sound_file_path))
        #                 ),
        #                 keyword=cst.Name(value="run_time"),
        #             )
        #             node_of_interest = updated_node.body[0]
        #             updated_args = node_of_interest.value.args + (run_time_arg,)

        #             updated_call = node_of_interest.value.with_changes(
        #                 args=updated_args
        #             )

        #             updated_body = [
        #                 node_of_interest.with_changes(value=updated_call)
        #             ] + list(updated_node.body[1:])

        #             updated_node = updated_node.with_changes(body=updated_body)

        #             sound_code: cst.SimpleStatementLine = cst.parse_statement(
        #                 f"self.add_sound('{sound_file_path}', {intensity})"
        #             )
        #             return cst.FlattenSentinel([sound_code, updated_node])

        return super().leave_SimpleStatementLine(original_node, updated_node)

    def leave_Arg(
        self: Self, original_node: cst.Arg, updated_node: cst.Arg
    ) -> Union[cst.Arg, cst.RemovalSentinel]:
        """
        Removes run_time=[value] from function calls for run_time=[sound_file_length] to be added later.
        """
        if m.matches(
            original_node,
            m.Arg(
                value=m.OneOf(m.Integer(), m.Float()),
                keyword=m.Name(value="run_time"),
            ),
        ):
            return RemoveFromParent()
        return updated_node


def add_interactivity(code: str, path: str = getcwd()) -> None:
    """
    Adds interactivity to the generated Gemini code.
    """
    code: cst.Module = cst.parse_module(code)

    # with open("cst_full_debug.txt", "w") as f:
    #     f.write(dump(code))

    sound_indicator_nodes: Dict[str, Tuple[str, int]] = {
        "Create": ("click.wav", 1),
        "Rotate": ("click.wav", 1),
        "FadeOut": ("click.wav", 1),
    }
    updated_cst: cst.Module = code.visit(GeminiTransformer(sound_indicator_nodes))

    print(f"Writing to {path}/generated_code.py...")
    with open(f"{path}/generated_code.py", "w") as f:
        f.write(updated_cst.code)

    print("Finished adding interactivity...")