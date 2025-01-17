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
    # score(solution_file, dataset)

# solve_problem('./datasets/a_example.txt')
# solve_problem('./datasets/b_read_on.txt')
# solve_problem('./datasets/c_incunabula.txt')
solve_problem('./datasets/d_tough_choices.txt')