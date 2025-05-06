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

from typing import Dict

from httpx import AsyncClient, RequestError, Response

from .cst_parser import add_interactivity

from shutil import which

MANIM_LIBRARY_API: str = \
"""
++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/config.py

def initialize_manim_config() -> Dict:
def parse_cli():
def update_directory_config(config: Dict):
def update_window_config(config: Dict, args: Namespace):
def update_camera_config(config: Dict, args: Namespace):
def update_file_writer_config(config: Dict, args: Namespace):
def update_scene_config(config: Dict, args: Namespace):
def update_run_config(config: Dict, args: Namespace):
def update_embed_config(config: Dict, args: Namespace):
def load_yaml(file_path: str):
def get_manim_dir():
def get_resolution_from_args(args: Optional[Namespace], resolution_options: dict) -> Optional[tuple[int, int]]:
def get_file_ext(args: Namespace) -> str:
def get_animations_numbers(args: Namespace) -> tuple[int | None, int | None]:
def get_output_directory(args: Namespace, config: Dict) -> str:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/window.py

--------------------------------------------------

class Window(PygletWindow):

def init_for_scene(self, scene: Scene):
def get_monitor(self, index):
def get_default_size(self, full_screen=False):
def position_from_string(self, position_string):
def focus(self):
def to_default_position(self):
def pixel_coords_to_space_coords(self,
    px: int,
    py: int,
    relative: bool = False
) -> np.ndarray:
def has_undrawn_event(self) -> bool:
def swap_buffers(self):
def note_undrawn_event(func: Callable[..., T]) -> Callable[..., T]:
def wrapper(self, *args, **kwargs):
def on_mouse_motion(self, x: int, y: int, dx: int, dy: int) -> None:
def on_mouse_drag(self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int) -> None:
def on_mouse_press(self, x: int, y: int, button: int, mods: int) -> None:
def on_mouse_release(self, x: int, y: int, button: int, mods: int) -> None:
def on_mouse_scroll(self, x: int, y: int, x_offset: float, y_offset: float) -> None:
def on_key_press(self, symbol: int, modifiers: int) -> None:
def on_key_release(self, symbol: int, modifiers: int) -> None:
def on_resize(self, width: int, height: int) -> None:
def on_show(self) -> None:
def on_hide(self) -> None:
def on_close(self) -> None:
def is_key_pressed(self, symbol: int) -> bool:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/constants.py


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/logger.py


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/shader_wrapper.py

--------------------------------------------------

class ShaderWrapper(object):

def init_program_code(self) -> None:
def get_code(name: str) -> str | None:
def init_program(self):
def init_textures(self):
def init_vertex_objects(self):
def add_texture(self, name: str, texture: moderngl.Texture):
def bind_to_mobject_uniforms(self, mobject_uniforms: UniformDict):
def get_id(self) -> int:
def refresh_id(self) -> None:
def replace_code(self, old: str, new: str) -> None:
def use_clip_plane(self):
def set_ctx_depth_test(self, enable: bool = True) -> None:
def set_ctx_clip_plane(self, enable: bool = True) -> None:
def read_in(self, data_list: Iterable[np.ndarray]):
def generate_vaos(self):
def pre_render(self):
def render(self):
def update_program_uniforms(self, camera_uniforms: UniformDict):
def release(self):
def release_textures(self):
--------------------------------------------------

--------------------------------------------------

class VShaderWrapper(ShaderWrapper):

def init_program_code(self) -> None:
def init_program(self):
def init_vertex_objects(self):
def generate_vaos(self):
def set_backstroke(self, value: bool = True):
def refresh_id(self):
def render_stroke(self):
def render_fill(self):
def get_fill_canvas(ctx: moderngl.Context) -> Tuple[Framebuffer, VertexArray, Framebuffer]:
def render(self):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/extract_scene.py

--------------------------------------------------

class BlankScene(InteractiveScene):

def construct(self):
--------------------------------------------------

def is_child_scene(obj, module):
def prompt_user_for_choice(scene_classes):
def compute_total_frames(scene_class, scene_config):
def scene_from_class(scene_class, scene_config: Dict, run_config: Dict):
def note_missing_scenes(arg_names, module_names):
def get_scenes_to_render(all_scene_classes: list, scene_config: Dict, run_config: Dict):
def get_scene_classes(module: Optional[Module]):
def get_indent(code_lines: list[str], line_number: int) -> str:
def insert_embed_line_to_module(module: Module, run_config: Dict) -> None:
def get_module(run_config: Dict) -> Module:
def main(scene_config: Dict, run_config: Dict):

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/typing.py


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/module_loader.py

--------------------------------------------------

class ModuleLoader:

def get_module(file_name: str | None, is_during_reload=False) -> Module | None:
def tracked_import(name, globals=None, locals=None, fromlist=(), level=0):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/__main__.py

def run_scenes():
def main():

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/event_handler/event_type.py

--------------------------------------------------

class EventType(Enum):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/event_handler/event_dispatcher.py

--------------------------------------------------

class EventDispatcher(object):

def add_listner(self, event_listner: EventListener):
def remove_listner(self, event_listner: EventListener):
def dispatch(self, event_type: EventType, **event_data):
def get_listners_count(self) -> int:
def get_mouse_point(self) -> np.ndarray:
def get_mouse_drag_point(self) -> np.ndarray:
def is_key_pressed(self, symbol: int) -> bool:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/event_handler/event_listner.py

--------------------------------------------------

class EventListener(object):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/camera/camera_frame.py

--------------------------------------------------

class CameraFrame(Mobject):

def set_orientation(self, rotation: Rotation):
def get_orientation(self):
def make_orientation_default(self):
def to_default_state(self):
def get_euler_angles(self) -> np.ndarray:
def get_theta(self):
def get_phi(self):
def get_gamma(self):
def get_scale(self):
def get_inverse_camera_rotation_matrix(self):
def get_view_matrix(self, refresh=False):
def get_inv_view_matrix(self):
def interpolate(self, *args, **kwargs):
def rotate(self, angle: float, axis: np.ndarray = OUT, **kwargs):
def set_euler_angles(self,
    theta: float | None = None,
    phi: float | None = None,
    gamma: float | None = None,
    units: float = RADIANS
):
def increment_euler_angles(self,
    dtheta: float = 0,
    dphi: float = 0,
    dgamma: float = 0,
    units: float = RADIANS
):
def set_euler_axes(self, seq: str):
def reorient(self,
    theta_degrees: float | None = None,
    phi_degrees: float | None = None,
    gamma_degrees: float | None = None,
    center: Vect3 | tuple[float, float, float] | None = None,
    height: float | None = None
):
def set_theta(self, theta: float):
def set_phi(self, phi: float):
def set_gamma(self, gamma: float):
def increment_theta(self, dtheta: float, units=RADIANS):
def increment_phi(self, dphi: float, units=RADIANS):
def increment_gamma(self, dgamma: float, units=RADIANS):
def add_ambient_rotation(self, angular_speed=1 * DEG):
def set_focal_distance(self, focal_distance: float):
def set_field_of_view(self, field_of_view: float):
def get_shape(self):
def get_aspect_ratio(self):
def get_center(self) -> np.ndarray:
def get_width(self) -> float:
def get_height(self) -> float:
def get_focal_distance(self) -> float:
def get_field_of_view(self) -> float:
def get_implied_camera_location(self) -> np.ndarray:
def to_fixed_frame_point(self, point: Vect3, relative: bool = False):
def from_fixed_frame_point(self, point: Vect3, relative: bool = False):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/camera/camera.py

--------------------------------------------------

class Camera(object):

def init_frame(self, **config) -> None:
def init_context(self) -> None:
def init_fbo(self) -> None:
def init_light_source(self) -> None:
def use_window_fbo(self, use: bool = True):
def get_fbo(self,
    samples: int = 0
) -> moderngl.Framebuffer:
def clear(self) -> None:
def blit(self, src_fbo, dst_fbo):
def get_raw_fbo_data(self, dtype: str = 'f1') -> bytes:
def get_image(self) -> Image.Image:
def get_pixel_array(self) -> np.ndarray:
def get_texture(self) -> moderngl.Texture:
def get_pixel_size(self) -> float:
def get_pixel_shape(self) -> tuple[int, int]:
def get_pixel_width(self) -> int:
def get_pixel_height(self) -> int:
def get_aspect_ratio(self):
def get_frame_height(self) -> float:
def get_frame_width(self) -> float:
def get_frame_shape(self) -> tuple[float, float]:
def get_frame_center(self) -> np.ndarray:
def get_location(self) -> tuple[float, float, float]:
def resize_frame_shape(self, fixed_dimension: bool = False) -> None:
def capture(self, *mobjects: Mobject) -> None:
def refresh_uniforms(self) -> None:
--------------------------------------------------

--------------------------------------------------

class ThreeDCamera(Camera):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/animation/update.py

--------------------------------------------------

class UpdateFromFunc(Animation):

def interpolate_mobject(self, alpha: float) -> None:
--------------------------------------------------

--------------------------------------------------

class UpdateFromAlphaFunc(Animation):

def interpolate_mobject(self, alpha: float) -> None:
--------------------------------------------------

--------------------------------------------------

class MaintainPositionRelativeTo(Animation):

def interpolate_mobject(self, alpha: float) -> None:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/animation/creation.py

--------------------------------------------------

class ShowPartial(Animation,ABC):

def interpolate_submobject(self,
    submob: VMobject,
    start_submob: VMobject,
    alpha: float
) -> None:
def get_bounds(self, alpha: float) -> tuple[float, float]:
--------------------------------------------------

--------------------------------------------------

class ShowCreation(ShowPartial):

def get_bounds(self, alpha: float) -> tuple[float, float]:
--------------------------------------------------

--------------------------------------------------

class Uncreate(ShowCreation):

--------------------------------------------------

--------------------------------------------------

class DrawBorderThenFill(Animation):

def begin(self) -> None:
def finish(self) -> None:
def get_outline(self) -> VMobject:
def get_all_mobjects(self) -> list[Mobject]:
def interpolate_submobject(self,
    submob: VMobject,
    start: VMobject,
    outline: VMobject,
    alpha: float
) -> None:
--------------------------------------------------

--------------------------------------------------

class Write(DrawBorderThenFill):

def compute_run_time(self, family_size: int, run_time: float):
def compute_lag_ratio(self, family_size: int, lag_ratio: float):
--------------------------------------------------

--------------------------------------------------

class ShowIncreasingSubsets(Animation):

def interpolate_mobject(self, alpha: float) -> None:
def update_submobject_list(self, index: int) -> None:
--------------------------------------------------

--------------------------------------------------

class ShowSubmobjectsOneByOne(ShowIncreasingSubsets):

def update_submobject_list(self, index: int) -> None:
--------------------------------------------------

--------------------------------------------------

class AddTextWordByWord(ShowIncreasingSubsets):

def clean_up_from_scene(self, scene: Scene) -> None:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/animation/transform_matching_parts.py

--------------------------------------------------

class TransformMatchingParts(AnimationGroup):

def add_transform(self,
    source: Mobject,
    target: Mobject,
):
def find_pairs_with_matching_shapes(self,
    chars1: list[Mobject],
    chars2: list[Mobject]
) -> list[tuple[Mobject, Mobject]]:
def clean_up_from_scene(self, scene: Scene) -> None:
--------------------------------------------------

--------------------------------------------------

class TransformMatchingShapes(TransformMatchingParts):

--------------------------------------------------

--------------------------------------------------

class TransformMatchingStrings(TransformMatchingParts):

def matching_blocks(self,
    source: StringMobject,
    target: StringMobject,
    matched_keys: Iterable[str],
    key_map: dict[str, str]
) -> list[tuple[VMobject, VMobject]]:
--------------------------------------------------

--------------------------------------------------

class TransformMatchingTex(TransformMatchingStrings):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/animation/numbers.py

--------------------------------------------------

class ChangingDecimal(Animation):

def interpolate_mobject(self, alpha: float) -> None:
--------------------------------------------------

--------------------------------------------------

class ChangeDecimalToValue(ChangingDecimal):

--------------------------------------------------

--------------------------------------------------

class CountInFrom(ChangingDecimal):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/animation/movement.py

--------------------------------------------------

class Homotopy(Animation):

def function_at_time_t(self, t: float) -> Callable[[np.ndarray], Sequence[float]]:
def result(p):
def interpolate_submobject(self,
    submob: Mobject,
    start: Mobject,
    alpha: float
) -> None:
--------------------------------------------------

--------------------------------------------------

class SmoothedVectorizedHomotopy(Homotopy):

--------------------------------------------------

--------------------------------------------------

class ComplexHomotopy(Homotopy):

def homotopy(x, y, z, t):
--------------------------------------------------

--------------------------------------------------

class PhaseFlow(Animation):

def interpolate_mobject(self, alpha: float) -> None:
--------------------------------------------------

--------------------------------------------------

class MoveAlongPath(Animation):

def interpolate_mobject(self, alpha: float) -> None:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/animation/animation.py

--------------------------------------------------

class Animation(object):

def begin(self) -> None:
def finish(self) -> None:
def clean_up_from_scene(self, scene: Scene) -> None:
def create_starting_mobject(self) -> Mobject:
def get_all_mobjects(self) -> tuple[Mobject, Mobject]:
def get_all_families_zipped(self) -> zip[tuple[Mobject]]:
def update_mobjects(self, dt: float) -> None:
def get_all_mobjects_to_update(self) -> list[Mobject]:
def copy(self):
def update_rate_info(self,
    run_time: float | None = None,
    rate_func: Callable[[float], float] | None = None,
    lag_ratio: float | None = None,
):
def interpolate(self, alpha: float) -> None:
def update(self, alpha: float) -> None:
def time_spanned_alpha(self, alpha: float) -> float:
def interpolate_mobject(self, alpha: float) -> None:
def interpolate_submobject(self,
    submobject: Mobject,
    starting_submobject: Mobject,
    alpha: float
):
def get_sub_alpha(self,
    alpha: float,
    index: int,
    num_submobjects: int
) -> float:
def set_run_time(self, run_time: float):
def get_run_time(self) -> float:
def set_rate_func(self, rate_func: Callable[[float], float]):
def get_rate_func(self) -> Callable[[float], float]:
def set_name(self, name: str):
def is_remover(self) -> bool:
--------------------------------------------------

def prepare_animation(anim: Animation | _AnimationBuilder):

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/animation/specialized.py

--------------------------------------------------

class Broadcast(LaggedStart):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/animation/transform.py

--------------------------------------------------

class Transform(Animation):

def init_path_func(self) -> None:
def begin(self) -> None:
def finish(self) -> None:
def create_target(self) -> Mobject:
def check_target_mobject_validity(self) -> None:
def clean_up_from_scene(self, scene: Scene) -> None:
def update_config(self, **kwargs) -> None:
def get_all_mobjects(self) -> list[Mobject]:
def get_all_families_zipped(self) -> zip[tuple[Mobject]]:
def interpolate_submobject(self,
    submob: Mobject,
    start: Mobject,
    target_copy: Mobject,
    alpha: float
):
--------------------------------------------------

--------------------------------------------------

class ReplacementTransform(Transform):

--------------------------------------------------

--------------------------------------------------

class TransformFromCopy(Transform):

--------------------------------------------------

--------------------------------------------------

class MoveToTarget(Transform):

def check_validity_of_input(self, mobject: Mobject) -> None:
--------------------------------------------------

--------------------------------------------------

--------------------------------------------------

class ApplyMethod(Transform):

def check_validity_of_input(self, method: Callable) -> None:
def create_target(self) -> Mobject:
--------------------------------------------------

--------------------------------------------------

class ApplyPointwiseFunction(ApplyMethod):

--------------------------------------------------

--------------------------------------------------

class ApplyPointwiseFunctionToCenter(Transform):

def create_target(self) -> Mobject:
--------------------------------------------------

--------------------------------------------------

class FadeToColor(ApplyMethod):

--------------------------------------------------

--------------------------------------------------

class ScaleInPlace(ApplyMethod):

--------------------------------------------------

--------------------------------------------------

class ShrinkToCenter(ScaleInPlace):

--------------------------------------------------

--------------------------------------------------

class Restore(Transform):

--------------------------------------------------

--------------------------------------------------

class ApplyFunction(Transform):

def create_target(self) -> Mobject:
--------------------------------------------------

--------------------------------------------------

class ApplyMatrix(ApplyPointwiseFunction):

def func(p):
def initialize_matrix(self, matrix: npt.ArrayLike) -> np.ndarray:
--------------------------------------------------

--------------------------------------------------

class ApplyComplexFunction(ApplyMethod):

def init_path_func(self) -> None:
--------------------------------------------------

--------------------------------------------------

class CyclicReplace(Transform):

def create_target(self) -> Mobject:
--------------------------------------------------

--------------------------------------------------

class Swap(CyclicReplace):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/animation/indication.py

--------------------------------------------------

class FocusOn(Transform):

def create_target(self) -> Dot:
def create_starting_mobject(self) -> Dot:
--------------------------------------------------

--------------------------------------------------

class Indicate(Transform):

def create_target(self) -> Mobject:
--------------------------------------------------

--------------------------------------------------

class Flash(AnimationGroup):

def create_lines(self) -> VGroup:
def create_line_anims(self) -> list[Animation]:
--------------------------------------------------

--------------------------------------------------

class CircleIndicate(Transform):

--------------------------------------------------

--------------------------------------------------

class ShowPassingFlash(ShowPartial):

def get_bounds(self, alpha: float) -> tuple[float, float]:
def finish(self) -> None:
--------------------------------------------------

--------------------------------------------------

class VShowPassingFlash(Animation):

def taper_kernel(self, x):
def begin(self) -> None:
def interpolate_submobject(self,
    submobject: VMobject,
    starting_sumobject: None,
    alpha: float
) -> None:
def finish(self) -> None:
--------------------------------------------------

--------------------------------------------------

class FlashAround(VShowPassingFlash):

def get_path(self, mobject: Mobject, buff: float) -> SurroundingRectangle:
--------------------------------------------------

--------------------------------------------------

class FlashUnder(FlashAround):

def get_path(self, mobject: Mobject, buff: float) -> Underline:
--------------------------------------------------

--------------------------------------------------

class ShowCreationThenDestruction(ShowPassingFlash):

--------------------------------------------------

--------------------------------------------------

class ShowCreationThenFadeOut(Succession):

--------------------------------------------------

--------------------------------------------------

class AnimationOnSurroundingRectangle(AnimationGroup):

--------------------------------------------------

--------------------------------------------------

class ShowPassingFlashAround(AnimationOnSurroundingRectangle):

--------------------------------------------------

--------------------------------------------------

class ShowCreationThenDestructionAround(AnimationOnSurroundingRectangle):

--------------------------------------------------

--------------------------------------------------

class ShowCreationThenFadeAround(AnimationOnSurroundingRectangle):

--------------------------------------------------

--------------------------------------------------

class ApplyWave(Homotopy):

def homotopy(x, y, z, t):
--------------------------------------------------

--------------------------------------------------

class WiggleOutThenIn(Animation):

def get_scale_about_point(self) -> np.ndarray:
def get_rotate_about_point(self) -> np.ndarray:
def interpolate_submobject(self,
    submobject: Mobject,
    starting_sumobject: Mobject,
    alpha: float
) -> None:
--------------------------------------------------

--------------------------------------------------

class TurnInsideOut(Transform):

def create_target(self) -> Mobject:
--------------------------------------------------

--------------------------------------------------

class FlashyFadeIn(AnimationGroup):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/animation/composition.py

--------------------------------------------------

class AnimationGroup(Animation):

def get_all_mobjects(self) -> Mobject:
def begin(self) -> None:
def finish(self) -> None:
def clean_up_from_scene(self, scene: Scene) -> None:
def update_mobjects(self, dt: float) -> None:
def calculate_max_end_time(self) -> None:
def build_animations_with_timings(self, lag_ratio: float) -> None:
def interpolate(self, alpha: float) -> None:
--------------------------------------------------

--------------------------------------------------

class Succession(AnimationGroup):

def begin(self) -> None:
def finish(self) -> None:
def update_mobjects(self, dt: float) -> None:
def interpolate(self, alpha: float) -> None:
--------------------------------------------------

--------------------------------------------------

class LaggedStart(AnimationGroup):

--------------------------------------------------

--------------------------------------------------

class LaggedStartMap(LaggedStart):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/animation/rotation.py

--------------------------------------------------

class Rotating(Animation):

def interpolate_mobject(self, alpha: float) -> None:
--------------------------------------------------

--------------------------------------------------

class Rotate(Rotating):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/animation/growing.py

--------------------------------------------------

class GrowFromPoint(Transform):

def create_target(self) -> Mobject:
def create_starting_mobject(self) -> Mobject:
--------------------------------------------------

--------------------------------------------------

class GrowFromCenter(GrowFromPoint):

--------------------------------------------------

--------------------------------------------------

class GrowFromEdge(GrowFromPoint):

--------------------------------------------------

--------------------------------------------------

class GrowArrow(GrowFromPoint):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/animation/fading.py

--------------------------------------------------

class Fade(Transform):

--------------------------------------------------

--------------------------------------------------

class FadeIn(Fade):

def create_target(self) -> Mobject:
def create_starting_mobject(self) -> Mobject:
--------------------------------------------------

--------------------------------------------------

class FadeOut(Fade):

def create_target(self) -> Mobject:
--------------------------------------------------

--------------------------------------------------

class FadeInFromPoint(FadeIn):

--------------------------------------------------

--------------------------------------------------

class FadeOutToPoint(FadeOut):

--------------------------------------------------

--------------------------------------------------

class FadeTransform(Transform):

def begin(self) -> None:
def ghost_to(self, source: Mobject, target: Mobject) -> None:
def get_all_mobjects(self) -> list[Mobject]:
def get_all_families_zipped(self) -> zip[tuple[Mobject]]:
def clean_up_from_scene(self, scene: Scene) -> None:
--------------------------------------------------

--------------------------------------------------

class FadeTransformPieces(FadeTransform):

def begin(self) -> None:
def ghost_to(self, source: Mobject, target: Mobject) -> None:
--------------------------------------------------

--------------------------------------------------

class VFadeIn(Animation):

def interpolate_submobject(self,
    submob: VMobject,
    start: VMobject,
    alpha: float
) -> None:
--------------------------------------------------

--------------------------------------------------

class VFadeOut(VFadeIn):

def interpolate_submobject(self,
    submob: VMobject,
    start: VMobject,
    alpha: float
) -> None:
--------------------------------------------------

--------------------------------------------------

class VFadeInThenOut(VFadeIn):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/utils/color.py

def color_to_rgb(color: ManimColor) -> Vect3:
def color_to_rgba(color: ManimColor, alpha: float = 1.0) -> Vect4:
def rgb_to_color(rgb: Vect3 | Sequence[float]) -> Color:
def rgba_to_color(rgba: Vect4) -> Color:
def rgb_to_hex(rgb: Vect3 | Sequence[float]) -> str:
def hex_to_rgb(hex_code: str) -> Vect3:
def invert_color(color: ManimColor) -> Color:
def color_to_int_rgb(color: ManimColor) -> np.ndarray[int, np.dtype[np.uint8]]:
def color_to_int_rgba(color: ManimColor, opacity: float = 1.0) -> np.ndarray[int, np.dtype[np.uint8]]:
def color_to_hex(color: ManimColor) -> str:
def hex_to_int(rgb_hex: str) -> int:
def int_to_hex(rgb_int: int) -> str:
def color_gradient(reference_colors: Iterable[ManimColor],
    length_of_output: int
) -> list[Color]:
def interpolate_color(color1: ManimColor,
    color2: ManimColor,
    alpha: float
) -> Color:
def interpolate_color_by_hsl(color1: ManimColor,
    color2: ManimColor,
    alpha: float
) -> Color:
def average_color(*colors: ManimColor) -> Color:
def random_color() -> Color:
def random_bright_color(hue_range: tuple[float, float] = (0.0, 1.0),
    saturation_range: tuple[float, float] = (0.5, 0.8),
    luminance_range: tuple[float, float] = (0.5, 1.0),
) -> Color:
def get_colormap_from_colors(colors: Iterable[ManimColor]) -> Callable[[Sequence[float]], Vect4Array]:
def func(values):
def get_color_map(map_name: str) -> Callable[[Sequence[float]], Vect4Array]:
def get_colormap_list(map_name: str = "viridis",
    n_colors: int = 9
) -> Vect3Array:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/utils/sounds.py

def get_full_sound_file_path(sound_file_name: str) -> str:
def play_sound(sound_file):

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/utils/rate_functions.py

def linear(t: float) -> float:
def smooth(t: float) -> float:
def rush_into(t: float) -> float:
def rush_from(t: float) -> float:
def slow_into(t: float) -> float:
def double_smooth(t: float) -> float:
def there_and_back(t: float) -> float:
def there_and_back_with_pause(t: float, pause_ratio: float = 1. / 3) -> float:
def running_start(t: float, pull_factor: float = -0.5) -> float:
def overshoot(t: float, pull_factor: float = 1.5) -> float:
def not_quite_there(func: Callable[[float], float] = smooth,
    proportion: float = 0.7
) -> Callable[[float], float]:
def result(t):
def wiggle(t: float, wiggles: float = 2) -> float:
def squish_rate_func(func: Callable[[float], float],
    a: float = 0.4,
    b: float = 0.6
) -> Callable[[float], float]:
def result(t):
def lingering(t: float) -> float:
def exponential_decay(t: float, half_life: float = 0.1) -> float:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/utils/tex.py

def num_tex_symbols(tex: str) -> int:
def remove_tex_environments(tex: str) -> str:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/utils/paths.py

def straight_path(start_points: np.ndarray,
    end_points: np.ndarray,
    alpha: float
) -> np.ndarray:
def path_along_arc(arc_angle: float, 
    axis: Vect3 = OUT
) -> Callable[[Vect3Array, Vect3Array, float], Vect3Array]:
def path(start_points, end_points, alpha):
def clockwise_path() -> Callable[[Vect3Array, Vect3Array, float], Vect3Array]:
def counterclockwise_path() -> Callable[[Vect3Array, Vect3Array, float], Vect3Array]:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/utils/directories.py

def get_directories() -> dict[str, str]:
def get_cache_dir() -> str:
def get_temp_dir() -> str:
def get_downloads_dir() -> str:
def get_output_dir() -> str:
def get_raster_image_dir() -> str:
def get_vector_image_dir() -> str:
def get_sound_dir() -> str:
def get_shader_dir() -> str:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/utils/bezier.py

def bezier(points: Sequence[float | FloatArray] | VectNArray
) -> Callable[[float], float | FloatArray]:
def result(t: float) -> float | FloatArray:
def partial_bezier_points(points: Sequence[Scalable],
    a: float,
    b: float
) -> list[Scalable]:
def partial_quadratic_bezier_points(points: Sequence[VectN] | VectNArray,
    a: float,
    b: float
) -> list[VectN]:
def curve(t):
def interpolate(start: Scalable, end: Scalable, alpha: float | VectN) -> Scalable:
def outer_interpolate(start: Scalable,
    end: Scalable,
    alpha: Scalable,
) -> np.ndarray:
def set_array_by_interpolation(arr: np.ndarray,
    arr1: np.ndarray,
    arr2: np.ndarray,
    alpha: float,
    interp_func: Callable[[np.ndarray, np.ndarray, float], np.ndarray] = interpolate
) -> np.ndarray:
def integer_interpolate(start: int,
    end: int,
    alpha: float
) -> tuple[int, float]:
def mid(start: Scalable, end: Scalable) -> Scalable:
def inverse_interpolate(start: Scalable, end: Scalable, value: Scalable) -> np.ndarray:
def match_interpolate(new_start: Scalable,
    new_end: Scalable,
    old_start: Scalable,
    old_end: Scalable,
    old_value: Scalable
) -> Scalable:
def quadratic_bezier_points_for_arc(angle: float, n_components: int = 8):
def approx_smooth_quadratic_bezier_handles(points: FloatArray
) -> FloatArray:
def smooth_quadratic_path(anchors: Vect3Array) -> Vect3Array:
def get_smooth_cubic_bezier_handle_points(points: Sequence[VectN] | VectNArray
) -> tuple[FloatArray, FloatArray]:
def solve_func(b):
def closed_curve_solve_func(b):
def diag_to_matrix(l_and_u: tuple[int, int], 
    diag: np.ndarray
) -> np.ndarray:
def is_closed(points: FloatArray) -> bool:
def get_quadratic_approximation_of_cubic(a0: FloatArray,
    h0: FloatArray,
    h1: FloatArray,
    a1: FloatArray
) -> FloatArray:
def get_smooth_quadratic_bezier_path_through(points: Sequence[VectN]
) -> np.ndarray:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/utils/simple_functions.py

def sigmoid(x: float | FloatArray):
def choose(n: int, k: int) -> int:
def gen_choose(n: int, r: int) -> int:
def get_num_args(function: Callable) -> int:
def get_parameters(function: Callable) -> Iterable[str]:
def clip(a: float, min_a: float, max_a: float) -> float:
def arr_clip(arr: np.ndarray, min_a: float, max_a: float) -> np.ndarray:
def fdiv(a: Scalable, b: Scalable, zero_over_zero_value: Scalable | None = None) -> Scalable:
def binary_search(function: Callable[[float], float],
    target: float,
    lower_bound: float,
    upper_bound: float,
    tolerance:float = 1e-4
) -> float | None:
def hash_string(string: str, n_bytes=16) -> str:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/utils/file_ops.py

def guarantee_existence(path: str | Path) -> Path:
def find_file(file_name: str,
    directories: Iterable[str] | None = None,
    extensions: Iterable[str] | None = None
) -> Path:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/utils/cache.py

def cache_on_disk(func: Callable[..., T]) -> Callable[..., T]:
def wrapper(*args, **kwargs):
def clear_cache():

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/utils/space_ops.py

def cross(v1: Vect3 | List[float],
    v2: Vect3 | List[float],
    out: np.ndarray | None = None
) -> Vect3 | Vect3Array:
def get_norm(vect: VectN | List[float]) -> float:
def get_dist(vect1: VectN, vect2: VectN):
def normalize(vect: VectN | List[float],
    fall_back: VectN | List[float] | None = None
) -> VectN:
def poly_line_length(points):
def quaternion_mult(*quats: Vect4) -> Vect4:
def quaternion_from_angle_axis(angle: float,
    axis: Vect3,
) -> Vect4:
def angle_axis_from_quaternion(quat: Vect4) -> Tuple[float, Vect3]:
def quaternion_conjugate(quaternion: Vect4) -> Vect4:
def rotate_vector(vector: Vect3,
    angle: float,
    axis: Vect3 = OUT
) -> Vect3:
def rotate_vector_2d(vector: Vect2, angle: float) -> Vect2:
def rotation_matrix_transpose_from_quaternion(quat: Vect4) -> Matrix3x3:
def rotation_matrix_from_quaternion(quat: Vect4) -> Matrix3x3:
def rotation_matrix(angle: float, axis: Vect3) -> Matrix3x3:
def rotation_matrix_transpose(angle: float, axis: Vect3) -> Matrix3x3:
def rotation_about_z(angle: float) -> Matrix3x3:
def rotation_between_vectors(v1: Vect3, v2: Vect3) -> Matrix3x3:
def z_to_vector(vector: Vect3) -> Matrix3x3:
def angle_of_vector(vector: Vect2 | Vect3) -> float:
def angle_between_vectors(v1: VectN, v2: VectN) -> float:
def project_along_vector(point: Vect3, vector: Vect3) -> Vect3:
def normalize_along_axis(array: np.ndarray,
    axis: int,
) -> np.ndarray:
def get_unit_normal(v1: Vect3,
    v2: Vect3,
    tol: float = 1e-6
) -> Vect3:
def thick_diagonal(dim: int, thickness: int = 2) -> np.ndarray:
def compass_directions(n: int = 4, start_vect: Vect3 = RIGHT) -> Vect3:
def complex_to_R3(complex_num: complex) -> Vect3:
def R3_to_complex(point: Vect3) -> complex:
def complex_func_to_R3_func(complex_func: Callable[[complex], complex]) -> Callable[[Vect3], Vect3]:
def result(p: Vect3):
def center_of_mass(points: Sequence[Vect3]) -> Vect3:
def midpoint(point1: VectN, point2: VectN) -> VectN:
def line_intersection(line1: Tuple[Vect3, Vect3],
    line2: Tuple[Vect3, Vect3]
) -> Vect3:
def det(a, b):
def find_intersection(p0: Vect3 | Vect3Array,
    v0: Vect3 | Vect3Array,
    p1: Vect3 | Vect3Array,
    v1: Vect3 | Vect3Array,
    threshold: float = 1e-5,
) -> Vect3:
def line_intersects_path(start: Vect2 | Vect3,
    end: Vect2 | Vect3,
    path: Vect2Array | Vect3Array,
) -> bool:
def get_closest_point_on_line(a: VectN, b: VectN, p: VectN) -> VectN:
def get_winding_number(points: Sequence[Vect2 | Vect3]) -> float:
def cross2d(a: Vect2 | Vect2Array, b: Vect2 | Vect2Array) -> Vect2 | Vect2Array:
def tri_area(a: Vect2,
    b: Vect2,
    c: Vect2
) -> float:
def is_inside_triangle(p: Vect2,
    a: Vect2,
    b: Vect2,
    c: Vect2
) -> bool:
def norm_squared(v: VectN | List[float]) -> float:
def earclip_triangulation(verts: Vect3Array | Vect2Array, ring_ends: list[int]) -> list[int]:
def is_in(point, ring_id):
def ring_area(ring_id):
def is_in_fast(ring_a, ring_b):

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/utils/debug.py

def print_family(mobject: Mobject, n_tabs: int = 0) -> None:
def index_labels(mobject: Mobject, 
    label_height: float = 0.15
) -> VGroup:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/utils/dict_ops.py

def merge_dicts_recursively(*dicts):

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/utils/images.py

def get_full_raster_image_path(image_file_name: str) -> str:
def get_full_vector_image_path(image_file_name: str) -> str:
def invert_image(image: Iterable) -> Image.Image:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/utils/family_ops.py

def extract_mobject_family_members(mobject_list: Iterable[Mobject],
    exclude_pointless: bool = False
) -> list[Mobject]:
def recursive_mobject_remove(mobjects: List[Mobject], to_remove: Set[Mobject]) -> Tuple[List[Mobject], bool]:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/utils/tex_to_symbol_count.py


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/utils/iterables.py

def remove_list_redundancies(lst: Sequence[T]) -> list[T]:
def list_update(l1: Iterable[T], l2: Iterable[T]) -> list[T]:
def list_difference_update(l1: Iterable[T], l2: Iterable[T]) -> list[T]:
def adjacent_n_tuples(objects: Sequence[T], n: int) -> zip[tuple[T, ...]]:
def adjacent_pairs(objects: Sequence[T]) -> zip[tuple[T, T]]:
def batch_by_property(items: Iterable[T],
    property_func: Callable[[T], S]
) -> list[tuple[T, S]]:
def listify(obj: object) -> list:
def shuffled(iterable: Iterable) -> list:
def resize_array(nparray: np.ndarray, length: int) -> np.ndarray:
def resize_preserving_order(nparray: np.ndarray, length: int) -> np.ndarray:
def resize_with_interpolation(nparray: np.ndarray, length: int) -> np.ndarray:
def make_even(iterable_1: Sequence[T],
    iterable_2: Sequence[S]
) -> tuple[Sequence[T], Sequence[S]]:
def arrays_match(arr1: np.ndarray, arr2: np.ndarray) -> bool:
def array_is_constant(arr: np.ndarray) -> bool:
def cartesian_product(*arrays: np.ndarray):
def hash_obj(obj: object) -> int:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/utils/tex_file_writing.py

def get_tex_template_config(template_name: str) -> dict[str, str]:
def get_tex_config(template: str = "") -> tuple[str, str]:
def get_full_tex(content: str, preamble: str = ""):
def latex_to_svg(latex: str,
    template: str = "",
    additional_preamble: str = "",
    short_tex: str = "",
    show_message_during_execution: bool = True,
) -> str:
def full_tex_to_svg(full_tex: str, compiler: str = "latex", message: str = ""):
--------------------------------------------------

class LatexError(Exception):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/utils/shaders.py

def image_path_to_texture(path: str, ctx: moderngl.Context) -> moderngl.Texture:
def get_shader_program(ctx: moderngl.context.Context,
        vertex_shader: str,
        fragment_shader: Optional[str] = None,
        geometry_shader: Optional[str] = None,
) -> moderngl.Program:
def set_program_uniform(program: moderngl.Program,
    name: str,
    value: float | tuple | np.ndarray
) -> bool:
def get_shader_code_from_file(filename: str) -> str | None:
def get_colormap_code(rgb_list: Sequence[float]) -> str:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/scene/scene_file_writer.py

--------------------------------------------------

class SceneFileWriter(object):

def init_output_directories(self) -> None:
def init_image_file_path(self) -> Path:
def init_movie_file_path(self) -> Path:
def init_partial_movie_directory(self):
def get_output_file_rootname(self) -> Path:
def get_output_file_name(self) -> str:
def get_image_file_path(self) -> str:
def get_next_partial_movie_path(self) -> str:
def get_movie_file_path(self) -> str:
def init_audio(self) -> None:
def create_audio_segment(self) -> None:
def add_audio_segment(self,
    new_segment: AudioSegment,
    time: float | None = None,
    gain_to_background: float | None = None
) -> None:
def add_sound(self,
    sound_file: str,
    time: float | None = None,
    gain: float | None = None,
    gain_to_background: float | None = None
) -> None:
def begin(self) -> None:
def begin_animation(self) -> None:
def end_animation(self) -> None:
def finish(self) -> None:
def open_movie_pipe(self, file_path: str) -> None:
def use_fast_encoding(self):
def get_insert_file_path(self, index: int) -> Path:
def begin_insert(self):
def end_insert(self):
def has_progress_display(self):
def set_progress_display_description(self, file: str = "", sub_desc: str = "") -> None:
def write_frame(self, camera: Camera) -> None:
def close_movie_pipe(self) -> None:
def add_sound_to_video(self) -> None:
def save_final_image(self, image: Image) -> None:
def print_file_ready_message(self, file_path: str) -> None:
def should_open_file(self) -> bool:
def open_file(self) -> None:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/scene/scene.py

--------------------------------------------------

class Scene(object):

def get_window(self) -> Window | None:
def run(self) -> None:
def setup(self) -> None:
def construct(self) -> None:
def tear_down(self) -> None:
def interact(self) -> None:
def embed(self,
    close_scene_on_exit: bool = True,
    show_animation_progress: bool = False,
) -> None:
def get_image(self) -> Image:
def show(self) -> None:
def update_frame(self, dt: float = 0, force_draw: bool = False) -> None:
def emit_frame(self) -> None:
def update_mobjects(self, dt: float) -> None:
def should_update_mobjects(self) -> bool:
def get_time(self) -> float:
def increment_time(self, dt: float) -> None:
def get_top_level_mobjects(self) -> list[Mobject]:
def is_top_level(mobject):
def get_mobject_family_members(self) -> list[Mobject]:
def assemble_render_groups(self):
def affects_mobject_list(func: Callable[..., T]) -> Callable[..., T]:
def wrapper(self, *args, **kwargs):
def add(self, *new_mobjects: Mobject):
def add_mobjects_among(self, values: Iterable):
def replace(self, mobject: Mobject, *replacements: Mobject):
def remove(self, *mobjects_to_remove: Mobject):
def bring_to_front(self, *mobjects: Mobject):
def bring_to_back(self, *mobjects: Mobject):
def clear(self):
def get_mobjects(self) -> list[Mobject]:
def get_mobject_copies(self) -> list[Mobject]:
def point_to_mobject(self,
    point: np.ndarray,
    search_set: Iterable[Mobject] | None = None,
    buff: float = 0
) -> Mobject | None:
def get_group(self, *mobjects):
def id_to_mobject(self, id_value):
def ids_to_group(self, *id_values):
def i2g(self, *id_values):
def i2m(self, id_value):
def update_skipping_status(self) -> None:
def stop_skipping(self) -> None:
def get_time_progression(self,
    run_time: float,
    n_iterations: int | None = None,
    desc: str = "",
    override_skip_animations: bool = False
) -> list[float] | np.ndarray | ProgressDisplay:
def get_run_time(self, animations: Iterable[Animation]) -> float:
def get_animation_time_progression(self,
    animations: Iterable[Animation]
) -> list[float] | np.ndarray | ProgressDisplay:
def get_wait_time_progression(self,
    duration: float,
    stop_condition: Callable[[], bool] | None = None
) -> list[float] | np.ndarray | ProgressDisplay:
def pre_play(self):
def post_play(self):
def begin_animations(self, animations: Iterable[Animation]) -> None:
def progress_through_animations(self, animations: Iterable[Animation]) -> None:
def finish_animations(self, animations: Iterable[Animation]) -> None:
def play(self,
    *proto_animations: Animation | _AnimationBuilder,
    run_time: float | None = None,
    rate_func: Callable[[float], float] | None = None,
    lag_ratio: float | None = None,
) -> None:
def wait(self,
    duration: Optional[float] = None,
    stop_condition: Callable[[], bool] = None,
    note: str = None,
    ignore_presenter_mode: bool = False
):
def hold_loop(self):
def wait_until(self,
    stop_condition: Callable[[], bool],
    max_time: float = 60
):
def force_skipping(self):
def revert_to_original_skipping_status(self):
def add_sound(self,
    sound_file: str,
    time_offset: float = 0,
    gain: float | None = None,
    gain_to_background: float | None = None
):
def get_state(self) -> SceneState:
def restore_state(self, scene_state: SceneState):
def save_state(self) -> None:
def undo(self):
def redo(self):
def temp_skip(self):
def temp_progress_bar(self):
def temp_record(self):
def temp_config_change(self, skip=False, record=False, progress_bar=False):
def is_window_closing(self):
def set_floor_plane(self, plane: str = "xy"):
def on_mouse_motion(self,
    point: Vect3,
    d_point: Vect3
) -> None:
def on_mouse_drag(self,
    point: Vect3,
    d_point: Vect3,
    buttons: int,
    modifiers: int
) -> None:
def on_mouse_press(self,
    point: Vect3,
    button: int,
    mods: int
) -> None:
def on_mouse_release(self,
    point: Vect3,
    button: int,
    mods: int
) -> None:
def on_mouse_scroll(self,
    point: Vect3,
    offset: Vect3,
    x_pixel_offset: float,
    y_pixel_offset: float
) -> None:
def on_key_release(self,
    symbol: int,
    modifiers: int
) -> None:
def on_key_press(self,
    symbol: int,
    modifiers: int
) -> None:
def on_resize(self, width: int, height: int) -> None:
def on_show(self) -> None:
def on_hide(self) -> None:
def on_close(self) -> None:
def focus(self) -> None:
--------------------------------------------------

--------------------------------------------------

class SceneState:

def mobjects_match(self, state: SceneState):
def n_changes(self, state: SceneState):
def restore_scene(self, scene: Scene):
--------------------------------------------------

--------------------------------------------------

class EndScene(Exception):

--------------------------------------------------

--------------------------------------------------

class ThreeDScene(Scene):

def add(self, *mobjects: Mobject, set_depth_test: bool = True, perp_stroke: bool = True):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/scene/interactive_scene.py

--------------------------------------------------

class InteractiveScene(Scene):

def setup(self):
def get_selection_rectangle(self):
def update_selection_rectangle(self, rect: Rectangle):
def get_selection_highlight(self):
def update_selection_highlight(self, highlight: Mobject):
def get_crosshair(self):
def get_color_palette(self):
def get_information_label(self):
def update_coords(loc_label):
def get_state(self):
def restore_state(self, scene_state: SceneState):
def add(self, *mobjects: Mobject):
def remove(self, *mobjects: Mobject):
def toggle_selection_mode(self):
def get_selection_search_set(self) -> list[Mobject]:
def regenerate_selection_search_set(self):
def refresh_selection_scope(self):
def get_corner_dots(self, mobject: Mobject) -> Mobject:
def get_highlight(self, mobject: Mobject) -> Mobject:
def add_to_selection(self, *mobjects: Mobject):
def toggle_from_selection(self, *mobjects: Mobject):
def clear_selection(self):
def disable_interaction(self, *mobjects: Mobject):
def enable_interaction(self, *mobjects: Mobject):
def copy_selection(self):
def paste_selection(self):
def delete_selection(self):
def enable_selection(self):
def gather_new_selection(self):
def prepare_grab(self):
def prepare_resizing(self, about_corner=False):
def toggle_color_palette(self):
def display_information(self, show=True):
def group_selection(self):
def ungroup_selection(self):
def nudge_selection(self, vect: np.ndarray, large: bool = False):
def on_key_press(self, symbol: int, modifiers: int) -> None:
def on_key_release(self, symbol: int, modifiers: int) -> None:
def handle_grabbing(self, point: Vect3):
def handle_resizing(self, point: Vect3):
def handle_sweeping_selection(self, point: Vect3):
def choose_color(self, point: Vect3):
def on_mouse_motion(self, point: Vect3, d_point: Vect3) -> None:
def on_mouse_drag(self,
    point: Vect3,
    d_point: Vect3,
    buttons: int,
    modifiers: int
) -> None:
def on_mouse_release(self, point: Vect3, button: int, mods: int) -> None:
def copy_frame_positioning(self):
def copy_cursor_position(self):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/scene/scene_embed.py

--------------------------------------------------

class InteractiveSceneEmbed:

def launch(self):
def get_ipython_shell_for_embedded_scene(self) -> InteractiveShellEmbed:
def get_shortcuts(self):
def enable_gui(self):
def inputhook(context):
def ensure_frame_update_post_cell(self):
def post_cell_func(*args, **kwargs):
def ensure_flash_on_error(self):
def custom_exc(shell, etype, evalue, tb, tb_offset=None):
def reload_scene(self, embed_line: int | None = None) -> None:
def auto_reload(self):
def pre_cell_func(*args, **kwargs):
def checkpoint_paste(self,
    skip: bool = False,
    record: bool = False,
    progress_bar: bool = True
):
--------------------------------------------------

--------------------------------------------------

class CheckpointManager:

def checkpoint_paste(self, shell, scene):
def get_leading_comment(code_string: str) -> str:
def handle_checkpoint_key(self, scene, key: str):
def clear_checkpoints(self):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/functions.py

--------------------------------------------------

class ParametricCurve(VMobject):

def get_point_from_function(self, t: float) -> Vect3:
def init_points(self):
def get_t_func(self):
def get_function(self):
def get_x_range(self):
--------------------------------------------------

--------------------------------------------------

class FunctionGraph(ParametricCurve):

def parametric_function(t):
--------------------------------------------------

--------------------------------------------------

class ImplicitFunction(VMobject):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/matrix.py

--------------------------------------------------

class Matrix(VMobject):

def copy(self, deep: bool = False):
def create_mobject_matrix(self,
    matrix: GenericMatrixType,
    v_buff: float,
    h_buff: float,
    aligned_corner: Vect3,
    **element_config
) -> VMobjectMatrixType:
def element_to_mobject(self, element, **config) -> VMobject:
def create_brackets(self, rows, v_buff: float, h_buff: float) -> VGroup:
def get_column(self, index: int):
def get_row(self, index: int):
def get_columns(self) -> VGroup:
def get_rows(self) -> VGroup:
def set_column_colors(self, *colors: ManimColor) -> Self:
def add_background_to_entries(self) -> Self:
def swap_entry_for_dots(self, entry, dots):
def swap_entries_for_ellipses(self,
    row_index: Optional[int] = None,
    col_index: Optional[int] = None,
    height_ratio: float = 0.65,
    width_ratio: float = 0.4
):
def get_mob_matrix(self) -> VMobjectMatrixType:
def get_entries(self) -> VGroup:
def get_brackets(self) -> VGroup:
def get_ellipses(self) -> VGroup:
--------------------------------------------------

--------------------------------------------------

class DecimalMatrix(Matrix):

def element_to_mobject(self, element, **decimal_config) -> DecimalNumber:
--------------------------------------------------

--------------------------------------------------

class IntegerMatrix(DecimalMatrix):

--------------------------------------------------

--------------------------------------------------

class TexMatrix(Matrix):

--------------------------------------------------

--------------------------------------------------

class MobjectMatrix(Matrix):

def element_to_mobject(self, element: VMobject, **config) -> VMobject:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/three_dimensions.py

--------------------------------------------------

class SurfaceMesh(VGroup):

def init_points(self) -> None:
--------------------------------------------------

--------------------------------------------------

class Sphere(Surface):

def uv_func(self, u: float, v: float) -> np.ndarray:
--------------------------------------------------

--------------------------------------------------

class Torus(Surface):

def uv_func(self, u: float, v: float) -> np.ndarray:
--------------------------------------------------

--------------------------------------------------

class Cylinder(Surface):

def init_points(self):
def uv_func(self, u: float, v: float) -> np.ndarray:
--------------------------------------------------

--------------------------------------------------

class Cone(Cylinder):

def uv_func(self, u: float, v: float) -> np.ndarray:
--------------------------------------------------

--------------------------------------------------

class Line3D(Cylinder):

--------------------------------------------------

--------------------------------------------------

class Disk3D(Surface):

def uv_func(self, u: float, v: float) -> np.ndarray:
--------------------------------------------------

--------------------------------------------------

class Square3D(Surface):

def uv_func(self, u: float, v: float) -> np.ndarray:
--------------------------------------------------

def square_to_cube_faces(square: T) -> list[T]:
--------------------------------------------------

class Cube(SGroup):

--------------------------------------------------

--------------------------------------------------

class Prism(Cube):

--------------------------------------------------

--------------------------------------------------

class VGroup3D(VGroup):

--------------------------------------------------

--------------------------------------------------

class VCube(VGroup3D):

--------------------------------------------------

--------------------------------------------------

class VPrism(VCube):

--------------------------------------------------

--------------------------------------------------

class Dodecahedron(VGroup3D):

--------------------------------------------------

--------------------------------------------------

class Prismify(VGroup3D):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/vector_field.py

def get_vectorized_rgb_gradient_function(min_value: T,
    max_value: T,
    color_map: str
) -> Callable[[VectN], Vect3Array]:
def func(values):
def get_rgb_gradient_function(min_value: T,
    max_value: T,
    color_map: str
) -> Callable[[float], Vect3]:
def ode_solution_points(function, state0, time, dt=0.01):
def move_along_vector_field(mobject: Mobject,
    func: Callable[[Vect3], Vect3]
) -> Mobject:
def move_submobjects_along_vector_field(mobject: Mobject,
    func: Callable[[Vect3], Vect3]
) -> Mobject:
def apply_nudge(mob, dt):
def move_points_along_vector_field(mobject: Mobject,
    func: Callable[[float, float], Iterable[float]],
    coordinate_system: CoordinateSystem
) -> Mobject:
def apply_nudge(mob, dt):
def get_sample_coords(coordinate_system: CoordinateSystem,
    density: float = 1.0
) -> it.product[tuple[Vect3, ...]]:
def vectorize(pointwise_function: Callable[[Tuple], Tuple]):
def v_func(coords_array: VectArray) -> VectArray:
--------------------------------------------------

class VectorField(VMobject):

def init_points(self):
def get_sample_points(self,
    center: np.ndarray,
    width: float,
    height: float,
    depth: float,
    x_density: float,
    y_density: float,
    z_density: float
) -> np.ndarray:
def init_base_stroke_width_array(self, n_sample_points):
def set_sample_coords(self, sample_coords: VectArray):
def set_stroke(self, color=None, width=None, opacity=None, behind=None, flat=None, recurse=True):
def set_stroke_width(self, width: float):
def update_sample_points(self):
def update_vectors(self):
--------------------------------------------------

--------------------------------------------------

class TimeVaryingVectorField(VectorField):

def func(coords):
def increment_time(self, dt):
--------------------------------------------------

--------------------------------------------------

class StreamLines(VGroup):

def point_func(self, points: Vect3Array) -> Vect3:
def draw_lines(self) -> None:
def get_sample_coords(self):
def init_style(self) -> None:
--------------------------------------------------

--------------------------------------------------

class AnimatedStreamLines(VGroup):

def update(self, dt: float) -> None:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/shape_matchers.py

--------------------------------------------------

class SurroundingRectangle(Rectangle):

def surround(self, mobject, buff=None) -> Self:
def set_buff(self, buff) -> Self:
--------------------------------------------------

--------------------------------------------------

class BackgroundRectangle(SurroundingRectangle):

def pointwise_become_partial(self, mobject: Mobject, a: float, b: float) -> Self:
def set_style(self,
    stroke_color: ManimColor | None = None,
    stroke_width: float | None = None,
    fill_color: ManimColor | None = None,
    fill_opacity: float | None = None,
    family: bool = True,
    **kwargs
) -> Self:
def get_fill_color(self) -> Color:
--------------------------------------------------

--------------------------------------------------

class Cross(VGroup):

--------------------------------------------------

--------------------------------------------------

class Underline(Line):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/boolean_ops.py

--------------------------------------------------

class Union(VMobject):

--------------------------------------------------

--------------------------------------------------

class Difference(VMobject):

--------------------------------------------------

--------------------------------------------------

class Intersection(VMobject):

--------------------------------------------------

--------------------------------------------------

class Exclusion(VMobject):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/numbers.py

def char_to_cahced_mob(char: str, **text_config):
--------------------------------------------------

class DecimalNumber(VMobject):

def set_submobjects_from_number(self, number: float | complex) -> None:
def get_num_string(self, number: float | complex) -> str:
def char_to_mob(self, char: str) -> Text:
def interpolate(self,
    mobject1: Mobject,
    mobject2: Mobject,
    alpha: float,
    path_func: Callable[[np.ndarray, np.ndarray, float], np.ndarray] = straight_path
) -> Self:
def get_font_size(self) -> float:
def get_formatter(self, **kwargs) -> str:
def get_complex_formatter(self, **kwargs) -> str:
def get_tex(self):
def set_value(self, number: float | complex) -> Self:
def get_value(self) -> float | complex:
def increment_value(self, delta_t: float | complex = 1) -> Self:
--------------------------------------------------

--------------------------------------------------

class Integer(DecimalNumber):

def get_value(self) -> int:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/interactive.py

--------------------------------------------------

class MotionMobject(Mobject):

def mob_on_mouse_drag(self, mob: Mobject, event_data: dict[str, np.ndarray]) -> bool:
--------------------------------------------------

--------------------------------------------------

class Button(Mobject):

def mob_on_mouse_press(self, mob: Mobject, event_data) -> bool:
--------------------------------------------------

--------------------------------------------------

class ControlMobject(ValueTracker):

def set_value(self, value: float):
def assert_value(self, value):
def set_value_anim(self, value):
--------------------------------------------------

--------------------------------------------------

class EnableDisableButton(ControlMobject):

def assert_value(self, value: bool) -> None:
def set_value_anim(self, value: bool) -> None:
def toggle_value(self) -> None:
def on_mouse_press(self, mob: Mobject, event_data) -> bool:
--------------------------------------------------

--------------------------------------------------

class Checkbox(ControlMobject):

def assert_value(self, value: bool) -> None:
def toggle_value(self) -> None:
def set_value_anim(self, value: bool) -> None:
def on_mouse_press(self, mob: Mobject, event_data) -> None:
def get_checkmark(self) -> VGroup:
def get_cross(self) -> VGroup:
--------------------------------------------------

--------------------------------------------------

class LinearNumberSlider(ControlMobject):

def assert_value(self, value: float) -> None:
def set_value_anim(self, value: float) -> None:
def slider_on_mouse_drag(self, mob, event_data: dict[str, np.ndarray]) -> bool:
def get_value_from_point(self, point: np.ndarray) -> float:
--------------------------------------------------

--------------------------------------------------

class ColorSliders(Group):

def get_background(self) -> VGroup:
def set_value(self, r: float, g: float, b: float, a: float):
def get_value(self) -> np.ndarary:
def get_picked_color(self) -> str:
def get_picked_opacity(self) -> float:
--------------------------------------------------

--------------------------------------------------

class Textbox(ControlMobject):

def set_value_anim(self, value: str) -> None:
def update_text(self, value: str) -> None:
def active_anim(self, isActive: bool) -> None:
def box_on_mouse_press(self, mob, event_data) -> bool:
def on_key_press(self, mob: Mobject, event_data: dict[str, int]) -> bool | None:
--------------------------------------------------

--------------------------------------------------

class ControlPanel(Group):

def move_panel_and_controls_to_panel_opener(self) -> None:
def add_controls(self, *new_controls: ControlMobject) -> None:
def remove_controls(self, *controls_to_remove: ControlMobject) -> None:
def open_panel(self):
def close_panel(self):
def panel_opener_on_mouse_drag(self, mob, event_data: dict[str, np.ndarray]) -> bool:
def panel_on_mouse_scroll(self, mob, event_data: dict[str, np.ndarray]) -> bool:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/frame.py

--------------------------------------------------

class ScreenRectangle(Rectangle):

--------------------------------------------------

--------------------------------------------------

class FullScreenRectangle(ScreenRectangle):

--------------------------------------------------

--------------------------------------------------

class FullScreenFadeRectangle(FullScreenRectangle):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/geometry.py

--------------------------------------------------

class TipableVMobject(VMobject):

def add_tip(self, at_start: bool = False, **kwargs) -> Self:
def create_tip(self, at_start: bool = False, **kwargs) -> ArrowTip:
def get_unpositioned_tip(self, **kwargs) -> ArrowTip:
def position_tip(self, tip: ArrowTip, at_start: bool = False) -> ArrowTip:
def reset_endpoints_based_on_tip(self, tip: ArrowTip, at_start: bool) -> Self:
def asign_tip_attr(self, tip: ArrowTip, at_start: bool) -> Self:
def has_tip(self) -> bool:
def has_start_tip(self) -> bool:
def pop_tips(self) -> VGroup:
def get_tips(self) -> VGroup:
def get_tip(self) -> ArrowTip:
def get_default_tip_length(self) -> float:
def get_first_handle(self) -> Vect3:
def get_last_handle(self) -> Vect3:
def get_end(self) -> Vect3:
def get_start(self) -> Vect3:
def get_length(self) -> float:
--------------------------------------------------

--------------------------------------------------

class Arc(TipableVMobject):

def get_arc_center(self) -> Vect3:
def get_start_angle(self) -> float:
def get_stop_angle(self) -> float:
def move_arc_center_to(self, point: Vect3) -> Self:
--------------------------------------------------

--------------------------------------------------

class ArcBetweenPoints(Arc):

--------------------------------------------------

--------------------------------------------------

class CurvedArrow(ArcBetweenPoints):

--------------------------------------------------

--------------------------------------------------

class CurvedDoubleArrow(CurvedArrow):

--------------------------------------------------

--------------------------------------------------

class Circle(Arc):

def surround(self,
    mobject: Mobject,
    dim_to_match: int = 0,
    stretch: bool = False,
    buff: float = MED_SMALL_BUFF
) -> Self:
def point_at_angle(self, angle: float) -> Vect3:
def get_radius(self) -> float:
--------------------------------------------------

--------------------------------------------------

class Dot(Circle):

--------------------------------------------------

--------------------------------------------------

class SmallDot(Dot):

--------------------------------------------------

--------------------------------------------------

class Ellipse(Circle):

--------------------------------------------------

--------------------------------------------------

class AnnularSector(VMobject):

--------------------------------------------------

--------------------------------------------------

class Sector(AnnularSector):

--------------------------------------------------

--------------------------------------------------

class Annulus(VMobject):

--------------------------------------------------

--------------------------------------------------

class Line(TipableVMobject):

def set_points_by_ends(self,
    start: Vect3,
    end: Vect3,
    buff: float = 0,
    path_arc: float = 0
) -> Self:
def set_path_arc(self, new_value: float) -> Self:
def set_start_and_end_attrs(self, start: Vect3 | Mobject, end: Vect3 | Mobject):
def pointify(self,
    mob_or_point: Mobject | Vect3,
    direction: Vect3 | None = None
) -> Vect3:
def put_start_and_end_on(self, start: Vect3, end: Vect3) -> Self:
def get_vector(self) -> Vect3:
def get_unit_vector(self) -> Vect3:
def get_angle(self) -> float:
def get_projection(self, point: Vect3) -> Vect3:
def get_slope(self) -> float:
def set_angle(self, angle: float, about_point: Optional[Vect3] = None) -> Self:
def set_length(self, length: float, **kwargs):
def get_arc_length(self) -> float:
--------------------------------------------------

--------------------------------------------------

class DashedLine(Line):

def calculate_num_dashes(self, dash_length: float, positive_space_ratio: float) -> int:
def get_start(self) -> Vect3:
def get_end(self) -> Vect3:
def get_start_and_end(self) -> Tuple[Vect3, Vect3]:
def get_first_handle(self) -> Vect3:
def get_last_handle(self) -> Vect3:
--------------------------------------------------

--------------------------------------------------

class TangentLine(Line):

--------------------------------------------------

--------------------------------------------------

class Elbow(VMobject):

--------------------------------------------------

--------------------------------------------------

class StrokeArrow(Line):

def set_points_by_ends(self,
    start: Vect3,
    end: Vect3,
    buff: float = 0,
    path_arc: float = 0
) -> Self:
def insert_tip_anchor(self) -> Self:
def create_tip_with_stroke_width(self) -> Self:
def reset_tip(self) -> Self:
def set_stroke(self,
    color: ManimColor | Iterable[ManimColor] | None = None,
    width: float | Iterable[float] | None = None,
    *args, **kwargs
) -> Self:
--------------------------------------------------

--------------------------------------------------

class Arrow(Line):

def get_key_dimensions(self, length):
def set_points_by_ends(self,
    start: Vect3,
    end: Vect3,
    buff: float = 0,
    path_arc: float = 0
) -> Self:
def reset_points_around_ends(self) -> Self:
def get_start(self) -> Vect3:
def get_end(self) -> Vect3:
def get_start_and_end(self):
def put_start_and_end_on(self, start: Vect3, end: Vect3) -> Self:
def scale(self, *args, **kwargs) -> Self:
def set_thickness(self, thickness: float) -> Self:
def set_path_arc(self, path_arc: float) -> Self:
def set_perpendicular_to_camera(self, camera_frame):
--------------------------------------------------

--------------------------------------------------

class Vector(Arrow):

--------------------------------------------------

--------------------------------------------------

class CubicBezier(VMobject):

--------------------------------------------------

--------------------------------------------------

class Polygon(VMobject):

def get_vertices(self) -> Vect3Array:
def round_corners(self, radius: Optional[float] = None) -> Self:
--------------------------------------------------

--------------------------------------------------

class Polyline(VMobject):

--------------------------------------------------

--------------------------------------------------

class RegularPolygon(Polygon):

--------------------------------------------------

--------------------------------------------------

class Triangle(RegularPolygon):

--------------------------------------------------

--------------------------------------------------

class ArrowTip(Triangle):

def get_base(self) -> Vect3:
def get_tip_point(self) -> Vect3:
def get_vector(self) -> Vect3:
def get_angle(self) -> float:
def get_length(self) -> float:
--------------------------------------------------

--------------------------------------------------

class Rectangle(Polygon):

def surround(self, mobject, buff=SMALL_BUFF) -> Self:
--------------------------------------------------

--------------------------------------------------

class Square(Rectangle):

--------------------------------------------------

--------------------------------------------------

class RoundedRectangle(Rectangle):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/number_line.py

--------------------------------------------------

class NumberLine(Line):

def get_tick_range(self) -> np.ndarray:
def add_ticks(self) -> None:
def get_tick(self, x: float, size: float | None = None) -> Line:
def get_tick_marks(self) -> VGroup:
def number_to_point(self, number: float | VectN) -> Vect3 | Vect3Array:
def point_to_number(self, point: Vect3 | Vect3Array) -> float | VectN:
def n2p(self, number: float | VectN) -> Vect3 | Vect3Array:
def p2n(self, point: Vect3 | Vect3Array) -> float | VectN:
def get_unit_size(self) -> float:
def get_number_mobject(self,
    x: float,
    direction: Vect3 | None = None,
    buff: float | None = None,
    unit: float = 1.0,
    unit_tex: str = "",
    **number_config
) -> DecimalNumber:
def add_numbers(self,
    x_values: Iterable[float] | None = None,
    excluding: Iterable[float] | None = None,
    font_size: int = 24,
    **kwargs
) -> VGroup:
--------------------------------------------------

--------------------------------------------------

class UnitInterval(NumberLine):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/probability.py

--------------------------------------------------

class SampleSpace(Rectangle):

def add_title(self,
    title: str = "Sample space",
    buff: float = MED_SMALL_BUFF
) -> None:
def add_label(self, label: str) -> None:
def complete_p_list(self, p_list: list[float]) -> list[float]:
def get_division_along_dimension(self,
    p_list: list[float],
    dim: int,
    colors: Iterable[ManimColor],
    vect: np.ndarray
) -> VGroup:
def get_horizontal_division(self,
    p_list: list[float],
    colors: Iterable[ManimColor] = [GREEN_E, BLUE_E],
    vect: np.ndarray = DOWN
) -> VGroup:
def get_vertical_division(self,
    p_list: list[float],
    colors: Iterable[ManimColor] = [MAROON_B, YELLOW],
    vect: np.ndarray = RIGHT
) -> VGroup:
def divide_horizontally(self, *args, **kwargs) -> None:
def divide_vertically(self, *args, **kwargs) -> None:
def get_subdivision_braces_and_labels(self,
    parts: VGroup,
    labels: str,
    direction: np.ndarray,
    buff: float = SMALL_BUFF,
) -> VGroup:
def get_side_braces_and_labels(self,
    labels: str,
    direction: np.ndarray = LEFT,
    **kwargs
) -> VGroup:
def get_top_braces_and_labels(self,
    labels: str,
    **kwargs
) -> VGroup:
def get_bottom_braces_and_labels(self,
    labels: str,
    **kwargs
) -> VGroup:
def add_braces_and_labels(self) -> None:
--------------------------------------------------

--------------------------------------------------

class BarChart(VGroup):

def add_axes(self) -> None:
def add_bars(self, values: Iterable[float]) -> None:
def change_bar_values(self, values: Iterable[float]) -> None:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/coordinate_systems.py

def full_range_specifier(range_args):
--------------------------------------------------

class CoordinateSystem(ABC):

def coords_to_point(self, *coords: float | VectN) -> Vect3 | Vect3Array:
def point_to_coords(self, point: Vect3 | Vect3Array) -> tuple[float | VectN, ...]:
def c2p(self, *coords: float) -> Vect3 | Vect3Array:
def p2c(self, point: Vect3) -> tuple[float | VectN, ...]:
def get_origin(self) -> Vect3:
def get_axes(self) -> VGroup:
def get_all_ranges(self) -> list[np.ndarray]:
def get_axis(self, index: int) -> NumberLine:
def get_x_axis(self) -> NumberLine:
def get_y_axis(self) -> NumberLine:
def get_z_axis(self) -> NumberLine:
def get_x_axis_label(self,
    label_tex: str,
    edge: Vect3 = RIGHT,
    direction: Vect3 = DL,
    **kwargs
) -> Tex:
def get_y_axis_label(self,
    label_tex: str,
    edge: Vect3 = UP,
    direction: Vect3 = DR,
    **kwargs
) -> Tex:
def get_axis_label(self,
    label_tex: str,
    axis: Vect3,
    edge: Vect3,
    direction: Vect3,
    buff: float = MED_SMALL_BUFF,
    ensure_on_screen: bool = False
) -> Tex:
def get_axis_labels(self,
    x_label_tex: str = "x",
    y_label_tex: str = "y"
) -> VGroup:
def get_line_from_axis_to_point(self, 
    index: int,
    point: Vect3,
    line_func: Type[T] = DashedLine,
    color: ManimColor = GREY_A,
    stroke_width: float = 2
) -> T:
def get_v_line(self, point: Vect3, **kwargs):
def get_h_line(self, point: Vect3, **kwargs):
def get_graph(self,
    function: Callable[[float], float],
    x_range: Sequence[float] | None = None,
    bind: bool = False,
    **kwargs
) -> ParametricCurve:
def parametric_function(t: float) -> Vect3:
def get_parametric_curve(self,
    function: Callable[[float], Vect3],
    **kwargs
) -> ParametricCurve:
def input_to_graph_point(self,
    x: float,
    graph: ParametricCurve
) -> Vect3 | None:
def i2gp(self, x: float, graph: ParametricCurve) -> Vect3 | None:
def bind_graph_to_func(self,
    graph: VMobject,
    func: Callable[[VectN], VectN],
    jagged: bool = False,
    get_discontinuities: Optional[Callable[[], Vect3]] = None
) -> VMobject:
def get_graph_points():
def get_graph_label(self,
    graph: ParametricCurve,
    label: str | Mobject = "f(x)",
    x: float | None = None,
    direction: Vect3 = RIGHT,
    buff: float = MED_SMALL_BUFF,
    color: ManimColor | None = None
) -> Tex | Mobject:
def get_v_line_to_graph(self, x: float, graph: ParametricCurve, **kwargs):
def get_h_line_to_graph(self, x: float, graph: ParametricCurve, **kwargs):
def get_scatterplot(self,
                    x_values: Vect3Array,
                    y_values: Vect3Array,
                    **dot_config):
def angle_of_tangent(self,
    x: float,
    graph: ParametricCurve,
    dx: float = EPSILON
) -> float:
def slope_of_tangent(self,
    x: float,
    graph: ParametricCurve,
    **kwargs
) -> float:
def get_tangent_line(self,
    x: float,
    graph: ParametricCurve,
    length: float = 5,
    line_func: Type[T] = Line
) -> T:
def get_riemann_rectangles(self,
    graph: ParametricCurve,
    x_range: Sequence[float] = None,
    dx: float | None = None,
    input_sample_type: str = "left",
    stroke_width: float = 1,
    stroke_color: ManimColor = BLACK,
    fill_opacity: float = 1,
    colors: Iterable[ManimColor] = (BLUE, GREEN),
    negative_color: ManimColor = RED,
    stroke_background: bool = True,
    show_signed_area: bool = True
) -> VGroup:
def get_area_under_graph(self, graph, x_range, fill_color=BLUE, fill_opacity=0.5):
--------------------------------------------------

--------------------------------------------------

class Axes(VGroup,CoordinateSystem):

def create_axis(self,
    range_terms: RangeSpecifier,
    axis_config: dict,
    length: float | None
) -> NumberLine:
def coords_to_point(self, *coords: float | VectN) -> Vect3 | Vect3Array:
def point_to_coords(self, point: Vect3 | Vect3Array) -> tuple[float | VectN, ...]:
def get_axes(self) -> VGroup:
def get_all_ranges(self) -> list[Sequence[float]]:
def add_coordinate_labels(self,
    x_values: Iterable[float] | None = None,
    y_values: Iterable[float] | None = None,
    excluding: Iterable[float] = [0],
    **kwargs
) -> VGroup:
--------------------------------------------------

--------------------------------------------------

class ThreeDAxes(Axes):

def get_all_ranges(self) -> list[Sequence[float]]:
def add_axis_labels(self, x_tex="x", y_tex="y", z_tex="z", font_size=24, buff=0.2):
def get_graph(self,
    func,
    color=BLUE_E,
    opacity=0.9,
    u_range=None,
    v_range=None,
    **kwargs
) -> ParametricSurface:
def get_parametric_surface(self,
    func,
    color=BLUE_E,
    opacity=0.9,
    **kwargs
) -> ParametricSurface:
--------------------------------------------------

--------------------------------------------------

class NumberPlane(Axes):

def init_background_lines(self) -> None:
def get_lines(self) -> tuple[VGroup, VGroup]:
def get_lines_parallel_to_axis(self,
    axis1: NumberLine,
    axis2: NumberLine
) -> tuple[VGroup, VGroup]:
def get_x_unit_size(self) -> float:
def get_y_unit_size(self) -> list:
def get_axes(self) -> VGroup:
def get_vector(self, coords: Iterable[float], **kwargs) -> Arrow:
def prepare_for_nonlinear_transform(self, num_inserted_curves: int = 50) -> Self:
--------------------------------------------------

--------------------------------------------------

class ComplexPlane(NumberPlane):

def number_to_point(self, number: complex | float) -> Vect3:
def n2p(self, number: complex | float) -> Vect3:
def point_to_number(self, point: Vect3) -> complex:
def p2n(self, point: Vect3) -> complex:
def get_default_coordinate_values(self,
    skip_first: bool = True
) -> list[complex]:
def add_coordinate_labels(self,
    numbers: list[complex] | None = None,
    skip_first: bool = True,
    font_size: int = 36,
    **kwargs
) -> Self:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/mobject.py

--------------------------------------------------

class Mobject(object):

def init_data(self, length: int = 0):
def init_uniforms(self):
def init_colors(self):
def init_points(self):
def set_uniforms(self, uniforms: dict) -> Self:
def animate(self) -> _AnimationBuilder:
def always(self) -> _UpdaterBuilder:
def f_always(self) -> _FunctionalUpdaterBuilder:
def note_changed_data(self, recurse_up: bool = True) -> Self:
def affects_data(func: Callable[..., T]) -> Callable[..., T]:
def wrapper(self, *args, **kwargs):
def affects_family_data(func: Callable[..., T]) -> Callable[..., T]:
def wrapper(self, *args, **kwargs):
def set_data(self, data: np.ndarray) -> Self:
def resize_points(self,
    new_length: int,
    resize_func: Callable[[np.ndarray, int], np.ndarray] = resize_array
) -> Self:
def set_points(self, points: Vect3Array | list[Vect3]) -> Self:
def append_points(self, new_points: Vect3Array) -> Self:
def reverse_points(self) -> Self:
def apply_points_function(self,
    func: Callable[[np.ndarray], np.ndarray],
    about_point: Vect3 | None = None,
    about_edge: Vect3 = ORIGIN,
    works_on_bounding_box: bool = False
) -> Self:
def match_points(self, mobject: Mobject) -> Self:
def get_points(self) -> Vect3Array:
def clear_points(self) -> Self:
def get_num_points(self) -> int:
def get_all_points(self) -> Vect3Array:
def has_points(self) -> bool:
def get_bounding_box(self) -> Vect3Array:
def compute_bounding_box(self) -> Vect3Array:
def refresh_bounding_box(self,
    recurse_down: bool = False,
    recurse_up: bool = True
) -> Self:
def are_points_touching(self,
    points: Vect3Array,
    buff: float = 0
) -> np.ndarray:
def is_point_touching(self,
    point: Vect3,
    buff: float = 0
) -> bool:
def is_touching(self, mobject: Mobject, buff: float = 1e-2) -> bool:
def split(self) -> list[Self]:
def note_changed_family(self, only_changed_order=False) -> Self:
def get_family(self, recurse: bool = True) -> list[Mobject]:
def family_members_with_points(self) -> list[Mobject]:
def get_ancestors(self, extended: bool = False) -> list[Mobject]:
def add(self, *mobjects: Mobject) -> Self:
def remove(self,
    *to_remove: Mobject,
    reassemble: bool = True,
    recurse: bool = True
) -> Self:
def clear(self) -> Self:
def add_to_back(self, *mobjects: Mobject) -> Self:
def replace_submobject(self, index: int, new_submob: Mobject) -> Self:
def insert_submobject(self, index: int, new_submob: Mobject) -> Self:
def set_submobjects(self, submobject_list: list[Mobject]) -> Self:
def digest_mobject_attrs(self) -> Self:
def arrange(self,
    direction: Vect3 = RIGHT,
    center: bool = True,
    **kwargs
) -> Self:
def arrange_in_grid(self,
    n_rows: int | None = None,
    n_cols: int | None = None,
    buff: float | None = None,
    h_buff: float | None = None,
    v_buff: float | None = None,
    buff_ratio: float | None = None,
    h_buff_ratio: float = 0.5,
    v_buff_ratio: float = 0.5,
    aligned_edge: Vect3 = ORIGIN,
    fill_rows_first: bool = True
) -> Self:
def arrange_to_fit_dim(self, length: float, dim: int, about_edge=ORIGIN) -> Self:
def arrange_to_fit_width(self, width: float, about_edge=ORIGIN) -> Self:
def arrange_to_fit_height(self, height: float, about_edge=ORIGIN) -> Self:
def arrange_to_fit_depth(self, depth: float, about_edge=ORIGIN) -> Self:
def sort(self,
    point_to_num_func: Callable[[np.ndarray], float] = lambda p: p[0],
    submob_func: Callable[[Mobject]] | None = None
) -> Self:
def shuffle(self, recurse: bool = False) -> Self:
def reverse_submobjects(self) -> Self:
def stash_mobject_pointers(func: Callable[..., T]) -> Callable[..., T]:
def wrapper(self, *args, **kwargs):
def serialize(self) -> bytes:
def deserialize(self, data: bytes) -> Self:
def deepcopy(self) -> Self:
def copy(self, deep: bool = False) -> Self:
def generate_target(self, use_deepcopy: bool = False) -> Self:
def save_state(self, use_deepcopy: bool = False) -> Self:
def restore(self) -> Self:
def become(self, mobject: Mobject, match_updaters=False) -> Self:
def looks_identical(self, mobject: Mobject) -> bool:
def has_same_shape_as(self, mobject: Mobject) -> bool:
def replicate(self, n: int) -> Self:
def get_grid(self,
    n_rows: int,
    n_cols: int,
    height: float | None = None,
    width: float | None = None,
    group_by_rows: bool = False,
    group_by_cols: bool = False,
    **kwargs
) -> Self:
def init_updaters(self):
def update(self, dt: float = 0, recurse: bool = True) -> Self:
def get_updaters(self) -> list[Updater]:
def add_updater(self, update_func: Updater, call: bool = True) -> Self:
def insert_updater(self, update_func: Updater, index=0):
def remove_updater(self, update_func: Updater) -> Self:
def clear_updaters(self, recurse: bool = True) -> Self:
def match_updaters(self, mobject: Mobject) -> Self:
def suspend_updating(self, recurse: bool = True) -> Self:
def resume_updating(self, recurse: bool = True, call_updater: bool = True) -> Self:
def has_updaters(self) -> bool:
def refresh_has_updater_status(self) -> Self:
def is_changing(self) -> bool:
def set_animating_status(self, is_animating: bool, recurse: bool = True) -> Self:
def shift(self, vector: Vect3) -> Self:
def scale(self,
    scale_factor: float | npt.ArrayLike,
    min_scale_factor: float = 1e-8,
    about_point: Vect3 | None = None,
    about_edge: Vect3 = ORIGIN
) -> Self:
def stretch(self, factor: float, dim: int, **kwargs) -> Self:
def func(points):
def rotate_about_origin(self, angle: float, axis: Vect3 = OUT) -> Self:
def rotate(self,
    angle: float,
    axis: Vect3 = OUT,
    about_point: Vect3 | None = None,
    **kwargs
) -> Self:
def flip(self, axis: Vect3 = UP, **kwargs) -> Self:
def apply_function(self, function: Callable[[np.ndarray], np.ndarray], **kwargs) -> Self:
def apply_function_to_position(self, function: Callable[[np.ndarray], np.ndarray]) -> Self:
def apply_function_to_submobject_positions(self,
    function: Callable[[np.ndarray], np.ndarray]
) -> Self:
def apply_matrix(self, matrix: npt.ArrayLike, **kwargs) -> Self:
def apply_complex_function(self, function: Callable[[complex], complex], **kwargs) -> Self:
def R3_func(point):
def wag(self,
    direction: Vect3 = RIGHT,
    axis: Vect3 = DOWN,
    wag_factor: float = 1.0
) -> Self:
def center(self) -> Self:
def align_on_border(self,
    direction: Vect3,
    buff: float = DEFAULT_MOBJECT_TO_EDGE_BUFF
) -> Self:
def to_corner(self,
    corner: Vect3 = LEFT + DOWN,
    buff: float = DEFAULT_MOBJECT_TO_EDGE_BUFF
) -> Self:
def to_edge(self,
    edge: Vect3 = LEFT,
    buff: float = DEFAULT_MOBJECT_TO_EDGE_BUFF
) -> Self:
def next_to(self,
    mobject_or_point: Mobject | Vect3,
    direction: Vect3 = RIGHT,
    buff: float = DEFAULT_MOBJECT_TO_MOBJECT_BUFF,
    aligned_edge: Vect3 = ORIGIN,
    submobject_to_align: Mobject | None = None,
    index_of_submobject_to_align: int | slice | None = None,
    coor_mask: Vect3 = np.array([1, 1, 1]),
) -> Self:
def shift_onto_screen(self, **kwargs) -> Self:
def is_off_screen(self) -> bool:
def stretch_about_point(self, factor: float, dim: int, point: Vect3) -> Self:
def stretch_in_place(self, factor: float, dim: int) -> Self:
def rescale_to_fit(self, length: float, dim: int, stretch: bool = False, **kwargs) -> Self:
def stretch_to_fit_width(self, width: float, **kwargs) -> Self:
def stretch_to_fit_height(self, height: float, **kwargs) -> Self:
def stretch_to_fit_depth(self, depth: float, **kwargs) -> Self:
def set_width(self, width: float, stretch: bool = False, **kwargs) -> Self:
def set_height(self, height: float, stretch: bool = False, **kwargs) -> Self:
def set_depth(self, depth: float, stretch: bool = False, **kwargs) -> Self:
def set_max_width(self, max_width: float, **kwargs) -> Self:
def set_max_height(self, max_height: float, **kwargs) -> Self:
def set_max_depth(self, max_depth: float, **kwargs) -> Self:
def set_min_width(self, min_width: float, **kwargs) -> Self:
def set_min_height(self, min_height: float, **kwargs) -> Self:
def set_min_depth(self, min_depth: float, **kwargs) -> Self:
def set_shape(self,
    width: Optional[float] = None,
    height: Optional[float] = None,
    depth: Optional[float] = None,
    **kwargs
) -> Self:
def set_coord(self, value: float, dim: int, direction: Vect3 = ORIGIN) -> Self:
def set_x(self, x: float, direction: Vect3 = ORIGIN) -> Self:
def set_y(self, y: float, direction: Vect3 = ORIGIN) -> Self:
def set_z(self, z: float, direction: Vect3 = ORIGIN) -> Self:
def set_z_index(self, z_index: int) -> Self:
def space_out_submobjects(self, factor: float = 1.5, **kwargs) -> Self:
def move_to(self,
    point_or_mobject: Mobject | Vect3,
    aligned_edge: Vect3 = ORIGIN,
    coor_mask: Vect3 = np.array([1, 1, 1])
) -> Self:
def replace(self, mobject: Mobject, dim_to_match: int = 0, stretch: bool = False) -> Self:
def surround(self,
    mobject: Mobject,
    dim_to_match: int = 0,
    stretch: bool = False,
    buff: float = MED_SMALL_BUFF
) -> Self:
def put_start_and_end_on(self, start: Vect3, end: Vect3) -> Self:
def set_rgba_array(self,
    rgba_array: npt.ArrayLike,
    name: str = "rgba",
    recurse: bool = False
) -> Self:
def set_color_by_rgba_func(self,
    func: Callable[[Vect3Array], Vect4Array],
    recurse: bool = True
) -> Self:
def set_color_by_rgb_func(self,
    func: Callable[[Vect3Array], Vect3Array],
    opacity: float = 1,
    recurse: bool = True
) -> Self:
def set_rgba_array_by_color(self,
    color: ManimColor | Iterable[ManimColor] | None = None,
    opacity: float | Iterable[float] | None = None,
    name: str = "rgba",
    recurse: bool = True
) -> Self:
def set_color(self,
    color: ManimColor | Iterable[ManimColor] | None,
    opacity: float | Iterable[float] | None = None,
    recurse: bool = True
) -> Self:
def set_opacity(self,
    opacity: float | Iterable[float] | None,
    recurse: bool = True
) -> Self:
def get_color(self) -> str:
def get_opacity(self) -> float:
def get_opacities(self) -> float:
def set_color_by_gradient(self, *colors: ManimColor) -> Self:
def set_submobject_colors_by_gradient(self, *colors: ManimColor) -> Self:
def fade(self, darkness: float = 0.5, recurse: bool = True) -> Self:
def get_shading(self) -> np.ndarray:
def set_shading(self,
    reflectiveness: float | None = None,
    gloss: float | None = None,
    shadow: float | None = None,
    recurse: bool = True
) -> Self:
def get_reflectiveness(self) -> float:
def get_gloss(self) -> float:
def get_shadow(self) -> float:
def set_reflectiveness(self, reflectiveness: float, recurse: bool = True) -> Self:
def set_gloss(self, gloss: float, recurse: bool = True) -> Self:
def set_shadow(self, shadow: float, recurse: bool = True) -> Self:
def add_background_rectangle(self,
    color: ManimColor | None = None,
    opacity: float = 1.0,
    **kwargs
) -> Self:
def add_background_rectangle_to_submobjects(self, **kwargs) -> Self:
def add_background_rectangle_to_family_members_with_points(self, **kwargs) -> Self:
def get_bounding_box_point(self, direction: Vect3) -> Vect3:
def get_edge_center(self, direction: Vect3) -> Vect3:
def get_corner(self, direction: Vect3) -> Vect3:
def get_all_corners(self):
def get_center(self) -> Vect3:
def get_center_of_mass(self) -> Vect3:
def get_boundary_point(self, direction: Vect3) -> Vect3:
def get_continuous_bounding_box_point(self, direction: Vect3) -> Vect3:
def get_top(self) -> Vect3:
def get_bottom(self) -> Vect3:
def get_right(self) -> Vect3:
def get_left(self) -> Vect3:
def get_zenith(self) -> Vect3:
def get_nadir(self) -> Vect3:
def length_over_dim(self, dim: int) -> float:
def get_width(self) -> float:
def get_height(self) -> float:
def get_depth(self) -> float:
def get_shape(self) -> Tuple[float]:
def get_coord(self, dim: int, direction: Vect3 = ORIGIN) -> float:
def get_x(self, direction=ORIGIN) -> float:
def get_y(self, direction=ORIGIN) -> float:
def get_z(self, direction=ORIGIN) -> float:
def get_start(self) -> Vect3:
def get_end(self) -> Vect3:
def get_start_and_end(self) -> tuple[Vect3, Vect3]:
def point_from_proportion(self, alpha: float) -> Vect3:
def pfp(self, alpha):
def get_pieces(self, n_pieces: int) -> Group:
def get_z_index_reference_point(self) -> Vect3:
def match_color(self, mobject: Mobject) -> Self:
def match_style(self, mobject: Mobject) -> Self:
def match_dim_size(self, mobject: Mobject, dim: int, **kwargs) -> Self:
def match_width(self, mobject: Mobject, **kwargs) -> Self:
def match_height(self, mobject: Mobject, **kwargs) -> Self:
def match_depth(self, mobject: Mobject, **kwargs) -> Self:
def match_coord(self,
    mobject_or_point: Mobject | Vect3,
    dim: int,
    direction: Vect3 = ORIGIN
) -> Self:
def match_x(self,
    mobject_or_point: Mobject | Vect3,
    direction: Vect3 = ORIGIN
) -> Self:
def match_y(self,
    mobject_or_point: Mobject | Vect3,
    direction: Vect3 = ORIGIN
) -> Self:
def match_z(self,
    mobject_or_point: Mobject | Vect3,
    direction: Vect3 = ORIGIN
) -> Self:
def align_to(self,
    mobject_or_point: Mobject | Vect3,
    direction: Vect3 = ORIGIN
) -> Self:
def get_group_class(self):
def is_aligned_with(self, mobject: Mobject) -> bool:
def align_data_and_family(self, mobject: Mobject) -> Self:
def align_data(self, mobject: Mobject) -> Self:
def align_points(self, mobject: Mobject) -> Self:
def align_family(self, mobject: Mobject) -> Self:
def push_self_into_submobjects(self) -> Self:
def add_n_more_submobjects(self, n: int) -> Self:
def invisible_copy(self) -> Self:
def interpolate(self,
    mobject1: Mobject,
    mobject2: Mobject,
    alpha: float,
    path_func: Callable[[np.ndarray, np.ndarray, float], np.ndarray] = straight_path
) -> Self:
def pointwise_become_partial(self, mobject, a, b) -> Self:
def lock_data(self, keys: Iterable[str]) -> Self:
def lock_uniforms(self, keys: Iterable[str]) -> Self:
def lock_matching_data(self, mobject1: Mobject, mobject2: Mobject) -> Self:
def unlock_data(self) -> Self:
def affects_shader_info_id(func: Callable[..., T]) -> Callable[..., T]:
def wrapper(self, *args, **kwargs):
def set_uniform(self, recurse: bool = True, **new_uniforms) -> Self:
def fix_in_frame(self, recurse: bool = True) -> Self:
def unfix_from_frame(self, recurse: bool = True) -> Self:
def is_fixed_in_frame(self) -> bool:
def apply_depth_test(self, recurse: bool = True) -> Self:
def deactivate_depth_test(self, recurse: bool = True) -> Self:
def set_clip_plane(self,
    vect: Vect3 | None = None,
    threshold: float | None = None,
    recurse=True
) -> Self:
def deactivate_clip_plane(self) -> Self:
def replace_shader_code(self, old: str, new: str) -> Self:
def set_color_by_code(self, glsl_code: str) -> Self:
def set_color_by_xyz_func(self,
    glsl_snippet: str,
    min_value: float = -5.0,
    max_value: float = 5.0,
    colormap: str = "viridis"
) -> Self:
def init_shader_wrapper(self, ctx: Context):
def refresh_shader_wrapper_id(self):
def get_shader_wrapper(self, ctx: Context) -> ShaderWrapper:
def get_shader_wrapper_list(self, ctx: Context) -> list[ShaderWrapper]:
def get_shader_data(self) -> np.ndarray:
def get_uniforms(self):
def get_shader_vert_indices(self) -> Optional[np.ndarray]:
def render(self, ctx: Context, camera_uniforms: dict):
def init_event_listners(self):
def add_event_listner(self,
    event_type: EventType,
    event_callback: Callable[[Mobject, dict[str]]]
):
def remove_event_listner(self,
    event_type: EventType,
    event_callback: Callable[[Mobject, dict[str]]]
):
def clear_event_listners(self, recurse: bool = True):
def get_event_listners(self):
def get_family_event_listners(self):
def get_has_event_listner(self):
def add_mouse_motion_listner(self, callback):
def remove_mouse_motion_listner(self, callback):
def add_mouse_press_listner(self, callback):
def remove_mouse_press_listner(self, callback):
def add_mouse_release_listner(self, callback):
def remove_mouse_release_listner(self, callback):
def add_mouse_drag_listner(self, callback):
def remove_mouse_drag_listner(self, callback):
def add_mouse_scroll_listner(self, callback):
def remove_mouse_scroll_listner(self, callback):
def add_key_press_listner(self, callback):
def remove_key_press_listner(self, callback):
def add_key_release_listner(self, callback):
def remove_key_release_listner(self, callback):
def throw_error_if_no_points(self):
--------------------------------------------------

--------------------------------------------------

class Group(Mobject,Generic):

--------------------------------------------------

--------------------------------------------------

class Point(Mobject):

def get_width(self) -> float:
def get_height(self) -> float:
def get_location(self) -> Vect3:
def get_bounding_box_point(self, *args, **kwargs) -> Vect3:
def set_location(self, new_loc: npt.ArrayLike) -> Self:
--------------------------------------------------

def update_target(*method_args, **method_kwargs):
def set_anim_args(self, **kwargs):
def build(self):
--------------------------------------------------

def override_animate(method):
def decorator(animation_method):
def add_updater(*method_args, **method_kwargs):
--------------------------------------------------

def add_updater(*method_args, **method_kwargs):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/mobject_update_utils.py

def assert_is_mobject_method(method):
def always(method, *args, **kwargs):
def f_always(method, *arg_generators, **kwargs):
def updater(mob):
def always_redraw(func: Callable[..., Mobject], *args, **kwargs) -> Mobject:
def always_shift(mobject: Mobject,
    direction: np.ndarray = RIGHT,
    rate: float = 0.1
) -> Mobject:
def always_rotate(mobject: Mobject,
    rate: float = 20 * DEG,
    **kwargs
) -> Mobject:
def turn_animation_into_updater(animation: Animation,
    cycle: bool = False,
    **kwargs
) -> Mobject:
def update(m, dt):
def cycle_animation(animation: Animation, **kwargs) -> Mobject:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/changing.py

--------------------------------------------------

class AnimatedBoundary(VGroup):

def update_boundary_copies(self, dt: float) -> Self:
def full_family_become_partial(self,
    mob1: VMobject,
    mob2: VMobject,
    a: float,
    b: float
) -> Self:
--------------------------------------------------

--------------------------------------------------

class TracedPath(VMobject):

def update_path(self, dt: float) -> Self:
--------------------------------------------------

--------------------------------------------------

class TracingTail(TracedPath):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/value_tracker.py

--------------------------------------------------

class ValueTracker(Mobject):

def init_uniforms(self) -> None:
def get_value(self) -> float | complex | np.ndarray:
def set_value(self, value: float | complex | np.ndarray) -> Self:
def increment_value(self, d_value: float | complex) -> None:
--------------------------------------------------

--------------------------------------------------

class ExponentialValueTracker(ValueTracker):

def get_value(self) -> float | complex:
def set_value(self, value: float | complex):
--------------------------------------------------

--------------------------------------------------

class ComplexValueTracker(ValueTracker):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/svg/drawings.py

--------------------------------------------------

class Checkmark(TexTextFromPresetString):

--------------------------------------------------

--------------------------------------------------

class Exmark(TexTextFromPresetString):

--------------------------------------------------

--------------------------------------------------

class Lightbulb(SVGMobject):

--------------------------------------------------

--------------------------------------------------

class Speedometer(VMobject):

def get_center(self):
def get_needle_tip(self):
def get_needle_angle(self):
def rotate_needle(self, angle):
def move_needle_to_velocity(self, velocity):
--------------------------------------------------

--------------------------------------------------

class Laptop(VGroup):

--------------------------------------------------

--------------------------------------------------

class VideoIcon(SVGMobject):

--------------------------------------------------

--------------------------------------------------

class VideoSeries(VGroup):

--------------------------------------------------

--------------------------------------------------

class Clock(VGroup):

--------------------------------------------------

--------------------------------------------------

class ClockPassesTime(AnimationGroup):

--------------------------------------------------

--------------------------------------------------

class Bubble(VGroup):

def get_body(self, content: VMobject, direction: Vect3, buff: float) -> VMobject:
def get_tip(self):
def get_bubble_center(self):
def move_tip_to(self, point):
def flip(self, axis=UP, only_body=True, **kwargs):
def pin_to(self, mobject, auto_flip=False):
def position_mobject_inside(self, mobject, buff=MED_LARGE_BUFF):
def add_content(self, mobject):
def write(self, text):
def resize_to_content(self, buff=1.0):
def clear(self):
--------------------------------------------------

--------------------------------------------------

class SpeechBubble(Bubble):

def get_body(self, content: VMobject, direction: Vect3, buff: float) -> VMobject:
--------------------------------------------------

--------------------------------------------------

class ThoughtBubble(Bubble):

def get_body(self, content: VMobject, direction: Vect3, buff: float) -> VMobject:
--------------------------------------------------

--------------------------------------------------

class OldSpeechBubble(Bubble):

--------------------------------------------------

--------------------------------------------------

class DoubleSpeechBubble(Bubble):

--------------------------------------------------

--------------------------------------------------

class OldThoughtBubble(Bubble):

def get_body(self, content: VMobject, direction: Vect3, buff: float) -> VMobject:
def make_green_screen(self):
--------------------------------------------------

--------------------------------------------------

class VectorizedEarth(SVGMobject):

--------------------------------------------------

--------------------------------------------------

class Piano(VGroup):

def add_white_keys(self):
def add_black_keys(self):
def sort_keys(self):
--------------------------------------------------

--------------------------------------------------

class Piano3D(VGroup):

--------------------------------------------------

--------------------------------------------------

class DieFace(VGroup):

--------------------------------------------------

--------------------------------------------------

class Dartboard(VGroup):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/svg/svg_mobject.py

--------------------------------------------------

class SVGMobject(VMobject):

def init_svg_mobject(self) -> None:
def hash_seed(self) -> tuple:
def mobjects_from_svg_string(self, svg_string: str) -> list[VMobject]:
def file_name_to_svg_string(self, file_name: str) -> str:
def modify_xml_tree(self, element_tree: ET.ElementTree) -> ET.ElementTree:
def generate_config_style_dict(self) -> dict[str, str]:
def mobjects_from_svg(self, svg: se.SVG) -> list[VMobject]:
def handle_transform(mob: VMobject, matrix: se.Matrix) -> VMobject:
def apply_style_to_mobject(mob: VMobject,
    shape: se.GraphicObject
) -> VMobject:
def path_to_mobject(self, path: se.Path) -> VMobjectFromSVGPath:
def line_to_mobject(self, line: se.SimpleLine) -> Line:
def rect_to_mobject(self, rect: se.Rect) -> Rectangle:
def ellipse_to_mobject(self, ellipse: se.Circle | se.Ellipse) -> Circle:
def polygon_to_mobject(self, polygon: se.Polygon) -> Polygon:
def polyline_to_mobject(self, polyline: se.Polyline) -> Polyline:
def text_to_mobject(self, text: se.Text):
--------------------------------------------------

--------------------------------------------------

class VMobjectFromSVGPath(VMobject):

def init_points(self) -> None:
def handle_commands(self) -> None:
def handle_arc(self, arc: se.Arc) -> None:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/svg/brace.py

--------------------------------------------------

class Brace(Tex):

def set_initial_width(self, width: float):
def put_at_tip(self,
    mob: Mobject,
    use_next_to: bool = True,
    **kwargs
):
def get_text(self, text: str, **kwargs) -> Text:
def get_tex(self, *tex: str, **kwargs) -> Tex:
def get_tip(self) -> np.ndarray:
def get_direction(self) -> np.ndarray:
--------------------------------------------------

--------------------------------------------------

class BraceLabel(VMobject):

def creation_anim(self,
    label_anim: Animation = FadeIn,
    brace_anim: Animation = GrowFromCenter
) -> AnimationGroup:
def shift_brace(self, obj: VMobject | list[VMobject], **kwargs):
def change_label(self, *text: str, **kwargs):
def change_brace_label(self, obj: VMobject | list[VMobject], *text: str):
def copy(self):
--------------------------------------------------

--------------------------------------------------

class BraceText(BraceLabel):

--------------------------------------------------

--------------------------------------------------

class LineBrace(Brace):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/svg/string_mobject.py

--------------------------------------------------

class StringMobject(SVGMobject,ABC):

def get_svg_string(self, is_labelled: bool = False) -> str:
def get_svg_string_by_content(self, content: str) -> str:
def assign_labels_by_color(self, mobjects: list[VMobject]) -> None:
def mobjects_from_svg_string(self, svg_string: str) -> list[VMobject]:
def rearrange_submobjects_by_positions(self, labelled_submobs: list[VMobject], unlabelled_submobs: list[VMobject],
) -> None:
def find_spans_by_selector(self, selector: Selector) -> list[Span]:
def find_spans_by_single_selector(sel):
def span_contains(span_0: Span, span_1: Span) -> bool:
def parse(self) -> None:
def get_substr(span: Span) -> str:
def get_key(category, i, flag):
def get_span_by_category(category, i):
def reconstruct_string(start_item: tuple[int, int],
    end_item: tuple[int, int],
    command_replace_func: Callable[[re.Match], str],
    command_insert_func: Callable[[int, int, dict[str, str]], str]
) -> str:
def get_edge_item(i: int, flag: int) -> tuple[Span, str]:
def get_content(self, is_labelled: bool) -> str:
def get_command_matches(string: str) -> list[re.Match]:
def get_command_flag(match_obj: re.Match) -> int:
def replace_for_content(match_obj: re.Match) -> str:
def replace_for_matching(match_obj: re.Match) -> str:
def get_attr_dict_from_command_pair(open_command: re.Match, close_command: re.Match,
) -> dict[str, str] | None:
def get_configured_items(self) -> list[tuple[Span, dict[str, str]]]:
def get_command_string(attr_dict: dict[str, str], is_end: bool, label_hex: str | None
) -> str:
def get_content_prefix_and_suffix(self, is_labelled: bool
) -> tuple[str, str]:
def get_submob_indices_list_by_span(self, arbitrary_span: Span
) -> list[int]:
def get_specified_part_items(self) -> list[tuple[str, list[int]]]:
def get_specified_substrings(self) -> list[str]:
def get_group_part_items(self) -> list[tuple[str, list[int]]]:
def get_neighbouring_pairs(vals):
def get_submob_indices_lists_by_selector(self, selector: Selector
) -> list[list[int]]:
def build_parts_from_indices_lists(self, indices_lists: list[list[int]]
) -> VGroup:
def build_groups(self) -> VGroup:
def select_parts(self, selector: Selector) -> VGroup:
def select_part(self, selector: Selector, index: int = 0) -> VMobject:
def substr_to_path_count(self, substr: str) -> int:
def get_symbol_substrings(self):
def select_unisolated_substring(self, pattern: str | re.Pattern) -> VGroup:
def set_parts_color(self, selector: Selector, color: ManimColor):
def set_parts_color_by_dict(self, color_map: dict[Selector, ManimColor]):
def get_string(self) -> str:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/svg/text_mobject.py

--------------------------------------------------

def markup_to_svg(markup_str: str,
    justify: bool = False,
    indent: float = 0,
    alignment: str = "CENTER",
    line_width: float | None = None,
) -> str:
--------------------------------------------------

class MarkupText(StringMobject):

def get_svg_string_by_content(self, content: str) -> str:
def escape_markup_char(substr: str) -> str:
def unescape_markup_char(substr: str) -> str:
def get_command_matches(string: str) -> list[re.Match]:
def get_command_flag(match_obj: re.Match) -> int:
def replace_for_content(match_obj: re.Match) -> str:
def replace_for_matching(match_obj: re.Match) -> str:
def get_attr_dict_from_command_pair(open_command: re.Match, close_command: re.Match
) -> dict[str, str] | None:
def get_configured_items(self) -> list[tuple[Span, dict[str, str]]]:
def get_command_string(attr_dict: dict[str, str], is_end: bool, label_hex: str | None
) -> str:
def get_content_prefix_and_suffix(self, is_labelled: bool
) -> tuple[str, str]:
def get_parts_by_text(self, selector: Selector) -> VGroup:
def get_part_by_text(self, selector: Selector, **kwargs) -> VGroup:
def set_color_by_text(self, selector: Selector, color: ManimColor):
def set_color_by_text_to_color_map(self, color_map: dict[Selector, ManimColor]
):
def get_text(self) -> str:
--------------------------------------------------

--------------------------------------------------

class Text(MarkupText):

def get_command_matches(string: str) -> list[re.Match]:
def get_command_flag(match_obj: re.Match) -> int:
def replace_for_content(match_obj: re.Match) -> str:
def replace_for_matching(match_obj: re.Match) -> str:
--------------------------------------------------

--------------------------------------------------

class Code(MarkupText):

--------------------------------------------------

def register_font(font_file: str | Path):

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/svg/old_tex_mobject.py

--------------------------------------------------

class SingleStringTex(SVGMobject):

def hash_seed(self) -> tuple:
def get_svg_string_by_content(self, content: str) -> str:
def get_tex_file_body(self, tex_string: str) -> str:
def get_modified_expression(self, tex_string: str) -> str:
def modify_special_strings(self, tex: str) -> str:
def balance_braces(self, tex: str) -> str:
def get_tex(self) -> str:
def organize_submobjects_left_to_right(self):
--------------------------------------------------

--------------------------------------------------

class OldTex(SingleStringTex):

def break_up_tex_strings(self, tex_strings: Iterable[str], substrings_to_isolate: List[str] = []) -> Iterable[str]:
def break_up_by_substrings(self, tex_strings: Iterable[str]):
def get_parts_by_tex(self,
    tex: str,
    substring: bool = True,
    case_sensitive: bool = True
) -> VGroup:
def test(tex1, tex2):
def get_part_by_tex(self, tex: str, **kwargs) -> SingleStringTex | None:
def set_color_by_tex(self, tex: str, color: ManimColor, **kwargs):
def set_color_by_tex_to_color_map(self,
    tex_to_color_map: dict[str, ManimColor],
    **kwargs
):
def index_of_part(self, part: SingleStringTex, start: int = 0) -> int:
def index_of_part_by_tex(self, tex: str, start: int = 0, **kwargs) -> int:
def slice_by_tex(self,
    start_tex: str | None = None,
    stop_tex: str | None = None,
    **kwargs
) -> VGroup:
def sort_alphabetically(self) -> None:
def set_bstroke(self, color: ManimColor = BLACK, width: float = 4):
--------------------------------------------------

--------------------------------------------------

class OldTexText(OldTex):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/svg/tex_mobject.py

--------------------------------------------------

class Tex(StringMobject):

def get_svg_string_by_content(self, content: str) -> str:
def get_command_matches(string: str) -> list[re.Match]:
def get_command_flag(match_obj: re.Match) -> int:
def replace_for_content(match_obj: re.Match) -> str:
def replace_for_matching(match_obj: re.Match) -> str:
def get_attr_dict_from_command_pair(open_command: re.Match, close_command: re.Match
) -> dict[str, str] | None:
def get_configured_items(self) -> list[tuple[Span, dict[str, str]]]:
def get_color_command(rgb_hex: str) -> str:
def get_command_string(attr_dict: dict[str, str], is_end: bool, label_hex: str | None
) -> str:
def get_content_prefix_and_suffix(self, is_labelled: bool
) -> tuple[str, str]:
def get_parts_by_tex(self, selector: Selector) -> VGroup:
def get_part_by_tex(self, selector: Selector, index: int = 0) -> VMobject:
def set_color_by_tex(self, selector: Selector, color: ManimColor):
def set_color_by_tex_to_color_map(self, color_map: dict[Selector, ManimColor]
):
def get_tex(self) -> str:
def substr_to_path_count(self, substr: str) -> int:
def get_symbol_substrings(self):
def make_number_changeable(self,
    value: float | int | str,
    index: int = 0,
    replace_all: bool = False,
    **config,
) -> VMobject:
--------------------------------------------------

--------------------------------------------------

class TexText(Tex):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/svg/special_tex.py

--------------------------------------------------

class BulletedList(VGroup):

def fade_all_but(self, index: int, opacity: float = 0.25, scale_factor=0.7) -> None:
--------------------------------------------------

--------------------------------------------------

class TexTextFromPresetString(TexText):

--------------------------------------------------

--------------------------------------------------

class Title(TexText):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/types/vectorized_mobject.py

--------------------------------------------------

class VMobject(Mobject):

def get_group_class(self):
def init_uniforms(self):
def add(self, *vmobjects: VMobject) -> Self:
def init_colors(self):
def set_fill(self,
    color: ManimColor | Iterable[ManimColor] = None,
    opacity: float | Iterable[float] | None = None,
    border_width: float | None = None,
    recurse: bool = True
) -> Self:
def set_stroke(self,
    color: ManimColor | Iterable[ManimColor] = None,
    width: float | Iterable[float] | None = None,
    opacity: float | Iterable[float] | None = None,
    behind: bool | None = None,
    flat: bool | None = None,
    recurse: bool = True
) -> Self:
def set_backstroke(self,
    color: ManimColor | Iterable[ManimColor] = BLACK,
    width: float | Iterable[float] = 3,
) -> Self:
def set_style(self,
    fill_color: ManimColor | Iterable[ManimColor] | None = None,
    fill_opacity: float | Iterable[float] | None = None,
    fill_rgba: Vect4 | None = None,
    fill_border_width: float | None = None,
    stroke_color: ManimColor | Iterable[ManimColor] | None = None,
    stroke_opacity: float | Iterable[float] | None = None,
    stroke_rgba: Vect4 | None = None,
    stroke_width: float | Iterable[float] | None = None,
    stroke_behind: bool | None = None,
    flat_stroke: Optional[bool] = None,
    shading: Tuple[float, float, float] | None = None,
    recurse: bool = True
) -> Self:
def get_style(self) -> dict[str, Any]:
def match_style(self, vmobject: VMobject, recurse: bool = True) -> Self:
def set_color(self,
    color: ManimColor | Iterable[ManimColor] | None,
    opacity: float | Iterable[float] | None = None,
    recurse: bool = True
) -> Self:
def set_opacity(self,
    opacity: float | Iterable[float] | None,
    recurse: bool = True
) -> Self:
def set_anti_alias_width(self, anti_alias_width: float, recurse: bool = True) -> Self:
def fade(self, darkness: float = 0.5, recurse: bool = True) -> Self:
def get_fill_colors(self) -> list[str]:
def get_fill_opacities(self) -> np.ndarray:
def get_stroke_colors(self) -> list[str]:
def get_stroke_opacities(self) -> np.ndarray:
def get_stroke_widths(self) -> np.ndarray:
def get_fill_color(self) -> str:
def get_fill_opacity(self) -> float:
def get_stroke_color(self) -> str:
def get_stroke_width(self) -> float:
def get_stroke_opacity(self) -> float:
def get_color(self) -> str:
def get_anti_alias_width(self):
def has_stroke(self) -> bool:
def has_fill(self) -> bool:
def get_opacity(self) -> float:
def set_flat_stroke(self, flat_stroke: bool = True, recurse: bool = True) -> Self:
def get_flat_stroke(self) -> bool:
def set_scale_stroke_with_zoom(self, scale_stroke_with_zoom: bool = True, recurse: bool = True) -> Self:
def get_scale_stroke_with_zoom(self) -> bool:
def set_joint_type(self, joint_type: str, recurse: bool = True) -> Self:
def get_joint_type(self) -> float:
def apply_depth_test(self,
    anti_alias_width: float = 0,
    recurse: bool = True
) -> Self:
def deactivate_depth_test(self,
    anti_alias_width: float = 1.0,
    recurse: bool = True
) -> Self:
def use_winding_fill(self, value: bool = True, recurse: bool = True) -> Self:
def set_anchors_and_handles(self,
    anchors: Vect3Array,
    handles: Vect3Array,
) -> Self:
def start_new_path(self, point: Vect3) -> Self:
def add_cubic_bezier_curve(self,
    anchor1: Vect3,
    handle1: Vect3,
    handle2: Vect3,
    anchor2: Vect3
) -> Self:
def add_cubic_bezier_curve_to(self,
    handle1: Vect3,
    handle2: Vect3,
    anchor: Vect3,
) -> Self:
def add_quadratic_bezier_curve_to(self, handle: Vect3, anchor: Vect3, allow_null_curve=True) -> Self:
def add_line_to(self, point: Vect3, allow_null_line: bool = True) -> Self:
def add_smooth_curve_to(self, point: Vect3) -> Self:
def add_smooth_cubic_curve_to(self, handle: Vect3, point: Vect3) -> Self:
def add_arc_to(self, point: Vect3, angle: float, n_components: int | None = None, threshold: float = 1e-3) -> Self:
def has_new_path_started(self) -> bool:
def get_last_point(self) -> Vect3:
def get_reflection_of_last_handle(self) -> Vect3:
def close_path(self, smooth: bool = False) -> Self:
def is_closed(self) -> bool:
def subdivide_curves_by_condition(self,
    tuple_to_subdivisions: Callable,
    recurse: bool = True
) -> Self:
def subdivide_sharp_curves(self,
    angle_threshold: float = 30 * DEG,
    recurse: bool = True
) -> Self:
def tuple_to_subdivisions(b0, b1, b2):
def subdivide_intersections(self, recurse: bool = True, n_subdivisions: int = 1) -> Self:
def tuple_to_subdivisions(b0, b1, b2):
def add_points_as_corners(self, points: Iterable[Vect3]) -> Self:
def set_points_as_corners(self, points: Iterable[Vect3]) -> Self:
def set_points_smoothly(self,
    points: Iterable[Vect3],
    approx: bool = True
) -> Self:
def is_smooth(self, angle_tol=1 * DEG) -> bool:
def change_anchor_mode(self, mode: str) -> Self:
def make_smooth(self, approx=True, recurse=True) -> Self:
def make_approximately_smooth(self, recurse=True) -> Self:
def make_jagged(self, recurse=True) -> Self:
def add_subpath(self, points: Vect3Array) -> Self:
def append_vectorized_mobject(self, vmobject: VMobject) -> Self:
def consider_points_equal(self, p0: Vect3, p1: Vect3) -> bool:
def get_bezier_tuples_from_points(self, points: Vect3Array) -> Iterable[Vect3Array]:
def get_bezier_tuples(self) -> Iterable[Vect3Array]:
def get_subpath_end_indices_from_points(self, points: Vect3Array) -> np.ndarray:
def get_subpath_end_indices(self) -> np.ndarray:
def get_subpaths_from_points(self, points: Vect3Array) -> list[Vect3Array]:
def get_subpaths(self) -> list[Vect3Array]:
def get_nth_curve_points(self, n: int) -> Vect3Array:
def get_nth_curve_function(self, n: int) -> Callable[[float], Vect3]:
def get_num_curves(self) -> int:
def quick_point_from_proportion(self, alpha: float) -> Vect3:
def curve_and_prop_of_partial_point(self, alpha) -> Tuple[int, float]:
def point_from_proportion(self, alpha: float) -> Vect3:
def get_anchors_and_handles(self) -> list[Vect3]:
def get_start_anchors(self) -> Vect3Array:
def get_end_anchors(self) -> Vect3:
def get_anchors(self) -> Vect3Array:
def get_points_without_null_curves(self, atol: float = 1e-9) -> Vect3Array:
def get_arc_length(self, n_sample_points: int | None = None) -> float:
def get_area_vector(self) -> Vect3:
def get_unit_normal(self, refresh: bool = False) -> Vect3:
def refresh_unit_normal(self) -> Self:
def rotate(self,
    angle: float,
    axis: Vect3 = OUT,
    about_point: Vect3 | None = None,
    **kwargs
) -> Self:
def ensure_positive_orientation(self, recurse=True) -> Self:
def align_points(self, vmobject: VMobject) -> Self:
def get_nth_subpath(path_list, n):
def insert_n_curves(self, n: int, recurse: bool = True) -> Self:
def insert_n_curves_to_point_list(self, n: int, points: Vect3Array) -> Vect3Array:
def pointwise_become_partial(self, vmobject: VMobject, a: float, b: float) -> Self:
def get_subcurve(self, a: float, b: float) -> Self:
def get_outer_vert_indices(self) -> np.ndarray:
def get_triangulation(self) -> np.ndarray:
def refresh_joint_angles(self) -> Self:
def get_joint_angles(self, refresh: bool = False) -> np.ndarray:
def lock_matching_data(self, vmobject1: VMobject, vmobject2: VMobject) -> Self:
def triggers_refresh(func: Callable):
def wrapper(self, *args, refresh=True, **kwargs):
def set_points(self, points: Vect3Array) -> Self:
def append_points(self, points: Vect3Array) -> Self:
def reverse_points(self, recurse: bool = True) -> Self:
def set_data(self, data: np.ndarray) -> Self:
def apply_function(self,
    function: Callable[[Vect3], Vect3],
    make_smooth: bool = False,
    **kwargs
) -> Self:
def stretch(self, *args, **kwargs) -> Self:
def apply_matrix(self, *args, **kwargs) -> Self:
def rotate(self,
    angle: float,
    axis: Vect3 = OUT,
    about_point: Vect3 | None = None,
    **kwargs
) -> Self:
def set_animating_status(self, is_animating: bool, recurse: bool = True):
def init_shader_wrapper(self, ctx: Context):
def refresh_shader_wrapper_id(self):
def get_shader_data(self) -> np.ndarray:
def get_shader_vert_indices(self) -> Optional[np.ndarray]:
--------------------------------------------------

--------------------------------------------------

class VGroup(Group,VMobject,Generic):

--------------------------------------------------

--------------------------------------------------

class VectorizedPoint(Point,VMobject):

--------------------------------------------------

--------------------------------------------------

class CurvesAsSubmobjects(VGroup):

--------------------------------------------------

--------------------------------------------------

class DashedVMobject(VMobject):

--------------------------------------------------

--------------------------------------------------

class VHighlight(VGroup):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/types/image_mobject.py

--------------------------------------------------

class ImageMobject(Mobject):

def init_data(self) -> None:
def init_points(self) -> None:
def set_opacity(self, opacity: float, recurse: bool = True):
def set_color(self, color, opacity=None, recurse=None):
def point_to_rgb(self, point: Vect3) -> Vect3:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/types/dot_cloud.py

--------------------------------------------------

class DotCloud(PMobject):

def init_uniforms(self) -> None:
def to_grid(self,
    n_rows: int,
    n_cols: int,
    n_layers: int = 1,
    buff_ratio: float | None = None,
    h_buff_ratio: float = 1.0,
    v_buff_ratio: float = 1.0,
    d_buff_ratio: float = 1.0,
    height: float = DEFAULT_GRID_HEIGHT,
) -> Self:
def set_radii(self, radii: npt.ArrayLike) -> Self:
def get_radii(self) -> np.ndarray:
def set_radius(self, radius: float) -> Self:
def get_radius(self) -> float:
def scale_radii(self, scale_factor: float) -> Self:
def set_glow_factor(self, glow_factor: float) -> Self:
def get_glow_factor(self) -> float:
def compute_bounding_box(self) -> Vect3Array:
def scale(self,
    scale_factor: float | npt.ArrayLike,
    scale_radii: bool = True,
    **kwargs
) -> Self:
def make_3d(self,
    reflectiveness: float = 0.5,
    gloss: float = 0.1,
    shadow: float = 0.2
) -> Self:
--------------------------------------------------

--------------------------------------------------

class TrueDot(DotCloud):

--------------------------------------------------

--------------------------------------------------

class GlowDots(DotCloud):

--------------------------------------------------

--------------------------------------------------

class GlowDot(GlowDots):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/types/point_cloud_mobject.py

--------------------------------------------------

class PMobject(Mobject):

def set_points(self, points: Vect3Array):
def add_points(self,
    points: Vect3Array,
    rgbas: Vect4Array | None = None,
    color: ManimColor | None = None,
    opacity: float | None = None
) -> Self:
def add_point(self, point: Vect3, rgba=None, color=None, opacity=None) -> Self:
def set_color_by_gradient(self, *colors: ManimColor) -> Self:
def match_colors(self, pmobject: PMobject) -> Self:
def filter_out(self, condition: Callable[[np.ndarray], bool]) -> Self:
def sort_points(self, function: Callable[[Vect3], None] = lambda p: p[0]) -> Self:
def ingest_submobjects(self) -> Self:
def point_from_proportion(self, alpha: float) -> np.ndarray:
def pointwise_become_partial(self, pmobject: PMobject, a: float, b: float) -> Self:
--------------------------------------------------

--------------------------------------------------

class PGroup(PMobject):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manimlib/mobject/types/surface.py

--------------------------------------------------

class Surface(Mobject):

def uv_func(self, u: float, v: float) -> tuple[float, float, float]:
def init_points(self):
def uv_to_point(self, u, v):
def apply_points_function(self, *args, **kwargs) -> Self:
def compute_triangle_indices(self) -> np.ndarray:
def get_triangle_indices(self) -> np.ndarray:
def get_unit_normals(self) -> Vect3Array:
def pointwise_become_partial(self,
    smobject: "Surface",
    a: float,
    b: float,
    axis: int | None = None
) -> Self:
def get_partial_points_array(self,
    points: Vect3Array,
    a: float,
    b: float,
    resolution: Sequence[int],
    axis: int
) -> Vect3Array:
def sort_faces_back_to_front(self, vect: Vect3 = OUT) -> Self:
def always_sort_to_camera(self, camera: Camera) -> Self:
def updater(surface: Surface):
def get_shader_vert_indices(self) -> np.ndarray:
--------------------------------------------------

--------------------------------------------------

class ParametricSurface(Surface):

def uv_func(self, u, v):
--------------------------------------------------

--------------------------------------------------

class SGroup(Surface):

def init_points(self):
--------------------------------------------------

--------------------------------------------------

class TexturedSurface(Surface):

def init_points(self):
def init_uniforms(self):
def set_opacity(self, opacity: float | Iterable[float], recurse=True) -> Self:
def set_color(self,
    color: ManimColor | Iterable[ManimColor] | None,
    opacity: float | Iterable[float] | None = None,
    recurse: bool = True
) -> Self:
def pointwise_become_partial(self,
    tsmobject: "TexturedSurface",
    a: float,
    b: float,
    axis: int = 1
) -> Self:
--------------------------------------------------
"""
async def run_manim_code(code: str, path: str = getcwd()) -> None:
    print("Adding interactivity...")
    add_interactivity(code, path)

    print("Running the scene...")
    manim_path = which("manim")
    if not manim_path:
        print("Manim executable not found.")
        return

    code_file = join(path, "generated_code.py")

    print(code[code.find("class ") + len("class ") + 1:])

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

        media_root = join(code_dir, "output_media", "videos")
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

async def generate_video(prompt: str, path: str = getcwd(), use_local_model: bool = False) -> None:
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
HERE IS ALL OF THE METHODS OF THE MANIM LIBRARY, MAKE SURE YOU USE THESE METHODS SOLELY: {MANIM_LIBRARY_API}
The prompt: {prompt}"""

    if use_local_model:
        pass
    else:
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
