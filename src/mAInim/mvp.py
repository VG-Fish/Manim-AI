# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
#     "ipython>=8.31.0",
#     "latex>=0.7.0",
#     "libcst>=1.7.0",
#     "lmstudio",
#     "manim>=0.19.0",
#     "openai",
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

import lmstudio as lms

MANIM_LIBRARY_API: str = """

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/constants.py

--------------------------------------------------

class QualityDict(TypedDict):

--------------------------------------------------

--------------------------------------------------

class RendererType(Enum):

--------------------------------------------------

--------------------------------------------------

class LineJointType(Enum):

--------------------------------------------------

--------------------------------------------------

class CapStyleType(Enum):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/typing.py


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/renderer/cairo_renderer.py

--------------------------------------------------

class CairoRenderer:

def init_scene(self, scene):
def play(self,
    scene: Scene,
    *args: Animation | Mobject | _AnimationBuilder,
    **kwargs,
):
def update_frame(self,
    scene,
    mobjects: typing.Iterable[Mobject] | None = None,
    include_submobjects: bool = True,
    ignore_skipping: bool = True,
    **kwargs,
):
def render(self, scene, time, moving_mobjects):
def get_frame(self) -> PixelArray:
def add_frame(self, frame: np.ndarray, num_frames: int = 1):
def freeze_current_frame(self, duration: float):
def show_frame(self):
def save_static_frame_data(self,
    scene: Scene,
    static_mobjects: typing.Iterable[Mobject],
) -> typing.Iterable[Mobject] | None:
def update_skipping_status(self):
def scene_finished(self, scene):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/renderer/shader.py

def get_shader_code_from_file(file_path: Path) -> str:
def filter_attributes(unfiltered_attributes, attributes):
--------------------------------------------------

class Object3D:

def interpolate(self, start, end, alpha, _):
def single_copy(self):
def copy(self):
def add(self, *children):
def remove(self, *children, current_children_only=True):
def get_position(self):
def set_position(self, position):
def get_meshes(self):
def get_family(self):
def align_data_and_family(self, _):
def hierarchical_model_matrix(self):
def hierarchical_normal_matrix(self):
def init_updaters(self):
def update(self, dt=0):
def get_time_based_updaters(self):
def has_time_based_updater(self):
def get_updaters(self):
def add_updater(self, update_function, index=None, call_updater=True):
def remove_updater(self, update_function):
def clear_updaters(self):
def match_updaters(self, mobject):
def suspend_updating(self):
def resume_updating(self, call_updater=True):
def refresh_has_updater_status(self):
--------------------------------------------------

--------------------------------------------------

class Mesh(Object3D):

def single_copy(self):
def set_uniforms(self, renderer):
def render(self):
--------------------------------------------------

--------------------------------------------------

class Shader:

def set_uniform(self, name, value):
--------------------------------------------------

--------------------------------------------------

class FullScreenQuad(Mesh):

def render(self):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/renderer/opengl_renderer_window.py

--------------------------------------------------

class Window(PygletWindow):

def on_mouse_motion(self, x, y, dx, dy):
def on_mouse_scroll(self, x, y, x_offset: float, y_offset: float):
def on_key_press(self, symbol, modifiers):
def on_key_release(self, symbol, modifiers):
def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
def find_initial_position(self, size, monitor):
def on_mouse_press(self, x, y, button, modifiers):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/renderer/vectorized_mobject_rendering.py

def build_matrix_lists(mob):
def render_opengl_vectorized_mobject_fill(renderer, mobject):
def render_mobject_fills_with_matrix(renderer, model_matrix, mobjects):
def triangulate_mobject(mob):
def render_opengl_vectorized_mobject_stroke(renderer, mobject):
def render_mobject_strokes_with_matrix(renderer, model_matrix, mobjects):

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/renderer/shader_wrapper.py

def get_shader_dir():
def find_file(file_name: Path, directories: list[Path]) -> Path:
--------------------------------------------------

class ShaderWrapper:

def copy(self):
def is_valid(self):
def get_id(self):
def get_program_id(self):
def create_id(self):
def refresh_id(self):
def create_program_id(self):
def init_program_code(self):
def get_code(name: str) -> str | None:
def get_program_code(self):
def replace_code(self, old, new):
def combine_with(self, *shader_wrappers):
--------------------------------------------------

def get_shader_code_from_file(filename: Path) -> str | None:
def get_colormap_code(rgb_list):

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/renderer/opengl_renderer.py

--------------------------------------------------

class OpenGLCamera(OpenGLMobject):

def get_position(self):
def set_position(self, position):
def formatted_view_matrix(self):
def unformatted_view_matrix(self):
def init_points(self):
def to_default_state(self):
def refresh_rotation_matrix(self):
def rotate(self, angle, axis=OUT, **kwargs):
def set_euler_angles(self, theta=None, phi=None, gamma=None):
def set_theta(self, theta):
def set_phi(self, phi):
def set_gamma(self, gamma):
def increment_theta(self, dtheta):
def increment_phi(self, dphi):
def increment_gamma(self, dgamma):
def get_shape(self):
def get_center(self):
def get_width(self):
def get_height(self):
def get_focal_distance(self):
def interpolate(self, *args, **kwargs):
--------------------------------------------------

--------------------------------------------------

class OpenGLRenderer:

def init_scene(self, scene):
def should_create_window(self):
def get_pixel_shape(self):
def refresh_perspective_uniforms(self, camera):
def render_mobject(self, mobject):
def get_texture_id(self, path):
def update_skipping_status(self) -> None:
def play(self, scene, *args, **kwargs):
def clear_screen(self):
def render(self, scene, frame_offset, moving_mobjects):
def update_frame(self, scene):
def scene_finished(self, scene):
def should_save_last_frame(self):
def get_image(self) -> Image.Image:
def save_static_frame_data(self, scene, static_mobjects):
def get_frame_buffer_object(self, context, samples=0):
def get_raw_frame_buffer_object_data(self, dtype="f1"):
def get_frame(self):
def pixel_coords_to_space_coords(self, px, py, relative=False, top_left=False):
def background_color(self):
def background_color(self, value):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/plugins/plugins_flags.py

def get_plugins() -> dict[str, Any]:
def list_plugins() -> None:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/camera/moving_camera.py

--------------------------------------------------

class MovingCamera(Camera):

def frame_height(self):
def frame_width(self):
def frame_center(self):
def frame_height(self, frame_height: float):
def frame_width(self, frame_width: float):
def frame_center(self, frame_center: np.ndarray | list | tuple | Mobject):
def capture_mobjects(self, mobjects, **kwargs):
def get_cached_cairo_context(self, pixel_array):
def cache_cairo_context(self, pixel_array, ctx):
def get_mobjects_indicating_movement(self):
def auto_zoom(self,
    mobjects: list[Mobject],
    margin: float = 0,
    only_mobjects_in_frame: bool = False,
    animate: bool = True,
):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/camera/three_d_camera.py

--------------------------------------------------

class ThreeDCamera(Camera):

def frame_center(self):
def frame_center(self, point):
def capture_mobjects(self, mobjects, **kwargs):
def get_value_trackers(self):
def modified_rgbas(self, vmobject, rgbas):
def get_stroke_rgbas(self,
    vmobject,
    background=False,
):
def get_fill_rgbas(self, vmobject):
def get_mobjects_to_display(self, *args, **kwargs):
def z_key(mob):
def get_phi(self):
def get_theta(self):
def get_focal_distance(self):
def get_gamma(self):
def get_zoom(self):
def set_phi(self, value: float):
def set_theta(self, value: float):
def set_focal_distance(self, value: float):
def set_gamma(self, value: float):
def set_zoom(self, value: float):
def reset_rotation_matrix(self):
def get_rotation_matrix(self):
def generate_rotation_matrix(self):
def project_points(self, points: np.ndarray | list):
def project_point(self, point: list | np.ndarray):
def transform_points_pre_display(self,
    mobject,
    points,
):
def add_fixed_orientation_mobjects(self,
    *mobjects: Mobject,
    use_static_center_func: bool = False,
    center_func: Callable[[], np.ndarray] | None = None,
):
def get_static_center_func(mobject):
def add_fixed_in_frame_mobjects(self, *mobjects: Mobject):
def remove_fixed_orientation_mobjects(self, *mobjects: Mobject):
def remove_fixed_in_frame_mobjects(self, *mobjects: Mobject):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/camera/multi_camera.py

--------------------------------------------------

class MultiCamera(MovingCamera):

def add_image_mobject_from_camera(self, image_mobject_from_camera: ImageMobject):
def update_sub_cameras(self):
def reset(self):
def capture_mobjects(self, mobjects, **kwargs):
def get_mobjects_indicating_movement(self):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/camera/camera.py

--------------------------------------------------

class Camera:

def background_color(self):
def background_color(self, color):
def background_opacity(self):
def background_opacity(self, alpha):
def type_or_raise(self, mobject: Mobject):
def reset_pixel_shape(self, new_height: float, new_width: float):
def resize_frame_shape(self, fixed_dimension: int = 0):
def init_background(self):
def get_image(self, pixel_array: np.ndarray | list | tuple | None = None):
def convert_pixel_array(self, pixel_array: np.ndarray | list | tuple, convert_from_floats: bool = False
):
def set_pixel_array(self, pixel_array: np.ndarray | list | tuple, convert_from_floats: bool = False
):
def set_background(self, pixel_array: np.ndarray | list | tuple, convert_from_floats: bool = False
):
def make_background_from_func(self, coords_to_colors_func: Callable[[np.ndarray], np.ndarray]
):
def set_background_from_func(self, coords_to_colors_func: Callable[[np.ndarray], np.ndarray]
):
def reset(self):
def set_frame_to_background(self, background):
def get_mobjects_to_display(self,
    mobjects: Iterable[Mobject],
    include_submobjects: bool = True,
    excluded_mobjects: list | None = None,
):
def is_in_frame(self, mobject: Mobject):
def capture_mobject(self, mobject: Mobject, **kwargs: Any):
def capture_mobjects(self, mobjects: Iterable[Mobject], **kwargs):
def get_cached_cairo_context(self, pixel_array: np.ndarray):
def cache_cairo_context(self, pixel_array: np.ndarray, ctx: cairo.Context):
def get_cairo_context(self, pixel_array: np.ndarray):
def display_multiple_vectorized_mobjects(self, vmobjects: list, pixel_array: np.ndarray
):
def display_multiple_non_background_colored_vmobjects(self, vmobjects: list, pixel_array: np.ndarray
):
def display_vectorized(self, vmobject: VMobject, ctx: cairo.Context):
def set_cairo_context_path(self, ctx: cairo.Context, vmobject: VMobject):
def set_cairo_context_color(self, ctx: cairo.Context, rgbas: np.ndarray, vmobject: VMobject
):
def apply_fill(self, ctx: cairo.Context, vmobject: VMobject):
def apply_stroke(self, ctx: cairo.Context, vmobject: VMobject, background: bool = False
):
def get_stroke_rgbas(self, vmobject: VMobject, background: bool = False):
def get_fill_rgbas(self, vmobject: VMobject):
def get_background_colored_vmobject_displayer(self):
def display_multiple_background_colored_vmobjects(self, cvmobjects: list, pixel_array: np.ndarray
):
def display_multiple_point_cloud_mobjects(self, pmobjects: list, pixel_array: np.ndarray
):
def display_point_cloud(self,
    pmobject: PMobject,
    points: list,
    rgbas: np.ndarray,
    thickness: float,
    pixel_array: np.ndarray,
):
def display_multiple_image_mobjects(self, image_mobjects: list, pixel_array: np.ndarray
):
def display_image_mobject(self, image_mobject: AbstractImageMobject, pixel_array: np.ndarray
):
def overlay_rgba_array(self, pixel_array: np.ndarray, new_array: np.ndarray):
def overlay_PIL_image(self, pixel_array: np.ndarray, image: Image):
def adjust_out_of_range_points(self, points: np.ndarray):
def transform_points_pre_display(self,
    mobject,
    points,
):
def points_to_pixel_coords(self,
    mobject,
    points,
):
def on_screen_pixels(self, pixel_coords: np.ndarray):
def adjusted_thickness(self, thickness: float) -> float:
def get_thickening_nudges(self, thickness: float):
def thickened_coordinates(self, pixel_coords: np.ndarray, thickness: float):
def get_coords_of_all_pixels(self):
--------------------------------------------------

--------------------------------------------------

class BackgroundColoredVMobjectDisplayer:

def reset_pixel_array(self):
def resize_background_array(self,
    background_array: np.ndarray,
    new_width: float,
    new_height: float,
    mode: str = "RGBA",
):
def resize_background_array_to_match(self, background_array: np.ndarray, pixel_array: np.ndarray
):
def get_background_array(self, image: Image.Image | pathlib.Path | str):
def display(self, *cvmobjects: VMobject):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/camera/mapping_camera.py

--------------------------------------------------

class MappingCamera(Camera):

def points_to_pixel_coords(self, mobject, points):
def capture_mobjects(self, mobjects, **kwargs):
--------------------------------------------------

--------------------------------------------------

class OldMultiCamera(Camera):

def capture_mobjects(self, mobjects, **kwargs):
def set_background(self, pixel_array, **kwargs):
def set_pixel_array(self, pixel_array, **kwargs):
def init_background(self):
--------------------------------------------------

--------------------------------------------------

class SplitScreenCamera(OldMultiCamera):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/animation/speedmodifier.py

--------------------------------------------------

class ChangeSpeed(Animation):

def condition(t,
    curr_time=curr_time,
    init_speed=init_speed,
    final_speed=final_speed,
    dur=dur,
):
def function(t,
    curr_time=curr_time,
    init_speed=init_speed,
    final_speed=final_speed,
    dur=dur,
    prevnode=prevnode,
):
def func(t):
def setup(self, anim):
def get_scaled_total_time(self) -> float:
def add_updater(cls,
    mobject: Mobject,
    update_function: Updater,
    index: int | None = None,
    call_updater: bool = False,
):
def interpolate(self, alpha: float) -> None:
def update_mobjects(self, dt: float) -> None:
def finish(self) -> None:
def begin(self) -> None:
def clean_up_from_scene(self, scene: Scene) -> None:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/animation/creation.py

--------------------------------------------------

class ShowPartial(Animation):

def interpolate_submobject(self,
    submobject: Mobject,
    starting_submobject: Mobject,
    alpha: float,
) -> None:
--------------------------------------------------

--------------------------------------------------

class Create(ShowPartial):

--------------------------------------------------

--------------------------------------------------

class Uncreate(Create):

--------------------------------------------------

--------------------------------------------------

class DrawBorderThenFill(Animation):

def begin(self) -> None:
def get_outline(self) -> Mobject:
def get_stroke_color(self, vmobject: VMobject | OpenGLVMobject) -> ManimColor:
def get_all_mobjects(self) -> Sequence[Mobject]:
def interpolate_submobject(self,
    submobject: Mobject,
    starting_submobject: Mobject,
    outline,
    alpha: float,
) -> None:
--------------------------------------------------

--------------------------------------------------

class Write(DrawBorderThenFill):

def reverse_submobjects(self) -> None:
def begin(self) -> None:
def finish(self) -> None:
--------------------------------------------------

--------------------------------------------------

class Unwrite(Write):

--------------------------------------------------

--------------------------------------------------

class SpiralIn(Animation):

def interpolate_mobject(self, alpha: float) -> None:
--------------------------------------------------

--------------------------------------------------

class ShowIncreasingSubsets(Animation):

def interpolate_mobject(self, alpha: float) -> None:
def update_submobject_list(self, index: int) -> None:
--------------------------------------------------

--------------------------------------------------

class AddTextLetterByLetter(ShowIncreasingSubsets):

--------------------------------------------------

--------------------------------------------------

class RemoveTextLetterByLetter(AddTextLetterByLetter):

--------------------------------------------------

--------------------------------------------------

class ShowSubmobjectsOneByOne(ShowIncreasingSubsets):

def update_submobject_list(self, index: int) -> None:
--------------------------------------------------

--------------------------------------------------

class AddTextWordByWord(Succession):

--------------------------------------------------

--------------------------------------------------

class TypeWithCursor(AddTextLetterByLetter):

def begin(self) -> None:
def finish(self) -> None:
def clean_up_from_scene(self, scene: Scene) -> None:
def update_submobject_list(self, index: int) -> None:
--------------------------------------------------

--------------------------------------------------

class UntypeWithCursor(TypeWithCursor):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/animation/transform_matching_parts.py

--------------------------------------------------

class TransformMatchingAbstractBase(AnimationGroup):

def get_shape_map(self, mobject: Mobject) -> dict:
def clean_up_from_scene(self, scene: Scene) -> None:
def get_mobject_parts(mobject: Mobject):
def get_mobject_key(mobject: Mobject):
--------------------------------------------------

--------------------------------------------------

class TransformMatchingShapes(TransformMatchingAbstractBase):

def get_mobject_parts(mobject: Mobject) -> list[Mobject]:
def get_mobject_key(mobject: Mobject) -> int:
--------------------------------------------------

--------------------------------------------------

class TransformMatchingTex(TransformMatchingAbstractBase):

def get_mobject_parts(mobject: Mobject) -> list[Mobject]:
def get_mobject_key(mobject: Mobject) -> str:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/animation/numbers.py

--------------------------------------------------

class ChangingDecimal(Animation):

def check_validity_of_input(self, decimal_mob: DecimalNumber) -> None:
def interpolate_mobject(self, alpha: float) -> None:
--------------------------------------------------

--------------------------------------------------

class ChangeDecimalToValue(ChangingDecimal):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/animation/movement.py

--------------------------------------------------

class Homotopy(Animation):

def function_at_time_t(self, t: float) -> tuple[float, float, float]:
def interpolate_submobject(self,
    submobject: Mobject,
    starting_submobject: Mobject,
    alpha: float,
) -> None:
--------------------------------------------------

--------------------------------------------------

class SmoothedVectorizedHomotopy(Homotopy):

def interpolate_submobject(self,
    submobject: Mobject,
    starting_submobject: Mobject,
    alpha: float,
) -> None:
--------------------------------------------------

--------------------------------------------------

class ComplexHomotopy(Homotopy):

def homotopy(x: float,
    y: float,
    z: float,
    t: float,
) -> tuple[float, float, float]:
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

Current file: manim/animation/animation.py

--------------------------------------------------

class Animation:

def run_time(self) -> float:
def run_time(self, value: float) -> None:
def begin(self) -> None:
def finish(self) -> None:
def clean_up_from_scene(self, scene: Scene) -> None:
def create_starting_mobject(self) -> Mobject:
def get_all_mobjects(self) -> Sequence[Mobject]:
def get_all_families_zipped(self) -> Iterable[tuple]:
def update_mobjects(self, dt: float) -> None:
def get_all_mobjects_to_update(self) -> list[Mobject]:
def copy(self) -> Animation:
def interpolate(self, alpha: float) -> None:
def interpolate_mobject(self, alpha: float) -> None:
def interpolate_submobject(self,
    submobject: Mobject,
    starting_submobject: Mobject,
    # target_copy: Mobject, #Todo: fix - signature of interpolate_submobject differs in Transform().
    alpha: float,
) -> Animation:
def get_sub_alpha(self, alpha: float, index: int, num_submobjects: int) -> float:
def set_run_time(self, run_time: float) -> Animation:
def get_run_time(self) -> float:
def set_rate_func(self,
    rate_func: Callable[[float], float],
) -> Animation:
def get_rate_func(self,
) -> Callable[[float], float]:
def set_name(self, name: str) -> Animation:
def is_remover(self) -> bool:
def is_introducer(self) -> bool:
def set_default(cls, **kwargs) -> None:
--------------------------------------------------

def prepare_animation(anim: Animation | mobject._AnimationBuilder,
) -> Animation:
--------------------------------------------------

class Wait(Animation):

def begin(self) -> None:
def finish(self) -> None:
def clean_up_from_scene(self, scene: Scene) -> None:
def update_mobjects(self, dt: float) -> None:
def interpolate(self, alpha: float) -> None:
--------------------------------------------------

--------------------------------------------------

class Add(Animation):

def begin(self) -> None:
def finish(self) -> None:
def clean_up_from_scene(self, scene: Scene) -> None:
def update_mobjects(self, dt: float) -> None:
def interpolate(self, alpha: float) -> None:
--------------------------------------------------

def override_animation(animation_class: type[Animation],
) -> Callable[[Callable], Callable]:
def decorator(func):

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/animation/specialized.py

--------------------------------------------------

class Broadcast(LaggedStart):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/animation/transform.py

--------------------------------------------------

class Transform(Animation):

def path_arc(self) -> float:
def path_arc(self, path_arc: float) -> None:
def path_func(self,
) -> Callable[
    [Iterable[np.ndarray], Iterable[np.ndarray], float],
    Iterable[np.ndarray],
]:
def path_func(self,
    path_func: Callable[
        [Iterable[np.ndarray], Iterable[np.ndarray], float],
        Iterable[np.ndarray],
    ],
) -> None:
def begin(self) -> None:
def create_target(self) -> Mobject:
def clean_up_from_scene(self, scene: Scene) -> None:
def get_all_mobjects(self) -> Sequence[Mobject]:
def get_all_families_zipped(self) -> Iterable[tuple]:
def interpolate_submobject(self,
    submobject: Mobject,
    starting_submobject: Mobject,
    target_copy: Mobject,
    alpha: float,
) -> Transform:
--------------------------------------------------

--------------------------------------------------

class ReplacementTransform(Transform):

--------------------------------------------------

--------------------------------------------------

class TransformFromCopy(Transform):

def interpolate(self, alpha: float) -> None:
--------------------------------------------------

--------------------------------------------------

class ClockwiseTransform(Transform):

--------------------------------------------------

--------------------------------------------------

class CounterclockwiseTransform(Transform):

--------------------------------------------------

--------------------------------------------------

class MoveToTarget(Transform):

def check_validity_of_input(self, mobject: Mobject) -> None:
--------------------------------------------------

def finish(self) -> None:
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

class ApplyPointwiseFunctionToCenter(ApplyPointwiseFunction):

def begin(self) -> None:
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

class Restore(ApplyMethod):

--------------------------------------------------

--------------------------------------------------

class ApplyFunction(Transform):

def create_target(self) -> Any:
--------------------------------------------------

--------------------------------------------------

class ApplyMatrix(ApplyPointwiseFunction):

def func(p):
def initialize_matrix(self, matrix: np.ndarray) -> np.ndarray:
--------------------------------------------------

--------------------------------------------------

class ApplyComplexFunction(ApplyMethod):

--------------------------------------------------

--------------------------------------------------

class CyclicReplace(Transform):

def create_target(self) -> Group:
--------------------------------------------------

--------------------------------------------------

class Swap(CyclicReplace):

--------------------------------------------------

--------------------------------------------------

class TransformAnimations(Transform):

def interpolate(self, alpha: float) -> None:
--------------------------------------------------

--------------------------------------------------

class FadeTransform(Transform):

def begin(self):
def ghost_to(self, source, target):
def get_all_mobjects(self) -> Sequence[Mobject]:
def get_all_families_zipped(self):
def clean_up_from_scene(self, scene):
--------------------------------------------------

--------------------------------------------------

class FadeTransformPieces(FadeTransform):

def begin(self):
def ghost_to(self, source, target):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/animation/indication.py

--------------------------------------------------

class FocusOn(Transform):

def create_target(self) -> Dot:
--------------------------------------------------

--------------------------------------------------

class Indicate(Transform):

def create_target(self) -> Mobject:
--------------------------------------------------

--------------------------------------------------

class Flash(AnimationGroup):

def create_lines(self) -> VGroup:
def create_line_anims(self) -> Iterable[ShowPassingFlash]:
--------------------------------------------------

--------------------------------------------------

class ShowPassingFlash(ShowPartial):

def clean_up_from_scene(self, scene: Scene) -> None:
--------------------------------------------------

--------------------------------------------------

class ShowPassingFlashWithThinningStrokeWidth(AnimationGroup):

--------------------------------------------------

--------------------------------------------------

class ApplyWave(Homotopy):

def wave(t):
def homotopy(x: float,
    y: float,
    z: float,
    t: float,
) -> tuple[float, float, float]:
--------------------------------------------------

--------------------------------------------------

class Wiggle(Animation):

def get_scale_about_point(self) -> np.ndarray:
def get_rotate_about_point(self) -> np.ndarray:
def interpolate_submobject(self,
    submobject: Mobject,
    starting_submobject: Mobject,
    alpha: float,
) -> None:
--------------------------------------------------

--------------------------------------------------

class Circumscribe(Succession):

--------------------------------------------------

--------------------------------------------------

class Blink(Succession):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/animation/composition.py

--------------------------------------------------

class AnimationGroup(Animation):

def get_all_mobjects(self) -> Sequence[Mobject]:
def begin(self) -> None:
def finish(self) -> None:
def clean_up_from_scene(self, scene: Scene) -> None:
def update_mobjects(self, dt: float) -> None:
def init_run_time(self, run_time) -> float:
def build_animations_with_timings(self) -> None:
def interpolate(self, alpha: float) -> None:
--------------------------------------------------

--------------------------------------------------

class Succession(AnimationGroup):

def begin(self) -> None:
def finish(self) -> None:
def update_mobjects(self, dt: float) -> None:
def update_active_animation(self, index: int) -> None:
def next_animation(self) -> None:
def interpolate(self, alpha: float) -> None:
--------------------------------------------------

--------------------------------------------------

class LaggedStart(AnimationGroup):

--------------------------------------------------

--------------------------------------------------

class LaggedStartMap(LaggedStart):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/animation/changing.py

--------------------------------------------------

class AnimatedBoundary(VGroup):

def update_boundary_copies(self, dt):
def full_family_become_partial(self, mob1, mob2, a, b):
--------------------------------------------------

--------------------------------------------------

class TracedPath(VMobject):

def update_path(self, mob, dt):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/animation/rotation.py

--------------------------------------------------

class Rotating(Animation):

def interpolate_mobject(self, alpha: float) -> None:
--------------------------------------------------

--------------------------------------------------

class Rotate(Transform):

def create_target(self) -> Mobject:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/animation/growing.py

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

def create_starting_mobject(self) -> Mobject:
--------------------------------------------------

--------------------------------------------------

class SpinInFromNothing(GrowFromCenter):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/animation/fading.py

--------------------------------------------------

--------------------------------------------------

class FadeIn(_Fade):

def create_target(self):
def create_starting_mobject(self):
--------------------------------------------------

--------------------------------------------------

class FadeOut(_Fade):

def create_target(self):
def clean_up_from_scene(self, scene: Scene = None) -> None:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/animation/updaters/update.py

--------------------------------------------------

class UpdateFromFunc(Animation):

def interpolate_mobject(self, alpha: float) -> None:
--------------------------------------------------

--------------------------------------------------

class UpdateFromAlphaFunc(UpdateFromFunc):

def interpolate_mobject(self, alpha: float) -> None:
--------------------------------------------------

--------------------------------------------------

class MaintainPositionRelativeTo(Animation):

def interpolate_mobject(self, alpha: float) -> None:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/animation/updaters/mobject_update_utils.py

def assert_is_mobject_method(method: Callable) -> None:
def always(method: Callable, *args, **kwargs) -> Mobject:
def f_always(method: Callable[[Mobject], None], *arg_generators, **kwargs) -> Mobject:
def updater(mob):
def always_redraw(func: Callable[[], Mobject]) -> Mobject:
def always_shift(mobject: Mobject, direction: np.ndarray[np.float64] = RIGHT, rate: float = 0.1
) -> Mobject:
def always_rotate(mobject: Mobject, rate: float = 20 * DEGREES, **kwargs) -> Mobject:
def turn_animation_into_updater(animation: Animation, cycle: bool = False, delay: float = 0, **kwargs
) -> Mobject:
def update(m: Mobject, dt: float):
def cycle_animation(animation: Animation, **kwargs) -> Mobject:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/sounds.py

def get_full_sound_file_path(sound_file_name: StrPath) -> Path:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/rate_functions.py

--------------------------------------------------

class RateFunction(Protocol):

--------------------------------------------------

def unit_interval(function: RateFunction) -> RateFunction:
def wrapper(t: float, *args: Any, **kwargs: Any) -> float:
def zero(function: RateFunction) -> RateFunction:
def wrapper(t: float, *args: Any, **kwargs: Any) -> float:
def linear(t: float) -> float:
def smooth(t: float, inflection: float = 10.0) -> float:
def smoothstep(t: float) -> float:
def smootherstep(t: float) -> float:
def smoothererstep(t: float) -> float:
def rush_into(t: float, inflection: float = 10.0) -> float:
def rush_from(t: float, inflection: float = 10.0) -> float:
def slow_into(t: float) -> float:
def double_smooth(t: float) -> float:
def there_and_back(t: float, inflection: float = 10.0) -> float:
def there_and_back_with_pause(t: float, pause_ratio: float = 1.0 / 3) -> float:
def running_start(t: float,
    pull_factor: float = -0.5,
) -> float:
def not_quite_there(func: RateFunction = smooth,
    proportion: float = 0.7,
) -> RateFunction:
def result(t: float, *args: Any, **kwargs: Any) -> float:
def wiggle(t: float, wiggles: float = 2) -> float:
def squish_rate_func(func: RateFunction,
    a: float = 0.4,
    b: float = 0.6,
) -> RateFunction:
def result(t: float, *args: Any, **kwargs: Any) -> float:
def lingering(t: float) -> float:
def identity(t: float) -> float:
def exponential_decay(t: float, half_life: float = 0.1) -> float:
def ease_in_sine(t: float) -> float:
def ease_out_sine(t: float) -> float:
def ease_in_out_sine(t: float) -> float:
def ease_in_quad(t: float) -> float:
def ease_out_quad(t: float) -> float:
def ease_in_out_quad(t: float) -> float:
def ease_in_cubic(t: float) -> float:
def ease_out_cubic(t: float) -> float:
def ease_in_out_cubic(t: float) -> float:
def ease_in_quart(t: float) -> float:
def ease_out_quart(t: float) -> float:
def ease_in_out_quart(t: float) -> float:
def ease_in_quint(t: float) -> float:
def ease_out_quint(t: float) -> float:
def ease_in_out_quint(t: float) -> float:
def ease_in_expo(t: float) -> float:
def ease_out_expo(t: float) -> float:
def ease_in_out_expo(t: float) -> float:
def ease_in_circ(t: float) -> float:
def ease_out_circ(t: float) -> float:
def ease_in_out_circ(t: float) -> float:
def ease_in_back(t: float) -> float:
def ease_out_back(t: float) -> float:
def ease_in_out_back(t: float) -> float:
def ease_in_elastic(t: float) -> float:
def ease_out_elastic(t: float) -> float:
def ease_in_out_elastic(t: float) -> float:
def ease_in_bounce(t: float) -> float:
def ease_out_bounce(t: float) -> float:
def ease_in_out_bounce(t: float) -> float:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/tex.py

--------------------------------------------------

class TexTemplate:

def body(self) -> str:
def body(self, value: str) -> None:
def from_file(cls, file: StrPath = "tex_template.tex", **kwargs: Any) -> Self:
def add_to_preamble(self, txt: str, prepend: bool = False) -> Self:
def add_to_document(self, txt: str) -> Self:
def get_texcode_for_expression(self, expression: str) -> str:
def get_texcode_for_expression_in_env(self, expression: str, environment: str
) -> str:
def copy(self) -> Self:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/paths.py

def straight_path() -> PathFuncType:
def path_along_circles(arc_angle: float, circles_centers: np.ndarray, axis: Vector3D = OUT
) -> PathFuncType:
def path(start_points: Point3D_Array, end_points: Point3D_Array, alpha: float
) -> Point3D_Array:
def path_along_arc(arc_angle: float, axis: Vector3D = OUT) -> PathFuncType:
def path(start_points: Point3D_Array, end_points: Point3D_Array, alpha: float
) -> Point3D_Array:
def clockwise_path() -> PathFuncType:
def counterclockwise_path() -> PathFuncType:
def spiral_path(angle: float, axis: Vector3D = OUT) -> PathFuncType:
def path(start_points: Point3D_Array, end_points: Point3D_Array, alpha: float
) -> Point3D_Array:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/ipython_magic.py

--------------------------------------------------

class ManimMagic(Magics):

def manim(self,
    line: str,
    cell: str | None = None,
    local_ns: dict[str, Any] | None = None,
) -> None:
def add_additional_args(self, args: list[str]) -> list[str]:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/deprecation.py

def deprecated(func: Callable[..., T],
    since: str | None = None,
    until: str | None = None,
    replacement: str | None = None,
    message: str | None = "",
) -> Callable[..., T]:
def deprecated(func: None = None,
    since: str | None = None,
    until: str | None = None,
    replacement: str | None = None,
    message: str | None = "",
) -> Callable[[Callable[..., T]], Callable[..., T]]:
def deprecated(func: Callable[..., T] | None = None,
    since: str | None = None,
    until: str | None = None,
    replacement: str | None = None,
    message: str | None = "",
) -> Callable[..., T] | Callable[[Callable[..., T]], Callable[..., T]]:
def warning_msg(for_docs: bool = False) -> str:
def deprecate_docs(func: Callable) -> None:
def deprecate(func: Callable[..., T], *args: Any, **kwargs: Any) -> T:
def deprecated_params(params: str | Iterable[str] | None = None,
    since: str | None = None,
    until: str | None = None,
    message: str = "",
    redirections: None
    | (Iterable[tuple[str, str] | Callable[..., dict[str, Any]]]) = None,
) -> Callable[..., T]:
def warning_msg(func: Callable[..., T], used: list[str]) -> str:
def redirect_params(kwargs: dict[str, Any], used: list[str]) -> None:
def deprecate_params(func: Callable[..., T], *args: Any, **kwargs: Any) -> T:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/bezier.py

def bezier(points: BezierPointsLike,
) -> Callable[[float | ColVector], Point3D | Point3D_Array]:
def bezier(points: Sequence[Point3DLike_Array],
) -> Callable[[float | ColVector], Point3D_Array]:
def bezier(points: Point3D_Array | Sequence[Point3D_Array],
) -> Callable[[float | ColVector], Point3D_Array]:
def zero_bezier(t: float | ColVector) -> Point3D | Point3D_Array:
def linear_bezier(t: float | ColVector) -> Point3D | Point3D_Array:
def quadratic_bezier(t: float | ColVector) -> Point3D | Point3D_Array:
def cubic_bezier(t: float | ColVector) -> Point3D | Point3D_Array:
def nth_grade_bezier(t: float | ColVector) -> Point3D | Point3D_Array:
def partial_bezier_points(points: BezierPointsLike, a: float, b: float) -> BezierPoints:
def split_bezier(points: BezierPointsLike, t: float) -> Spline:
def subdivide_bezier(points: BezierPointsLike, n_divisions: int) -> Spline:
def bezier_remap(bezier_tuples: BezierPointsLike_Array,
    new_number_of_curves: int,
) -> BezierPoints_Array:
def interpolate(start: float, end: float, alpha: float) -> float:
def interpolate(start: float, end: float, alpha: ColVector) -> ColVector:
def interpolate(start: Point3D, end: Point3D, alpha: float) -> Point3D:
def interpolate(start: Point3D, end: Point3D, alpha: ColVector) -> Point3D_Array:
def interpolate(start: float | Point3D,
    end: float | Point3D,
    alpha: float | ColVector,
) -> float | ColVector | Point3D | Point3D_Array:
def integer_interpolate(start: float,
    end: float,
    alpha: float,
) -> tuple[int, float]:
def mid(start: float, end: float) -> float:
def mid(start: Point3D, end: Point3D) -> Point3D:
def mid(start: float | Point3D, end: float | Point3D) -> float | Point3D:
def inverse_interpolate(start: float, end: float, value: float) -> float:
def inverse_interpolate(start: float, end: float, value: Point3D) -> Point3D:
def inverse_interpolate(start: Point3D, end: Point3D, value: Point3D) -> Point3D:
def inverse_interpolate(start: float | Point3D,
    end: float | Point3D,
    value: float | Point3D,
) -> float | Point3D:
def match_interpolate(new_start: float,
    new_end: float,
    old_start: float,
    old_end: float,
    old_value: float,
) -> float:
def match_interpolate(new_start: float,
    new_end: float,
    old_start: float,
    old_end: float,
    old_value: Point3D,
) -> Point3D:
def match_interpolate(new_start: float,
    new_end: float,
    old_start: float,
    old_end: float,
    old_value: float | Point3D,
) -> float | Point3D:
def get_smooth_cubic_bezier_handle_points(anchors: Point3DLike_Array,
) -> tuple[Point3D_Array, Point3D_Array]:
def get_smooth_closed_cubic_bezier_handle_points(anchors: Point3DLike_Array,
) -> tuple[Point3D_Array, Point3D_Array]:
def get_smooth_open_cubic_bezier_handle_points(anchors: Point3DLike_Array,
) -> tuple[Point3D_Array, Point3D_Array]:
def get_quadratic_approximation_of_cubic(a0: Point3DLike, h0: Point3DLike, h1: Point3DLike, a1: Point3DLike
) -> QuadraticSpline:
def get_quadratic_approximation_of_cubic(a0: Point3DLike_Array,
    h0: Point3DLike_Array,
    h1: Point3DLike_Array,
    a1: Point3DLike_Array,
) -> QuadraticBezierPath:
def get_quadratic_approximation_of_cubic(a0: Point3D | Point3D_Array,
    h0: Point3D | Point3D_Array,
    h1: Point3D | Point3D_Array,
    a1: Point3D | Point3D_Array,
) -> QuadraticSpline | QuadraticBezierPath:
def is_closed(points: Point3D_Array) -> bool:
def proportions_along_bezier_curve_for_point(point: Point3DLike,
    control_points: BezierPointsLike,
    round_to: float = 1e-6,
) -> MatrixMN:
def point_lies_on_bezier(point: Point3DLike,
    control_points: BezierPointsLike,
    round_to: float = 1e-6,
) -> bool:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/simple_functions.py

def binary_search(function: Callable[[float], float],
    target: float,
    lower_bound: float,
    upper_bound: float,
    tolerance: float = 1e-4,
) -> float | None:
def choose(n: int, k: int) -> int:
--------------------------------------------------

class Comparable(Protocol):

--------------------------------------------------

def clip(a: ComparableT, min_a: ComparableT, max_a: ComparableT) -> ComparableT:
def sigmoid(x: float) -> float:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/file_ops.py

def is_mp4_format() -> bool:
def is_gif_format() -> bool:
def is_webm_format() -> bool:
def is_mov_format() -> bool:
def is_png_format() -> bool:
def write_to_movie() -> bool:
def ensure_executable(path_to_exe: Path) -> bool:
def add_extension_if_not_present(file_name: Path, extension: str) -> Path:
def add_version_before_extension(file_name: Path) -> Path:
def guarantee_existence(path: Path) -> Path:
def guarantee_empty_existence(path: Path) -> Path:
def seek_full_path_from_defaults(file_name: StrPath, default_dir: Path, extensions: list[str]
) -> Path:
def modify_atime(file_path: str) -> None:
def open_file(file_path: Path, in_browser: bool = False) -> None:
def open_media_file(file_writer: SceneFileWriter) -> None:
def get_template_names() -> list[str]:
def get_template_path() -> Path:
def add_import_statement(file: Path) -> None:
def copy_template_files(project_dir: Path = Path("."), template_name: str = "Default"
) -> None:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/space_ops.py

def norm_squared(v: float) -> float:
def cross(v1: Vector3D, v2: Vector3D) -> Vector3D:
def quaternion_mult(*quats: Sequence[float],
) -> np.ndarray | list[float | np.ndarray]:
def quaternion_from_angle_axis(angle: float,
    axis: np.ndarray,
    axis_normalized: bool = False,
) -> list[float]:
def angle_axis_from_quaternion(quaternion: Sequence[float]) -> Sequence[float]:
def quaternion_conjugate(quaternion: Sequence[float]) -> np.ndarray:
def rotate_vector(vector: np.ndarray, angle: float, axis: np.ndarray = OUT
) -> np.ndarray:
def thick_diagonal(dim: int, thickness: int = 2) -> MatrixMN:
def rotation_matrix_transpose_from_quaternion(quat: np.ndarray) -> list[np.ndarray]:
def rotation_matrix_from_quaternion(quat: np.ndarray) -> np.ndarray:
def rotation_matrix_transpose(angle: float, axis: np.ndarray) -> np.ndarray:
def rotation_matrix(angle: float,
    axis: np.ndarray,
    homogeneous: bool = False,
) -> np.ndarray:
def rotation_about_z(angle: float) -> np.ndarray:
def z_to_vector(vector: np.ndarray) -> np.ndarray:
def angle_of_vector(vector: Sequence[float] | np.ndarray) -> float:
def angle_between_vectors(v1: np.ndarray, v2: np.ndarray) -> float:
def normalize(vect: np.ndarray | tuple[float], fall_back: np.ndarray | None = None
) -> np.ndarray:
def normalize_along_axis(array: np.ndarray, axis: np.ndarray) -> np.ndarray:
def get_unit_normal(v1: Vector3D, v2: Vector3D, tol: float = 1e-6) -> Vector3D:
def compass_directions(n: int = 4, start_vect: np.ndarray = RIGHT) -> np.ndarray:
def regular_vertices(n: int, *, radius: float = 1, start_angle: float | None = None
) -> tuple[np.ndarray, float]:
def complex_to_R3(complex_num: complex) -> np.ndarray:
def R3_to_complex(point: Sequence[float]) -> np.ndarray:
def complex_func_to_R3_func(complex_func: Callable[[complex], complex],
) -> Callable[[Point3DLike], Point3D]:
def center_of_mass(points: PointNDLike_Array) -> PointND:
def midpoint(point1: Sequence[float],
    point2: Sequence[float],
) -> float | np.ndarray:
def line_intersection(line1: Sequence[np.ndarray], line2: Sequence[np.ndarray]
) -> np.ndarray:
def find_intersection(p0s: Point3DLike_Array,
    v0s: Vector3D_Array,
    p1s: Point3DLike_Array,
    v1s: Vector3D_Array,
    threshold: float = 1e-5,
) -> list[Point3D]:
def get_winding_number(points: Sequence[np.ndarray]) -> float:
def shoelace(x_y: Point2D_Array) -> float:
def shoelace_direction(x_y: Point2D_Array) -> str:
def cross2d(a: Vector2D | Vector2D_Array,
    b: Vector2D | Vector2D_Array,
) -> ManimFloat | npt.NDArray[ManimFloat]:
def earclip_triangulation(verts: np.ndarray, ring_ends: list) -> list:
def cartesian_to_spherical(vec: Sequence[float]) -> np.ndarray:
def spherical_to_cartesian(spherical: Sequence[float]) -> np.ndarray:
def perpendicular_bisector(line: Sequence[np.ndarray],
    norm_vector: Vector3D = OUT,
) -> Sequence[np.ndarray]:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/polylabel.py

--------------------------------------------------

class Polygon:

def compute_distance(self, point: Point2DLike) -> float:
def inside(self, point: Point2DLike) -> bool:
--------------------------------------------------

--------------------------------------------------

class Cell:

--------------------------------------------------

def polylabel(rings: Sequence[Point3DLike_Array], precision: float = 0.01) -> Cell:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/config_ops.py

def merge_dicts_recursively(*dicts: dict[Any, Any]) -> dict[Any, Any]:
def update_dict_recursively(current_dict: dict[Any, Any], *others: dict[Any, Any]
) -> None:
--------------------------------------------------

class DictAsObject:

--------------------------------------------------

--------------------------------------------------

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/opengl.py

def matrix_to_shader_input(matrix: MatrixMN) -> FlattenedMatrix4x4:
def orthographic_projection_matrix(width: float | None = None,
    height: float | None = None,
    near: float = 1,
    far: float = depth + 1,
    format_: bool = True,
) -> MatrixMN | FlattenedMatrix4x4:
def perspective_projection_matrix(width: float | None = None,
    height: float | None = None,
    near: float = 2,
    far: float = 50,
    format_: bool = True,
) -> MatrixMN | FlattenedMatrix4x4:
def translation_matrix(x: float = 0, y: float = 0, z: float = 0) -> MatrixMN:
def x_rotation_matrix(x: float = 0) -> MatrixMN:
def y_rotation_matrix(y: float = 0) -> MatrixMN:
def z_rotation_matrix(z: float = 0) -> MatrixMN:
def rotate_in_place_matrix(initial_position: Point3D, x: float = 0, y: float = 0, z: float = 0
) -> MatrixMN:
def rotation_matrix(x: float = 0, y: float = 0, z: float = 0) -> MatrixMN:
def scale_matrix(scale_factor: float = 1) -> npt.NDArray:
def view_matrix(translation: Point3D | None = None,
    x_rotation: float = 0,
    y_rotation: float = 0,
    z_rotation: float = 0,
) -> MatrixMN:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/module_ops.py

def get_module(file_name: Path) -> types.ModuleType:
def get_scene_classes_from_module(module: types.ModuleType) -> list[type[Scene]]:
def is_child_scene(obj: Any, module: types.ModuleType) -> bool:
def get_scenes_to_render(scene_classes: list[type[Scene]]) -> list[type[Scene]]:
def prompt_user_for_choice(scene_classes: list[type[Scene]]) -> list[type[Scene]]:
def scene_classes_from_file(file_path: Path, require_single_scene: bool, full_list: Literal[True]
) -> list[type[Scene]]:
def scene_classes_from_file(file_path: Path,
    require_single_scene: Literal[True],
    full_list: Literal[False] = False,
) -> type[Scene]:
def scene_classes_from_file(file_path: Path,
    require_single_scene: Literal[False] = False,
    full_list: Literal[False] = False,
) -> list[type[Scene]]:
def scene_classes_from_file(file_path: Path, require_single_scene: bool = False, full_list: bool = False
) -> type[Scene] | list[type[Scene]]:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/caching.py

def handle_caching_play(func: Callable[..., None]) -> Callable[..., None]:
def wrapper(self: OpenGLRenderer, scene: Scene, *args: Any, **kwargs: Any) -> None:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/debug.py

def print_family(mobject: Mobject, n_tabs: int = 0) -> None:
def index_labels(mobject: Mobject,
    label_height: float = 0.15,
    background_stroke_width: float = 5,
    background_stroke_color: ManimColor = BLACK,
    **kwargs: Any,
) -> VGroup:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/unit.py

--------------------------------------------------

--------------------------------------------------

class Percent:

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/images.py

def get_full_raster_image_path(image_file_name: str | PurePath) -> Path:
def get_full_vector_image_path(image_file_name: str | PurePath) -> Path:
def drag_pixels(frames: list[np.array]) -> list[np.array]:
def invert_image(image: np.array) -> Image:
def change_to_rgba_array(image: RGBPixelArray, dtype: str = "uint8") -> RGBPixelArray:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/family.py

def extract_mobject_family_members(mobjects: Iterable[Mobject],
    use_z_index: bool = False,
    only_those_with_points: bool = False,
) -> list[Mobject]:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/exceptions.py

--------------------------------------------------

class EndSceneEarlyException(Exception):

--------------------------------------------------

--------------------------------------------------

class RerunSceneException(Exception):

--------------------------------------------------

--------------------------------------------------

class MultiAnimationOverrideException(Exception):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/qhull.py

--------------------------------------------------

class QuickHullPoint:

--------------------------------------------------

--------------------------------------------------

class SubFacet:

--------------------------------------------------

--------------------------------------------------

class Facet:

def compute_normal(self, internal: PointND) -> PointND:
--------------------------------------------------

--------------------------------------------------

class Horizon:

--------------------------------------------------

--------------------------------------------------

class QuickHull:

def initialize(self, points: PointND_Array) -> None:
def classify(self, facet: Facet) -> None:
def compute_horizon(self, eye: PointND, start_facet: Facet) -> Horizon:
def build(self, points: PointND_Array) -> None:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/tex_templates.py

--------------------------------------------------

class TexTemplateLibrary:

--------------------------------------------------

--------------------------------------------------

class TexFontTemplates:

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/family_ops.py

def extract_mobject_family_members(mobject_list: list[Mobject], only_those_with_points: bool = False
) -> list[Mobject]:
def restructure_list_to_exclude_certain_family_members(mobject_list: list[Mobject], to_remove: list[Mobject]
) -> list[Mobject]:
def add_safe_mobjects_from_list(list_to_examine: list[Mobject], set_to_remove: set[Mobject]
) -> None:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/commands.py

def capture(command: str, cwd: StrOrBytesPath | None = None, command_input: str | None = None
) -> tuple[str, str, int]:
--------------------------------------------------

class VideoMetadata(TypedDict):

--------------------------------------------------

def get_video_metadata(path_to_video: str | os.PathLike) -> VideoMetadata:
def get_dir_layout(dirpath: Path) -> Generator[str, None, None]:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/hashing.py

def reset_already_processed(cls):
def check_already_processed_decorator(cls: _Memoizer, is_method: bool = False):
def layer(func):
def check_already_processed(cls, obj: Any) -> Any:
def mark_as_processed(cls, obj: Any) -> None:
--------------------------------------------------

def default(self, obj: Any):
def encode(self, obj: Any):
--------------------------------------------------

def get_json(obj: dict):
def get_hash_from_play_call(scene_object: Scene,
    camera_object: Camera | OpenGLCamera,
    animations_list: typing.Iterable[Animation],
    current_mobjects_list: typing.Iterable[Mobject],
) -> str:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/parameter_parsing.py

def flatten_iterable_parameters(args: Iterable[T | Iterable[T] | GeneratorType],
) -> list[T]:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/iterables.py

def adjacent_n_tuples(objects: Sequence[T], n: int) -> zip[tuple[T, ...]]:
def adjacent_pairs(objects: Sequence[T]) -> zip[tuple[T, ...]]:
def all_elements_are_instances(iterable: Iterable[object], Class: type[object]) -> bool:
def batch_by_property(items: Iterable[T], property_func: Callable[[T], U]
) -> list[tuple[list[T], U | None]]:
def concatenate_lists(*list_of_lists: Iterable[T]) -> list[T]:
def list_difference_update(l1: Iterable[T], l2: Iterable[T]) -> list[T]:
def list_update(l1: Iterable[T], l2: Iterable[T]) -> list[T]:
def listify(obj: str) -> list[str]:
def listify(obj: Iterable[T]) -> list[T]:
def listify(obj: T) -> list[T]:
def listify(obj: str | Iterable[T] | T) -> list[str] | list[T]:
def make_even(iterable_1: Iterable[T], iterable_2: Iterable[U]
) -> tuple[list[T], list[U]]:
def make_even_by_cycling(iterable_1: Collection[T], iterable_2: Collection[U]
) -> tuple[list[T], list[U]]:
def remove_list_redundancies(lst: Reversible[H]) -> list[H]:
def remove_nones(sequence: Iterable[T | None]) -> list[T]:
def resize_array(nparray: npt.NDArray[F], length: int) -> npt.NDArray[F]:
def resize_preserving_order(nparray: npt.NDArray[np.float64], length: int
) -> npt.NDArray[np.float64]:
def resize_with_interpolation(nparray: npt.NDArray[F], length: int) -> npt.NDArray[F]:
def stretch_array_to_length(nparray: npt.NDArray[F], length: int) -> npt.NDArray[F]:
def tuplify(obj: str) -> tuple[str]:
def tuplify(obj: Iterable[T]) -> tuple[T]:
def tuplify(obj: T) -> tuple[T]:
def tuplify(obj: str | Iterable[T] | T) -> tuple[str] | tuple[T]:
def uniq_chain(*args: Iterable[T]) -> Generator[T, None, None]:
def hash_obj(obj: object) -> int:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/tex_file_writing.py

def tex_hash(expression: Any) -> str:
def tex_to_svg_file(expression: str,
    environment: str | None = None,
    tex_template: TexTemplate | None = None,
) -> Path:
def generate_tex_file(expression: str,
    environment: str | None = None,
    tex_template: TexTemplate | None = None,
) -> Path:
def make_tex_compilation_command(tex_compiler: str, output_format: str, tex_file: Path, tex_dir: Path
) -> list[str]:
def insight_inputenc_error(matching: Match[str]) -> Generator[str]:
def insight_package_not_found_error(matching: Match[str]) -> Generator[str]:
def compile_tex(tex_file: Path, tex_compiler: str, output_format: str) -> Path:
def convert_to_svg(dvi_file: Path, extension: str, page: int = 1) -> Path:
def delete_nonsvg_files(additional_endings: Iterable[str] = ()) -> None:
def print_all_tex_errors(log_file: Path, tex_compiler: str, tex_file: Path) -> None:
def print_tex_error(tex_compilation_log: Sequence[str],
    error_start_index: int,
    tex_source: Sequence[str],
) -> None:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/color/DVIPSNAMES.py


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/color/SVGNAMES.py


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/color/core.py

--------------------------------------------------

class ManimColor:

def to_integer(self) -> int:
def to_rgb(self) -> RGB_Array_Float:
def to_int_rgb(self) -> RGB_Array_Int:
def to_rgba(self) -> RGBA_Array_Float:
def to_int_rgba(self) -> RGBA_Array_Int:
def to_rgba_with_alpha(self, alpha: float) -> RGBA_Array_Float:
def to_int_rgba_with_alpha(self, alpha: float) -> RGBA_Array_Int:
def to_hex(self, with_alpha: bool = False) -> str:
def to_hsv(self) -> HSV_Array_Float:
def to_hsl(self) -> HSL_Array_Float:
def invert(self, with_alpha: bool = False) -> Self:
def interpolate(self, other: Self, alpha: float) -> Self:
def darker(self, blend: float = 0.2) -> Self:
def lighter(self, blend: float = 0.2) -> Self:
def contrasting(self,
    threshold: float = 0.5,
    light: Self | None = None,
    dark: Self | None = None,
) -> Self:
def opacity(self, opacity: float) -> Self:
def into(self, class_type: type[ManimColorT]) -> ManimColorT:
def from_rgb(cls,
    rgb: RGB_Array_Float | RGB_Tuple_Float | RGB_Array_Int | RGB_Tuple_Int,
    alpha: float = 1.0,
) -> Self:
def from_rgba(cls, rgba: RGBA_Array_Float | RGBA_Tuple_Float | RGBA_Array_Int | RGBA_Tuple_Int
) -> Self:
def from_hex(cls, hex_str: str, alpha: float = 1.0) -> Self:
def from_hsv(cls, hsv: HSV_Array_Float | HSV_Tuple_Float, alpha: float = 1.0
) -> Self:
def from_hsl(cls, hsl: HSL_Array_Float | HSL_Tuple_Float, alpha: float = 1.0
) -> Self:
def parse(cls,
    color: ParsableManimColor | None,
    alpha: float = ...,
) -> Self:
def parse(cls,
    color: Sequence[ParsableManimColor],
    alpha: float = ...,
) -> list[Self]:
def parse(cls,
    color: ParsableManimColor | Sequence[ParsableManimColor] | None,
    alpha: float = 1.0,
) -> Self | list[Self]:
def is_sequence(color: ParsableManimColor | Sequence[ParsableManimColor] | None,
) -> TypeIs[Sequence[ParsableManimColor]]:
def gradient(colors: list[ManimColor], length: int
) -> ManimColor | list[ManimColor]:
--------------------------------------------------

--------------------------------------------------

class HSV(ManimColor):

def hue(self) -> float:
def hue(self, hue: float) -> None:
def saturation(self) -> float:
def saturation(self, saturation: float) -> None:
def value(self) -> float:
def value(self, value: float) -> None:
def h(self) -> float:
def h(self, hue: float) -> None:
def s(self) -> float:
def s(self, saturation: float) -> None:
def v(self) -> float:
def v(self, value: float) -> None:
--------------------------------------------------

def color_to_rgb(color: ParsableManimColor) -> RGB_Array_Float:
def color_to_rgba(color: ParsableManimColor, alpha: float = 1.0) -> RGBA_Array_Float:
def color_to_int_rgb(color: ParsableManimColor) -> RGB_Array_Int:
def color_to_int_rgba(color: ParsableManimColor, alpha: float = 1.0) -> RGBA_Array_Int:
def rgb_to_color(rgb: RGB_Array_Float | RGB_Tuple_Float | RGB_Array_Int | RGB_Tuple_Int,
) -> ManimColor:
def rgba_to_color(rgba: RGBA_Array_Float | RGBA_Tuple_Float | RGBA_Array_Int | RGBA_Tuple_Int,
) -> ManimColor:
def rgb_to_hex(rgb: RGB_Array_Float | RGB_Tuple_Float | RGB_Array_Int | RGB_Tuple_Int,
) -> str:
def hex_to_rgb(hex_code: str) -> RGB_Array_Float:
def invert_color(color: ManimColorT) -> ManimColorT:
def color_gradient(reference_colors: Sequence[ParsableManimColor],
    length_of_output: int,
) -> list[ManimColor] | ManimColor:
def interpolate_color(color1: ManimColorT, color2: ManimColorT, alpha: float
) -> ManimColorT:
def average_color(*colors: ParsableManimColor) -> ManimColor:
def random_bright_color() -> ManimColor:
def random_color() -> ManimColor:
def get_shaded_rgb(rgb: RGB_Array_Float,
    point: Point3D,
    unit_normal_vect: Vector3D,
    light_source: Point3D,
) -> RGB_Array_Float:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/color/AS2700.py


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/color/manim_colors.py


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/color/BS381.py


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/color/XKCD.py


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/color/X11.py


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/testing/_test_class_makers.py

def construct(self) -> None:
--------------------------------------------------

--------------------------------------------------

--------------------------------------------------

class DummySceneFileWriter(SceneFileWriter):

def init_output_directories(self, scene_name: StrPath) -> None:
def add_partial_movie_file(self, hash_animation: str) -> None:
def begin_animation(self, allow_write: bool = True, file_path: StrPath | None = None
) -> Any:
def end_animation(self, allow_write: bool = False) -> None:
def combine_to_movie(self) -> None:
def combine_to_section_videos(self) -> None:
def clean_cache(self) -> None:
def write_frame(self, frame_or_renderer: PixelArray | OpenGLRenderer, num_frames: int = 1
) -> None:
--------------------------------------------------

--------------------------------------------------

class TestSceneFileWriter(DummySceneFileWriter):

def write_frame(self, frame_or_renderer: PixelArray | OpenGLRenderer, num_frames: int = 1
) -> None:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/testing/frames_comparison.py

def frames_comparison(func: Callable | None = None,
    *,
    last_frame: bool = True,
    renderer_class: type[CairoRenderer | OpenGLRenderer] = CairoRenderer,
    base_scene: type[Scene] = Scene,
    **custom_config: Any,
) -> Callable:
def decorator_maker(tested_scene_construct: Callable) -> Callable:
def wrapper(*args: Any, request: FixtureRequest, tmp_path: StrPath, **kwargs: Any
) -> None:
def real_test() -> None:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/testing/_show_diff.py

def show_diff_helper(frame_number: int,
    frame_data: PixelArray,
    expected_frame_data: PixelArray,
    control_data_filename: str,
) -> None:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/testing/_frames_testers.py

def testing(self) -> Generator[None, None, None]:
def check_frame(self, frame_number: int, frame: PixelArray) -> None:
--------------------------------------------------

def check_frame(self, index: int, frame: PixelArray) -> None:
def testing(self) -> Generator[None, None, None]:
def save_contol_data(self) -> None:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/docbuild/autoaliasattr_directive.py

def smart_replace(base: str, alias: str, substitution: str) -> str:
def condition(char: str) -> bool:
def setup(app: Sphinx) -> None:
--------------------------------------------------

class AliasAttrDocumenter(Directive):

def run(self) -> list[nodes.Element]:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/docbuild/autocolor_directive.py

def setup(app: Sphinx) -> None:
--------------------------------------------------

class ManimColorModuleDocumenter(Directive):

def add_directive_header(self, sig: str) -> None:
def run(self) -> list[nodes.Element]:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/docbuild/manim_directive.py

--------------------------------------------------

class SetupMetadata(TypedDict):

--------------------------------------------------

--------------------------------------------------

class SkipManimNode(nodes,nodes):

--------------------------------------------------

def visit(self: SkipManimNode, node: nodes.Element, name: str = "") -> None:
def depart(self: SkipManimNode, node: nodes.Element) -> None:
def process_name_list(option_input: str, reference_type: str) -> list[str]:
--------------------------------------------------

class ManimDirective(Directive):

def run(self) -> list[nodes.Element]:
--------------------------------------------------

def setup(app: Sphinx) -> SetupMetadata:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/utils/docbuild/module_parsing.py

def parse_module_attributes() -> tuple[AliasDocsDict, DataDict, TypeVarDict]:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/cli/default_group.py

--------------------------------------------------

class DefaultGroup(cloup):

def set_default_command(self, command: Command) -> None:
def parse_args(self, ctx: Context, args: list[str]) -> list[str]:
def get_command(self, ctx: Context, cmd_name: str) -> Command | None:
def resolve_command(self, ctx: Context, args: list[str]
) -> tuple[str | None, Command | None, list[str]]:
def command(self, *args: Any, **kwargs: Any
) -> Callable[[Callable[..., object]], Command]:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/cli/init/commands.py

def select_resolution() -> tuple[int, int]:
def update_cfg(cfg_dict: dict[str, Any], project_cfg_path: Path) -> None:
def project(default_settings: bool, **kwargs: Any) -> None:
def scene(**kwargs: Any) -> None:
def init(ctx: cloup.Context) -> None:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/cli/plugins/commands.py

def plugins(list_available: bool) -> None:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/cli/render/render_options.py

def validate_scene_range(ctx: Context, param: Option, value: str | None
) -> tuple[int] | tuple[int, int] | None:
def validate_resolution(ctx: Context, param: Option, value: str | None
) -> tuple[int, int] | None:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/cli/render/global_options.py

def validate_gui_location(ctx: Context, param: Option, value: str | None
) -> tuple[int, int] | None:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/cli/render/ease_of_access_options.py


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/cli/render/output_options.py


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/cli/render/commands.py

--------------------------------------------------

class ClickArgs(Namespace):

--------------------------------------------------

def render(**kwargs: Any) -> ClickArgs | dict[str, Any]:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/cli/cfg/group.py

def value_from_string(value: str) -> str | int | bool:
def is_valid_style(style: str) -> bool:
def replace_keys(default: dict[str, Any]) -> dict[str, Any]:
def cfg(ctx: cloup.Context) -> None:
def write(level: str | None = None, openfile: bool = False) -> None:
def show() -> None:
def export(ctx: cloup.Context, directory: str) -> None:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/cli/checkhealth/checks.py

--------------------------------------------------

class HealthCheckFunction(Protocol):

--------------------------------------------------

def healthcheck(description: str,
    recommendation: str,
    skip_on_failed: list[HealthCheckFunction | str] | None = None,
    post_fail_fix_hook: Callable[..., object] | None = None,
) -> Callable[[Callable[[], bool]], HealthCheckFunction]:
def wrapper(func: Callable[[], bool]) -> HealthCheckFunction:
def is_manim_on_path() -> bool:
def is_manim_executable_associated_to_this_library() -> bool:
def is_latex_available() -> bool:
def is_dvisvgm_available() -> bool:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/cli/checkhealth/commands.py

def checkhealth() -> None:
--------------------------------------------------

class CheckHealthDemo(mn):

def construct(self) -> None:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/gui/gui.py

def configure_pygui(renderer, widgets, update=True):
def rerun_callback(sender, data):
def continue_callback(sender, data):
def scene_selection_callback(sender, data):

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/scene/zoomed_scene.py

--------------------------------------------------

class ZoomedScene(MovingCameraScene):

def setup(self):
def activate_zooming(self, animate: bool = False):
def get_zoom_in_animation(self, run_time: float = 2, **kwargs):
def get_zoomed_display_pop_out_animation(self, **kwargs):
def get_zoom_factor(self):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/scene/three_d_scene.py

--------------------------------------------------

class ThreeDScene(Scene):

def set_camera_orientation(self,
    phi: float | None = None,
    theta: float | None = None,
    gamma: float | None = None,
    zoom: float | None = None,
    focal_distance: float | None = None,
    frame_center: Mobject | Sequence[float] | None = None,
    **kwargs,
):
def begin_ambient_camera_rotation(self, rate: float = 0.02, about: str = "theta"):
def stop_ambient_camera_rotation(self, about="theta"):
def begin_3dillusion_camera_rotation(self,
    rate: float = 1,
    origin_phi: float | None = None,
    origin_theta: float | None = None,
):
def update_theta(m, dt):
def update_phi(m, dt):
def stop_3dillusion_camera_rotation(self):
def move_camera(self,
    phi: float | None = None,
    theta: float | None = None,
    gamma: float | None = None,
    zoom: float | None = None,
    focal_distance: float | None = None,
    frame_center: Mobject | Sequence[float] | None = None,
    added_anims: Iterable[Animation] = [],
    **kwargs,
):
def get_moving_mobjects(self, *animations: Animation):
def add_fixed_orientation_mobjects(self, *mobjects: Mobject, **kwargs):
def add_fixed_in_frame_mobjects(self, *mobjects: Mobject):
def remove_fixed_orientation_mobjects(self, *mobjects: Mobject):
def remove_fixed_in_frame_mobjects(self, *mobjects: Mobject):
def set_to_default_angled_camera_orientation(self, **kwargs):
--------------------------------------------------

--------------------------------------------------

class SpecialThreeDScene(ThreeDScene):

def get_axes(self):
def get_sphere(self, **kwargs):
def get_default_camera_position(self):
def set_camera_to_default_position(self):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/scene/scene_file_writer.py

def to_av_frame_rate(fps):
def convert_audio(input_path: Path, output_path: Path, codec_name: str):
--------------------------------------------------

class SceneFileWriter:

def init_output_directories(self, scene_name: StrPath) -> None:
def finish_last_section(self) -> None:
def next_section(self, name: str, type_: str, skip_animations: bool) -> None:
def add_partial_movie_file(self, hash_animation: str):
def get_resolution_directory(self):
def init_audio(self):
def create_audio_segment(self):
def add_audio_segment(self,
    new_segment: AudioSegment,
    time: float | None = None,
    gain_to_background: float | None = None,
):
def add_sound(self,
    sound_file: str,
    time: float | None = None,
    gain: float | None = None,
    **kwargs,
):
def begin_animation(self, allow_write: bool = False, file_path: StrPath | None = None
) -> None:
def end_animation(self, allow_write: bool = False) -> None:
def listen_and_write(self):
def encode_and_write_frame(self, frame: PixelArray, num_frames: int) -> None:
def write_frame(self, frame_or_renderer: np.ndarray | OpenGLRenderer, num_frames: int = 1
):
def output_image(self, image: Image.Image, target_dir, ext, zero_pad: bool):
def save_final_image(self, image: np.ndarray):
def finish(self) -> None:
def open_partial_movie_stream(self, file_path=None) -> None:
def close_partial_movie_stream(self) -> None:
def is_already_cached(self, hash_invocation: str):
def combine_files(self,
    input_files: list[str],
    output_file: Path,
    create_gif=False,
    includes_sound=False,
):
def combine_to_movie(self):
def combine_to_section_videos(self) -> None:
def clean_cache(self):
def flush_cache_directory(self):
def write_subcaption_file(self):
def print_file_ready_message(self, file_path):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/scene/scene.py

--------------------------------------------------

class RerunSceneHandler(FileSystemEventHandler):

def on_modified(self, event):
--------------------------------------------------

--------------------------------------------------

class Scene:

def camera(self):
def time(self) -> float:
def render(self, preview: bool = False):
def setup(self):
def tear_down(self):
def construct(self):
def next_section(self,
    name: str = "unnamed",
    section_type: str = DefaultSectionType.NORMAL,
    skip_animations: bool = False,
) -> None:
def get_attrs(self, *keys: str):
def update_mobjects(self, dt: float):
def update_meshes(self, dt):
def update_self(self, dt: float):
def should_update_mobjects(self) -> bool:
def get_top_level_mobjects(self):
def is_top_level(mobject):
def get_mobject_family_members(self):
def add(self, *mobjects: Mobject):
def add_mobjects_from_animations(self, animations: list[Animation]) -> None:
def remove(self, *mobjects: Mobject):
def replace(self, old_mobject: Mobject, new_mobject: Mobject) -> None:
def replace_in_list(mobj_list: list[Mobject], old_m: Mobject, new_m: Mobject
) -> bool:
def add_updater(self, func: Callable[[float], None]) -> None:
def remove_updater(self, func: Callable[[float], None]) -> None:
def restructure_mobjects(self,
    to_remove: Sequence[Mobject],
    mobject_list_name: str = "mobjects",
    extract_families: bool = True,
):
def get_restructured_mobject_list(self, mobjects: list, to_remove: list):
def add_safe_mobjects_from_list(list_to_examine, set_to_remove):
def add_foreground_mobjects(self, *mobjects: Mobject):
def add_foreground_mobject(self, mobject: Mobject):
def remove_foreground_mobjects(self, *to_remove: Mobject):
def remove_foreground_mobject(self, mobject: Mobject):
def bring_to_front(self, *mobjects: Mobject):
def bring_to_back(self, *mobjects: Mobject):
def clear(self):
def get_moving_mobjects(self, *animations: Animation):
def get_moving_and_static_mobjects(self, animations):
def compile_animations(self,
    *args: Animation | Mobject | _AnimationBuilder,
    **kwargs,
):
def get_time_progression(self,
    run_time: float,
    description,
    n_iterations: int | None = None,
    override_skip_animations: bool = False,
):
def validate_run_time(cls,
    run_time: float,
    method: Callable[[Any, ...], Any],
    parameter_name: str = "run_time",
) -> float:
def get_run_time(self, animations: list[Animation]):
def play(self,
    *args: Animation | Mobject | _AnimationBuilder,
    subcaption=None,
    subcaption_duration=None,
    subcaption_offset=0,
    **kwargs,
):
def wait(self,
    duration: float = DEFAULT_WAIT_TIME,
    stop_condition: Callable[[], bool] | None = None,
    frozen_frame: bool | None = None,
):
def pause(self, duration: float = DEFAULT_WAIT_TIME):
def wait_until(self, stop_condition: Callable[[], bool], max_time: float = 60):
def compile_animation_data(self,
    *animations: Animation | Mobject | _AnimationBuilder,
    **play_kwargs,
):
def begin_animations(self) -> None:
def is_current_animation_frozen_frame(self) -> bool:
def play_internal(self, skip_rendering: bool = False):
def check_interactive_embed_is_valid(self):
def interactive_embed(self):
def ipython(shell, namespace):
def load_module_into_namespace(module, namespace):
def embedded_rerun(*args, **kwargs):
def get_embedded_method(method_name):
def interact(self, shell, keyboard_thread):
def embed(self):
def update_to_time(self, t):
def add_subcaption(self, content: str, duration: float = 1, offset: float = 0
) -> None:
def add_sound(self,
    sound_file: str,
    time_offset: float = 0,
    gain: float | None = None,
    **kwargs,
):
def on_mouse_motion(self, point, d_point):
def on_mouse_scroll(self, point, offset):
def on_key_press(self, symbol, modifiers):
def on_key_release(self, symbol, modifiers):
def on_mouse_drag(self, point, d_point, buttons, modifiers):
def mouse_scroll_orbit_controls(self, point, offset):
def mouse_drag_orbit_controls(self, point, d_point, buttons, modifiers):
def set_key_function(self, char, func):
def on_mouse_press(self, point, button, modifiers):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/scene/section.py

--------------------------------------------------

class DefaultSectionType(str,Enum):

--------------------------------------------------

--------------------------------------------------

class Section:

def is_empty(self) -> bool:
def get_clean_partial_movie_files(self) -> list[str]:
def get_dict(self, sections_dir: Path) -> dict[str, Any]:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/scene/vector_space_scene.py

--------------------------------------------------

class VectorScene(Scene):

def add_plane(self, animate: bool = False, **kwargs):
def add_axes(self, animate: bool = False, color: bool = WHITE, **kwargs):
def lock_in_faded_grid(self, dimness: float = 0.7, axes_dimness: float = 0.5):
def get_vector(self, numerical_vector: np.ndarray | list | tuple, **kwargs):
def add_vector(self,
    vector: Arrow | list | tuple | np.ndarray,
    color: str = YELLOW,
    animate: bool = True,
    **kwargs,
):
def write_vector_coordinates(self, vector: Arrow, **kwargs):
def get_basis_vectors(self, i_hat_color: str = X_COLOR, j_hat_color: str = Y_COLOR):
def get_basis_vector_labels(self, **kwargs):
def get_vector_label(self,
    vector: Vector,
    label,
    at_tip: bool = False,
    direction: str = "left",
    rotate: bool = False,
    color: str | None = None,
    label_scale_factor: float = LARGE_BUFF - 0.2,
):
def label_vector(self, vector: Vector, label: MathTex | str, animate: bool = True, **kwargs
):
def position_x_coordinate(self,
    x_coord,
    x_line,
    vector,
):
def position_y_coordinate(self,
    y_coord,
    y_line,
    vector,
):
def coords_to_vector(self,
    vector: np.ndarray | list | tuple,
    coords_start: np.ndarray | list | tuple = 2 * RIGHT + 2 * UP,
    clean_up: bool = True,
):
def vector_to_coords(self,
    vector: np.ndarray | list | tuple,
    integer_labels: bool = True,
    clean_up: bool = True,
):
def show_ghost_movement(self, vector: Arrow | list | tuple | np.ndarray):
--------------------------------------------------

--------------------------------------------------

class LinearTransformationScene(VectorScene):

def update_default_configs(default_configs, passed_configs):
def setup(self):
def add_special_mobjects(self, mob_list: list, *mobs_to_add: Mobject):
def add_background_mobject(self, *mobjects: Mobject):
def add_foreground_mobject(self, *mobjects: Mobject):
def add_transformable_mobject(self, *mobjects: Mobject):
def add_moving_mobject(self, mobject: Mobject, target_mobject: Mobject | None = None
):
def get_ghost_vectors(self) -> VGroup:
def get_unit_square(self, color: str = YELLOW, opacity: float = 0.3, stroke_width: float = 3
):
def add_unit_square(self, animate: bool = False, **kwargs):
def add_vector(self, vector: Arrow | list | tuple | np.ndarray, color: str = YELLOW, **kwargs
):
def write_vector_coordinates(self, vector: Arrow, **kwargs):
def add_transformable_label(self,
    vector: Vector,
    label: MathTex | str,
    transformation_name: str | MathTex = "L",
    new_label: str | MathTex | None = None,
    **kwargs,
):
def add_title(self,
    title: str | MathTex | Tex,
    scale_factor: float = 1.5,
    animate: bool = False,
):
def get_matrix_transformation(self, matrix: np.ndarray | list | tuple):
def get_transposed_matrix_transformation(self, transposed_matrix: np.ndarray | list | tuple
):
def get_piece_movement(self, pieces: list | tuple | np.ndarray):
def get_moving_mobject_movement(self, func: Callable[[np.ndarray], np.ndarray]):
def get_vector_movement(self, func: Callable[[np.ndarray], np.ndarray]):
def get_transformable_label_movement(self):
def apply_matrix(self, matrix: np.ndarray | list | tuple, **kwargs):
def apply_inverse(self, matrix: np.ndarray | list | tuple, **kwargs):
def apply_transposed_matrix(self, transposed_matrix: np.ndarray | list | tuple, **kwargs
):
def apply_inverse_transpose(self, t_matrix: np.ndarray | list | tuple, **kwargs):
def apply_nonlinear_transformation(self, function: Callable[[np.ndarray], np.ndarray], **kwargs
):
def apply_function(self,
    function: Callable[[np.ndarray], np.ndarray],
    added_anims: list = [],
    **kwargs,
):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/scene/moving_camera_scene.py

--------------------------------------------------

class MovingCameraScene(Scene):

def get_moving_mobjects(self, *animations: Animation):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/matrix.py

def matrix_to_tex_string(matrix):
def matrix_to_mobject(matrix):
--------------------------------------------------

class Matrix(VMobject):

def get_columns(self):
def set_column_colors(self, *colors: str):
def get_rows(self):
def set_row_colors(self, *colors: str):
def add_background_to_entries(self):
def get_mob_matrix(self):
def get_entries(self):
def get_brackets(self):
--------------------------------------------------

--------------------------------------------------

class DecimalMatrix(Matrix):

--------------------------------------------------

--------------------------------------------------

class IntegerMatrix(Matrix):

--------------------------------------------------

--------------------------------------------------

class MobjectMatrix(Matrix):

--------------------------------------------------

def get_det_text(matrix: Matrix,
    determinant: int | str | None = None,
    background_rect: bool = False,
    initial_scale_factor: float = 2,
):

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/vector_field.py

--------------------------------------------------

class VectorField(VGroup):

def color_scheme(p):
def pos_to_rgb(pos: np.ndarray) -> tuple[float, float, float, float]:
def shift_func(func: Callable[[np.ndarray], np.ndarray],
    shift_vector: np.ndarray,
) -> Callable[[np.ndarray], np.ndarray]:
def scale_func(func: Callable[[np.ndarray], np.ndarray],
    scalar: float,
) -> Callable[[np.ndarray], np.ndarray]:
def fit_to_coordinate_system(self, coordinate_system: CoordinateSystem):
def nudge(self,
    mob: Mobject,
    dt: float = 1,
    substeps: int = 1,
    pointwise: bool = False,
) -> VectorField:
def runge_kutta(self, p: Sequence[float], step_size: float) -> float:
def nudge_submobjects(self,
    dt: float = 1,
    substeps: int = 1,
    pointwise: bool = False,
) -> VectorField:
def get_nudge_updater(self,
    speed: float = 1,
    pointwise: bool = False,
) -> Callable[[Mobject, float], Mobject]:
def start_submobject_movement(self,
    speed: float = 1,
    pointwise: bool = False,
) -> VectorField:
def stop_submobject_movement(self) -> VectorField:
def get_colored_background_image(self, sampling_rate: int = 5) -> Image.Image:
def get_vectorized_rgba_gradient_function(self,
    start: float,
    end: float,
    colors: Iterable[ParsableManimColor],
):
def func(values, opacity=1):
--------------------------------------------------

--------------------------------------------------

class ArrowVectorField(VectorField):

def get_vector(self, point: np.ndarray):
--------------------------------------------------

--------------------------------------------------

class StreamLines(VectorField):

def outside_box(p):
def create(self,
    lag_ratio: float | None = None,
    run_time: Callable[[float], float] | None = None,
    **kwargs,
) -> AnimationGroup:
def start_animation(self,
    warm_up: bool = True,
    flow_speed: float = 1,
    time_width: float = 0.3,
    rate_func: Callable[[float], float] = linear,
    line_animation_class: type[ShowPassingFlash] = ShowPassingFlash,
    **kwargs,
) -> None:
def updater(mob, dt):
def end_animation(self) -> AnimationGroup:
def hide_and_wait(mob, alpha):
def finish_updater_cycle(line, alpha):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/graph.py

--------------------------------------------------

class LayoutFunction(Protocol):

--------------------------------------------------

def slide(v, dx):
--------------------------------------------------

class GenericGraph(VMobject):

def add_vertices(self: Graph,
    *vertices: Hashable,
    positions: dict | None = None,
    labels: bool = False,
    label_fill_color: str = BLACK,
    vertex_type: type[Mobject] = Dot,
    vertex_config: dict | None = None,
    vertex_mobjects: dict | None = None,
):
def on_finish(scene: Scene):
def remove_vertices(self, *vertices):
def add_edges(self,
    *edges: tuple[Hashable, Hashable],
    edge_type: type[Mobject] = Line,
    edge_config: dict | None = None,
    **kwargs,
):
def remove_edges(self, *edges: tuple[Hashable]):
def from_networkx(cls, nxgraph: nx.classes.graph.Graph | nx.classes.digraph.DiGraph, **kwargs
):
def change_layout(self,
    layout: LayoutName | dict[Hashable, Point3DLike] | LayoutFunction = "spring",
    layout_scale: float | tuple[float, float, float] = 2,
    layout_config: dict[str, Any] | None = None,
    partitions: list[list[Hashable]] | None = None,
    root_vertex: Hashable | None = None,
) -> Graph:
--------------------------------------------------

--------------------------------------------------

class Graph(GenericGraph):

def update_edges(self, graph):
--------------------------------------------------

--------------------------------------------------

class DiGraph(GenericGraph):

def update_edges(self, graph):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/logo.py

--------------------------------------------------

class ManimBanner(VGroup):

def scale(self, scale_factor: float, **kwargs) -> ManimBanner:
def create(self, run_time: float = 2) -> AnimationGroup:
def expand(self, run_time: float = 1.5, direction="center") -> Succession:
def shift(vector):
def slide_and_uncover(mob, alpha):
def slide_back(mob, alpha):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/utils.py

def get_mobject_class() -> type:
def get_vectorized_mobject_class() -> type:
def get_point_mobject_class() -> type:

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/frame.py

--------------------------------------------------

class ScreenRectangle(Rectangle):

def aspect_ratio(self):
def aspect_ratio(self, value):
--------------------------------------------------

--------------------------------------------------

class FullScreenRectangle(ScreenRectangle):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/table.py

--------------------------------------------------

class Table(VGroup):

def get_horizontal_lines(self) -> VGroup:
def get_vertical_lines(self) -> VGroup:
def get_columns(self) -> VGroup:
def get_rows(self) -> VGroup:
def set_column_colors(self, *colors: Iterable[ParsableManimColor]) -> Table:
def set_row_colors(self, *colors: Iterable[ParsableManimColor]) -> Table:
def get_entries(self,
    pos: Sequence[int] | None = None,
) -> VMobject | VGroup:
def get_entries_without_labels(self,
    pos: Sequence[int] | None = None,
) -> VMobject | VGroup:
def get_row_labels(self) -> VGroup:
def get_col_labels(self) -> VGroup:
def get_labels(self) -> VGroup:
def add_background_to_entries(self, color: ParsableManimColor = BLACK) -> Table:
def get_cell(self, pos: Sequence[int] = (1, 1), **kwargs) -> Polygon:
def get_highlighted_cell(self, pos: Sequence[int] = (1, 1), color: ParsableManimColor = YELLOW, **kwargs
) -> BackgroundRectangle:
def add_highlighted_cell(self, pos: Sequence[int] = (1, 1), color: ParsableManimColor = YELLOW, **kwargs
) -> Table:
def create(self,
    lag_ratio: float = 1,
    line_animation: Callable[[VMobject | VGroup], Animation] = Create,
    label_animation: Callable[[VMobject | VGroup], Animation] = Write,
    element_animation: Callable[[VMobject | VGroup], Animation] = Create,
    entry_animation: Callable[[VMobject | VGroup], Animation] = FadeIn,
    **kwargs,
) -> AnimationGroup:
def scale(self, scale_factor: float, **kwargs):
--------------------------------------------------

--------------------------------------------------

class MathTable(Table):

--------------------------------------------------

--------------------------------------------------

class MobjectTable(Table):

--------------------------------------------------

--------------------------------------------------

class IntegerTable(Table):

--------------------------------------------------

--------------------------------------------------

class DecimalTable(Table):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/mobject.py

--------------------------------------------------

class Mobject:

def animation_override_for(cls,
    animation_class: type[Animation],
) -> FunctionOverride | None:
def add_animation_override(cls,
    animation_class: type[Animation],
    override_func: FunctionOverride,
) -> None:
def set_default(cls, **kwargs) -> None:
def animate(self) -> _AnimationBuilder | Self:
def reset_points(self) -> None:
def init_colors(self) -> object:
def generate_points(self) -> object:
def add(self, *mobjects: Mobject) -> Self:
def insert(self, index: int, mobject: Mobject) -> None:
def add_to_back(self, *mobjects: Mobject) -> Self:
def remove(self, *mobjects: Mobject) -> Self:
def set(self, **kwargs) -> Self:
def getter(self):
def setter(self, value):
def width(self) -> float:
def width(self, value: float):
def height(self) -> float:
def height(self, value: float):
def depth(self) -> float:
def depth(self, value: float):
def get_array_attrs(self) -> list[Literal["points"]]:
def apply_over_attr_arrays(self, func: MultiMappingFunction) -> Self:
def get_image(self, camera=None) -> PixelArray:
def show(self, camera=None) -> None:
def save_image(self, name: str | None = None) -> None:
def copy(self) -> Self:
def generate_target(self, use_deepcopy: bool = False) -> Self:
def update(self, dt: float = 0, recursive: bool = True) -> Self:
def get_time_based_updaters(self) -> list[TimeBasedUpdater]:
def has_time_based_updater(self) -> bool:
def get_updaters(self) -> list[Updater]:
def get_family_updaters(self) -> list[Updater]:
def add_updater(self,
    update_function: Updater,
    index: int | None = None,
    call_updater: bool = False,
) -> Self:
def remove_updater(self, update_function: Updater) -> Self:
def clear_updaters(self, recursive: bool = True) -> Self:
def match_updaters(self, mobject: Mobject) -> Self:
def suspend_updating(self, recursive: bool = True) -> Self:
def resume_updating(self, recursive: bool = True) -> Self:
def apply_to_family(self, func: Callable[[Mobject], None]) -> None:
def shift(self, *vectors: Vector3D) -> Self:
def scale(self, scale_factor: float, **kwargs) -> Self:
def rotate_about_origin(self, angle: float, axis: Vector3D = OUT, axes=[]) -> Self:
def rotate(self,
    angle: float,
    axis: Vector3D = OUT,
    about_point: Point3DLike | None = None,
    **kwargs,
) -> Self:
def flip(self, axis: Vector3D = UP, **kwargs) -> Self:
def stretch(self, factor: float, dim: int, **kwargs) -> Self:
def func(points: Point3D_Array) -> Point3D_Array:
def apply_function(self, function: MappingFunction, **kwargs) -> Self:
def multi_mapping_function(points: Point3D_Array) -> Point3D_Array:
def apply_function_to_position(self, function: MappingFunction) -> Self:
def apply_function_to_submobject_positions(self, function: MappingFunction) -> Self:
def apply_matrix(self, matrix, **kwargs) -> Self:
def apply_complex_function(self, function: Callable[[complex], complex], **kwargs
) -> Self:
def R3_func(point):
def reverse_points(self) -> Self:
def repeat(self, count: int) -> Self:
def repeat_array(array):
def apply_points_function_about_point(self,
    func: MultiMappingFunction,
    about_point: Point3DLike | None = None,
    about_edge: Vector3D | None = None,
) -> Self:
def pose_at_angle(self, **kwargs):
def center(self) -> Self:
def align_on_border(self, direction: Vector3D, buff: float = DEFAULT_MOBJECT_TO_EDGE_BUFFER
) -> Self:
def to_corner(self, corner: Vector3D = DL, buff: float = DEFAULT_MOBJECT_TO_EDGE_BUFFER
) -> Self:
def to_edge(self, edge: Vector3D = LEFT, buff: float = DEFAULT_MOBJECT_TO_EDGE_BUFFER
) -> Self:
def next_to(self,
    mobject_or_point: Mobject | Point3DLike,
    direction: Vector3D = RIGHT,
    buff: float = DEFAULT_MOBJECT_TO_MOBJECT_BUFFER,
    aligned_edge: Vector3D = ORIGIN,
    submobject_to_align: Mobject | None = None,
    index_of_submobject_to_align: int | None = None,
    coor_mask: Vector3D = np.array([1, 1, 1]),
) -> Self:
def shift_onto_screen(self, **kwargs) -> Self:
def is_off_screen(self):
def stretch_about_point(self, factor: float, dim: int, point: Point3DLike) -> Self:
def rescale_to_fit(self, length: float, dim: int, stretch: bool = False, **kwargs
) -> Self:
def scale_to_fit_width(self, width: float, **kwargs) -> Self:
def stretch_to_fit_width(self, width: float, **kwargs) -> Self:
def scale_to_fit_height(self, height: float, **kwargs) -> Self:
def stretch_to_fit_height(self, height: float, **kwargs) -> Self:
def scale_to_fit_depth(self, depth: float, **kwargs) -> Self:
def stretch_to_fit_depth(self, depth: float, **kwargs) -> Self:
def set_coord(self, value, dim: int, direction: Vector3D = ORIGIN) -> Self:
def set_x(self, x: float, direction: Vector3D = ORIGIN) -> Self:
def set_y(self, y: float, direction: Vector3D = ORIGIN) -> Self:
def set_z(self, z: float, direction: Vector3D = ORIGIN) -> Self:
def space_out_submobjects(self, factor: float = 1.5, **kwargs) -> Self:
def move_to(self,
    point_or_mobject: Point3DLike | Mobject,
    aligned_edge: Vector3D = ORIGIN,
    coor_mask: Vector3D = np.array([1, 1, 1]),
) -> Self:
def replace(self, mobject: Mobject, dim_to_match: int = 0, stretch: bool = False
) -> Self:
def surround(self,
    mobject: Mobject,
    dim_to_match: int = 0,
    stretch: bool = False,
    buff: float = MED_SMALL_BUFF,
) -> Self:
def put_start_and_end_on(self, start: Point3DLike, end: Point3DLike) -> Self:
def add_background_rectangle(self, color: ParsableManimColor | None = None, opacity: float = 0.75, **kwargs
) -> Self:
def add_background_rectangle_to_submobjects(self, **kwargs) -> Self:
def add_background_rectangle_to_family_members_with_points(self, **kwargs) -> Self:
def set_color(self, color: ParsableManimColor = YELLOW_C, family: bool = True
) -> Self:
def set_color_by_gradient(self, *colors: ParsableManimColor) -> Self:
def set_colors_by_radial_gradient(self,
    center: Point3DLike | None = None,
    radius: float = 1,
    inner_color: ParsableManimColor = WHITE,
    outer_color: ParsableManimColor = BLACK,
) -> Self:
def set_submobject_colors_by_gradient(self, *colors: Iterable[ParsableManimColor]):
def set_submobject_colors_by_radial_gradient(self,
    center: Point3DLike | None = None,
    radius: float = 1,
    inner_color: ParsableManimColor = WHITE,
    outer_color: ParsableManimColor = BLACK,
) -> Self:
def to_original_color(self) -> Self:
def fade_to(self, color: ParsableManimColor, alpha: float, family: bool = True
) -> Self:
def fade(self, darkness: float = 0.5, family: bool = True) -> Self:
def get_color(self) -> ManimColor:
def save_state(self) -> Self:
def restore(self) -> Self:
def reduce_across_dimension(self, reduce_func: Callable, dim: int):
def nonempty_submobjects(self) -> list[Self]:
def get_merged_array(self, array_attr: str) -> np.ndarray:
def get_all_points(self) -> Point3D_Array:
def get_points_defining_boundary(self) -> Point3D_Array:
def get_num_points(self) -> int:
def get_extremum_along_dim(self, points: Point3DLike_Array | None = None, dim: int = 0, key: int = 0
) -> float:
def get_critical_point(self, direction: Vector3D) -> Point3D:
def get_edge_center(self, direction: Vector3D) -> Point3D:
def get_corner(self, direction: Vector3D) -> Point3D:
def get_center(self) -> Point3D:
def get_center_of_mass(self) -> Point3D:
def get_boundary_point(self, direction: Vector3D) -> Point3D:
def get_midpoint(self) -> Point3D:
def get_top(self) -> Point3D:
def get_bottom(self) -> Point3D:
def get_right(self) -> Point3D:
def get_left(self) -> Point3D:
def get_zenith(self) -> Point3D:
def get_nadir(self) -> Point3D:
def length_over_dim(self, dim: int) -> float:
def get_coord(self, dim: int, direction: Vector3D = ORIGIN):
def get_x(self, direction: Vector3D = ORIGIN) -> float:
def get_y(self, direction: Vector3D = ORIGIN) -> float:
def get_z(self, direction: Vector3D = ORIGIN) -> float:
def get_start(self) -> Point3D:
def get_end(self) -> Point3D:
def get_start_and_end(self) -> tuple[Point3D, Point3D]:
def point_from_proportion(self, alpha: float) -> Point3D:
def proportion_from_point(self, point: Point3DLike) -> float:
def get_pieces(self, n_pieces: float) -> Group:
def get_z_index_reference_point(self) -> Point3D:
def has_points(self) -> bool:
def has_no_points(self) -> bool:
def match_color(self, mobject: Mobject) -> Self:
def match_dim_size(self, mobject: Mobject, dim: int, **kwargs) -> Self:
def match_width(self, mobject: Mobject, **kwargs) -> Self:
def match_height(self, mobject: Mobject, **kwargs) -> Self:
def match_depth(self, mobject: Mobject, **kwargs) -> Self:
def match_coord(self, mobject: Mobject, dim: int, direction: Vector3D = ORIGIN
) -> Self:
def match_x(self, mobject: Mobject, direction=ORIGIN) -> Self:
def match_y(self, mobject: Mobject, direction=ORIGIN) -> Self:
def match_z(self, mobject: Mobject, direction=ORIGIN) -> Self:
def align_to(self,
    mobject_or_point: Mobject | Point3DLike,
    direction: Vector3D = ORIGIN,
) -> Self:
def get_group_class(self) -> type[Group]:
def get_mobject_type_class() -> type[Mobject]:
def split(self) -> list[Self]:
def get_family(self, recurse: bool = True) -> list[Self]:
def family_members_with_points(self) -> list[Self]:
def arrange(self,
    direction: Vector3D = RIGHT,
    buff: float = DEFAULT_MOBJECT_TO_MOBJECT_BUFFER,
    center: bool = True,
    **kwargs,
) -> Self:
def arrange_in_grid(self,
    rows: int | None = None,
    cols: int | None = None,
    buff: float | tuple[float, float] = MED_SMALL_BUFF,
    cell_alignment: Vector3D = ORIGIN,
    row_alignments: str | None = None,  # "ucd"
    col_alignments: str | None = None,  # "lcr"
    row_heights: Iterable[float | None] | None = None,
    col_widths: Iterable[float | None] | None = None,
    flow_order: str = "rd",
    **kwargs,
) -> Self:
def init_size(num, alignments, sizes):
def init_alignments(alignments, num, mapping, name, dir_):
def reverse(maybe_list):
def init_sizes(sizes, num, measures, name):
def sort(self,
    point_to_num_func: Callable[[Point3DLike], float] = lambda p: p[0],
    submob_func: Callable[[Mobject], Any] | None = None,
) -> Self:
def submob_func(m: Mobject) -> float:
def shuffle(self, recursive: bool = False) -> None:
def invert(self, recursive: bool = False) -> None:
def arrange_submobjects(self, *args, **kwargs) -> Self:
def sort_submobjects(self, *args, **kwargs) -> Self:
def shuffle_submobjects(self, *args, **kwargs) -> None:
def align_data(self, mobject: Mobject, skip_point_alignment: bool = False) -> None:
def get_point_mobject(self, center=None):
def align_points(self, mobject: Mobject) -> Self:
def align_points_with_larger(self, larger_mobject: Mobject):
def align_submobjects(self, mobject: Mobject) -> Self:
def null_point_align(self, mobject: Mobject):
def push_self_into_submobjects(self) -> Self:
def add_n_more_submobjects(self, n: int) -> Self | None:
def repeat_submobject(self, submob: Mobject) -> Self:
def interpolate(self,
    mobject1: Mobject,
    mobject2: Mobject,
    alpha: float,
    path_func: PathFuncType = straight_path(),
) -> Self:
def interpolate_color(self, mobject1: Mobject, mobject2: Mobject, alpha: float):
def become(self,
    mobject: Mobject,
    match_height: bool = False,
    match_width: bool = False,
    match_depth: bool = False,
    match_center: bool = False,
    stretch: bool = False,
) -> Self:
def match_points(self, mobject: Mobject, copy_submobjects: bool = True) -> Self:
def throw_error_if_no_points(self) -> None:
def set_z_index(self,
    z_index_value: float,
    family: bool = True,
) -> Self:
def set_z_index_by_z_Point3D(self) -> Self:
--------------------------------------------------

--------------------------------------------------

class Group(Mobject):

--------------------------------------------------

def update_target(*method_args, **method_kwargs):
def build(self) -> Animation:
--------------------------------------------------

def override_animate(method) -> types.FunctionType:
def decorator(animation_method):

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/value_tracker.py

--------------------------------------------------

class ValueTracker(Mobject):

def get_value(self) -> float:
def set_value(self, value: float):
def increment_value(self, d_value: float):
def interpolate(self, mobject1, mobject2, alpha, path_func=straight_path()):
--------------------------------------------------

--------------------------------------------------

class ComplexValueTracker(ValueTracker):

def get_value(self):
def set_value(self, z):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/svg/svg_mobject.py

--------------------------------------------------

class SVGMobject(VMobject):

def init_svg_mobject(self, use_svg_cache: bool) -> None:
def hash_seed(self) -> tuple:
def generate_mobject(self) -> None:
def get_file_path(self) -> Path:
def modify_xml_tree(self, element_tree: ET.ElementTree) -> ET.ElementTree:
def generate_config_style_dict(self) -> dict[str, str]:
def get_mobjects_from(self, svg: se.SVG) -> list[VMobject]:
def handle_transform(mob: VMobject, matrix: se.Matrix) -> VMobject:
def apply_style_to_mobject(mob: VMobject, shape: se.GraphicObject) -> VMobject:
def path_to_mobject(self, path: se.Path) -> VMobjectFromSVGPath:
def line_to_mobject(line: se.Line) -> Line:
def rect_to_mobject(rect: se.Rect) -> Rectangle:
def ellipse_to_mobject(ellipse: se.Ellipse | se.Circle) -> Circle:
def polygon_to_mobject(polygon: se.Polygon) -> Polygon:
def polyline_to_mobject(self, polyline: se.Polyline) -> VMobject:
def text_to_mobject(text: se.Text):
def move_into_position(self) -> None:
--------------------------------------------------

--------------------------------------------------

class VMobjectFromSVGPath(VMobject):

def init_points(self) -> None:
def handle_commands(self) -> None:
def move_pen(pt, *, true_move: bool = False):
def add_cubic(start, cp1, cp2, end):
def add_quad(start, cp, end):
def add_line(start, end):
def add_cubic(start, cp1, cp2, end):
def add_quad(start, cp, end):
def add_line(start, end):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/svg/brace.py

--------------------------------------------------

class Brace(VMobjectFromSVGPath):

def put_at_tip(self, mob: Mobject, use_next_to: bool = True, **kwargs):
def get_text(self, *text, **kwargs):
def get_tex(self, *tex, **kwargs):
def get_tip(self):
def get_direction(self):
--------------------------------------------------

--------------------------------------------------

class BraceLabel(VMobject):

def creation_anim(self, label_anim=FadeIn, brace_anim=GrowFromCenter):
def shift_brace(self, obj, **kwargs):
def change_label(self, *text, **kwargs):
def change_brace_label(self, obj, *text, **kwargs):
--------------------------------------------------

--------------------------------------------------

class BraceText(BraceLabel):

--------------------------------------------------

--------------------------------------------------

class BraceBetweenPoints(Brace):

--------------------------------------------------

--------------------------------------------------

class ArcBrace(Brace):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/types/vectorized_mobject.py

--------------------------------------------------

class VMobject(Mobject):

def n_points_per_curve(self) -> int:
def get_group_class(self) -> type[VGroup]:
def get_mobject_type_class() -> type[VMobject]:
def init_colors(self, propagate_colors: bool = True) -> Self:
def generate_rgbas_array(self, color: ManimColor | list[ManimColor], opacity: float | Iterable[float]
) -> RGBA_Array_Float:
def update_rgbas_array(self,
    array_name: str,
    color: ManimColor | None = None,
    opacity: float | None = None,
) -> Self:
def set_fill(self,
    color: ParsableManimColor | None = None,
    opacity: float | None = None,
    family: bool = True,
) -> Self:
def set_stroke(self,
    color: ParsableManimColor = None,
    width: float | None = None,
    opacity: float | None = None,
    background=False,
    family: bool = True,
) -> Self:
def set_cap_style(self, cap_style: CapStyleType) -> Self:
def set_background_stroke(self, **kwargs) -> Self:
def set_style(self,
    fill_color: ParsableManimColor | None = None,
    fill_opacity: float | None = None,
    stroke_color: ParsableManimColor | None = None,
    stroke_width: float | None = None,
    stroke_opacity: float | None = None,
    background_stroke_color: ParsableManimColor | None = None,
    background_stroke_width: float | None = None,
    background_stroke_opacity: float | None = None,
    sheen_factor: float | None = None,
    sheen_direction: Vector3D | None = None,
    background_image: Image | str | None = None,
    family: bool = True,
) -> Self:
def get_style(self, simple: bool = False) -> dict:
def match_style(self, vmobject: VMobject, family: bool = True) -> Self:
def set_color(self, color: ParsableManimColor, family: bool = True) -> Self:
def set_opacity(self, opacity: float, family: bool = True) -> Self:
def scale(self, scale_factor: float, scale_stroke: bool = False, **kwargs) -> Self:
def fade(self, darkness: float = 0.5, family: bool = True) -> Self:
def get_fill_rgbas(self) -> RGBA_Array_Float | Zeros:
def get_fill_color(self) -> ManimColor:
def get_fill_opacity(self) -> ManimFloat:
def get_fill_colors(self) -> list[ManimColor | None]:
def get_fill_opacities(self) -> npt.NDArray[ManimFloat]:
def get_stroke_rgbas(self, background: bool = False) -> RGBA_Array_float | Zeros:
def get_stroke_color(self, background: bool = False) -> ManimColor | None:
def get_stroke_width(self, background: bool = False) -> float:
def get_stroke_opacity(self, background: bool = False) -> ManimFloat:
def get_stroke_colors(self, background: bool = False) -> list[ManimColor | None]:
def get_stroke_opacities(self, background: bool = False) -> npt.NDArray[ManimFloat]:
def get_color(self) -> ManimColor:
def set_sheen_direction(self, direction: Vector3D, family: bool = True) -> Self:
def rotate_sheen_direction(self, angle: float, axis: Vector3D = OUT, family: bool = True
) -> Self:
def set_sheen(self, factor: float, direction: Vector3D | None = None, family: bool = True
) -> Self:
def get_sheen_direction(self) -> Vector3D:
def get_sheen_factor(self) -> float:
def get_gradient_start_and_end_points(self) -> tuple[Point3D, Point3D]:
def color_using_background_image(self, background_image: Image | str) -> Self:
def get_background_image(self) -> Image | str:
def match_background_image(self, vmobject: VMobject) -> Self:
def set_shade_in_3d(self, value: bool = True, z_index_as_group: bool = False
) -> Self:
def set_points(self, points: Point3DLike_Array) -> Self:
def resize_points(self,
    new_length: int,
    resize_func: Callable[[Point3D_Array, int], Point3D_Array] = resize_array,
) -> Self:
def set_anchors_and_handles(self,
    anchors1: Point3DLike_Array,
    handles1: Point3DLike_Array,
    handles2: Point3DLike_Array,
    anchors2: Point3DLike_Array,
) -> Self:
def clear_points(self) -> None:
def append_points(self, new_points: Point3DLike_Array) -> Self:
def start_new_path(self, point: Point3DLike) -> Self:
def add_cubic_bezier_curve(self,
    anchor1: Point3DLike,
    handle1: Point3DLike,
    handle2: Point3DLike,
    anchor2: Point3DLike,
) -> None:
def add_cubic_bezier_curves(self, curves) -> None:
def add_cubic_bezier_curve_to(self,
    handle1: Point3DLike,
    handle2: Point3DLike,
    anchor: Point3DLike,
) -> Self:
def add_quadratic_bezier_curve_to(self,
    handle: Point3DLike,
    anchor: Point3DLike,
) -> Self:
def add_line_to(self, point: Point3DLike) -> Self:
def add_smooth_curve_to(self, *points: Point3DLike) -> Self:
def has_new_path_started(self) -> bool:
def get_last_point(self) -> Point3D:
def is_closed(self) -> bool:
def close_path(self) -> None:
def add_points_as_corners(self, points: Point3DLike_Array) -> Self:
def set_points_as_corners(self, points: Point3DLike_Array) -> Self:
def set_points_smoothly(self, points: Point3DLike_Array) -> Self:
def change_anchor_mode(self, mode: Literal["jagged", "smooth"]) -> Self:
def make_smooth(self) -> Self:
def make_jagged(self) -> Self:
def add_subpath(self, points: CubicBezierPathLike) -> Self:
def append_vectorized_mobject(self, vectorized_mobject: VMobject) -> None:
def apply_function(self, function: MappingFunction) -> Self:
def rotate(self,
    angle: float,
    axis: Vector3D = OUT,
    about_point: Point3DLike | None = None,
    **kwargs,
) -> Self:
def scale_handle_to_anchor_distances(self, factor: float) -> Self:
def consider_points_equals(self, p0: Point3DLike, p1: Point3DLike) -> bool:
def consider_points_equals_2d(self, p0: Point2DLike, p1: Point2DLike) -> bool:
def get_cubic_bezier_tuples_from_points(self, points: CubicBezierPathLike
) -> CubicBezierPoints_Array:
def gen_cubic_bezier_tuples_from_points(self, points: CubicBezierPathLike
) -> tuple[CubicBezierPointsLike, ...]:
def get_cubic_bezier_tuples(self) -> CubicBezierPoints_Array:
def get_subpaths_from_points(self, points: CubicBezierPath) -> list[CubicSpline]:
def gen_subpaths_from_points_2d(self, points: CubicBezierPath
) -> Iterable[CubicSpline]:
def get_subpaths(self) -> list[CubicSpline]:
def get_nth_curve_points(self, n: int) -> CubicBezierPoints:
def get_nth_curve_function(self, n: int) -> Callable[[float], Point3D]:
def get_nth_curve_length_pieces(self,
    n: int,
    sample_points: int | None = None,
) -> npt.NDArray[ManimFloat]:
def get_nth_curve_length(self,
    n: int,
    sample_points: int | None = None,
) -> float:
def get_nth_curve_function_with_length(self,
    n: int,
    sample_points: int | None = None,
) -> tuple[Callable[[float], Point3D], float]:
def get_num_curves(self) -> int:
def get_curve_functions(self,
) -> Iterable[Callable[[float], Point3D]]:
def get_curve_functions_with_lengths(self, **kwargs
) -> Iterable[tuple[Callable[[float], Point3D], float]]:
def point_from_proportion(self, alpha: float) -> Point3D:
def proportion_from_point(self,
    point: Point3DLike,
) -> float:
def get_anchors_and_handles(self) -> list[Point3D_Array]:
def get_start_anchors(self) -> Point3D_Array:
def get_end_anchors(self) -> Point3D_Array:
def get_anchors(self) -> list[Point3D]:
def get_points_defining_boundary(self) -> Point3D_Array:
def get_arc_length(self, sample_points_per_curve: int | None = None) -> float:
def align_points(self, vmobject: VMobject) -> Self:
def get_nth_subpath(path_list, n):
def insert_n_curves(self, n: int) -> Self:
def insert_n_curves_to_point_list(self, n: int, points: BezierPathLike
) -> BezierPath:
def align_rgbas(self, vmobject: VMobject) -> Self:
def get_point_mobject(self, center: Point3DLike | None = None) -> VectorizedPoint:
def interpolate_color(self, mobject1: VMobject, mobject2: VMobject, alpha: float
) -> None:
def pointwise_become_partial(self,
    vmobject: VMobject,
    a: float,
    b: float,
) -> Self:
def get_subcurve(self, a: float, b: float) -> Self:
def get_direction(self) -> Literal["CW", "CCW"]:
def reverse_direction(self) -> Self:
def force_direction(self, target_direction: Literal["CW", "CCW"]) -> Self:
--------------------------------------------------

--------------------------------------------------

class VGroup(VMobject):

def add(self,
    *vmobjects: VMobject | Iterable[VMobject],
) -> Self:
def get_type_error_message(invalid_obj, invalid_indices):
--------------------------------------------------

--------------------------------------------------

class VDict(VMobject):

def add(self,
    mapping_or_iterable: (
        Mapping[Hashable, VMobject] | Iterable[tuple[Hashable, VMobject]]
    ),
) -> Self:
def remove(self, key: Hashable) -> Self:
def get_all_submobjects(self) -> list[list]:
def add_key_value_pair(self, key: Hashable, value: VMobject) -> None:
--------------------------------------------------

--------------------------------------------------

class VectorizedPoint(VMobject):

def width(self) -> float:
def height(self) -> float:
def get_location(self) -> Point3D:
def set_location(self, new_loc: Point3D):
--------------------------------------------------

--------------------------------------------------

class CurvesAsSubmobjects(VGroup):

def point_from_proportion(self, alpha: float) -> Point3D:
--------------------------------------------------

--------------------------------------------------

class DashedVMobject(VMobject):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/types/image_mobject.py

--------------------------------------------------

class AbstractImageMobject(Mobject):

def get_pixel_array(self) -> None:
def set_color(self, color, alpha=None, family=True):
def set_resampling_algorithm(self, resampling_algorithm: int) -> Self:
def reset_points(self) -> None:
--------------------------------------------------

--------------------------------------------------

class ImageMobject(AbstractImageMobject):

def get_pixel_array(self):
def set_color(self, color, alpha=None, family=True):
def set_opacity(self, alpha: float) -> Self:
def fade(self, darkness: float = 0.5, family: bool = True) -> Self:
def interpolate_color(self, mobject1: ImageMobject, mobject2: ImageMobject, alpha: float
) -> None:
def get_style(self) -> dict[str, Any]:
--------------------------------------------------

--------------------------------------------------

class ImageMobjectFromCamera(AbstractImageMobject):

def get_pixel_array(self):
def add_display_frame(self, **kwargs: Any) -> Self:
def interpolate_color(self, mobject1, mobject2, alpha) -> None:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/types/point_cloud_mobject.py

--------------------------------------------------

class PMobject(Mobject):

def reset_points(self) -> Self:
def get_array_attrs(self) -> list[str]:
def add_points(self,
    points: npt.NDArray,
    rgbas: npt.NDArray | None = None,
    color: ParsableManimColor | None = None,
    alpha: float = 1,
) -> Self:
def set_color(self, color: ParsableManimColor = YELLOW, family: bool = True
) -> Self:
def get_stroke_width(self) -> int:
def set_stroke_width(self, width: int, family: bool = True) -> Self:
def set_color_by_gradient(self, *colors: ParsableManimColor) -> Self:
def set_colors_by_radial_gradient(self,
    center: Point3DLike | None = None,
    radius: float = 1,
    inner_color: ParsableManimColor = WHITE,
    outer_color: ParsableManimColor = BLACK,
) -> Self:
def match_colors(self, mobject: Mobject) -> Self:
def filter_out(self, condition: npt.NDArray) -> Self:
def thin_out(self, factor: int = 5) -> Self:
def sort_points(self, function: Callable[[npt.NDArray[ManimFloat]], float] = lambda p: p[0]
) -> Self:
def fade_to(self, color: ParsableManimColor, alpha: float, family: bool = True
) -> Self:
def get_all_rgbas(self) -> npt.NDArray:
def ingest_submobjects(self) -> Self:
def get_color(self) -> ManimColor:
def point_from_proportion(self, alpha: float) -> Any:
def get_mobject_type_class() -> type[PMobject]:
def align_points_with_larger(self, larger_mobject: Mobject) -> None:
def get_point_mobject(self, center: Point3DLike | None = None) -> Point:
def interpolate_color(self, mobject1: Mobject, mobject2: Mobject, alpha: float
) -> Self:
def pointwise_become_partial(self, mobject: Mobject, a: float, b: float) -> None:
--------------------------------------------------

--------------------------------------------------

class Mobject1D(PMobject):

def add_line(self,
    start: npt.NDArray,
    end: npt.NDArray,
    color: ParsableManimColor | None = None,
) -> None:
--------------------------------------------------

--------------------------------------------------

class Mobject2D(PMobject):

--------------------------------------------------

--------------------------------------------------

class PGroup(PMobject):

def fade_to(self, color: ParsableManimColor, alpha: float, family: bool = True
) -> Self:
--------------------------------------------------

--------------------------------------------------

class PointCloudDot(Mobject1D):

def init_points(self) -> None:
def generate_points(self) -> None:
--------------------------------------------------

--------------------------------------------------

class Point(PMobject):

def init_points(self) -> None:
def generate_points(self) -> None:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/graphing/functions.py

--------------------------------------------------

class ParametricFunction(VMobject):

def internal_parametric_function(t: float) -> Point3D:
def get_function(self) -> Callable[[float], Point3D]:
def get_point_from_function(self, t: float) -> Point3D:
def generate_points(self) -> Self:
--------------------------------------------------

--------------------------------------------------

class FunctionGraph(ParametricFunction):

def get_function(self):
def get_point_from_function(self, x):
--------------------------------------------------

--------------------------------------------------

class ImplicitFunction(VMobject):

def generate_points(self):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/graphing/number_line.py

--------------------------------------------------

class NumberLine(Line):

def rotate_about_zero(self, angle: float, axis: Sequence[float] = OUT, **kwargs):
def rotate_about_number(self, number: float, angle: float, axis: Sequence[float] = OUT, **kwargs
):
def add_ticks(self):
def get_tick(self, x: float, size: float | None = None) -> Line:
def get_tick_marks(self) -> VGroup:
def get_tick_range(self) -> np.ndarray:
def number_to_point(self, number: float | np.ndarray) -> np.ndarray:
def point_to_number(self, point: Sequence[float]) -> float:
def n2p(self, number: float | np.ndarray) -> np.ndarray:
def p2n(self, point: Sequence[float]) -> float:
def get_unit_size(self) -> float:
def get_unit_vector(self) -> np.ndarray:
def get_number_mobject(self,
    x: float,
    direction: Sequence[float] | None = None,
    buff: float | None = None,
    font_size: float | None = None,
    label_constructor: VMobject | None = None,
    **number_config,
) -> VMobject:
def get_number_mobjects(self, *numbers, **kwargs) -> VGroup:
def get_labels(self) -> VGroup:
def add_numbers(self,
    x_values: Iterable[float] | None = None,
    excluding: Iterable[float] | None = None,
    font_size: float | None = None,
    label_constructor: VMobject | None = None,
    **kwargs,
):
def add_labels(self,
    dict_values: dict[float, str | float | VMobject],
    direction: Sequence[float] = None,
    buff: float | None = None,
    font_size: float | None = None,
    label_constructor: VMobject | None = None,
):
--------------------------------------------------

--------------------------------------------------

class UnitInterval(NumberLine):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/graphing/probability.py

--------------------------------------------------

class SampleSpace(Rectangle):

def add_title(self, title="Sample space", buff=MED_SMALL_BUFF):
def add_label(self, label):
def complete_p_list(self, p_list):
def get_division_along_dimension(self, p_list, dim, colors, vect):
def get_horizontal_division(self, p_list, colors=[GREEN_E, BLUE_E], vect=DOWN):
def get_vertical_division(self, p_list, colors=[MAROON_B, YELLOW], vect=RIGHT):
def divide_horizontally(self, *args, **kwargs):
def divide_vertically(self, *args, **kwargs):
def get_subdivision_braces_and_labels(self,
    parts,
    labels,
    direction,
    buff=SMALL_BUFF,
    min_num_quads=1,
):
def get_side_braces_and_labels(self, labels, direction=LEFT, **kwargs):
def get_top_braces_and_labels(self, labels, **kwargs):
def get_bottom_braces_and_labels(self, labels, **kwargs):
def add_braces_and_labels(self):
--------------------------------------------------

--------------------------------------------------

class BarChart(Axes):

def get_bar_labels(self,
    color: ParsableManimColor | None = None,
    font_size: float = 24,
    buff: float = MED_SMALL_BUFF,
    label_constructor: type[VMobject] = Tex,
):
def change_bar_values(self, values: Iterable[float], update_colors: bool = True):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/graphing/coordinate_systems.py

--------------------------------------------------

class CoordinateSystem:

def coords_to_point(self, *coords: ManimFloat):
def point_to_coords(self, point: Point3DLike):
def polar_to_point(self, radius: float, azimuth: float) -> Point2D:
def point_to_polar(self, point: Point2DLike) -> Point2D:
def c2p(self, *coords: float | Sequence[float] | Sequence[Sequence[float]] | np.ndarray
) -> np.ndarray:
def p2c(self, point: Point3DLike):
def pr2pt(self, radius: float, azimuth: float) -> np.ndarray:
def pt2pr(self, point: np.ndarray) -> tuple[float, float]:
def get_axes(self):
def get_axis(self, index: int) -> Mobject:
def get_origin(self) -> np.ndarray:
def get_x_axis(self) -> Mobject:
def get_y_axis(self) -> Mobject:
def get_z_axis(self) -> Mobject:
def get_x_unit_size(self) -> float:
def get_y_unit_size(self) -> float:
def get_x_axis_label(self,
    label: float | str | Mobject,
    edge: Sequence[float] = UR,
    direction: Sequence[float] = UR,
    buff: float = SMALL_BUFF,
    **kwargs,
) -> Mobject:
def get_y_axis_label(self,
    label: float | str | Mobject,
    edge: Sequence[float] = UR,
    direction: Sequence[float] = UP * 0.5 + RIGHT,
    buff: float = SMALL_BUFF,
    **kwargs,
) -> Mobject:
def get_axis_labels(self):
def add_coordinates(self,
    *axes_numbers: Iterable[float] | None | dict[float, str | float | Mobject],
    **kwargs: Any,
) -> Self:
def get_line_from_axis_to_point(self,
    index: int,
    point: Sequence[float],
    line_config: dict | None = ...,
    color: ParsableManimColor | None = ...,
    stroke_width: float = ...,
) -> DashedLine:
def get_line_from_axis_to_point(self,
    index: int,
    point: Sequence[float],
    line_func: type[LineType],
    line_config: dict | None = ...,
    color: ParsableManimColor | None = ...,
    stroke_width: float = ...,
) -> LineType:
def get_line_from_axis_to_point(self,
    index,
    point,
    line_func=DashedLine,
    line_config=None,
    color=None,
    stroke_width=2,
):
def get_vertical_line(self, point: Sequence[float], **kwargs: Any) -> Line:
def get_horizontal_line(self, point: Sequence[float], **kwargs) -> Line:
def get_lines_to_point(self, point: Sequence[float], **kwargs) -> VGroup:
def plot(self,
    function: Callable[[float], float],
    x_range: Sequence[float] | None = None,
    use_vectorized: bool = False,
    colorscale: Union[Iterable[Color], Iterable[Color, float]] | None = None,
    colorscale_axis: int = 1,
    **kwargs: Any,
) -> ParametricFunction:
def plot_implicit_curve(self,
    func: Callable[[float, float], float],
    min_depth: int = 5,
    max_quads: int = 1500,
    **kwargs: Any,
) -> ImplicitFunction:
def plot_parametric_curve(self,
    function: Callable[[float], np.ndarray],
    use_vectorized: bool = False,
    **kwargs: Any,
) -> ParametricFunction:
def plot_polar_graph(self,
    r_func: Callable[[float], float],
    theta_range: Sequence[float] | None = None,
    **kwargs: Any,
) -> ParametricFunction:
def plot_surface(self,
    function: Callable[[float], float],
    u_range: Sequence[float] | None = None,
    v_range: Sequence[float] | None = None,
    colorscale: (
        Sequence[ParsableManimColor]
        | Sequence[tuple[ParsableManimColor, float]]
        | None
    ) = None,
    colorscale_axis: int = 2,
    **kwargs: Any,
) -> Surface | OpenGLSurface:
def input_to_graph_point(self,
    x: float,
    graph: ParametricFunction | VMobject,
) -> Point3D:
def input_to_graph_coords(self, x: float, graph: ParametricFunction
) -> tuple[float, float]:
def i2gc(self, x: float, graph: ParametricFunction) -> tuple[float, float]:
def i2gp(self, x: float, graph: ParametricFunction) -> np.ndarray:
def get_graph_label(self,
    graph: ParametricFunction,
    label: float | str | Mobject = "f(x)",
    x_val: float | None = None,
    direction: Sequence[float] = RIGHT,
    buff: float = MED_SMALL_BUFF,
    color: ParsableManimColor | None = None,
    dot: bool = False,
    dot_config: dict[str, Any] | None = None,
) -> Mobject:
def get_riemann_rectangles(self,
    graph: ParametricFunction,
    x_range: Sequence[float] | None = None,
    dx: float | None = 0.1,
    input_sample_type: str = "left",
    stroke_width: float = 1,
    stroke_color: ParsableManimColor = BLACK,
    fill_opacity: float = 1,
    color: Iterable[ParsableManimColor] | ParsableManimColor = (BLUE, GREEN),
    show_signed_area: bool = True,
    bounded_graph: ParametricFunction = None,
    blend: bool = False,
    width_scale_factor: float = 1.001,
) -> VGroup:
def get_area(self,
    graph: ParametricFunction,
    x_range: tuple[float, float] | None = None,
    color: ParsableManimColor | Iterable[ParsableManimColor] = (BLUE, GREEN),
    opacity: float = 0.3,
    bounded_graph: ParametricFunction = None,
    **kwargs: Any,
) -> Polygon:
def angle_of_tangent(self,
    x: float,
    graph: ParametricFunction,
    dx: float = 1e-8,
) -> float:
def slope_of_tangent(self, x: float, graph: ParametricFunction, **kwargs: Any
) -> float:
def plot_derivative_graph(self, graph: ParametricFunction, color: ParsableManimColor = GREEN, **kwargs
) -> ParametricFunction:
def deriv(x):
def plot_antiderivative_graph(self,
    graph: ParametricFunction,
    y_intercept: float = 0,
    samples: int = 50,
    use_vectorized: bool = False,
    **kwargs: Any,
) -> ParametricFunction:
def antideriv(x):
def get_secant_slope_group(self,
    x: float,
    graph: ParametricFunction,
    dx: float | None = None,
    dx_line_color: ParsableManimColor = YELLOW,
    dy_line_color: ParsableManimColor | None = None,
    dx_label: float | str | None = None,
    dy_label: float | str | None = None,
    include_secant_line: bool = True,
    secant_line_color: ParsableManimColor = GREEN,
    secant_line_length: float = 10,
) -> VGroup:
def get_vertical_lines_to_graph(self,
    graph: ParametricFunction,
    x_range: Sequence[float] | None = None,
    num_lines: int = 20,
    **kwargs: Any,
) -> VGroup:
def get_T_label(self,
    x_val: float,
    graph: ParametricFunction,
    label: float | str | Mobject | None = None,
    label_color: ParsableManimColor | None = None,
    triangle_size: float = MED_SMALL_BUFF,
    triangle_color: ParsableManimColor | None = WHITE,
    line_func: type[Line] = Line,
    line_color: ParsableManimColor = YELLOW,
) -> VGroup:
--------------------------------------------------

--------------------------------------------------

class Axes(VGroup,CoordinateSystem):

def coords_to_point(self, *coords: float | Sequence[float] | Sequence[Sequence[float]] | np.ndarray
) -> np.ndarray:
def point_to_coords(self, point: Sequence[float]) -> np.ndarray:
def get_axes(self) -> VGroup:
def get_axis_labels(self,
    x_label: float | str | Mobject = "x",
    y_label: float | str | Mobject = "y",
) -> VGroup:
def plot_line_graph(self,
    x_values: Iterable[float],
    y_values: Iterable[float],
    z_values: Iterable[float] | None = None,
    line_color: ParsableManimColor = YELLOW,
    add_vertex_dots: bool = True,
    vertex_dot_radius: float = DEFAULT_DOT_RADIUS,
    vertex_dot_style: dict[str, Any] | None = None,
    **kwargs: Any,
) -> VDict:
--------------------------------------------------

--------------------------------------------------

class ThreeDAxes(Axes):

def make_func(axis):
def get_y_axis_label(self,
    label: float | str | Mobject,
    edge: Sequence[float] = UR,
    direction: Sequence[float] = UR,
    buff: float = SMALL_BUFF,
    rotation: float = PI / 2,
    rotation_axis: Vector3D = OUT,
    **kwargs,
) -> Mobject:
def get_z_axis_label(self,
    label: float | str | Mobject,
    edge: Vector3D = OUT,
    direction: Vector3D = RIGHT,
    buff: float = SMALL_BUFF,
    rotation: float = PI / 2,
    rotation_axis: Vector3D = RIGHT,
    **kwargs: Any,
) -> Mobject:
def get_axis_labels(self,
    x_label: float | str | Mobject = "x",
    y_label: float | str | Mobject = "y",
    z_label: float | str | Mobject = "z",
) -> VGroup:
--------------------------------------------------

--------------------------------------------------

class NumberPlane(Axes):

def get_vector(self, coords: Sequence[ManimFloat], **kwargs: Any) -> Arrow:
def prepare_for_nonlinear_transform(self, num_inserted_curves: int = 50) -> Self:
--------------------------------------------------

--------------------------------------------------

class PolarPlane(Axes):

def get_axes(self) -> VGroup:
def get_vector(self, coords: Sequence[ManimFloat], **kwargs: Any) -> Arrow:
def prepare_for_nonlinear_transform(self, num_inserted_curves: int = 50) -> Self:
def get_coordinate_labels(self,
    r_values: Iterable[float] | None = None,
    a_values: Iterable[float] | None = None,
    **kwargs: Any,
) -> VDict:
def add_coordinates(self,
    r_values: Iterable[float] | None = None,
    a_values: Iterable[float] | None = None,
) -> Self:
def get_radian_label(self, number, font_size: float = 24, **kwargs: Any) -> MathTex:
--------------------------------------------------

--------------------------------------------------

class ComplexPlane(NumberPlane):

def number_to_point(self, number: float | complex) -> np.ndarray:
def n2p(self, number: float | complex) -> np.ndarray:
def point_to_number(self, point: Point3DLike) -> complex:
def p2n(self, point: Point3DLike) -> complex:
def get_coordinate_labels(self, *numbers: Iterable[float | complex], **kwargs: Any
) -> VGroup:
def add_coordinates(self, *numbers: Iterable[float | complex], **kwargs: Any
) -> Self:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/graphing/scale.py

def function(self, value: float) -> float:
def inverse_function(self, value: float) -> float:
def get_custom_labels(self,
    val_range: Iterable[float],
) -> Iterable[Mobject]:
--------------------------------------------------

--------------------------------------------------

class LinearBase(_ScaleBase):

def function(self, value: float) -> float:
def inverse_function(self, value: float) -> float:
--------------------------------------------------

--------------------------------------------------

class LogBase(_ScaleBase):

def function(self, value: float) -> float:
def inverse_function(self, value: float) -> float:
def func(value, base):
def get_custom_labels(self,
    val_range: Iterable[float],
    unit_decimal_places: int = 0,
    **base_config: dict[str, Any],
) -> list[Mobject]:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/geometry/line.py

--------------------------------------------------

class Line(TipableVMobject):

def generate_points(self) -> None:
def set_points_by_ends(self,
    start: Point3DLike | Mobject,
    end: Point3DLike | Mobject,
    buff: float = 0,
    path_arc: float = 0,
) -> None:
def set_path_arc(self, new_value: float) -> None:
def put_start_and_end_on(self,
    start: Point3DLike,
    end: Point3DLike,
) -> Self:
def get_vector(self) -> Vector3D:
def get_unit_vector(self) -> Vector3D:
def get_angle(self) -> float:
def get_projection(self, point: Point3DLike) -> Point3D:
def get_slope(self) -> float:
def set_angle(self, angle: float, about_point: Point3DLike | None = None) -> Self:
def set_length(self, length: float) -> Self:
--------------------------------------------------

--------------------------------------------------

class DashedLine(Line):

def get_start(self) -> Point3D:
def get_end(self) -> Point3D:
def get_first_handle(self) -> Point3D:
def get_last_handle(self) -> Point3D:
--------------------------------------------------

--------------------------------------------------

class TangentLine(Line):

--------------------------------------------------

--------------------------------------------------

class Elbow(VMobject):

--------------------------------------------------

--------------------------------------------------

class Arrow(Line):

def scale(self, factor: float, scale_tips: bool = False, **kwargs: Any) -> Self:
def get_normal_vector(self) -> Vector3D:
def reset_normal_vector(self) -> Self:
def get_default_tip_length(self) -> float:
--------------------------------------------------

--------------------------------------------------

class Vector(Arrow):

def coordinate_label(self,
    integer_labels: bool = True,
    n_dim: int = 2,
    color: ParsableManimColor | None = None,
    **kwargs: Any,
) -> Matrix:
--------------------------------------------------

--------------------------------------------------

class DoubleArrow(Arrow):

--------------------------------------------------

--------------------------------------------------

class Angle(VMobject):

def get_lines(self) -> VGroup:
def get_value(self, degrees: bool = False) -> float:
def from_three_points(A: Point3DLike, B: Point3DLike, C: Point3DLike, **kwargs: Any
) -> Angle:
--------------------------------------------------

--------------------------------------------------

class RightAngle(Angle):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/geometry/shape_matchers.py

--------------------------------------------------

class SurroundingRectangle(RoundedRectangle):

--------------------------------------------------

--------------------------------------------------

class BackgroundRectangle(SurroundingRectangle):

def pointwise_become_partial(self, mobject: Mobject, a: Any, b: float) -> Self:
def set_style(self, fill_opacity: float, **kwargs: Any) -> Self:
def get_fill_color(self) -> ManimColor:
--------------------------------------------------

--------------------------------------------------

class Cross(VGroup):

--------------------------------------------------

--------------------------------------------------

class Underline(Line):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/geometry/boolean_ops.py

--------------------------------------------------

--------------------------------------------------

class Union(_BooleanOps):

--------------------------------------------------

--------------------------------------------------

class Difference(_BooleanOps):

--------------------------------------------------

--------------------------------------------------

class Intersection(_BooleanOps):

--------------------------------------------------

--------------------------------------------------

class Exclusion(_BooleanOps):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/geometry/tips.py

--------------------------------------------------

class ArrowTip(VMobject):

def base(self) -> Point3D:
def tip_point(self) -> Point3D:
def vector(self) -> Vector3D:
def tip_angle(self) -> float:
def length(self) -> float:
--------------------------------------------------

--------------------------------------------------

class StealthTip(ArrowTip):

def length(self) -> float:
--------------------------------------------------

--------------------------------------------------

class ArrowTriangleTip(ArrowTip,Triangle):

--------------------------------------------------

--------------------------------------------------

class ArrowTriangleFilledTip(ArrowTriangleTip):

--------------------------------------------------

--------------------------------------------------

class ArrowCircleTip(ArrowTip,Circle):

--------------------------------------------------

--------------------------------------------------

class ArrowCircleFilledTip(ArrowCircleTip):

--------------------------------------------------

--------------------------------------------------

class ArrowSquareTip(ArrowTip,Square):

--------------------------------------------------

--------------------------------------------------

class ArrowSquareFilledTip(ArrowSquareTip):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/geometry/polygram.py

--------------------------------------------------

class Polygram(VMobject):

def get_vertices(self) -> Point3D_Array:
def get_vertex_groups(self) -> npt.NDArray[ManimFloat]:
def round_corners(self,
    radius: float | list[float] = 0.5,
    evenly_distribute_anchors: bool = False,
    components_per_rounded_corner: int = 2,
) -> Self:
--------------------------------------------------

--------------------------------------------------

class Polygon(Polygram):

--------------------------------------------------

--------------------------------------------------

class RegularPolygram(Polygram):

def gen_polygon_vertices(start_angle: float | None) -> tuple[list[Any], float]:
--------------------------------------------------

--------------------------------------------------

class RegularPolygon(RegularPolygram):

--------------------------------------------------

--------------------------------------------------

class Star(Polygon):

--------------------------------------------------

--------------------------------------------------

class Triangle(RegularPolygon):

--------------------------------------------------

--------------------------------------------------

class Rectangle(Polygon):

--------------------------------------------------

--------------------------------------------------

class Square(Rectangle):

def side_length(self) -> float:
def side_length(self, value: float) -> None:
--------------------------------------------------

--------------------------------------------------

class RoundedRectangle(Rectangle):

--------------------------------------------------

--------------------------------------------------

class Cutout(VMobject):

--------------------------------------------------

--------------------------------------------------

class ConvexHull(Polygram):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/geometry/arc.py

--------------------------------------------------

class TipableVMobject(VMobject):

def add_tip(self,
    tip: tips.ArrowTip | None = None,
    tip_shape: type[tips.ArrowTip] | None = None,
    tip_length: float | None = None,
    tip_width: float | None = None,
    at_start: bool = False,
) -> Self:
def create_tip(self,
    tip_shape: type[tips.ArrowTip] | None = None,
    tip_length: float | None = None,
    tip_width: float | None = None,
    at_start: bool = False,
) -> tips.ArrowTip:
def get_unpositioned_tip(self,
    tip_shape: type[tips.ArrowTip] | None = None,
    tip_length: float | None = None,
    tip_width: float | None = None,
) -> tips.ArrowTip | tips.ArrowTriangleFilledTip:
def position_tip(self, tip: tips.ArrowTip, at_start: bool = False) -> tips.ArrowTip:
def reset_endpoints_based_on_tip(self, tip: tips.ArrowTip, at_start: bool) -> Self:
def asign_tip_attr(self, tip: tips.ArrowTip, at_start: bool) -> Self:
def has_tip(self) -> bool:
def has_start_tip(self) -> bool:
def pop_tips(self) -> VGroup:
def get_tips(self) -> VGroup:
def get_tip(self) -> VMobject:
def get_default_tip_length(self) -> float:
def get_first_handle(self) -> Point3D:
def get_last_handle(self) -> Point3D:
def get_end(self) -> Point3D:
def get_start(self) -> Point3D:
def get_length(self) -> float:
--------------------------------------------------

--------------------------------------------------

class Arc(TipableVMobject):

def generate_points(self) -> None:
def init_points(self) -> None:
def get_arc_center(self, warning: bool = True) -> Point3D:
def move_arc_center_to(self, point: Point3DLike) -> Self:
def stop_angle(self) -> float:
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
    buffer_factor: float = 1.2,
) -> Self:
def point_at_angle(self, angle: float) -> Point3D:
def from_three_points(p1: Point3DLike, p2: Point3DLike, p3: Point3DLike, **kwargs: Any
) -> Circle:
--------------------------------------------------

--------------------------------------------------

class Dot(Circle):

--------------------------------------------------

--------------------------------------------------

class AnnotationDot(Dot):

--------------------------------------------------

--------------------------------------------------

class LabeledDot(Dot):

--------------------------------------------------

--------------------------------------------------

class Ellipse(Circle):

--------------------------------------------------

--------------------------------------------------

class AnnularSector(Arc):

def generate_points(self) -> None:
--------------------------------------------------

--------------------------------------------------

class Sector(AnnularSector):

--------------------------------------------------

--------------------------------------------------

class Annulus(Circle):

def generate_points(self) -> None:
--------------------------------------------------

--------------------------------------------------

class CubicBezier(VMobject):

--------------------------------------------------

--------------------------------------------------

class ArcPolygon(VMobject):

--------------------------------------------------

--------------------------------------------------

class ArcPolygonFromArcs(VMobject):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/geometry/labeled.py

--------------------------------------------------

class Label(VGroup):

--------------------------------------------------

--------------------------------------------------

class LabeledLine(Line):

--------------------------------------------------

--------------------------------------------------

class LabeledArrow(LabeledLine,Arrow):

--------------------------------------------------

--------------------------------------------------

class LabeledPolygram(Polygram):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/text/text_mobject.py

def remove_invisible_chars(mobject: SVGMobject) -> SVGMobject:
--------------------------------------------------

class Paragraph(VGroup):

--------------------------------------------------

--------------------------------------------------

class Text(SVGMobject):

def font_list() -> list[str]:
def add_line_to(end):
def add_line_to(end):
def font_size(self):
def font_size(self, font_val):
def init_colors(self, propagate_colors=True):
--------------------------------------------------

--------------------------------------------------

class MarkupText(SVGMobject):

def font_list() -> list[str]:
def add_line_to(end):
def add_line_to(end):
def font_size(self):
def font_size(self, font_val):
--------------------------------------------------

def register_font(font_file: str | Path):

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/text/numbers.py

--------------------------------------------------

class DecimalNumber(VMobject):

def font_size(self):
def font_size(self, font_val):
def set_value(self, number: float):
def get_value(self):
def increment_value(self, delta_t=1):
--------------------------------------------------

--------------------------------------------------

class Integer(DecimalNumber):

def get_value(self):
--------------------------------------------------

--------------------------------------------------

class Variable(VMobject):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/text/tex_mobject.py

--------------------------------------------------

class SingleStringMathTex(SVGMobject):

def font_size(self):
def font_size(self, font_val):
def get_tex_string(self):
def init_colors(self, propagate_colors=True):
--------------------------------------------------

--------------------------------------------------

class MathTex(SingleStringMathTex):

def get_parts_by_tex(self, tex, substring=True, case_sensitive=True):
def test(tex1, tex2):
def get_part_by_tex(self, tex, **kwargs):
def set_color_by_tex(self, tex, color, **kwargs):
def set_opacity_by_tex(self, tex: str, opacity: float = 0.5, remaining_opacity: float = None, **kwargs
):
def set_color_by_tex_to_color_map(self, texs_to_color_map, **kwargs):
def index_of_part(self, part):
def index_of_part_by_tex(self, tex, **kwargs):
def sort_alphabetically(self):
--------------------------------------------------

--------------------------------------------------

class Tex(MathTex):

--------------------------------------------------

--------------------------------------------------

class BulletedList(Tex):

def fade_all_but(self, index_or_string, opacity=0.5):
--------------------------------------------------

--------------------------------------------------

class Title(Tex):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/text/code_mobject.py

--------------------------------------------------

class Code(VMobject):

def get_styles_list(cls) -> list[str]:
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/opengl/opengl_geometry.py

--------------------------------------------------

class OpenGLTipableVMobject(OpenGLVMobject):

def add_tip(self, at_start=False, **kwargs):
def create_tip(self, at_start=False, **kwargs):
def get_unpositioned_tip(self, **kwargs):
def position_tip(self, tip, at_start=False):
def reset_endpoints_based_on_tip(self, tip, at_start):
def asign_tip_attr(self, tip, at_start):
def has_tip(self):
def has_start_tip(self):
def pop_tips(self):
def get_tips(self):
def get_tip(self):
def get_default_tip_length(self):
def get_first_handle(self):
def get_last_handle(self):
def get_end(self):
def get_start(self):
def get_length(self):
--------------------------------------------------

--------------------------------------------------

class OpenGLArc(OpenGLTipableVMobject):

def init_points(self):
def create_quadratic_bezier_points(angle, start_angle=0, n_components=8):
def get_arc_center(self):
def get_start_angle(self):
def get_stop_angle(self):
def move_arc_center_to(self, point):
--------------------------------------------------

--------------------------------------------------

class OpenGLArcBetweenPoints(OpenGLArc):

--------------------------------------------------

--------------------------------------------------

class OpenGLCurvedArrow(OpenGLArcBetweenPoints):

--------------------------------------------------

--------------------------------------------------

class OpenGLCurvedDoubleArrow(OpenGLCurvedArrow):

--------------------------------------------------

--------------------------------------------------

class OpenGLCircle(OpenGLArc):

def surround(self, mobject, dim_to_match=0, stretch=False, buff=MED_SMALL_BUFF):
def point_at_angle(self, angle):
--------------------------------------------------

--------------------------------------------------

class OpenGLDot(OpenGLCircle):

--------------------------------------------------

--------------------------------------------------

class OpenGLEllipse(OpenGLCircle):

--------------------------------------------------

--------------------------------------------------

class OpenGLAnnularSector(OpenGLArc):

def init_points(self):
--------------------------------------------------

--------------------------------------------------

class OpenGLSector(OpenGLAnnularSector):

--------------------------------------------------

--------------------------------------------------

class OpenGLAnnulus(OpenGLCircle):

def init_points(self):
--------------------------------------------------

--------------------------------------------------

class OpenGLLine(OpenGLTipableVMobject):

def init_points(self):
def set_points_by_ends(self, start, end, buff=0, path_arc=0):
def set_path_arc(self, new_value):
def account_for_buff(self, buff):
def set_start_and_end_attrs(self, start, end):
def pointify(self, mob_or_point, direction=None):
def put_start_and_end_on(self, start, end):
def get_vector(self):
def get_unit_vector(self):
def get_angle(self):
def get_projection(self, point):
def get_slope(self):
def set_angle(self, angle, about_point=None):
def set_length(self, length):
--------------------------------------------------

--------------------------------------------------

class OpenGLDashedLine(OpenGLLine):

def calculate_num_dashes(self, dashed_ratio):
def get_start(self):
def get_end(self):
def get_first_handle(self):
def get_last_handle(self):
--------------------------------------------------

--------------------------------------------------

class OpenGLTangentLine(OpenGLLine):

--------------------------------------------------

--------------------------------------------------

class OpenGLElbow(OpenGLVMobject):

--------------------------------------------------

--------------------------------------------------

class OpenGLArrow(OpenGLLine):

def set_points_by_ends(self, start, end, buff=0, path_arc=0):
def reset_points_around_ends(self):
def get_start(self):
def get_end(self):
def put_start_and_end_on(self, start, end):
def scale(self, *args, **kwargs):
def set_thickness(self, thickness):
def set_path_arc(self, path_arc):
--------------------------------------------------

--------------------------------------------------

class OpenGLVector(OpenGLArrow):

--------------------------------------------------

--------------------------------------------------

class OpenGLDoubleArrow(OpenGLArrow):

--------------------------------------------------

--------------------------------------------------

class OpenGLCubicBezier(OpenGLVMobject):

--------------------------------------------------

--------------------------------------------------

class OpenGLPolygon(OpenGLVMobject):

def init_points(self):
def get_vertices(self):
def round_corners(self, radius=0.5):
--------------------------------------------------

--------------------------------------------------

class OpenGLRegularPolygon(OpenGLPolygon):

--------------------------------------------------

--------------------------------------------------

class OpenGLTriangle(OpenGLRegularPolygon):

--------------------------------------------------

--------------------------------------------------

class OpenGLArrowTip(OpenGLTriangle):

def get_base(self):
def get_tip_point(self):
def get_vector(self):
def get_angle(self):
def get_length(self):
--------------------------------------------------

--------------------------------------------------

class OpenGLRectangle(OpenGLPolygon):

--------------------------------------------------

--------------------------------------------------

class OpenGLSquare(OpenGLRectangle):

--------------------------------------------------

--------------------------------------------------

class OpenGLRoundedRectangle(OpenGLRectangle):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/opengl/opengl_surface.py

--------------------------------------------------

class OpenGLSurface(OpenGLMobject):

def uv_func(self, u, v):
def init_points(self):
def compute_triangle_indices(self):
def get_triangle_indices(self):
def get_surface_points_and_nudged_points(self):
def get_unit_normals(self):
def pointwise_become_partial(self, smobject, a, b, axis=None):
def get_partial_points_array(self, points, a, b, resolution, axis):
def sort_faces_back_to_front(self, vect=OUT):
def index_dot(index):
def get_shader_data(self):
def fill_in_shader_color_info(self, shader_data):
def get_shader_vert_indices(self):
--------------------------------------------------

--------------------------------------------------

class OpenGLSurfaceGroup(OpenGLSurface):

def init_points(self):
--------------------------------------------------

--------------------------------------------------

class OpenGLTexturedSurface(OpenGLSurface):

def get_image_from_file(self,
    image_file: str | Path,
    image_mode: str,
):
def init_data(self):
def init_points(self):
def init_colors(self):
def set_opacity(self, opacity, recurse=True):
def pointwise_become_partial(self, tsmobject, a, b, axis=1):
def fill_in_shader_color_info(self, shader_data):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/opengl/opengl_mobject.py

def affects_shader_info_id(func: Callable[[OpenGLMobject], OpenGLMobject],
) -> Callable[[OpenGLMobject], OpenGLMobject]:
def wrapper(self: OpenGLMobject) -> OpenGLMobject:
--------------------------------------------------

class OpenGLMobject:

def set_default(cls, **kwargs) -> None:
def init_data(self) -> None:
def init_colors(self) -> object:
def init_points(self) -> object:
def set(self, **kwargs) -> Self:
def set_data(self, data: dict[str, Any]) -> Self:
def set_uniforms(self, uniforms: dict[str, Any]) -> Self:
def animate(self) -> _AnimationBuilder | Self:
def width(self) -> float:
def width(self, value: float) -> None:
def height(self) -> float:
def height(self, value: float) -> None:
def depth(self) -> float:
def depth(self, value: float) -> None:
def resize_points(self, new_length, resize_func=resize_array):
def set_points(self, points: Point3DLike_Array) -> Self:
def apply_over_attr_arrays(self, func: Callable[[npt.NDArray[T]], npt.NDArray[T]]
) -> Self:
def append_points(self, new_points: Point3DLike_Array) -> Self:
def reverse_points(self) -> Self:
def get_midpoint(self) -> Point3D:
def apply_points_function(self,
    func: MultiMappingFunction,
    about_point: Point3DLike | None = None,
    about_edge: Vector3D | None = ORIGIN,
    works_on_bounding_box: bool = False,
) -> Self:
def match_points(self, mobject: OpenGLMobject) -> Self:
def clear_points(self) -> Self:
def get_num_points(self) -> int:
def get_all_points(self) -> Point3D_Array:
def has_points(self) -> bool:
def get_bounding_box(self) -> npt.NDArray[float]:
def compute_bounding_box(self) -> npt.NDArray[float]:
def refresh_bounding_box(self, recurse_down: bool = False, recurse_up: bool = True
) -> Self:
def is_point_touching(self, point: Point3DLike, buff: float = MED_SMALL_BUFF
) -> bool:
def split(self) -> Sequence[OpenGLMobject]:
def assemble_family(self) -> Self:
def get_family(self, recurse: bool = True) -> Sequence[OpenGLMobject]:
def family_members_with_points(self) -> Sequence[OpenGLMobject]:
def add(self, *mobjects: OpenGLMobject, update_parent: bool = False) -> Self:
def insert(self, index: int, mobject: OpenGLMobject, update_parent: bool = False
) -> Self:
def remove(self, *mobjects: OpenGLMobject, update_parent: bool = False) -> Self:
def add_to_back(self, *mobjects: OpenGLMobject) -> Self:
def replace_submobject(self, index: int, new_submob: OpenGLMobject) -> Self:
def arrange(self, direction: Vector3D = RIGHT, center: bool = True, **kwargs
) -> Self:
def arrange_in_grid(self,
    rows: int | None = None,
    cols: int | None = None,
    buff: float | tuple[float, float] = MED_SMALL_BUFF,
    cell_alignment: Vector3D = ORIGIN,
    row_alignments: str | None = None,  # "ucd"
    col_alignments: str | None = None,  # "lcr"
    row_heights: Sequence[float | None] | None = None,
    col_widths: Sequence[float | None] | None = None,
    flow_order: str = "rd",
    **kwargs,
) -> Self:
def init_size(num: int | None,
    alignments: str | None,
    sizes: Sequence[float | None] | None,
    name: str,
) -> int:
def init_alignments(str_alignments: str | None,
    num: int,
    mapping: dict[str, Vector3D],
    name: str,
    direction: Vector3D,
) -> Sequence[Vector3D]:
def reverse(maybe_list: Sequence[Any] | None) -> Sequence[Any] | None:
def init_sizes(sizes: Sequence[float | None] | None,
    num: int,
    measures: Sequence[float],
    name: str,
) -> Sequence[float]:
def get_grid(self, n_rows: int, n_cols: int, height: float | None = None, **kwargs
) -> OpenGLGroup:
def duplicate(self, n: int) -> OpenGLGroup:
def sort(self,
    point_to_num_func: Callable[[Point3DLike], float] = lambda p: p[0],
    submob_func: Callable[[OpenGLMobject], Any] | None = None,
) -> Self:
def shuffle(self, recurse: bool = False) -> Self:
def invert(self, recursive: bool = False) -> Self:
def copy(self, shallow: bool = False) -> OpenGLMobject:
def deepcopy(self) -> OpenGLMobject:
def generate_target(self, use_deepcopy: bool = False) -> OpenGLMobject:
def save_state(self, use_deepcopy: bool = False) -> Self:
def restore(self) -> Self:
def init_updaters(self) -> None:
def update(self, dt: float = 0, recurse: bool = True) -> Self:
def get_time_based_updaters(self) -> Sequence[TimeBasedUpdater]:
def has_time_based_updater(self) -> bool:
def get_updaters(self) -> Sequence[Updater]:
def get_family_updaters(self) -> Sequence[Updater]:
def add_updater(self,
    update_function: Updater,
    index: int | None = None,
    call_updater: bool = False,
) -> Self:
def remove_updater(self, update_function: Updater) -> Self:
def clear_updaters(self, recurse: bool = True) -> Self:
def match_updaters(self, mobject: OpenGLMobject) -> Self:
def suspend_updating(self, recurse: bool = True) -> Self:
def resume_updating(self, recurse: bool = True, call_updater: bool = True) -> Self:
def refresh_has_updater_status(self) -> Self:
def shift(self, vector: Vector3D) -> Self:
def scale(self,
    scale_factor: float,
    about_point: Sequence[float] | None = None,
    about_edge: Sequence[float] = ORIGIN,
    **kwargs,
) -> Self:
def stretch(self, factor: float, dim: int, **kwargs) -> Self:
def func(points: Point3D_Array) -> Point3D_Array:
def rotate_about_origin(self, angle: float, axis: Vector3D = OUT) -> Self:
def rotate(self,
    angle: float,
    axis: Vector3D = OUT,
    about_point: Sequence[float] | None = None,
    **kwargs,
) -> Self:
def flip(self, axis: Vector3D = UP, **kwargs) -> Self:
def apply_function(self, function: MappingFunction, **kwargs) -> Self:
def multi_mapping_function(points: Point3D_Array) -> Point3D_Array:
def apply_function_to_position(self, function: MappingFunction) -> Self:
def apply_function_to_submobject_positions(self, function: MappingFunction) -> Self:
def apply_matrix(self, matrix: MatrixMN, **kwargs) -> Self:
def apply_complex_function(self, function: Callable[[complex], complex], **kwargs
) -> Self:
def R3_func(point):
def hierarchical_model_matrix(self) -> MatrixMN:
def wag(self,
    direction: Vector3D = RIGHT,
    axis: Vector3D = DOWN,
    wag_factor: float = 1.0,
) -> Self:
def center(self) -> Self:
def align_on_border(self,
    direction: Vector3D,
    buff: float = DEFAULT_MOBJECT_TO_EDGE_BUFFER,
) -> Self:
def to_corner(self,
    corner: Vector3D = LEFT + DOWN,
    buff: float = DEFAULT_MOBJECT_TO_EDGE_BUFFER,
) -> Self:
def to_edge(self,
    edge: Vector3D = LEFT,
    buff: float = DEFAULT_MOBJECT_TO_EDGE_BUFFER,
) -> Self:
def next_to(self,
    mobject_or_point: OpenGLMobject | Point3DLike,
    direction: Vector3D = RIGHT,
    buff: float = DEFAULT_MOBJECT_TO_MOBJECT_BUFFER,
    aligned_edge: Vector3D = ORIGIN,
    submobject_to_align: OpenGLMobject | None = None,
    index_of_submobject_to_align: int | None = None,
    coor_mask: Point3DLike = np.array([1, 1, 1]),
) -> Self:
def shift_onto_screen(self, **kwargs) -> Self:
def is_off_screen(self) -> bool:
def stretch_about_point(self, factor: float, dim: int, point: Point3DLike) -> Self:
def rescale_to_fit(self, length: float, dim: int, stretch: bool = False, **kwargs
) -> Self:
def stretch_to_fit_width(self, width: float, **kwargs) -> Self:
def stretch_to_fit_height(self, height: float, **kwargs) -> Self:
def stretch_to_fit_depth(self, depth: float, **kwargs) -> Self:
def set_width(self, width: float, stretch: bool = False, **kwargs) -> Self:
def set_height(self, height: float, stretch: bool = False, **kwargs) -> Self:
def set_depth(self, depth: float, stretch: bool = False, **kwargs):
def set_coord(self, value: float, dim: int, direction: Vector3D = ORIGIN) -> Self:
def set_x(self, x: float, direction: Vector3D = ORIGIN) -> Self:
def set_y(self, y: float, direction: Vector3D = ORIGIN) -> Self:
def set_z(self, z: float, direction: Vector3D = ORIGIN) -> Self:
def space_out_submobjects(self, factor: float = 1.5, **kwargs) -> Self:
def move_to(self,
    point_or_mobject: Point3DLike | OpenGLMobject,
    aligned_edge: Vector3D = ORIGIN,
    coor_mask: Point3DLike = np.array([1, 1, 1]),
) -> Self:
def replace(self,
    mobject: OpenGLMobject,
    dim_to_match: int = 0,
    stretch: bool = False,
) -> Self:
def surround(self,
    mobject: OpenGLMobject,
    dim_to_match: int = 0,
    stretch: bool = False,
    buff: float = MED_SMALL_BUFF,
) -> Self:
def put_start_and_end_on(self, start: Point3DLike, end: Point3DLike) -> Self:
def set_rgba_array(self,
    color: ParsableManimColor | Iterable[ParsableManimColor] | None = None,
    opacity: float | Iterable[float] | None = None,
    name: str = "rgbas",
    recurse: bool = True,
) -> Self:
def set_rgba_array_direct(self,
    rgbas: npt.NDArray[RGBA_Array_Float],
    name: str = "rgbas",
    recurse: bool = True,
) -> Self:
def set_color(self,
    color: ParsableManimColor | Iterable[ParsableManimColor] | None,
    opacity: float | Iterable[float] | None = None,
    recurse: bool = True,
) -> Self:
def set_opacity(self, opacity: float | Iterable[float] | None, recurse: bool = True
) -> Self:
def get_color(self) -> str:
def get_opacity(self) -> float:
def set_color_by_gradient(self, *colors: ParsableManimColor) -> Self:
def set_submobject_colors_by_gradient(self, *colors: ParsableManimColor) -> Self:
def fade(self, darkness: float = 0.5, recurse: bool = True) -> Self:
def get_gloss(self) -> float:
def set_gloss(self, gloss: float, recurse: bool = True) -> Self:
def get_shadow(self) -> float:
def set_shadow(self, shadow: float, recurse: bool = True) -> Self:
def add_background_rectangle(self,
    color: ParsableManimColor | None = None,
    opacity: float = 0.75,
    **kwargs,
) -> Self:
def add_background_rectangle_to_submobjects(self, **kwargs) -> Self:
def add_background_rectangle_to_family_members_with_points(self, **kwargs) -> Self:
def get_bounding_box_point(self, direction: Vector3D) -> Point3D:
def get_edge_center(self, direction: Vector3D) -> Point3D:
def get_corner(self, direction: Vector3D) -> Point3D:
def get_center(self) -> Point3D:
def get_center_of_mass(self) -> Point3D:
def get_boundary_point(self, direction: Vector3D) -> Point3D:
def get_continuous_bounding_box_point(self, direction: Vector3D) -> Point3D:
def get_top(self) -> Point3D:
def get_bottom(self) -> Point3D:
def get_right(self) -> Point3D:
def get_left(self) -> Point3D:
def get_zenith(self) -> Point3D:
def get_nadir(self) -> Point3D:
def length_over_dim(self, dim: int) -> float:
def get_width(self) -> float:
def get_height(self) -> float:
def get_depth(self) -> float:
def get_coord(self, dim: int, direction: Vector3D = ORIGIN) -> ManimFloat:
def get_x(self, direction: Vector3D = ORIGIN) -> ManimFloat:
def get_y(self, direction: Vector3D = ORIGIN) -> ManimFloat:
def get_z(self, direction: Vector3D = ORIGIN) -> ManimFloat:
def get_start(self) -> Point3D:
def get_end(self) -> Point3D:
def get_start_and_end(self) -> tuple[Point3D, Point3D]:
def point_from_proportion(self, alpha: float) -> Point3D:
def pfp(self, alpha: float) -> Point3D:
def get_pieces(self, n_pieces: int) -> OpenGLMobject:
def get_z_index_reference_point(self) -> Point3D:
def match_color(self, mobject: OpenGLMobject) -> Self:
def match_dim_size(self, mobject: OpenGLMobject, dim: int, **kwargs) -> Self:
def match_width(self, mobject: OpenGLMobject, **kwargs) -> Self:
def match_height(self, mobject: OpenGLMobject, **kwargs) -> Self:
def match_depth(self, mobject: OpenGLMobject, **kwargs) -> Self:
def match_coord(self, mobject: OpenGLMobject, dim: int, direction: Vector3D = ORIGIN
) -> Self:
def match_x(self, mobject: OpenGLMobject, direction: Vector3D = ORIGIN) -> Self:
def match_y(self, mobject: OpenGLMobject, direction: Vector3D = ORIGIN) -> Self:
def match_z(self, mobject: OpenGLMobject, direction: Vector3D = ORIGIN) -> Self:
def align_to(self,
    mobject_or_point: OpenGLMobject | Point3DLike,
    direction: Vector3D = ORIGIN,
) -> Self:
def get_group_class(self) -> type[OpenGLGroup]:
def get_mobject_type_class() -> type[OpenGLMobject]:
def align_data_and_family(self, mobject: OpenGLMobject) -> Self:
def align_data(self, mobject: OpenGLMobject) -> Self:
def align_points(self, mobject: OpenGLMobject) -> Self:
def align_family(self, mobject: OpenGLMobject) -> Self:
def push_self_into_submobjects(self) -> Self:
def add_n_more_submobjects(self, n: int) -> Self:
def interpolate(self,
    mobject1: OpenGLMobject,
    mobject2: OpenGLMobject,
    alpha: float,
    path_func: PathFuncType = straight_path(),
) -> Self:
def pointwise_become_partial(self, mobject: OpenGLMobject, a: float, b: float
) -> None:
def become(self,
    mobject: OpenGLMobject,
    match_height: bool = False,
    match_width: bool = False,
    match_depth: bool = False,
    match_center: bool = False,
    stretch: bool = False,
) -> Self:
def lock_data(self, keys: Iterable[str]) -> None:
def lock_matching_data(self, mobject1: OpenGLMobject, mobject2: OpenGLMobject
) -> Self:
def unlock_data(self) -> None:
def fix_in_frame(self) -> Self:
def fix_orientation(self) -> Self:
def unfix_from_frame(self) -> Self:
def unfix_orientation(self) -> Self:
def apply_depth_test(self) -> Self:
def deactivate_depth_test(self) -> Self:
def replace_shader_code(self, old_code: str, new_code: str) -> Self:
def set_color_by_code(self, glsl_code: str) -> Self:
def set_color_by_xyz_func(self,
    glsl_snippet: str,
    min_value: float = -5.0,
    max_value: float = 5.0,
    colormap: str = "viridis",
) -> Self:
def refresh_shader_wrapper_id(self) -> Self:
def get_shader_wrapper(self) -> ShaderWrapper:
def get_shader_wrapper_list(self) -> Sequence[ShaderWrapper]:
def check_data_alignment(self, array: npt.NDArray, data_key: str) -> Self:
def get_resized_shader_data_array(self, length: float) -> npt.NDArray:
def read_data_to_shader(self,
    shader_data: npt.NDArray,  # has structured data type, ex. ("point", np.float32, (3,))
    shader_data_key: str,
    data_key: str,
) -> None:
def get_shader_data(self) -> npt.NDArray:
def refresh_shader_data(self) -> None:
def get_shader_uniforms(self) -> dict[str, Any]:
def get_shader_vert_indices(self) -> Sequence[int]:
def submobjects(self) -> Sequence[OpenGLMobject]:
def submobjects(self, submobject_list: Iterable[OpenGLMobject]) -> None:
def throw_error_if_no_points(self) -> None:
--------------------------------------------------

--------------------------------------------------

class OpenGLGroup(OpenGLMobject):

--------------------------------------------------

--------------------------------------------------

class OpenGLPoint(OpenGLMobject):

def get_width(self) -> float:
def get_height(self) -> float:
def get_location(self) -> Point3D:
def get_bounding_box_point(self, *args, **kwargs) -> Point3D:
def set_location(self, new_loc: Point3D) -> None:
--------------------------------------------------

def update_target(*method_args, **method_kwargs):
def build(self) -> _MethodAnimation:
--------------------------------------------------

def override_animate(method: types.FunctionType) -> types.FunctionType:
def decorator(animation_method):

++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/opengl/opengl_point_cloud_mobject.py

--------------------------------------------------

class OpenGLPMobject(OpenGLMobject):

def reset_points(self):
def get_array_attrs(self):
def add_points(self, points, rgbas=None, color=None, opacity=None):
def thin_out(self, factor=5):
def thin_func(num_points=num_points):
def set_color_by_gradient(self, *colors):
def set_colors_by_radial_gradient(self,
    center=None,
    radius=1,
    inner_color=WHITE,
    outer_color=BLACK,
):
def match_colors(self, pmobject):
def fade_to(self, color, alpha, family=True):
def filter_out(self, condition):
def sort_points(self, function=lambda p: p[0]):
def ingest_submobjects(self):
def point_from_proportion(self, alpha):
def pointwise_become_partial(self, pmobject, a, b):
def get_shader_data(self):
def get_mobject_type_class():
--------------------------------------------------

--------------------------------------------------

class OpenGLPGroup(OpenGLPMobject):

def fade_to(self, color, alpha, family=True):
--------------------------------------------------

--------------------------------------------------

class OpenGLPMPoint(OpenGLPMobject):

def init_points(self):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/opengl/dot_cloud.py

--------------------------------------------------

class DotCloud(OpenGLPMobject):

def init_points(self):
def make_3d(self, gloss=0.5, shadow=0.2):
--------------------------------------------------

--------------------------------------------------

class TrueDot(DotCloud):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/opengl/opengl_compatibility.py

--------------------------------------------------

class ConvertToOpenGL(ABCMeta):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/opengl/opengl_vectorized_mobject.py

def triggers_refreshed_triangulation(func):
def wrapper(self, *args, **kwargs):
--------------------------------------------------

class OpenGLVMobject(OpenGLMobject):

def get_group_class(self):
def get_mobject_type_class():
def init_data(self):
def init_colors(self):
def set_fill(self,
    color: ParsableManimColor | None = None,
    opacity: float | None = None,
    recurse: bool = True,
) -> OpenGLVMobject:
def set_stroke(self,
    color=None,
    width=None,
    opacity=None,
    background=None,
    recurse=True,
):
def set_style(self,
    fill_color=None,
    fill_opacity=None,
    fill_rgba=None,
    stroke_color=None,
    stroke_opacity=None,
    stroke_rgba=None,
    stroke_width=None,
    gloss=None,
    shadow=None,
    recurse=True,
):
def get_style(self):
def match_style(self, vmobject, recurse=True):
def set_color(self, color, opacity=None, recurse=True):
def set_opacity(self, opacity, recurse=True):
def fade(self, darkness=0.5, recurse=True):
def get_fill_colors(self):
def get_fill_opacities(self):
def get_stroke_colors(self):
def get_stroke_opacities(self):
def get_stroke_widths(self):
def get_fill_color(self):
def get_fill_opacity(self):
def get_stroke_color(self):
def get_stroke_width(self):
def get_stroke_opacity(self):
def get_color(self):
def get_colors(self):
def has_stroke(self):
def has_fill(self):
def get_opacity(self):
def set_flat_stroke(self, flat_stroke=True, recurse=True):
def get_flat_stroke(self):
def set_anchors_and_handles(self, anchors1, handles, anchors2):
def start_new_path(self, point):
def add_cubic_bezier_curve(self, anchor1, handle1, handle2, anchor2):
def add_cubic_bezier_curve_to(self, handle1, handle2, anchor):
def add_quadratic_bezier_curve_to(self, handle, anchor):
def add_line_to(self, point: Sequence[float]) -> OpenGLVMobject:
def add_smooth_curve_to(self, point):
def add_smooth_cubic_curve_to(self, handle, point):
def has_new_path_started(self):
def get_last_point(self):
def get_reflection_of_last_handle(self):
def close_path(self):
def is_closed(self):
def subdivide_sharp_curves(self, angle_threshold=30 * DEGREES, recurse=True):
def add_points_as_corners(self, points):
def set_points_as_corners(self, points: Iterable[float]) -> OpenGLVMobject:
def set_points_smoothly(self, points, true_smooth=False):
def change_anchor_mode(self, mode):
def make_smooth(self):
def make_approximately_smooth(self):
def make_jagged(self):
def add_subpath(self, points):
def append_vectorized_mobject(self, vectorized_mobject):
def consider_points_equals(self, p0, p1):
def force_direction(self, target_direction: str):
def reverse_direction(self):
def get_bezier_tuples_from_points(self, points):
def get_bezier_tuples(self):
def get_subpaths_from_points(self, points):
def get_subpaths(self):
def get_nth_curve_points(self, n: int) -> np.ndarray:
def get_nth_curve_function(self, n: int) -> Callable[[float], np.ndarray]:
def get_nth_curve_function_with_length(self,
    n: int,
    sample_points: int | None = None,
) -> tuple[Callable[[float], np.ndarray], float]:
def get_num_curves(self) -> int:
def get_nth_curve_length(self,
    n: int,
    sample_points: int | None = None,
) -> float:
def get_curve_functions(self,
) -> Iterable[Callable[[float], np.ndarray]]:
def get_nth_curve_length_pieces(self,
    n: int,
    sample_points: int | None = None,
) -> np.ndarray:
def get_curve_functions_with_lengths(self, **kwargs
) -> Iterable[tuple[Callable[[float], np.ndarray], float]]:
def point_from_proportion(self, alpha: float) -> np.ndarray:
def proportion_from_point(self,
    point: Iterable[float | int],
) -> float:
def get_anchors_and_handles(self) -> Iterable[np.ndarray]:
def get_start_anchors(self) -> np.ndarray:
def get_end_anchors(self) -> np.ndarray:
def get_anchors(self) -> Iterable[np.ndarray]:
def get_points_without_null_curves(self, atol=1e-9):
def get_arc_length(self, sample_points_per_curve: int | None = None) -> float:
def get_area_vector(self):
def get_direction(self):
def get_unit_normal(self, recompute=False):
def refresh_unit_normal(self):
def align_points(self, vmobject):
def get_nth_subpath(path_list, n):
def insert_n_curves(self, n: int, recurse=True) -> OpenGLVMobject:
def insert_n_curves_to_point_list(self, n: int, points: np.ndarray) -> np.ndarray:
def interpolate(self, mobject1, mobject2, alpha, *args, **kwargs):
def pointwise_become_partial(self, vmobject: OpenGLVMobject, a: float, b: float, remap: bool = True
) -> OpenGLVMobject:
def get_subcurve(self, a: float, b: float) -> OpenGLVMobject:
def refresh_triangulation(self):
def get_triangulation(self, normal_vector=None):
def set_points(self, points):
def set_data(self, data):
def apply_function(self, function, make_smooth=False, **kwargs):
def apply_points_function(self, *args, **kwargs):
def flip(self, *args, **kwargs):
def init_shader_data(self):
def refresh_shader_wrapper_id(self):
def get_fill_shader_wrapper(self):
def update_fill_shader_wrapper(self):
def get_stroke_shader_wrapper(self):
def update_stroke_shader_wrapper(self):
def get_shader_wrapper_list(self):
def get_stroke_uniforms(self):
def get_fill_uniforms(self):
def get_stroke_shader_data(self):
def get_fill_shader_data(self):
def refresh_shader_data(self):
def get_fill_shader_vert_indices(self):
--------------------------------------------------

--------------------------------------------------

class OpenGLVGroup(OpenGLVMobject):

def add(self, *vmobjects: OpenGLVMobject):
--------------------------------------------------

--------------------------------------------------

class OpenGLVectorizedPoint(OpenGLPoint,OpenGLVMobject):

--------------------------------------------------

--------------------------------------------------

class OpenGLCurvesAsSubmobjects(OpenGLVGroup):

--------------------------------------------------

--------------------------------------------------

class OpenGLDashedVMobject(OpenGLVMobject):

--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/opengl/opengl_image_mobject.py

--------------------------------------------------

class OpenGLImageMobject(OpenGLTexturedSurface):

def get_image_from_file(self,
    image_file: str | Path | np.ndarray,
    image_mode: str,
):
--------------------------------------------------


++++++++++++++++++++++++++++++++++++++++++++++++++

Current file: manim/mobject/opengl/opengl_three_dimensions.py

--------------------------------------------------

class OpenGLSurfaceMesh(OpenGLVGroup):

def init_points(self):
--------------------------------------------------
"""


