from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> Union[str]:
        if not self.validate(data):
            return self.format_output("invalid numeric data")
        try:
            len_data = len(data)
            sum_data = sum(data)
            avg_data = sum_data / len_data
            return self.format_output(
                f"Processed {len_data} numeric values, sum = {sum_data}, "
                f"avg = {avg_data}"
            )
        except Exception as e:
            return self.format_output(f"Error processing numeric data: {e}")

    def validate(self, data: Any) -> bool:
        try:
            sum(data)
            return True
        except Exception:
            return False


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return self.format_output("invalid text data")
        try:
            len_data = len(data)
            word_count = len(data.split())
            return self.format_output(
                f"Processed text: {len_data} characters, {word_count} words"
            )
        except Exception as e:
            return self.format_output(f"Error processing text data: {e}")

    def validate(self, data: Any) -> bool:
        try:
            data.split()
            return True
        except Exception:
            return False


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return self.format_output("invalid log entry")
        try:
            level, message = data.split(":", 1)
            level = level.strip().upper()
            message = message.strip()

            if level == "ERROR":
                alert = "[ALERT]"
            elif level == "WARNING":
                alert = "[WARNING]"
            elif level == "INFO":
                alert = "[INFO]"
            else:
                alert = "[LOG]"

            return self.format_output(
                f"{alert} {level} level detected: {message}"
            )
        except Exception as e:
            return self.format_output(f"Error processing log data: {e}")

    def validate(self, data: Any) -> bool:
        try:
            data.split(":")
            return True
        except Exception:
            return False


def main() -> None:
    numeric_data: List[Union[int, Optional[str, Dict]]] = [1, 2, 3, 4, 5]
    print("Initializing Numeric Processor...")
    num_proc = NumericProcessor()
    print(f"Processing data: {numeric_data}")
    validation_msg = (
        "Numeric data verified"
        if num_proc.validate(numeric_data)
        else "Invalid numeric data"
    )
    print(f"Validation: {validation_msg}")
    print(num_proc.process(numeric_data))
    print()

    text_data = "Hello Nexus World"
    print("Initializing Text Processor...")
    text_proc = TextProcessor()
    print(f"Processing data: \"{text_data}\"")
    validation_msg = (
        "Text data verified"
        if text_proc.validate(text_data)
        else "Invalid text data"
    )
    print(f"Validation: {validation_msg}")
    print(text_proc.process(text_data))
    print()

    log_data = "ERROR: Connection timeout"
    print("Initializing Log Processor...")
    log_proc = LogProcessor()
    print(f"Processing data: \"{log_data}\"")
    validation_msg = (
        "Log entry verified"
        if log_proc.validate(log_data)
        else "Invalid log entry"
    )
    print(f"Validation: {validation_msg}")
    print(log_proc.process(log_data))
    print()

    print("=== Polymorphic Processing Demo ===")
    data_streams: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]

    sample_data = [
        [1, 2, 3],
        "Hello Nexus.",
        "INFO: System ready",
    ]

    print("Processing multiple data types through same interface...")
    for i in range(len(data_streams)):
        processor = data_streams[i]
        result = processor.process(sample_data[i])
        print(f"Result {i + 1}: {result}")

    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
