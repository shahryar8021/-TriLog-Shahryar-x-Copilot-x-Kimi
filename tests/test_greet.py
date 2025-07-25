from typer.testing import CliRunner
from ai_log.cli import app

runner = CliRunner()

def test_greet_default():
    result = runner.invoke(app, ["greet"])
    assert "TriLog bot is alive" in result.stdout
    assert result.exit_code == 0

def test_greet_custom_name():
    result = runner.invoke(app, ["greet", "--name", "Shahryar"])
    assert "Hey Shahryar" in result.stdout
