from contextlib import contextmanager

@contextmanager
def example_of(text: str):
    print(f"\n---Begin: Example of {text}---")
    try:
        yield
    finally:
        print(f"---End: Example of {text}---")