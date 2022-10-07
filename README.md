# RF Documentations Indexer

Rfdocsindexer is a simple Python3 module to generate [RobotFramework](https://robotframework.org/) 4+ libraries documentation.

One can configure the tool from a simple [TOML](https://github.com/toml-lang/toml) configuration file and run it from a console.

The tool then uses the RobotFramework [Libdoc](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#libdoc) module to generate an HTML, XML, JSON or Libspec documentation for any RobotFramework keyword library.

An HTML index is also generated to centralize the generated documentations.

![RFDocsIndexer Diagram](https://github.com/Vincema/rfdocsindexer/raw/main/docs/diagrams/rfdocsindexer_diagram.svg)

Below is an overview of the HTML index generated. It makes it easy to navigate among external resources and keywords documentation.

![Index File Overview](https://github.com/Vincema/rfdocsindexer/raw/main/docs/rfdocsindexer-overview.gif)

## Installing the tool

Install from Pypi:
```bash
pip install rfdocsindexer
```

## Configuring the tool

The tool can be configured with a config file in [TOML](https://github.com/toml-lang/toml) format.

Example configuration file:

```toml
[rfdocsindexer]
library_paths = ["**/libraries/*.robot", "my_library.resource"]
library_names = ["MyLibrary", "MyOtherLibary.MyOtherLibrary"]
extra_modules_searchpaths = ["./library_dir"]
external_resources = ["RF homepage | https://robotframework.org/", "http://example.org"]
build_machine_readable_libdoc = true
include_robotframework_resources = true
```

The configuration file must contain the section `[rfdocindexer]` and any or none of the following options:

* `library_paths`: a list of paths (glob format accepted) to RF resource files (can be `*.resource`, `*.robot`, `*.spec`...)
* `library_names`: a list of RF library modules
* `extra_modules_searchpaths`: a list of paths to append to `PYTHONPATH`
* `external_resources`: a list of URLs which will be added to the HTML index file, or `<name> | <URL>`. Useful to include frequently used external resources when developing tests.
* `build_machine_readable_libdoc`: whether to generate documentation in XML, JSON and Libspec format. If set to `False`, only the HTML documenation will be generated. Default is `False`.
* `include_robotframework_resources`: whether to generate documentation for default RobotFramework libraries (`BuiltIn`, `Collection`, ...). Default is `True`.


## Running the tool

In a standard shell, run the following:

```bash
# To generate documentation for default RobotFramework libraries
indexrfdocs

# To specify the configuration file to use
indexrfdocs -c path/to/configfile.toml

# To specify the output directory (content will not be erased if already existing), default is "rfdocs"
indexrfdocs -o path/to/outdir
```
