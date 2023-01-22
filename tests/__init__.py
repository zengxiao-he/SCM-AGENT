# Test package for SCM-AGENT
import unittest

# Test discovery
def load_tests(loader, tests, pattern):
    return loader.discover('.', pattern='test_*.py')
