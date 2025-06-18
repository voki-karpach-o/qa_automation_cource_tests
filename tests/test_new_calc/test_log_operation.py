from qa_automation_cource.new_calc import NewCalc


class TestNewCalc:
    def test_log_operation(self, temp_log_file):
        NewCalc.log_operation("add", (5, 3), 8, temp_log_file)
        assert temp_log_file.exists(), "Log file should exist"

        with open(temp_log_file, "r", encoding="utf-8") as file:
            log_content = file.read()
            assert "Операция" in log_content, "Log file should contain operation"
            assert "Аргументы" in log_content, "Log file should contain arguments"
            assert "Результат" in log_content, "Log file should contain result"
