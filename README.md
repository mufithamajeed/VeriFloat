# VeriFloat — Lightweight Formal Verification of Financial Model Consistency Using Z3

---

## Overview

**VeriFloat** is a lightweight, formal verification tool for financial models, built using the **Z3 SMT Solver**.  
It symbolically verifies that numerical properties (such as portfolio constraints or risk limits) are always satisfied under all possible valid inputs, providing **formal guarantees** that go beyond traditional numerical testing.

This project demonstrates how **automated reasoning** can be applied to **quantitative finance**, a domain where such techniques are rarely used but critically important—especially in the presence of floating-point computations that can lead to subtle but dangerous errors.

---

## Why This Matters

Financial models often involve:
- Allocation constraints
- Thresholds and inequalities
- Repetitive calculations over time
- Floating-point computations that are prone to rounding errors

Errors in such models can lead to:
- **Unexpected violations of constraints**
- **Financial losses or overexposure**
- **Compliance and regulatory risks**

By using formal methods, **VeriFloat** checks whether such violations are possible in *any scenario*, not just in sampled test cases.

---

## What VeriFloat Does

VeriFloat models a simple **portfolio return function**:

$$
\text{Portfolio Return} = w_1 r_1 + w_2 r_2 + w_3 r_3
$$

Subject to:

- **Asset weight constraints:**  
  `0 ≤ w₁, w₂, w₃ ≤ 1`

- **Total allocation constraint:**  
  `w₁ + w₂ + w₃ ≤ 1`

- **Asset returns bounded:**  
  `-1 ≤ r₁, r₂, r₃ ≤ 1`

We verify whether the following **safety property** holds under all valid inputs:

`-1 ≤ Portfolio Return ≤ 1`

---

## Features and Verifications Included

| Module                | What It Verifies                                                     |
|-----------------------|----------------------------------------------------------------------|
| `verifloat.py`        |  Basic portfolio return consistency (single period)                  |
| `verifloat_fp.py`     |  Robustness under floating-point numerical drift (epsilon modeling)  |
| `verifloat_multi.py`  |  Multi-period portfolio consistency (temporal reasoning)             |

Each module uses **Z3 symbolic reasoning** to check whether any possible combination of inputs could lead to violations.

---

## How to Run

### Install Z3:
```bash
pip install z3-solver
````

### Run All Tests:

```bash
python test_cases.py
```

You will see results for:

* Basic verification
* Floating-point error verification
* Multi-period verification

---

## Sample Outputs

```
Running Basic Portfolio Return Test:
 Property holds: Portfolio return within [-1, 1]

Running Floating-Point Drift Test:
 Property holds even under small numerical errors.

Running Multi-Period Portfolio Return Test:
 Property holds in multi-period scenario.
```

If a violation exists, Z3 will generate a **counterexample** showing exact values that lead to failure.

---

## Project Structure

| File                   | Purpose                                     |
| ---------------------- | ------------------------------------------- |
| `verifloat.py`         | Basic portfolio model + verification        |
| `verifloat_fp.py`      | Portfolio model with floating-point drift   |
| `verifloat_multi.py`   | Multi-period portfolio model                |
| `test_cases.py`        | Runs all verification scenarios in sequence |
| `demo_verifloat.ipynb` | Interactive notebook (optional)             |
| `README.md`            | Project overview and instructions           |

---

## Key Concepts Demonstrated

* **Satisfiability Modulo Theories (SMT) solving** with Z3
* **Formal specification of financial models as logical constraints**
* **Bounded reasoning** for symbolic inputs
* **Robustness verification under numerical uncertainty (floating-point drift)**
* **Temporal consistency across multiple periods**

---

## Future Directions

This project lays the groundwork for more advanced research and development in:

* Formal verification of **option pricing models**
* Automated reasoning for **Value-at-Risk (VaR)** compliance checks
* Integration with **interactive theorem provers** (Coq, Isabelle)
* **Parametric floating-point reasoning** — directly aligned with ongoing research in programming language theory and formal methods.

---

## Relevance to Research

This work reflects key research challenges in:

* **Automated Reasoning**
* **Formal Verification of Numerical Computations**
* **Parametric and Floating-Point Aware Theorem Proving**

It serves as a proof-of-concept for how formal methods can be brought into financial software development—an area where correctness is crucial yet often unverified at a deep level.

---

## License

This project is licensed under the **MIT License** — free to use, modify, and share.

---
