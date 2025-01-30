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


class GeminiTransformer(cst.CSTTransformer):
    """
    A class to add code to a Gemini generated code file.
    """

    def __init__(
        self: Self,
        sound_indicator_nodes: Dict[str, Tuple[str, float]],
        debug: bool = False,
        debug_file_path: str = "",
        num_new_lines: int = 1,
    ):
        self.sound_indicator_nodes: Dict[str, Tuple[str, float]] = sound_indicator_nodes

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

        pygame_code: cst.SimpleStatementLine = cst.parse_statement(
            "pygame.mixer.init()"
        )
        interactive_code: cst.SimpleStatementLine = cst.parse_statement(
            "self.interactive_embed()"
        )
        new_body: cst.IndentedBlock = cst.IndentedBlock(
            body=[pygame_code, *updated_node.body.body, interactive_code]
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
        Additionally, this function adds `import pygame` to the top of the file.
        """
        for child in original_node.children:
            # This for loop matches specific nodes to add `self.add_sound(...)` after lines containing certain Manim function calls.
            for idx, (node, (sound_file_path, intensity)) in enumerate(
                self.sound_indicator_nodes.items()
            ):
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
                    sound_code: cst.SimpleStatementLine = cst.parse_module(
                        f"sound_{idx} = pygame.mixer.Sound('{sound_file_path}')\n" +
                        f"sound_{idx}.set_volume({intensity})\n" +
                        f"sound_{idx}.play()\n"
                    )
                    return cst.FlattenSentinel([updated_node, sound_code])
                elif m.matches(
                    child,
                    m.OneOf(
                        m.ImportFrom(module=m.Name(value="manim")),
                        m.Import(names=m.ImportAlias(name=m.Name(value="manim"))),
                    ),
                ):
                    pygame_code: cst.SimpleStatementLine = cst.parse_statement(
                        f"import pygame"
                    )
                    return cst.FlattenSentinel([updated_node, pygame_code])

        return super().leave_SimpleStatementLine(original_node, updated_node)


def add_interactivity() -> None:
    """
    Adds interactivity to the generated Gemini code.
    """
    with open("generated_code.py", "r") as f:
        code: str = f.read()
    code: cst.Module = cst.parse_module(code)

    debug = True
    if debug:
        with open("code_debug.txt", "w") as f:
            f.write(dump(code))

    sound_indicator_nodes: Dict[str, str] = {
        "Create": ("Up_bend_250ms.wav", 1),
        "Rotate": ("Up_bend_250ms.wav", 1),
        "FadeOut": ("Up_bend_250ms.wav", 1),
    }
    updated_cst = code.visit(
        GeminiTransformer(
            sound_indicator_nodes,
            debug,
            "parser_debug.txt" if debug else None,
            3 if debug else None,
        )
    )
    with open("generated_code.py", "w") as f:
        f.write(updated_cst.code)


if __name__ == "__main__":
    add_interactivity()
