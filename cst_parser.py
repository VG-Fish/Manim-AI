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

class Visitor(cst.CSTTransformer):
    def __init__(self, sound_file_path: str):
        self.sound_file_path = sound_file_path
    
    def leave_FunctionDef(
        self: Self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
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
        for child in original_node.children:
            node_matches = m.matches(
                child, 
                m.Expr(
                    value=m.Call(
                        args=[
                            m.ZeroOrMore(m.Arg()),
                            m.Arg(
                                value=m.Call(
                                    func=m.Name(
                                        value="Create"
                                    )
                                )
                            ),
                            m.ZeroOrMore(m.Arg()),
                        ],
                    )
                )
            )
            if not node_matches:
                continue
            
            code_to_add: cst.Module = cst.parse_statement(
                f"self.add_sound('{self.sound_file_path}', time_offset=0, gain=None)"
            )
            return cst.FlattenSentinel([
                updated_node,
                code_to_add
            ])

        return super().leave_SimpleStatementLine(original_node, updated_node)

def add_interactivity() -> None: 
    """
    Adds interactivity to the generated Gemini code.
    """
    with open("generated_code.py", "r") as f:
        code: str = f.read()
    code: cst.Module = cst.parse_module(code)

    updated_cst = code.visit(Visitor("KeyClick_2.wav"))
    with open("generated_code.py", "w") as f:
        f.write(updated_cst.code)


add_interactivity()
