import os

def check_alignment():
    specs = [f.replace('.md', '') for f in os.listdir('specs') if f.endswith('.md')]
    tests = [f.replace('test_', '').replace('.py', '') for f in os.listdir('tests') if f.endswith('.py')]
    
    for spec in specs:
        if spec in tests or f"{spec}_interface" in tests:
            print(f"Spec '{spec}' has associated tests.")
        else:
            print(f"Warning: Spec '{spec}' has no matching test suite!")

if __name__ == "__main__":
    check_alignment()