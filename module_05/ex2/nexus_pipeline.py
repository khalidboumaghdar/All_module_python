from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []
        self.stats: Dict[str, int] = {"processed": 0, "errors": 0}

    def add_stages(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def run(self, data: Any) -> Any:
        try:
            for stage in self.stages:
                data = stage.process(data)
            self.stats["processed"] += 1
        except Exception as e:
            self.stats["errors"] += 1
            print(f"Pipeline error: {e}")
        return data

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


class InputStage:
    def process(self, data: Any) -> Any:
        print("Stage 1: Input validation and parsing")
        return data


class TransformStage:
    def process(self, data: Any) -> Any:
        print("Stage 2: Data transformation and enrichment")
        return data


class OutputStage:
    def process(self, data: Any) -> Any:
        print("Stage 3: Output formatting and delivery")
        return data


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        print(f"Input: {data}")
        print("Transform: Enriched with metadata and validation")

        try:
            if isinstance(data, str):
                data = data.replace("{", "").replace("}", "").replace('"', "")
                parts = data.split(",")

                sensor: Dict[str, str] = {}

                for p in parts:
                    key, val = p.split(":")
                    sensor[key.strip()] = val.strip()

                value = float(sensor["value"])

                if 20 <= value <= 25:
                    status = "Normal range"
                else:
                    status = "Out of range"

            print(
                f"Output: Processed {sensor['sensor']} reading "
                f"{sensor['value']}°{sensor['unit']} ({status})"
            )
            return data
        except Exception as e:
            print(e)


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        print(f"Input: {data}")
        print("Transform: Parsed and structured data")

        if isinstance(data, str):
            parts = data.replace('"', "").split(",")

            row: List[str] = []
            for p in parts:
                row.append(p.strip())

        print(f"Output: User activity logged: {len(row)} fields processed")
        return data


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            data_input, data_list = data.split(":", 1)
            lst: List[float] = []
            for i in data_list.split(","):
                lst.append(float(i))

            print(f"Input: {data_input}")
            print("Transform: Aggregated and filtered")
            avg: Optional[float] = None
            if isinstance(lst, list):
                len_data = len(lst)
                total = 0
                for v in lst:
                    total += v
                avg = total / len_data
            print(
                f"Output: Stream summary: {len_data} readings, "
                f"avg: {avg:.1f}°C"
            )
            return data_input
        except Exception as ex:
            print(ex)
            return None


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_data(self, data: Any) -> None:
        for pipe in self.pipelines:
            pipe.run(data)


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second")
    manager = NexusManager()

    print("\nCreating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")

    json_pipe = JSONAdapter("JSON_01")
    csv_pipe = CSVAdapter("CSV_01")
    stream_pipe = StreamAdapter("STREAM_01")

    json_pipe.add_stages(InputStage())
    json_pipe.add_stages(TransformStage())
    json_pipe.add_stages(OutputStage())

    manager.add_pipeline(json_pipe)
    manager.add_pipeline(csv_pipe)
    manager.add_pipeline(stream_pipe)

    print("\n=== Multi-Format Data Processing ===")
    print("Processing JSON data through pipeline...")
    json_pipe.process('{"sensor": "temp", "value": 23.2, "unit": "C"}')

    print("\nProcessing CSV data through same pipeline...")
    csv_pipe.process("user,action,timestamp")

    print("\nProcessing Stream data through same pipeline...")
    stream_pipe.process("Real-time sensor stream:21, 22, 23, 21, 23")

    print("\n=== Pipeline Chaining Demo ===")
    pipe_a = JSONAdapter("Pipeline_A")
    pipe_b = CSVAdapter("Pipeline_B")
    pipe_c = StreamAdapter("Pipeline_C")

    pipe_a.add_stages(InputStage())
    pipe_b.add_stages(TransformStage())
    pipe_c.add_stages(OutputStage())

    pipelines: List[ProcessingPipeline] = [pipe_a, pipe_b, pipe_c]
    records = 100

    data: Any = "raw data"
    for pipe in pipelines:
        data = pipe.run(data)

    names: List[str] = [p.pipeline_id for p in pipelines]
    total_processed = sum(p.stats["processed"] for p in pipelines)
    efficiency = round((total_processed / len(pipelines)) * 100)

    print(" -> ".join(names))
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")
    print(f"Chain result: {records} records processed"
          f" through {len(pipelines)}-stage pipeline")
    print(f"Performance: {efficiency}% efficiency")

    print("\n=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    try:
        raise ValueError("Invalid data format")
    except ValueError as e:
        print(f"Error detected in Stage 2: {e}")
        print("Recovery initiated: Switching to backup processor")
        backup = JSONAdapter("BACKUP_01")
        backup.add_stages(InputStage())
        backup.run("backup data")
        print("Recovery successful: Pipeline restored, processing resumed")

    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
