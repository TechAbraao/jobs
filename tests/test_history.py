from jobs.core import history


def test_create_tables_and_save_history_round_trip(monkeypatch, tmp_path):
    db_path = tmp_path / "jobs.db"
    monkeypatch.setattr(history, "DATA_DIR", tmp_path)
    monkeypatch.setattr(history, "DB_NAME", db_path)

    history.create_tables()
    history.save_history("jobs-cli search --city 'São Paulo'")
    history.save_history("jobs-cli history --limit 5")

    commands = history.all_commands()

    assert len(commands) == 2
    assert [command for command, _ in commands] == [
        "jobs-cli search --city 'São Paulo'",
        "jobs-cli history --limit 5",
    ]
