class PipeMaze:
    def __init__(self, file_path):
        self.file_path = file_path
        self.grid = []
        self.height = 0
        self.width = 0
        self.start_x = -1
        self.start_y = -1
        self.loop_grid = []  # for part 2
        self.load_grid()
        self.find_start()

    def load_grid(self):
        with open(self.file_path, "r") as f:
            self.grid = f.read().strip().split("\n")
        self.height = len(self.grid)
        self.width = len(self.grid[0]) if self.height > 0 else 0
        self.loop_grid = [[0] * self.width for _ in range(self.height)]

    def find_start(self):
        for i, row in enumerate(self.grid):
            if "S" in row:
                self.start_x = i
                self.start_y = row.find("S")
                return
        raise ValueError("Start position not found")

    def solve_puzzle(self):
        self.trace_loop()
        max_distance = self.find_max_distance()
        enclosed_area = self.calculate_enclosed_area()
        return max_distance, enclosed_area

    def trace_loop(self):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        happy = ["-7J", "|LJ", "-FL", "|F7"]
        Sdirs = self.get_start_directions(dirs, happy)

        transform = {
            (0, "-"): 0,
            (0, "7"): 1,
            (0, "J"): 3,
            (2, "-"): 2,
            (2, "F"): 1,
            (2, "L"): 3,
            (1, "|"): 1,
            (1, "L"): 0,
            (1, "J"): 2,
            (3, "|"): 3,
            (3, "F"): 0,
            (3, "7"): 2,
        }

        curdir = Sdirs[0]
        cx, cy = self.start_x + dirs[curdir][0], self.start_y + dirs[curdir][1]
        while (cx, cy) != (self.start_x, self.start_y):
            self.loop_grid[cx][cy] = 1
            curdir = transform[(curdir, self.grid[cx][cy])]
            cx += dirs[curdir][0]
            cy += dirs[curdir][1]
        self.loop_grid[self.start_x][self.start_y] = 1

    def get_start_directions(self, dirs, happy):
        Sdirs = []
        for i, pos in enumerate(dirs):
            bx, by = self.start_x + pos[0], self.start_y + pos[1]
            if 0 <= bx < self.height and 0 <= by < self.width and self.grid[bx][by] in happy[i]:
                Sdirs.append(i)
        return Sdirs

    def find_max_distance(self):
        distance = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.loop_grid[i][j] == 1:
                    distance += 1
        return distance // 2

    def calculate_enclosed_area(self):
        count = 0
        for i in range(self.height):
            inside = False
            for j in range(self.width):
                if self.loop_grid[i][j]:
                    if self.grid[i][j] in "|JL" or (self.grid[i][j] == "S" and 3 in self.get_start_directions([(0, 1), (1, 0), (0, -1), (-1, 0)], ["-7J", "|LJ", "-FL", "|F7"])):
                        inside = not inside
                else:
                    count += inside
        return count

# Usage
maze = PipeMaze("input.txt")
max_distance, enclosed_area = maze.solve_puzzle()
print(f"Max distance: {max_distance}")
print(f"Enclosed area: {enclosed_area}")
