from matplotlib import cbook

from collections.abc import Callable
from typing import Literal
import numpy as np
from numpy.typing import ArrayLike

def window_hanning(x: ArrayLike) -> ArrayLike: ...
def window_none(x: ArrayLike) -> ArrayLike: ...
def detrend(
    x: ArrayLike,
    key: Literal["default", "constant", "mean", "linear", "none"]
    | Callable[[ArrayLike, int | None], ArrayLike]
    | None = ...,
    axis: int | None = ...,
): ...
def detrend_mean(x: ArrayLike, axis: int | None = ...) -> ArrayLike: ...
def detrend_none(x: ArrayLike, axis: int | None = ...) -> ArrayLike: ...
def detrend_linear(y: ArrayLike) -> ArrayLike: ...
def psd(
    x: ArrayLike,
    NFFT: int | None = ...,
    Fs: float | None = ...,
    detrend: Literal["none", "mean", "linear"]
    | Callable[[ArrayLike, int | None], ArrayLike]
    | None = ...,
    window: Callable[[ArrayLike], ArrayLike] | ArrayLike | None = ...,
    noverlap: int | None = ...,
    pad_to: int | None = ...,
    sides: Literal["default", "onesided", "twosided"] | None = ...,
    scale_by_freq: bool | None = ...,
) -> tuple[ArrayLike, ArrayLike]: ...
def csd(
    x: ArrayLike,
    y: ArrayLike | None,
    NFFT: int | None = ...,
    Fs: float | None = ...,
    detrend: Literal["none", "mean", "linear"]
    | Callable[[ArrayLike, int | None], ArrayLike]
    | None = ...,
    window: Callable[[ArrayLike], ArrayLike] | ArrayLike | None = ...,
    noverlap: int | None = ...,
    pad_to: int | None = ...,
    sides: Literal["default", "onesided", "twosided"] | None = ...,
    scale_by_freq: bool | None = ...,
) -> tuple[ArrayLike, ArrayLike]: ...
def complex_spectrum(
    x: ArrayLike,
    Fs: float | None = ...,
    window: Callable[[ArrayLike], ArrayLike] | ArrayLike | None = ...,
    pad_to: int | None = ...,
    sides: Literal["default", "onesided", "twosided"] | None = ...,
) -> tuple[ArrayLike, ArrayLike]: ...
def magnitude_spectrum(
    x: ArrayLike,
    Fs: float | None = ...,
    window: Callable[[ArrayLike], ArrayLike] | ArrayLike | None = ...,
    pad_to: int | None = ...,
    sides: Literal["default", "onesided", "twosided"] | None = ...,
) -> tuple[ArrayLike, ArrayLike]: ...
def angle_spectrum(
    x: ArrayLike,
    Fs: float | None = ...,
    window: Callable[[ArrayLike], ArrayLike] | ArrayLike | None = ...,
    pad_to: int | None = ...,
    sides: Literal["default", "onesided", "twosided"] | None = ...,
) -> tuple[ArrayLike, ArrayLike]: ...
def phase_spectrum(
    x: ArrayLike,
    Fs: float | None = ...,
    window: Callable[[ArrayLike], ArrayLike] | ArrayLike | None = ...,
    pad_to: int | None = ...,
    sides: Literal["default", "onesided", "twosided"] | None = ...,
) -> tuple[ArrayLike, ArrayLike]: ...
def specgram(
    x: ArrayLike,
    NFFT: int | None = ...,
    Fs: float | None = ...,
    detrend: Literal["none", "mean", "linear"]
    | Callable[[ArrayLike, int | None], ArrayLike]
    | None = ...,
    window: Callable[[ArrayLike], ArrayLike] | ArrayLike | None = ...,
    noverlap: int | None = ...,
    pad_to: int | None = ...,
    sides: Literal["default", "onesided", "twosided"] | None = ...,
    scale_by_freq: bool | None = ...,
    mode: Literal["psd", "complex", "magnitude", "angle", "phase"] | None = ...,
): ...
def cohere(
    x: ArrayLike,
    y: ArrayLike,
    NFFT: int = ...,
    Fs: float = ...,
    detrend: Literal["none", "mean", "linear"]
    | Callable[[ArrayLike, int | None], ArrayLike] = ...,
    window: Callable[[ArrayLike], ArrayLike] | ArrayLike = ...,
    noverlap: int = ...,
    pad_to: int | None = ...,
    sides: Literal["default", "onesided", "twosided"] = ...,
    scale_by_freq: bool | None = ...,
): ...

class GaussianKDE:
    dataset: ArrayLike
    dim: int
    num_dp: int
    factor: float
    data_covariance: ArrayLike
    data_inv_cov: ArrayLike
    covariance: ArrayLike
    inv_cov: ArrayLike
    norm_factor: float
    def __init__(
        self,
        dataset: ArrayLike,
        bw_method: Literal["scott", "silverman"]
        | float
        | Callable[[GaussianKDE], float]
        | None = ...,
    ) -> None: ...
    def scotts_factor(self) -> float: ...
    def silverman_factor(self) -> float: ...
    def covariance_factor(self) -> float: ...
    def evaluate(self, points: ArrayLike) -> np.ndarray: ...
    def __call__(self, points: ArrayLike) -> np.ndarray: ...
