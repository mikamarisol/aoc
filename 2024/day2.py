import numpy as np


def read_reports():
    with open('resources/reactor_reports.txt') as reports_file:
        reports = [np.array(line.strip().split(), dtype=int) for line in reports_file.readlines()]
        return reports


def count_safe_reports(reports):
    count = 0
    for report in reports:
        if is_report_safe(report):
            count += 1
    return count


def is_report_safe(report):
    level_delta = np.array([report[i + 1] - report[i] for i in range(len(report) - 1)])
    delta_signs = set(np.sign(level_delta))
    delta_magnitudes = set(abs(level_delta))

    return (delta_signs == {1} or delta_signs == {-1}) and delta_magnitudes.issubset({1, 2, 3})


if __name__ == '__main__':
    reports = read_reports()
    print(reports)
    print(count_safe_reports(reports))