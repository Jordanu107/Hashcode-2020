# Import functions from the different py files
from scoring import score
from output import write
from parsing import parse
from solver import solve

SUBMISSION_FILENAME = "submission.txt"

# Solve Problem executes the four steps: read from input, solve, output and score
def solve_problem(filename):
    dataset = parse(filename)
    solution = solve(dataset)
    solution_file = write(solution, SUBMISSION_FILENAME)
    score(solution_file, SUBMISSION_FILENAME)

solve_problem('./datasets/a_example.txt')