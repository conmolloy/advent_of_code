import re


def solve(inp: list[str], red: int, green: int, blue: int) -> int:
    hold = {}
    for line in inp:
        game_id = re.search(r"Game (\d+):", line).group(1).strip()
        colors = re.findall(r"(\d+)\s*(red|green|blue)", line, flags=re.IGNORECASE)

        counts = {"red": 0, "green": 0, "blue": 0}
        for count, color in colors:
            if int(count) > counts[color.lower()]:
                counts[color.lower()] = int(count)

        hold[game_id] = counts

    final_score = 0
    for k, v in hold.items():
        if v["red"] <= red and v["green"] <= green and v["blue"] <= blue:
            final_score += int(k)
    return final_score


def solve_pt2(inp: list[str]) -> int:
    hold = {}
    for line in inp:
        game_id = re.search(r"Game (\d+):", line).group(1).strip()
        colors = re.findall(r"(\d+)\s*(red|green|blue)", line, flags=re.IGNORECASE)

        counts = {"red": 0, "green": 0, "blue": 0}
        for count, color in colors:
            if int(count) > counts[color.lower()]:
                counts[color.lower()] = int(count)

        hold[game_id] = counts

    final_score = 0
    for _, v in hold.items():
        final_score += v["red"] * v["green"] * v["blue"]
    return final_score


if __name__ == "__main__":
    test = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    print(solve(test.split("\n"), red=12, green=13, blue=14))

    with open("input.txt", "r") as file:
        content_list = file.read().splitlines()

    # part 2
    print(solve(content_list, red=12, green=13, blue=14))

    print(solve_pt2(content_list))
