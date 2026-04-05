#!/usr/bin/env python3

import os
import sys
import subprocess
import json
from pathlib import Path

# Add parent directory to path to import compiler
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestRunner:
    def __init__(self, test_dir):
        self.test_dir = Path(test_dir)
        self.tests_passed = 0
        self.tests_failed = 0
        self.results = []
        self.binaries_created = set()

    def run_all_tests(self):
        """Discover and run all tests."""
        test_files = sorted(self.test_dir.glob("*.json"))
        
        if not test_files:
            print("No test files found!")
            return False
        
        print(f"Found {len(test_files)} test files\n")
        
        for test_file in test_files:
            self.run_test_file(test_file)
        
        self.print_summary()
        self.cleanup_binaries()
        return self.tests_failed == 0

    def run_test_file(self, test_file):
        """Run a single test file."""
        with open(test_file, 'r') as f:
            try:
                tests = json.load(f)
            except json.JSONDecodeError as e:
                print(f"ERROR: Invalid JSON in {test_file}: {e}")
                self.tests_failed += 1
                return
        
        test_name = test_file.stem
        print(f"Running tests from {test_name}...")
        
        for i, test in enumerate(tests):
            test_id = f"{test_name}[{i}]"
            success = self.run_single_test(test, test_id)
            if success:
                self.tests_passed += 1
                print(f"  ✓ {test['name']}")
            else:
                self.tests_failed += 1
                print(f"  ✗ {test['name']}")
        
        print()

    def run_single_test(self, test, test_id):
        """Run a single test case."""
        source_file = test.get("source")
        expected_output = test.get("expected_output", "").strip()
        should_fail = test.get("should_fail", False)
        
        if not source_file:
            print(f"    ERROR: No source file specified in test {test_id}")
            return False
        
        source_path = self.test_dir / source_file
        if not source_path.exists():
            print(f"    ERROR: Source file not found: {source_path}")
            return False
        
        # Generate binary name and path
        binary_name = source_path.stem
        binary_path = self.test_dir.parent / binary_name
        
        # Track binary for cleanup
        self.binaries_created.add(binary_path)
        
        # Compile from parent directory
        compile_result = subprocess.run(
            ["python3", "main.py", str(source_path)],
            capture_output=True,
            text=True,
            cwd=self.test_dir.parent
        )
        
        # Check compilation result
        if should_fail:
            if compile_result.returncode != 0:
                return True  # Expected failure
            else:
                self.results.append({
                    "test": test_id,
                    "error": "Expected compilation to fail but it succeeded"
                })
                return False
        
        if compile_result.returncode != 0:
            self.results.append({
                "test": test_id,
                "error": f"Compilation failed: {compile_result.stderr}"
            })
            return False
        
        # Run binary - should be in parent directory
        if not binary_path.exists():
            self.results.append({
                "test": test_id,
                "error": f"Binary not created: {binary_path}"
            })
            return False
        
        run_result = subprocess.run(
            [str(binary_path)],
            capture_output=True,
            text=True,
            cwd=self.test_dir.parent
        )
        
        actual_output = run_result.stdout.strip()
        
        # Compare output
        if actual_output == expected_output:
            return True
        else:
            self.results.append({
                "test": test_id,
                "expected": expected_output,
                "actual": actual_output
            })
            return False

    def print_summary(self):
        """Print test summary."""
        total = self.tests_passed + self.tests_failed
        print("=" * 60)
        print(f"Test Results: {self.tests_passed}/{total} passed")
        print("=" * 60)
        
        if self.results:
            print("\nFailed Tests:\n")
            for result in self.results:
                print(f"Test: {result['test']}")
                if "error" in result:
                    print(f"  Error: {result['error']}")
                else:
                    print(f"  Expected: {repr(result['expected'])}")
                    print(f"  Actual:   {repr(result['actual'])}")
                print()

    def cleanup_binaries(self):
        """Clean up generated binary files."""
        print("\nCleaning up binaries...")
        cleaned = 0
        for binary_path in self.binaries_created:
            if binary_path.exists():
                try:
                    os.remove(binary_path)
                    cleaned += 1
                except OSError as e:
                    print(f"Warning: Could not remove {binary_path}: {e}")
        print(f"Cleaned up {cleaned} binary file(s)")

def main():
    test_dir = Path(__file__).parent
    runner = TestRunner(test_dir)
    success = runner.run_all_tests()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
