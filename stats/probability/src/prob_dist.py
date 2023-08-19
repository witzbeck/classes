from math import comb, factorial as fact, e

from matplotlib.pyplot import subplots as plt


def binom(n: int,   # number of trials
          k: int,   # number of successes 
          p: float  # prob of success
          ):
    q = 1 - p           # prob of failure
    n_fails = n - k     # number of failures
    ways = comb(n, k)   # number of ways to pick k from n

    return ways * (p ** k) * (q ** n_fails)


def binom_dist(n: int,      # number of trials
               p: float,
               max_iter: int = None):   # prob of success)
    if max_iter is None:
        _range = range(n + 1)
    else:
        _range = range(max_iter)
    return {
        "x": [x for x in _range],
        "prob": [binom(n, k, p) for k in _range]
    } 


def geom(
    k: int,     # number of failures
    p: float    # prob of success
):
    q = 1 - p   # prob of failure
    j = k - 1   # number of failures before 1st success

    return p * (q ** j)


def geom_dist(
    p: float,               # prob of success
    min_prob: float = 1e-4  # prob below which to stop dist
):
    k = prob = 1
    k_list = []
    prob_list = []
    while prob > min_prob:
        prob = geom(k, p)
        k_list.append(k)
        prob_list.append(prob)
        k += 1

    return {
        "k": k_list,
        "prob": prob_list
    } 


def neg_binom(
    k: int,     # number of trials
    r: int,     # number of successes
    p: float    # prob of one success
):
    q = 1 - p   # prob of single failure
    if (k > 0 and r > 0):
        ways = comb(k - 1, r - 1)
    else:
        ways = 1
    prob_fails = q ** (k - r)   # number of failures to occur
    return ways * (p ** r) * prob_fails


def neg_binom_dist(
    r: int,                 # number of successes    
    p: float,               # prob of success
    min_prob: float = 1e-3  # prob below which to stop dist
):
    k = r
    prob = 1
    k_list = []
    prob_list = []
    while prob > min_prob:
        prob = neg_binom(k, r, p)
        k_list.append(k)
        prob_list.append(prob)
        k += 1

    return {
        "k": k_list,
        "prob": prob_list
    }


def hgeom(
    k: int,         # number of r-type 
    n: int,         # count of total units
    r: int,         # count of units of interest
    m: int          # count of units selected without replacement
):
    r_not = n - r   # count of units of not interest
    numer = comb(r, k) * comb(r_not, m - k)
    denom = comb(n, m)
    return numer / denom

def hgeom_dist(
    n: int,         # count of total units
    r: int,         # count of units of interest
    m: int,          # count of units selected without replacement
    min_prob = 1e-4
):
    k = 0
    prob = 1
    k_list = []
    prob_list = []
    while prob > min_prob:
        prob = hgeom(k, n, r, m)
        k_list.append(k)
        prob_list.append(prob)
        k += 1

    return {
        "k": k_list,
        "prob": prob_list
    }

def pois(
    k: int,         # number of periods before occurance
    λ: float        # avg of occurances / period
):
    numer = (λ ** k) 
    denom = fact(k) * (e ** (λ))
    return numer / denom


def pois_dist(
    λ: float,       # avg of occurances / period
    min_prob: float = 1e-8,
):
    k = 0
    prob = 1
    k_list = []
    prob_list = []
    while not prob < min_prob:
        prob = pois(k, λ)
        k_list.append(k)
        prob_list.append(prob)
        k += 1

    return {
        "x": k_list,
        "prob": prob_list
    }


def show_dist(dist_dict: dict,
              figsize: tuple = (8, 4.5),
              label: str = None
              ):
    keys = list(dist_dict.keys())
    x_key = keys[0]
    y_key = keys[-1]
    
    x = dist_dict[x_key]
    y = dist_dict[y_key]
    fig, ax = plt(1, 1, figsize=figsize)
    ax.set_xlabel(x_key)
    ax.set_ylabel(f"P(X = {x_key})")
    ax.scatter(x, y, label=label)
    if label is not None:
        ax.legend()
    return ax


dist_def = {
    "binomial": {
        "parameters": {
            "n": "fixed number of independent trials",
            "k": "number of successes",
            "p": "prob of success for each trial"
        },
        "formula": "p(X = k) = comb(n, k) * p^k * (1 - p)^(n - k)",
        "definition": "prob of k successes in n trials",
        "freq_func": binom,
        "dist_func": binom_dist,
    },
    "geometric": {
        "parameters": {
            "p": "prob of success for each trial",
            "k": "total number of trials including first success",
        },
        "formula": "p(X = k) = p * (1 - p)^(k - 1)",
        "definition": "prob of k trials before first success",
        "freq_func": geom,
        "dist_func": geom_dist,
    },
    "negative binomial": {
        "parameters": {
            "p": "prob of success for each trial",
            "k": "total number of trials",
            "r": "count of successes in k trials",
        },
        "formula": "p(X = k) = comb(k - 1, r - 1) * p^r * (1 - p)^(k - r)",
        "definition": "prob of k trials before r successes",
        "freq_func": neg_binom,
        "dist_func": neg_binom_dist,
    },
    "hypergeometric": {
        "parameters": {
            "r": "count of units of interest in n",
            "n": "total number of available units",
            "m": "number selected from n",
        },
        "formula": """p(X = k) = comb(r, k) *
                                 comb(n - r, m - k) / 
                                 comb(n, m)""",
        "definition": """prob of selecting k units of interest
                         from m units selected when selecting 
                         from n units containing r units of interest
                         """,
        "freq_func": hgeom,
        "dist_func": hgeom_dist,
    },
    "poisson": {
        "parameters": {
            "λ": "avg count of successes per unit time",
        },
        "formula": "p(X = k) = λ^k * e^-λ / k!",
        "definition": "prob of k trials before r successes",
        "freq_func": pois,
        "dist_func": pois_dist,
    },
}

if __name__ == '__main__':
    show_dist(geom_dist(.3))
