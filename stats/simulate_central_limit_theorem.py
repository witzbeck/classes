import numpy as np
from pandas import DataFrame
from numpy.random import randn
import math
from matplotlib.pyplot import subplots, ylabel
from scipy.stats import beta, poisson


def gen_sample(
        size: int,
        mean: float,
        stddev: float,
) -> np.array:
    while True:
        yield stddev * randn(size) + mean


def central_limit_sim(
        n_sims: int,
        size: int,
        mean: float | int = 0,
        stddev: float = 1,
) -> DataFrame:
    rng = range(n_sims)
    sim_gen = gen_sample(size, mean, stddev)
    samples = [next(sim_gen) for _ in rng]
    dct = {
        "Simulation": [i for i in rng],
        "Mean": [x.mean() for x in samples],
        "Variance": [x.var() for x in samples]
    }
    return DataFrame.from_dict(dct)

    
def clt_hist(
        n_sims: int,
        size: int,
        mean: float | int = 0,
        stddev: float = 1,
        nrows: int = 1,
        ncols: int = 2,
        figsize: tuple[int] = (16, 9)
        ) -> None:
    df = central_limit_sim(
        n_sims,
        size,
        mean=mean,
        stddev=stddev,
    )
    fig, axs = subplots(
        nrows=nrows,
        ncols=ncols,
        figsize=figsize,
        sharey=True
        )
    bins = n_sims // 2
    axs[0].hist(df.Mean, label="Mean")
    axs[1].hist(df.Variance, label="Variance")
    ylabel("Frequency")
    return fig, axs
