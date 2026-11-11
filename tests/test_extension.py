import json
import subprocess
from pathlib import Path

def test_manifest_json():
    manifest_path = Path("manifest.json")
    assert manifest_path.exists()
    data = json.loads(manifest_path.read_text())
    assert data["manifest_version"] == 3
    assert "name" in data
    assert "permissions" in data

def test_node_suite_execution():
    res = subprocess.run(["node", "tests/run_tests.js"], capture_output=True, text=True)
    assert res.returncode == 0
    assert "ALL TESTS COMPLETED SUCCESSFULLY" in res.stdout
