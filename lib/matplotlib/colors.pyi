from ._color_data import BASE_COLORS, CSS4_COLORS, TABLEAU_COLORS, XKCD_COLORS
from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from matplotlib import cbook, scale
import re

from typing import Any, Literal, TypeAlias, overload

import numpy as np
from numpy.typing import ArrayLike

Color: TypeAlias = tuple[float, float, float] | tuple[float, float, float, float] | str

class _ColorMapping(dict[str, Color]):
    cache: dict[tuple[Color, float | None], tuple[float, float, float, float]]
    def __init__(self, mapping) -> None: ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...

def get_named_colors_mapping() -> _ColorMapping: ...

class ColorSequenceRegistry(Mapping):
    def __init__(self) -> None: ...
    def __getitem__(self, item: str) -> list[Color]: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def register(self, name: str, color_list: Iterable[Color]) -> None: ...
    def unregister(self, name: str) -> None: ...

_color_sequences: ColorSequenceRegistry = ...

def is_color_like(c: Any) -> bool: ...
def same_color(c1: Color, c2: Color) -> bool: ...
def to_rgba(
    c: Color, alpha: float | None = ...
) -> tuple[float, float, float, float]: ...
def to_rgba_array(
    c: Color | ArrayLike, alpha: float | ArrayLike | None = ...
) -> np.ndarray: ...
def to_rgb(c: Color) -> tuple[float, float, float]: ...
def to_hex(c: Color, keep_alpha: bool = ...) -> str: ...

cnames: dict[str, Color]
hexColorPattern: re.Pattern
rgb2hex = to_hex
hex2color = to_rgb

class ColorConverter:
    colors: _ColorMapping
    cache: dict[tuple[Color, float | None], tuple[float, float, float, float]]
    @staticmethod
    def to_rgb(c: Color) -> tuple[float, float, float]: ...
    @staticmethod
    def to_rgba(
        c: Color, alpha: float | None = ...
    ) -> tuple[float, float, float, float]: ...
    @staticmethod
    def to_rgba_array(
        c: Color | ArrayLike, alpha: float | ArrayLike | None = ...
    ) -> np.ndarray: ...

colorConverter: ColorConverter

class Colormap:
    name: str
    N: int
    colorbar_extend: bool
    def __init__(self, name: str, N: int = ...) -> None: ...
    def __call__(
        self, X: ArrayLike, alpha: ArrayLike | None = ..., bytes: bool = ...
    ) -> tuple[float, float, float, float] | np.ndarray: ...
    def __copy__(self) -> Colormap: ...
    def __eq__(self, other: object) -> bool: ...
    def get_bad(self) -> np.ndarray: ...
    def set_bad(self, color: Color = ..., alpha: float | None = ...) -> None: ...
    def get_under(self) -> np.ndarray: ...
    def set_under(self, color: Color = ..., alpha: float | None = ...) -> None: ...
    def get_over(self) -> np.ndarray: ...
    def set_over(self, color: Color = ..., alpha: float | None = ...) -> None: ...
    def set_extremes(
        self,
        *,
        bad: Color | None = ...,
        under: Color | None = ...,
        over: Color | None = ...
    ) -> None: ...
    def with_extremes(
        self,
        *,
        bad: Color | None = ...,
        under: Color | None = ...,
        over: Color | None = ...
    ) -> Colormap: ...
    def is_gray(self) -> bool: ...
    def resampled(self, lutsize: int) -> Colormap: ...
    def reversed(self, name: str | None = ...) -> Colormap: ...
    def copy(self) -> Colormap: ...

class LinearSegmentedColormap(Colormap):
    monochrome: bool
    def __init__(
        self,
        name: str,
        segmentdata: dict[
            Literal["red", "green", "blue", "alpha"], Sequence[tuple[float, ...]]
        ],
        N: int = ...,
        gamma: float = ...,
    ) -> None: ...
    def set_gamma(self, gamma: float) -> None: ...
    @staticmethod
    def from_list(
        name: str, colors: ArrayLike, N: int = ..., gamma: float = ...
    ) -> LinearSegmentedColormap: ...
    def resampled(self, lutsize: int) -> LinearSegmentedColormap: ...
    def reversed(self, name: str | None = ...) -> LinearSegmentedColormap: ...

class ListedColormap(Colormap):
    monochrome: bool
    colors: ArrayLike | Color
    def __init__(
        self, colors: ArrayLike | Color, name: str = ..., N: int | None = ...
    ) -> None: ...
    def resampled(self, lutsize: int) -> ListedColormap: ...
    def reversed(self, name: str | None = ...) -> ListedColormap: ...

class Normalize:
    callbacks: cbook.CallbackRegistry
    def __init__(
        self, vmin: float | None = ..., vmax: float | None = ..., clip: bool = ...
    ) -> None: ...
    @property
    def vmin(self) -> float | None: ...
    @vmin.setter
    def vmin(self, value: float | None) -> None: ...
    @property
    def vmax(self) -> float | None: ...
    @vmax.setter
    def vmax(self, value: float | None) -> None: ...
    @property
    def clip(self) -> bool: ...
    @clip.setter
    def clip(self, value: bool) -> None: ...
    @staticmethod
    def process_value(value: ArrayLike) -> tuple[np.ma.MaskedArray, bool]: ...
    def __call__(self, value: ArrayLike, clip: bool | None = ...) -> ArrayLike: ...
    def inverse(self, value: ArrayLike) -> ArrayLike: ...
    def autoscale(self, A: ArrayLike) -> None: ...
    def autoscale_None(self, A: ArrayLike) -> None: ...
    def scaled(self) -> bool: ...

