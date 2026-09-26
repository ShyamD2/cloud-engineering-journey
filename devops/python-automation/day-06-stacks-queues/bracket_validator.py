"""
Day 6: Basic DSA — Stacks in DevOps Configuration Linting
Script: bracket_validator.py
DevOps & Cloud Engineer 36-Day Master Plan — Candidate: Shyam Kumar D

Functionality:
- Implements LIFO (Last-In, First-Out) Stack using Python list append() and pop()
- Validates matching brackets '()', '[]', '{}' in JSON, YAML, and Terraform HCL files
- Reports precise character and column positions of syntax/nesting errors
- Includes automated unit tests and LeetCode #20 verification
"""

from __future__ import annotations
from typing import Dict, List, Optional, Tuple


BRACKET_MAP: Dict[str, str] = {
    ")": "(",
    "]": "[",
    "}": "{",
}
OPENING_BRACKETS = set(BRACKET_MAP.values())
CLOSING_BRACKETS = set(BRACKET_MAP.keys())


def validate_brackets(text: str) -> Tuple[bool, Optional[str]]:
    """
    Validates bracket balance using a LIFO Stack.
    Returns: (is_valid, error_message)
    """
    stack: List[Tuple[str, int, int]] = []  # (char, line_num, col_num)
    line_num = 1
    col_num = 0

    for idx, ch in enumerate(text):
        if ch == "\n":
            line_num += 1
            col_num = 0
            continue
        col_num += 1

        if ch in OPENING_BRACKETS:
            stack.append((ch, line_num, col_num))
        elif ch in CLOSING_BRACKETS:
            if not stack:
                return False, f"Unexpected closing bracket '{ch}' at line {line_num}, col {col_num}"
            top_char, top_line, top_col = stack.pop()
            expected_opening = BRACKET_MAP[ch]
            if top_char != expected_opening:
                return (
                    False,
                    f"Mismatched bracket: opened with '{top_char}' (line {top_line}, col {top_col}) "
                    f"but closed with '{ch}' at line {line_num}, col {col_num}",
                )

    if stack:
        unclosed_char, u_line, u_col = stack[-1]
        return False, f"Unclosed bracket '{unclosed_char}' remaining from line {u_line}, col {u_col}"

    return True, None


def run_tests() -> None:
    print("\n[TEST] Running automated test suite for bracket_validator.py...")

    valid_cases = [
        "()",
        "()[]{}",
        "{[()]}",
        'resource "aws_s3_bucket" "b" { bucket = "my-bucket" tags = { Env = "prod" } }',
        "",
        "abc(def[ghi{jkl}mno]pqr)stu",
    ]

    invalid_cases = [
        ("(]", "Mismatched bracket"),
        ("([)]", "Mismatched bracket"),
        ("((()", "Unclosed bracket"),
        (")", "Unexpected closing bracket"),
        ('terraform { required_version = ">= 1.0" {', "Unclosed bracket"),
    ]

    for code in valid_cases:
        ok, err = validate_brackets(code)
        assert ok, f"Expected valid for '{code}', but got error: {err}"

    for code, expected_snippet in invalid_cases:
        ok, err = validate_brackets(code)
        assert not ok, f"Expected invalid for '{code}', but passed"
        assert expected_snippet in err, f"Expected '{expected_snippet}' in error: {err}"

    print("[PASS] Valid bracket structures recognized.")
    print("[PASS] Syntax errors and mismatched pairs caught with line/col telemetry.\n")


def main() -> None:
    run_tests()
    sample_hcl = """
    locals {
        subnets = [
            "10.0.1.0/24",
            "10.0.2.0/24"
        ]
        tags = {
            Environment = "Production"
            Owner       = "DevOps"
        }
    }
    """
    ok, err = validate_brackets(sample_hcl)
    print("=" * 65)
    print("  TERRAFORM / CONFIG BRACKET VALIDATOR (LIFO STACK)")
    print("=" * 65)
    print("  Config Content Check:")
    print(f"    - Syntax Valid : {ok}")
    if not ok:
        print(f"    - Error Detail : {err}")
    else:
        print("    - Result       : Clean! All brackets, braces, and parens are balanced.")
    print("=" * 65)


if __name__ == "__main__":
    main()
