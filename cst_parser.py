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
from os.path import exists
from typing import Dict

class GeminiTransformer(cst.CSTTransformer):
    """
    A class to add code to the Gemini generated code.
    """
    def __init__(
        self: Self,
        sound_indicator_nodes: Dict[str, str],
        debug: bool = False,
        debug_file_path: str = "",
        num_new_lines: int = 1,
    ):
        # TODO: add these changes.
        self.sound_indicator_nodes: Dict[str, str] = sound_indicator_nodes

        # Debug variables.
        self.debug: bool = debug
        self.debug_file_path: str = debug_file_path
        self.debug_num_new_lines: int = num_new_lines

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

        code_to_add: cst.Module = cst.parse_statement("self.interactive_embed()")
        new_body: cst.IndentedBlock = cst.IndentedBlock(
            body=[*updated_node.body.body, code_to_add]
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
            for node, sound_file_path in self.sound_indicator_nodes.items():
                if self.sound_indicator_nodes.get("Create", "") and m.matches(
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
                    code_to_add: cst.Module = cst.parse_statement(
                        f"self.add_sound('{sound_file_path}')"
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

    sound_indicator_nodes: Dict[str, str] = {
        "Create": "Up_bend_250ms.wav",
        "Rotate": "Up_bend_250ms.wav",
        "FadeOut": "Up_bend_250ms.wav"
    }
    updated_cst = code.visit(GeminiTransformer(sound_indicator_nodes, True, "parser_debug.txt", 3))
    with open("generated_code.py", "w") as f:
        f.write(updated_cst.code)


if __name__ == "__main__":
    add_interactivity()
