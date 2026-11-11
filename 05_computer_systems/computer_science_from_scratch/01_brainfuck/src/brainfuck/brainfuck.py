from pathlib import Path


class Brainfuck:
    def __init__(self, file_name: str | Path):
        with open(file_name, "r") as text_file:
            self.source_code: str = text_file.read()

    def execute(self):
        cells: list[int] = [0] * 30000
        cell_index = 0
        instruction_index = 0
        while instruction_index < len(self.source_code):
            instruction = self.source_code[instruction_index]
            match instruction:
                case ">":
                    cell_index += 1
                case "<":
                    cell_index -= 1
                case "+":
                    cells[cell_index] = self.clamp0_255_wraparound(
                        cells[cell_index] + 1
                    )
                case "-":
                    cells[cell_index] = self.clamp0_255_wraparound(
                        cells[cell_index] - 1
                    )
                case ".":
                    print(chr(cells[cell_index]), end="", flush=True)
                case ",":
                    cells[cell_index] = self.clamp0_255_wraparound(int(input()))
                case "[":
                    if cells[cell_index] == 0:
                        instruction_index = self.find_bracket_match(
                            instruction_index, True
                        )
                case "]":
                    if cells[cell_index] != 0:
                        instruction_index = self.find_bracket_match(
                            instruction_index, False
                        )
            instruction_index += 1

    # find the location of the corresponding bracket to the one at start
    # if forward is true, go to the right looking for a matching "]"
    # otherwise do the reverse
    def find_bracket_match(self, start: int, forward: bool) -> int:
        in_between_brackets = 0
        direction = 1 if forward else -1
        location = start + direction
        start_bracket = "[" if forward else "]"
        end_bracket = "]" if forward else "["

        while 0 <= location < len(self.source_code):
            if self.source_code[location] == end_bracket:
                if in_between_brackets == 0:
                    return location
                in_between_brackets -= 1
            elif self.source_code[location] == start_bracket:
                in_between_brackets += 1
            location += direction

        # did not find a match
        print(f"Error: cound not find a match for {start_bracket} at {start}")
        return start

    def clamp0_255_wraparound(self, num: int) -> int:
        if num > 255:
            return 0
        elif num < 0:
            return 0
        else:
            return num
