from z3 import Real, Solver, And, Or, sat

def verify_two_period_portfolio():
    # Period 1
    w1, w2, w3 = Real('w1'), Real('w2'), Real('w3')
    r1_1, r2_1, r3_1 = Real('r1_1'), Real('r2_1'), Real('r3_1')
    
    # Period 2
    r1_2, r2_2, r3_2 = Real('r1_2'), Real('r2_2'), Real('r3_2')
    
    # Constraints
    constraints = [
        w1 >= 0, w1 <= 1,
        w2 >= 0, w2 <= 1,
        w3 >= 0, w3 <= 1,
        (w1 + w2 + w3) <= 1,
    ]

    for r in [r1_1, r2_1, r3_1, r1_2, r2_2, r3_2]:
        constraints += [r >= -1, r <= 1]

    # Period 1 return
    period1_return = w1 * r1_1 + w2 * r2_1 + w3 * r3_1
    # Period 2 return
    period2_return = w1 * r1_2 + w2 * r2_2 + w3 * r3_2
    # Total return (simplified sum)
    total_return = period1_return + period2_return

    solver = Solver()
    solver.add(constraints)
    solver.add(Or(total_return < -2, total_return > 2))

    result = solver.check()

    if result == sat:
        print("Violation found in multi-period model!")
        print(solver.model())
    else:
        print("Multi-period portfolio return is consistent.")

if __name__ == "__main__":
    verify_two_period_portfolio()