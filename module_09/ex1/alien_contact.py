from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime = Field(default_factory=datetime.now)
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def check_business_rules(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                "Contact ID must start with 'AC'"
            )

        if (
            self.contact_type == ContactType.physical
            and not self.is_verified
        ):
            raise ValueError(
                "Physical contact reports must be verified"
            )

        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (>7.0) should include received messages"
            )

        return self


def main():
    print("Alien Contact Log Validation")
    print("=" * 40)

    try:
        valid_contact = AlienContact(
            contact_id="AC_2024_001",
            contact_type=ContactType.radio,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )

        print("Valid contact report:")
        print(f"ID: {valid_contact.contact_id}")
        print(f"Type: {valid_contact.contact_type}")
        print(f"Location: {valid_contact.location}")
        print(f"Signal: {valid_contact.signal_strength}/10")
        print(f"Duration: {valid_contact.duration_minutes} minutes")
        print(f"Witnesses: {valid_contact.witness_count}")
        print(f"Message: '{valid_contact.message_received}'")
        print("=" * 40)

    except ValidationError as e:
        print("Unexpected error in valid data:", e)

    try:
        AlienContact(
            contact_id="AC_2024_002",
            contact_type=ContactType.telepathic,
            location="Mars Outpost",
            signal_strength=5.0,
            duration_minutes=30,
            witness_count=2,
            message_received="Hello Earth"
        )

    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            print(err['msg'])


if __name__ == "__main__":
    main()
