from __future__ import absolute_import
import nox

BLACK_PATHS = [
        "firestore_auth",
        "tests"
]


@nox.session(python="3.7")
def lint(session):
    """Run linters.
    Returns a failure if the linters find linting errors or sufficiently
    sersious code quality issues.
    """
    session.install("flake8", "black")
    session.install("-r", "requirements.txt")
    session.run("black", "--check", "-l", "79", *BLACK_PATHS)
    session.run("flake8", *BLACK_PATHS)


@nox.session(python="3.7")
def blacken(session):
    """Run black.
    """
    session.install("black")
    session.run("black", "-l", "79", *BLACK_PATHS)


def default(session):
    # Install all test dependencies, then isntall this package in-place.
    session.install("mock", "pytest", "pytest-cov", "mock-firestore")
    session.install("-r", "requirements.txt")
    session.install("-e", ".")
    session.run(
            "py.test",
            "--quiet",
            "--cov=firestore_auth",
            "--cov-fail-under=0",
            *session.posargs
    )


@nox.session(python=["3.7"])
def unit(session):
    default(session)
