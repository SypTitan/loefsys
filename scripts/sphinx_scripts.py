import subprocess


def docs():
    subprocess.run(
        ["sphinx-build", "-M", "html", "./docs", "./docs/_build"], check=False
    )


def api_docs():
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
