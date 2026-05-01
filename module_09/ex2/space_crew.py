from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(default_factory=datetime.now)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_mission_rules(self):
        if not self.mission_id.startswith("M"):
            raise ValueError(
                "Mission ID must start with 'M'"
            )

        has_lead = any(
            member.rank in (Rank.commander, Rank.captain)
            for member in self.crew
        )
        if not has_lead:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced_count = sum(
                1 for member in self.crew if member.years_experience >= 5
            )
            if experienced_count < len(self.crew) / 2:
                raise ValueError(
                    "Long missions require at least 50% of crew "
                    "with 5+ years experience"
                )

        inactive_members = [m.name for m in self.crew if not m.is_active]
        if inactive_members:
            raise ValueError(
                f"All crew members must be active. "
                f"Inactive: {', '.join(inactive_members)}"
            )

        return self


def main():
    print("Space Mission Crew Validation")
    print("=" * 40)

    try:
        crew = [
            CrewMember(
                member_id="C001",
                name="Sarah Connor",
                rank=Rank.commander,
                age=40,
                specialization="Mission Command",
                years_experience=15,
            ),
            CrewMember(
                member_id="C002",
                name="John Smith",
                rank=Rank.lieutenant,
                age=35,
                specialization="Navigation",
                years_experience=7,
            ),
            CrewMember(
                member_id="C003",
                name="Alice Johnson",
                rank=Rank.officer,
                age=30,
                specialization="Engineering",
                years_experience=6,
            ),
        ]

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            duration_days=900,
            budget_millions=2500.0,
            crew=crew,
        )

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(
                f"- {member.name} ({member.rank}) - "
                f"{member.specialization}"
            )

        print("=" * 40)

    except ValidationError as e:
        print("Unexpected validation error:", e)

    try:
        invalid_crew = [
            CrewMember(
                member_id="C004",
                name="Tom Hardy",
                rank=Rank.lieutenant,
                age=32,
                specialization="Navigation",
                years_experience=4,
            ),
            CrewMember(
                member_id="C005",
                name="Emily Rose",
                rank=Rank.officer,
                age=28,
                specialization="Engineering",
                years_experience=3,
            ),
        ]

        SpaceMission(
            mission_id="M2024_INVALID",
            mission_name="Test Mission",
            destination="Venus",
            duration_days=100,
            budget_millions=500.0,
            crew=invalid_crew,
        )

    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            print(err['msg'])


if __name__ == "__main__":
    main()
