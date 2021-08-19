# type: ignore
from invoke import task


@task
def generate_indexfile_example_libdir_recursive(c):
    """
    Recreate the index file example used in acceptance tests.
    """
    c.run("indexrfdocs -c tests/assets/config_file_examples/config_valid.toml -o tmp")
    c.run(
        "cp tmp/index.html tests/assets/index_file_examples/index_libdir_recursive.html"
    )
    c.run("rm -rf tmp")
    print("Indexfile example created!")
