"""Common test fixtures and pytest configuration."""

import os


def pytest_report_header(config):
    """Pytest hook — runs at session start, output appears in pytest header."""
    return [
        "CONFTEST_LOADED: conftest.py pytest_report_header was invoked",
        f"CONFTEST_CWD: {os.getcwd()}",
        f"CONFTEST_PID: {os.getpid()}",
    ]


def pytest_configure(config):
    """Pytest hook — runs at session configure."""
    # Mutate config to make execution detectable in output
    config._conftest_marker = "CONFTEST_CONFIGURE_RAN"
