import typer, requests, json, os, subprocess
from typing_extensions import Annotated
from pathlib import Path
from datetime import datetime
from rich import print

def main(
        aoc_session: Annotated[str, typer.Argument(envvar="AOC_SESSION")],
        day: Annotated[int, typer.Option()] = datetime.today().day,
        year: Annotated[int, typer.Option()] = datetime.today().year,
        ):

    selected_date = f"day{str(day).zfill(2)}"

    path = f"{year}/{selected_date}"

    if os.path.exists(f"{path}"):
        print(f"Project for {selected_date} already exists, not overwriting")
    else:
        os.makedirs(f"{year}", exist_ok=True)
        subprocess.run(f"cp -r ./template {year}/{selected_date}", shell=True)


    session = requests.Session()
    session.cookies.set("session", aoc_session)

    print(f"Getting Puzzle for {path}")
    puzzle_input = session.get(
        f"https://adventofcode.com/{year}/day/{day}/input",
        ).text[:-1]

    with open(f"{path}/task_input/input.txt", "w") as f:
        f.write(puzzle_input)

    subprocess.run(
        (
        f"code ./{path} "
        f"./{path}/task_input/test_1.txt "
        f"./{path}/tests/test_solve.py "
        f"./{path}/solver/part_1.py "
        f"./{path}/solver/part_2.py"
        ),
        shell=True,
    )

    subprocess.run(
        f"cd {path} && uv run ptw -c --ignore .venv --ext .txt,.py -- -s -raFP -W ignore::pytest.PytestReturnNotNoneWarning -p no:cacheprovider", shell=True
    )


if __name__ == "__main__":
    typer.run(main)
