# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "libcst",
# ]
# ///

import libcst as cst
from typing import Self
from libcst.display import dump
import libcst.matchers as m


class GeminiTransformer(cst.CSTTransformer):
    """
    A class to add code to the Gemini generated code.
    """
    def __init__(
        self,
        sound_file_path: str,
        debug: bool = False,
        debug_file_path: str = "",
        num_new_lines: int = 0,
    ):
        self.sound_file_path = sound_file_path
        self.debug = debug
        self.debug_file_path = debug_file_path
        self.num_new_lines = num_new_lines

    def leave_FunctionDef(
        self: Self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        """
        This function adds `self.interactive_embed()` to the end of the construct function.
        """
        if original_node.name.value != "construct":
            return super().leave_FunctionDef(original_node, updated_node)

        code_to_add: cst.Module = cst.parse_statement("self.interactive_embed()")
        new_body: cst.IndentedBlock = cst.IndentedBlock(
            body=[*updated_node.body.body, code_to_add]
        )
        return updated_node.with_changes(body=new_body)

    def leave_SimpleStatementLine(
        self: Self,
        original_node: cst.SimpleStatementLine,
        updated_node: cst.SimpleStatementLine,
    ) -> cst.SimpleStatementLine:
        """
        This function adds `self.add_sound(...)` after certain Manim function calls, such as `Create()` or `FadeOut()`.
        """
        for child in original_node.children:
            # For debugging purposes.
            if self.debug:
                with open(self.debug_file_path, "w") as f:
                    f.write(dump(child))
                    f.write("\n" * self.num_new_lines)

            # These if statement(s) match specific nodes to add `self.add_sound(...)` after lines containing certain Manim function calls.
            if m.matches(
                child,
                m.Expr(
                    value=m.Call(
                        args=[
                            m.ZeroOrMore(m.Arg()),
                            m.Arg(value=m.Call(func=m.Name(value="Create"))),
                            m.ZeroOrMore(m.Arg()),
                        ],
                    )
                ),
            ):
                code_to_add: cst.Module = cst.parse_statement(
                    f"self.add_sound('{self.sound_file_path}')"
                )
                return cst.FlattenSentinel([updated_node, code_to_add])

        return super().leave_SimpleStatementLine(original_node, updated_node)


def add_interactivity() -> None:
    """
    Adds interactivity to the generated Gemini code.
    """
    with open("generated_code.py", "r") as f:
        code: str = f.read()
    code: cst.Module = cst.parse_module(code)

    updated_cst = code.visit(GeminiTransformer("Up_bend_250ms.wav", True, "parser_debug.txt"))
    with open("generated_code.py", "w") as f:
        f.write(updated_cst.code)


add_interactivity()
