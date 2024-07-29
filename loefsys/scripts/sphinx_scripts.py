import subprocess


def makedocs():
    subprocess.run(
        ["sphinx-build", "-M", "html", "./docs", "./docs/_build"], check=False
    )


def parsedocstrings():
    subprocess.run(
        [
            "sphinx-apidoc",
            "-M",
            "-f",
            "-o",
            "./docs",
            "./loefsys",
            "./loefsys/*/migrations",
            "./loefsys/*/tests*",
        ],
        check=False,
    )