class TwoSlopeNorm(Normalize):
    def __init__(
        self, vcenter: float, vmin: float | None = ..., vmax: float | None = ...
    ) -> None: ...
    @property
    def vcenter(self) -> float: ...
    @vcenter.setter
    def vcenter(self, value: float) -> None: ...
    def autoscale_None(self, A: ArrayLike) -> None: ...
    def __call__(self, value: ArrayLike, clip: bool | None = ...) -> ArrayLike: ...
    def inverse(self, value: ArrayLike) -> ArrayLike: ...

class CenteredNorm(Normalize):
    def __init__(
        self, vcenter: float = ..., halfrange: float | None = ..., clip: bool = ...
    ) -> None: ...
    @property
    def vcenter(self) -> float: ...
    @vcenter.setter
    def vcenter(self, vcenter: float) -> None: ...
    @property
    def halfrange(self) -> float: ...
    @halfrange.setter
    def halfrange(self, halfrange: float) -> None: ...

@overload
def make_norm_from_scale(
    scale_cls: type[scale.ScaleBase],
    base_norm_cls: type[Normalize],
    *,
    init: Callable | None = ...
) -> type[Normalize]: ...
@overload
def make_norm_from_scale(
    scale_cls: type[scale.ScaleBase],
    base_norm_cls: None = ...,
    *,
    init: Callable | None = ...
) -> Callable[[type[Normalize]], type[Normalize]]: ...

class FuncNorm(Normalize): ...
class LogNorm(Normalize): ...

class SymLogNorm(Normalize):
    @property
    def linthresh(self) -> float: ...
    @linthresh.setter
    def linthresh(self, value: float) -> None: ...

class AsinhNorm(Normalize):
    @property
    def linear_width(self) -> float: ...
    @linear_width.setter
    def linear_width(self, value: float) -> None: ...

class PowerNorm(Normalize):
    gamma: float
    def __init__(
        self,
        gamma: float,
        vmin: float | None = ...,
        vmax: float | None = ...,
        clip: bool = ...,
    ) -> None: ...
    def __call__(self, value: ArrayLike, clip: bool | None = ...) -> ArrayLike: ...
    def inverse(self, value: ArrayLike) -> ArrayLike: ...

class BoundaryNorm(Normalize):
    boundaries: np.ndarray
    N: int
    Ncmap: int
    extend: Literal["neither", "both", "min", "max"]
    def __init__(
        self,
        boundaries: ArrayLike,
        ncolors: int,
        clip: bool = ...,
        *,
        extend: Literal["neither", "both", "min", "max"] = ...
    ) -> None: ...
    def __call__(self, value: ArrayLike, clip: bool | None = ...) -> ArrayLike: ...
    def inverse(self, value: ArrayLike) -> ArrayLike: ...

class NoNorm(Normalize):
    def __call__(self, value: ArrayLike, clip: bool | None = ...) -> ArrayLike: ...
    def inverse(self, value: ArrayLike) -> ArrayLike: ...

def rgb_to_hsv(arr: ArrayLike) -> np.ndarray: ...
def hsv_to_rgb(hsv: ArrayLike) -> np.ndarray: ...

class LightSource:
    azdeg: float
    altdeg: float
    hsv_min_val: float
    hsv_max_val: float
    hsv_min_sat: float
    hsv_max_sat: float
    def __init__(
        self,
        azdeg: float = ...,
        altdeg: float = ...,
        hsv_min_val: float = ...,
        hsv_max_val: float = ...,
        hsv_min_sat: float = ...,
        hsv_max_sat: float = ...,
    ) -> None: ...
    @property
    def direction(self) -> np.ndarray: ...
    def hillshade(
        self,
        elevation: ArrayLike,
        vert_exag: float = ...,
        dx: float = ...,
        dy: float = ...,
        fraction: float = ...,
    ) -> np.ndarray: ...
    def shade_normals(
        self, normals: np.ndarray, fraction: float = ...
    ) -> np.ndarray: ...
    def shade(
        self,
        data: ArrayLike,
        cmap: Colormap,
        norm: Normalize | None = ...,
        blend_mode: Literal["hsv", "overlay", "soft"] | Callable = ...,
        vmin: float | None = ...,
        vmax: float | None = ...,
        vert_exag: float = ...,
        dx: float = ...,
        dy: float = ...,
        fraction: float = ...,
        **kwargs
    ) -> np.ndarray: ...
    def shade_rgb(
        self,
        rgb: ArrayLike,
        elevation: ArrayLike,
        fraction: float = ...,
        blend_mode: Literal["hsv", "overlay", "soft"] | Callable = ...,
        vert_exag: float = ...,
        dx: float = ...,
        dy: float = ...,
        **kwargs
    ) -> np.ndarray: ...
    def blend_hsv(
        self,
        rgb: ArrayLike,
        intensity: ArrayLike,
        hsv_max_sat: float | None = ...,
        hsv_max_val: float | None = ...,
        hsv_min_val: float | None = ...,
        hsv_min_sat: float | None = ...,
    ) -> ArrayLike: ...
    def blend_soft_light(
        self, rgb: np.ndarray, intensity: np.ndarray
    ) -> np.ndarray: ...
    def blend_overlay(self, rgb: np.ndarray, intensity: np.ndarray) -> np.ndarray: ...

def from_levels_and_colors(
    levels: Sequence[float],
    colors: Sequence[Color],
    extend: Literal["neither", "min", "max", "both"] = ...,
) -> tuple[ListedColormap, BoundaryNorm]: ...
