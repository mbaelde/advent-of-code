from typing import List


class MirageMaintenance:
    """Class for calculating extrapolated values in a number series.

    Attributes:
        series (List[int]): The series of numbers to analyze.
    """

    def __init__(self, series: List[int]) -> None:
        self.series = series

    def find_next_value(self) -> int:
        """Finds the next extrapolated value in the series.

        Returns:
            int: The next value in the series.
        """
        return self.extrapolate(self.series, forward=True)

    def find_previous_value(self) -> int:
        """Finds the previous extrapolated value in the series.

        Returns:
            int: The previous value in the series.
        """
        return self.extrapolate(self.series, forward=False)

    def extrapolate(self, series: List[int], forward: bool = True) -> int:
        """Extrapolates the next or previous value in the series based on the direction.

        Args:
            series (List[int]): The series to extrapolate.
            forward (bool): True to extrapolate forward, False for backward.

        Returns:
            int: The extrapolated value.
        """
        sequences = [series]
        while sequences[-1].count(0) != len(sequences[-1]):
            if forward:
                new_sequence = [
                    sequences[-1][i + 1] - sequences[-1][i]
                    for i in range(len(sequences[-1]) - 1)
                ]
            else:
                new_sequence = [
                    sequences[-1][i] - sequences[-1][i - 1]
                    for i in range(1, len(sequences[-1]))
                ]
            sequences.append(new_sequence)

        for i in range(len(sequences) - 2, -1, -1):
            if forward:
                sequences[i].append(sequences[i][-1] + sequences[i + 1][-1])
            else:
                sequences[i].insert(0, sequences[i][0] - sequences[i + 1][0])

        return sequences[0][-1 if forward else 0]


def main():
    file_path = "input.txt"

    # Part One
    with open(file_path, "r") as file:
        lines = file.readlines()

    sum_of_extrapolated_values = sum(
        MirageMaintenance(list(map(int, line.strip().split()))).find_next_value()
        for line in lines
    )
    print(f"Sum of next extrapolated values: {sum_of_extrapolated_values}")

    # Part Two
    sum_of_previous_extrapolated_values = sum(
        MirageMaintenance(list(map(int, line.strip().split()))).find_previous_value()
        for line in lines
    )
    print(f"Sum of previous extrapolated values: {sum_of_previous_extrapolated_values}")


if __name__ == "__main__":
    main()
