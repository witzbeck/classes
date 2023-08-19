from math import sqrt

from scipy.stats import norm

def norm_mean(p: float, n: int):
    return p * n

def norm_stddev(p: float, n: int, samplesize: int = None):
    var = n * p * (1 - p)
    stddev = sqrt(var)
    if samplesize is None:
        return stddev
    else:
        return stddev / samplesize    

def zfactor(α: float):
    return norm.ppf(α / 2)

def bounds(α: float, mean: float, stddev: float):
    lbound = mean + stddev * zfactor(α)
    ubound = mean - stddev * zfactor(α)
    return lbound, ubound

def z(val: float,
      mean: float,
      stddev: float,
      ) -> float:
    return (val - mean) / stddev

def type2(p: float,
          n: int,
          α: float,
          rv, # Random Variable
          mean: float = None,
          stddev: float = None,
          ) -> float:
    if mean is None:
        mean = n * p
    if stddev is None:
        stddev = n * p * (1 - p)
    zlow, zupp = bounds(α, mean, stddev)
    # zlow = z(lowerb, mean, stddev)
    # zupp = z(upperb, mean, stddev)
    inner_p = rv.cdf(zupp) - rv.cdf(zlow)
    return 1 - inner_p
