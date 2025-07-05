from z3 import Real, Solver, Or, sat, And

def verify_portfolio_with_fp_error():
    # Symbolic variables
    w1, w2, w3 = Real('w1'), Real('w2'), Real('w3')
    r1, r2, r3 = Real('r1'), Real('r2'), Real('r3')
    epsilon = Real('epsilon')  # Small drift

    # Portfolio return + error term
    portfolio_return = w1 * r1 + w2 * r2 + w3 * r3 + epsilon

    constraints = [
        w1 >= 0, w1 <= 1,
        w2 >= 0, w2 <= 1,
        w3 >= 0, w3 <= 1,
        (w1 + w2 + w3) <= 1,
        r1 >= -1, r1 <= 1,
        r2 >= -1, r2 <= 1,
        r3 >= -1, r3 <= 1,
        epsilon >= -0.001, epsilon <= 0.001  # Simulating small numerical drift
    ]

    solver = Solver()
    solver.add(constraints)
    solver.add(Or(portfolio_return < -1, portfolio_return > 1))  # Violation check

    result = solver.check()

    if result == sat:
        return "Violation with numerical drift!", solver.model()
    else:
        return "Property holds even under small numerical errors."

if __name__ == "__main__":
    print(verify_portfolio_with_fp_error())