async def run_manim_code(code: str, path: str = getcwd()) -> None:
    print("Adding interactivity...")
    add_interactivity(code, path)

    name_of_file_index: str = code.find("class ")
    file_name: str = code[
        name_of_file_index + len("class ") : code.find("(", name_of_file_index)
    ]
    print(file_name)

    print("Running the scene...")
    manim_path = which("manim")
    if not manim_path:
        print("Manim executable not found.")
        return

    code_file = join(path, "generated_code.py")

    try:
        proc = await create_subprocess_exec(
            manim_path,
            "-ql",
            code_file,
            "--media_dir",
            f"{path}/output_media",
            file_name,
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
                if file.startswith(file_name):
                    video_path = join(root, file)
                    print(f"Opening video at: {video_path}")
                    await create_subprocess_exec("open", video_path)
                    return

        print("Video file not found in:", media_root)

    except Exception as e:
        print(f"Error while running Manim: {e}")


async def generate_video(
    prompt: str, path: str = getcwd(), use_local_model: bool = False
) -> None:
    GEMINI_URL: str = "https://gemini-wrapper-nine.vercel.app/gemini"

    print("Getting response...")

    PROMPT: str = f"""Your sole purpose is to convert natural language into Manim code. 
You will be given some text and must write valid Manim code to the best of your abilities.
DON'T code bugs and SOLELY OUTPUT PYTHON CODE. Import ALL the necessary libraries.
Define ALL constants. After you generate your code, check to make sure that it can run.
Ensure all the generated manim code is compatible with manim 0.19.0.
Ensure EVERY element in the scene is visually distinctive. 
Define EVERY function you use. Write text at the top to explain what you're doing.
REMEMBER, YOU MUST OUTPUT CODE THAT DOESN'T CAUSE BUGS. ASSUME YOUR CODE IS BUGGY, AND RECODE IT AGAIN.
HERE IS ALL OF THE METHODS OF THE MANIM LIBRARY, MAKE SURE YOU USE THESE METHODS SOLELY: 
{MANIM_LIBRARY_API} AND CREATE ONLY ONE MANIM CLASS. 
The prompt: {prompt}"""

    generated_code: str = ""

    if use_local_model:
        model: lms.LLM = lms.llm("deepseek-coder-v2-lite-instruct")
        prediction_stream: lms.PredictionStream = model.complete(PROMPT)
        generated_code = prediction_stream.content

    else:
        async with AsyncClient() as client:
            try:
                response: Response = await client.post(
                    GEMINI_URL, json={"prompt": PROMPT}
                )
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

        generated_code = json["output"]
        generated_code = "\n".join(generated_code.splitlines()[1:-1])

    print("Creating the interactive scene...")
    await run_manim_code(generated_code, path)
