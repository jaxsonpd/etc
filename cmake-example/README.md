# Embedded Terminal

This is an example cmake project for use with an embedded microcontroller.

## Documentation

### Setup

- Rename the test project in [tests CMake](tests/CMakeLists.txt).
- Rename the example project in [target CMake](target/CMakeLists.txt)
- Rename the target executable in [src CMake](target/src/CMakeLists.txt)
- Update the "cmake.sourceDirectory" in [.vscode/settings.json](.vscode/settings.json) to reflect new location of target and tests (if moved).

### Testing

This project uses the [unity](https://github.com/ThrowTheSwitch/Unity) test framework to allow unity testing. This is supplemented by the [FFF](https://github.com/meekrosoft/fff) Fake Function Framework used for faking where needed. The tests are located in `./tests/` and use cmake for execution. It can be manually executed from the host directory using:

```bash
cmake -B build tests
cmake --build build --parallel
ctest --test-dir build --output-on-error
```

Or using the provided bash script as follows:

```bash
source run_tests.sh
```