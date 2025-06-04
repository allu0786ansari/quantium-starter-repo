# Activate the virtual environment
& .\qvenv\Scripts\Activate.ps1

# Run the test suite
pytest

# Capture the exit code of pytest
$exitCode = $LASTEXITCODE

# Exit with 0 if tests passed, else 1
if ($exitCode -eq 0) {
    exit 0
} else {
    exit 1
}
