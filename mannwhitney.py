import scipy


def mann_whitney():
    hairy = [10, 10, 8, 9, 7, 9, 9, 5, 9, 8]
    non_hairy = [7, 5, 6, 4, 8, 5, 6, 6, 1, 3]
    print(scipy.stats.mannwhitneyu(hairy, non_hairy))
    print(scipy.stats.mannwhitneyu(non_hairy, hairy))


def fisher():
    table = [[6, 0], [1, 5]]
    print(scipy.stats.fisher_exact(table))


def mcnemar():
    table = [[3, 9], [0, 3]]
    b = table[0][1]
    c = table[1][0]
    chi_2 = ((abs(b - c) - 1) ** 2) / (b + c)

    print(scipy.stats.chi2.pdf(chi_2, 1))


def wilcoxon():
    x = [9, 6, 5, 7, 6, 5, 6, 4, 6, 7, 7, 8]
    y = [9, 10, 8, 8, 10, 9, 6, 11, 12, 6, 12, 10]
    print(scipy.stats.wilcoxon(x, y))


def kolmogorov_smirnov():
    # marathon_data =
    # rvs = scipy.stats.norm
    # cdf = scipy.stats.
    # print(scipy.stats.kstest(rvs, cdf, N=2))
    pass


if __name__ == '__main__':
    # mann_whitney()
    fisher()
    mcnemar()
    wilcoxon()
    kolmogorov_smirnov()
