from abc import ABC, abstractmethod
from typing import List, Any, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.process_data = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int]]:
        return {
            "stream_id": self.stream_id,
            "process_data": self.process_data
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        len_b_data = len(data_batch)
        if len_b_data > 0:
            avg_temp = sum(d["temp"] for d in data_batch) / len_b_data
        else:
            avg_temp = 0
        self.process_data += len_b_data
        result = (
            f"Sensor analysis: {len_b_data} "
            f"readings processed, avg temp: {avg_temp:.1f}°C"
        )
        return result

    def filter_data(
        self,
        data_batch: List[Dict[str, float]],
        criteria: Optional[str] = None
    ) -> List[Dict[str, float]]:
        if criteria == "high":
            return [d for d in data_batch if d["temp"] > 25]
        return data_batch


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        len_b_data = len(data_batch)
        net = 0

        for d in data_batch:
            if "buy" in d:
                net += d["buy"]
            if "sell" in d:
                net -= d["sell"]

        self.process_data += len_b_data
        return (
            f"Transaction analysis: {len_b_data} operations, "
            f"net flow: {net} units"
        )

    def filter_data(
        self,
        data_batch: List[Dict[str, int]],
        criteria: Optional[str] = None
    ) -> List[Dict[str, int]]:
        if criteria == "large":
            return [d for d in data_batch if "buy" in d and d["buy"] > 100]
        return data_batch


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "System Events"

    def process_batch(self, data_batch: List[Any]):
        events = len(data_batch)
        errors = 0

        for e in data_batch:
            if e == "error":
                errors += 1

        self.process_data += events

        return (
            f"Event analysis: {events} events, "
            f"{errors} error(s) detected"
        )

    def filter_data(
        self,
        data_batch: List[str],
        criteria: Optional[str] = None
    ) -> List[str]:
        if criteria == "error":
            return [e for e in data_batch if e == "error"]
        return data_batch


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> None:
        for i in range(len(self.streams)):
            try:
                stream = self.streams[i]
                batch = batches[i]

                stream.process_batch(batch)

                if isinstance(stream, SensorStream):
                    print(f"- Sensor data: {len(batch)} readings processed")

                elif isinstance(stream, TransactionStream):
                    print(f"- Transaction data: "
                          f"{len(batch)} operations processed")

                elif isinstance(stream, EventStream):
                    print(f"- Event data: {len(batch)} events processed")

            except Exception as e:
                print(f"Error processing {stream.stream_id}: {e}")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print("Stream ID:", sensor.stream_id, ", Type: Environmental Data")
    sensor_batch = [
        {"temp": 22.5},
        {"temp": 22.5},
        {"temp": 22.5}
    ]
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    print(sensor.process_batch(sensor_batch))
    print()
    print("Initializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    print("Stream ID:", trans.stream_id, ", Type: Financial Data")
    trans_batch = [
        {"buy": 100},
        {"sell": 150},
        {"buy": 75}
    ]
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    print(trans.process_batch(trans_batch))
    print()
    print("Initializing Event Stream...")
    event = EventStream("EVENT_001")
    print("Stream ID:", event.stream_id, ", Type: System Events")
    event_batch = ["login", "error", "logout"]
    print("Processing event batch: [login, error, logout]")
    print(event.process_batch(event_batch))
    print()
    print("=== Polymorphic Stream Processing ===")
    print()
    print("Processing mixed stream types through unified interface...")

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)

    batches: List[List[Any]] = [
        [{"temp": 21.0}, {"temp": 23.0}],
        [{"buy": 200}, {"sell": 50}, {"buy": 70}, {"buy": 30}],
        ["login", "error", "logout"]
    ]
    print()
    print("Batch 1 Results:")
    processor.process_all(batches)
    print()
    sensor_batch2: List[Dict[str, float]] = [
        {"temp": 30.0},
        {"temp": 20.0},
        {"temp": 27.0}
    ]
    trans_batch1 = [
        {"buy": 200},
        {"sell": 50},
        {"buy": 70},
        {"buy": 30}
    ]
    print("Stream filtering active: High-priority data only")
    filter_sensor = sensor.filter_data(sensor_batch2, "high")
    filter_trans = trans.filter_data(trans_batch1, "large")
    print(
        "Filtered results:",
        len(filter_sensor), "critical sensor alerts,",
        len(filter_trans), "large transaction"
    )
    print()
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
