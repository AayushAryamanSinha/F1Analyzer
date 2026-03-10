import pandas as pd
from research_question_2_3_development_plus_EDA import (
    build_q2_dataset,
    build_q4_dataset
)


def test_champion_case() -> None:
    """Test when first race winner becomes champion."""

    races = pd.DataFrame({
        "raceId": [1, 2],
        "year": [2000, 2000],
        "round": [1, 2]
    })

    results = pd.DataFrame({
        "raceId": [1],
        "driverId": [10],
        "position": [1]
    })

    driver_standings = pd.DataFrame({
        "raceId": [2],
        "driverId": [10],
        "position": [1]
    })

    result = build_q2_dataset(races, results, driver_standings)

    assert len(result) == 1
    assert result.iloc[0]["final_championship_position"] == 1


def test_non_champion_case() -> None:
    """Test when first race winner does not become champion."""

    races = pd.DataFrame({
        "raceId": [1, 2],
        "year": [2001, 2001],
        "round": [1, 2]
    })

    results = pd.DataFrame({
        "raceId": [1],
        "driverId": [20],
        "position": [1]
    })

    driver_standings = pd.DataFrame({
        "raceId": [2],
        "driverId": [20],
        "position": [2]
    })

    result = build_q2_dataset(races, results, driver_standings)

    assert result.iloc[0]["final_championship_position"] == 2


def test_multiple_seasons() -> None:
    """Test handling of multiple seasons."""

    races = pd.DataFrame({
        "raceId": [1, 2, 3, 4],
        "year": [2000, 2000, 2001, 2001],
        "round": [1, 2, 1, 2]
    })

    results = pd.DataFrame({
        "raceId": [1, 3],
        "driverId": [10, 20],
        "position": [1, 1]
    })

    driver_standings = pd.DataFrame({
        "raceId": [2, 4],
        "driverId": [10, 20],
        "position": [1, 3]
    })

    result = build_q2_dataset(races, results, driver_standings)

    assert len(result) == 2

    season_2000 = result[result["year"] == 2000]
    assert season_2000.iloc[0]["final_championship_position"] == 1

    season_2001 = result[result["year"] == 2001]
    assert season_2001.iloc[0]["final_championship_position"] == 3



def test_pit_time_aggregation() -> None:
    """Test pit stop times are summed correctly."""

    pit_stops = pd.DataFrame({
        "raceId": [1, 1],
        "driverId": [10, 10],
        "milliseconds": [2000, 3000]
    })

    results = pd.DataFrame({
        "raceId": [1],
        "driverId": [10],
        "position": [5]
    })

    merged = build_q4_dataset(pit_stops, results)

    assert merged.iloc[0]["total_pit_time"] == 5000
    assert merged.iloc[0]["finish_position"] == 5


def test_multiple_drivers_q4() -> None:
    """Test multiple drivers in same race."""

    pit_stops = pd.DataFrame({
        "raceId": [1, 1, 1],
        "driverId": [10, 20, 20],
        "milliseconds": [2000, 1000, 1000]
    })

    results = pd.DataFrame({
        "raceId": [1, 1],
        "driverId": [10, 20],
        "position": [3, 1]
    })

    merged = build_q4_dataset(pit_stops, results)

    assert len(merged) == 2
    assert merged[merged["driverId"] == 10]["total_pit_time"].iloc[0] == 2000
    assert merged[merged["driverId"] == 20]["total_pit_time"].iloc[0] == 2000


def test_missing_finish_removed() -> None:
    """Ensure drivers without finish position are excluded."""

    pit_stops = pd.DataFrame({
        "raceId": [1],
        "driverId": [10],
        "milliseconds": [2000]
    })

    results = pd.DataFrame({
        "raceId": [1],
        "driverId": [10],
        "position": [None]
    })

    merged = build_q4_dataset(pit_stops, results)

    assert len(merged) == 0



def run_tests() -> None:
    """Run all Question 2 and Question 4 tests."""

    test_champion_case()
    test_non_champion_case()
    test_multiple_seasons()

    test_pit_time_aggregation()
    test_multiple_drivers_q4()
    test_missing_finish_removed()

    print("All EDA tests passed.")


if __name__ == "__main__":
    run_tests()