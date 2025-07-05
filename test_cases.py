from verifloat import verify_portfolio_return
from verifloat_fp import verify_portfolio_with_fp_error
from verifloat_multi import verify_two_period_portfolio

def run_all_tests():
    print("\nRunning Basic Portfolio Return Test:")
    print(verify_portfolio_return())

    print("\nRunning Floating-Point Drift Test:")
    print(verify_portfolio_with_fp_error())

    print("\nRunning Multi-Period Portfolio Return Test:")
    print(verify_two_period_portfolio())

if __name__ == "__main__":
    run_all_tests()
