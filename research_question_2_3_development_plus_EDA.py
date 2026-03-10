"""
This program filters and prunes the raw F1 data based on the requirements
for Research Questions 2 and 3, both exploratory data analysis and the graphs
required to answer these questions are included
"""
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict
import altair as alt


def load_datasets() -> Dict[str, pd.DataFrame]:
    """
    Load all required F1 datasets and return them in a dictionary.
    """

    races = pd.read_csv("datasets/raw/races.csv", na_values="\\N")
    results = pd.read_csv("datasets/raw/results.csv", na_values="\\N")
    driver_standings = pd.read_csv(
        "datasets/raw/driver_standings.csv", na_values="\\N"
    )
    drivers = pd.read_csv("datasets/raw/drivers.csv", na_values="\\N")
    pit_stops = pd.read_csv("datasets/raw/pit_stops.csv", na_values="\\N")
    qualifying = pd.read_csv("datasets/raw/qualifying.csv", na_values="\\N")

    return {
        "races": races,
        "results": results,
        "driver_standings": driver_standings,
        "drivers": drivers,
        "pit_stops": pit_stops,
        "qualifying": qualifying,
    }


def inspect_datasets(datasets: Dict[str, pd.DataFrame]) -> None:
    """
    Print shape, columns, and missing values for each dataset.
    """
    for name, df in datasets.items():
        print("\n" + "=" * 60)
        print(name.upper())
        print("=" * 60)
        print("Shape:", df.shape)
        print("\nColumns:")
        print(df.columns.tolist())
        print("\nMissing Values:")
        print(df.isna().sum())
        print("\n")


def build_q2_dataset(
    races: pd.DataFrame,
    results: pd.DataFrame,
    driver_standings: pd.DataFrame
) -> pd.DataFrame:
    """
    Create a season-level dataset linking first race winners to final
    championship positions.
    """
    first_races = (
        races.sort_values(["year", "round"])
        .groupby("year")
        .first()
        .reset_index()
    )

    first_winners = results[
        (results["raceId"].isin(first_races["raceId"])) &
        (results["position"] == 1)
    ]

    first_winners = pd.merge(
        first_winners,
        first_races[["raceId", "year"]],
        on="raceId"
    )

    final_rounds = races.groupby("year")["round"].max().reset_index()

    final_races = pd.merge(
        races,
        final_rounds,
        on=["year", "round"]
    )

    final_standings = driver_standings[
        driver_standings["raceId"].isin(final_races["raceId"])
    ]

    final_standings = pd.merge(
        final_standings,
        final_races[["raceId", "year"]],
        on="raceId"
    )

    merged_q2 = pd.merge(
        first_winners[["year", "driverId"]],
        final_standings[["year", "driverId", "position"]],
        on=["year", "driverId"],
        how="left"
    )

    merged_q2.rename(
        columns={"position": "final_championship_position"},
        inplace=True
    )

    return merged_q2


def inspect_q2_dataset(merged_q2: pd.DataFrame) -> None:
    """
    Print shape, columns, and missing values for the
    merged Question 2 dataset.
    """

    print("\n" + "=" * 60)
    print("QUESTION 2 MERGED DATASET")
    print("=" * 60)

    print("Shape:", merged_q2.shape)

    print("\nColumns:")
    print(merged_q2.columns.tolist())

    print("\nMissing Values:")
    print(merged_q2.isna().sum())
    print("\n")


def summarize_q2(merged_q2: pd.DataFrame) -> None:
    """
    Print descriptive statistics and outcome counts for Question 2.
    """

    print("\n" + "=" * 60)
    print("QUESTION 2 VARIABLE SUMMARIES")
    print("=" * 60)

    print("\nFinal Championship Position Summary:")
    print(merged_q2["final_championship_position"].describe())

    print("\nDistribution of Final Championship Positions:")
    print(
        merged_q2["final_championship_position"]
        .value_counts()
        .sort_index()
    )

    champion_binary = (
        merged_q2["final_championship_position"] == 1
    )

    print("\nDid First Race Winner Become Champion?")
    print(champion_binary.value_counts())


def visualize_q2(merged_q2: pd.DataFrame) -> None:
    """
    Generate and save plots for Question 2.
    """

    counts = (
        merged_q2["final_championship_position"]
        .value_counts()
        .sort_index()
    )

    plt.figure()
    plt.bar(counts.index, counts.values)
    plt.title("Final Championship Position of First Race Winners")
    plt.xlabel("Final Championship Position")
    plt.ylabel("Number of Seasons")
    plt.savefig("q2_final_championship_position.png",
                bbox_inches="tight")

    champion_binary = (
        merged_q2["final_championship_position"] == 1
    )

    counts_binary = champion_binary.value_counts()

    plt.figure()
    plt.bar(
        ["Did Not Win Championship", "Won Championship"],
        [counts_binary.get(False, 0),
         counts_binary.get(True, 0)]
    )
    plt.title("Did First Race Winner Become Champion?")
    plt.xlabel("Outcome")
    plt.ylabel("Number of Seasons")
    plt.savefig("q2_first_race_winner_champion.png",
                bbox_inches="tight")


def build_q3_dataset(
    pit_stops: pd.DataFrame,
    results: pd.DataFrame
) -> pd.DataFrame:

    """
    Create race-level dataset linking total pit stop
    time to finishing position.
    """

    pit_totals = (
        pit_stops.groupby(["raceId", "driverId"])["milliseconds"]
        .sum()
        .reset_index()
    )

    pit_totals.rename(
        columns={"milliseconds": "total_pit_time"},
        inplace=True
    )

    merged = pd.merge(
        pit_totals,
        results[["raceId", "driverId", "position"]].dropna(
            subset=["position"]),
        on=["raceId", "driverId"],
        how="inner"
    )

    merged.rename(
        columns={"position": "finish_position"},
        inplace=True
    )

    return merged


def inspect_q3_dataset(merged_q3: pd.DataFrame) -> None:
    """
    Print shape, columns, and missing values for the
    merged Question 4 dataset.
    """

    print("\n" + "=" * 60)
    print("QUESTION 4 MERGED DATASET")
    print("=" * 60)

    print("Shape:", merged_q3.shape)

    print("\nColumns:")
    print(merged_q3.columns.tolist())

    print("\nMissing Values:")
    print(merged_q3.isna().sum())
    print("\n")


def summarize_q3(merged_q3: pd.DataFrame) -> None:
    """
    Print descriptive statistics for pit stop time
    and finishing position.
    """

    print("\n" + "=" * 60)
    print("QUESTION 4 VARIABLE SUMMARIES")
    print("=" * 60)

    print("\nTotal Pit Stop Time Summary:")
    print(merged_q3["total_pit_time"].describe())

    print("\nFinish Position Summary:")
    print(merged_q3["finish_position"].describe())


def visualize_q2_altair(
                            merged_q2: pd.DataFrame,
                            drivers: pd.DataFrame
                        ) -> None:
    """
    Interactive visualization showing whether the first race winner
    """

    df = merged_q2.copy()

    drivers = drivers.copy()
    drivers["driver_name"] = drivers["forename"] + " " + drivers["surname"]

    df = df.merge(
        drivers[["driverId", "driver_name"]],
        on="driverId",
        how="left"
    )

    df["became_champion"] = df["final_championship_position"] == 1

    chart = alt.Chart(df).mark_circle(size=120).encode(
        x=alt.X("year:O", title="Season"),
        y=alt.Y(
            "final_championship_position",
            title="Final Championship Position"
        ),
        color=alt.Color(
            "became_champion:N",
            title="Outcome",
            scale=alt.Scale(
                domain=[True, False],
                range=["green", "red"]
            )
        ),
        tooltip=[
            alt.Tooltip("year", title="Season"),
            alt.Tooltip("driver_name", title="First Race Winner"),
            alt.Tooltip(
                "final_championship_position",
                title="Final Championship Position"
            ),
            alt.Tooltip("became_champion", title="Won Championship")
        ]
    ).properties(
        width=900,
        height=450,
        title="Did the First Race Winner Become World Champion?"
    ).interactive()

    chart.save("q2_first_race_interactive.html")


def visualize_q3(merged_q3: pd.DataFrame) -> None:
    """
    Generate two visualizations for Question 4.
    """

    plt.figure()
    plt.scatter(
        merged_q3["total_pit_time"],
        merged_q3["finish_position"],
        alpha=0.4
    )

    plt.title("Pit Stop Time vs Finish Position")
    plt.xlabel("Total Pit Stop Time (ms)")
    plt.ylabel("Finish Position")

    plt.savefig("q3_pit_time_vs_finish.png",
                bbox_inches="tight")
    plt.show()

    merged_q3["pit_time_bin"] = pd.qcut(
        merged_q3["total_pit_time"],
        q=4,
        duplicates="drop"
    )

    bin_means = (
        merged_q3.groupby("pit_time_bin")["finish_position"]
        .mean()
    )

    plt.figure()
    plt.bar(
        range(len(bin_means)),
        bin_means.values
    )

    plt.title("Average Finish Position by Pit Time Quartile")
    plt.xlabel("Pit Time Quartile (Low → High)")
    plt.ylabel("Average Finish Position")

    plt.savefig("q3_pit_time_bins.png",
                bbox_inches="tight")
    plt.show()


def visualize_q3_altair(
                            merged_q3: pd.DataFrame,
                            drivers: pd.DataFrame,
                            races: pd.DataFrame
                        ) -> None:
    """
    Interactive Altair visualization for pit stop time vs finish position
    """

    df = merged_q3.copy()

    if "pit_time_bin" in df.columns:
        df = df.drop(columns=["pit_time_bin"])

    drivers["driver_name"] = drivers["forename"] + " " + drivers["surname"]
    df = df.merge(
        drivers[["driverId", "driver_name"]],
        on="driverId",
        how="left"
    )

    df = df.merge(
        races[["raceId", "name", "year"]],
        on="raceId",
        how="left"
    )

    df.rename(columns={"name": "race_name"}, inplace=True)

    chart = alt.Chart(df).mark_circle(size=70).encode(
        x=alt.X(
            "total_pit_time",
            title="Total Pit Stop Time (ms)"
        ),
        y=alt.Y(
            "finish_position",
            title="Finish Position"
        ),
        tooltip=[
            alt.Tooltip("driver_name", title="Driver"),
            alt.Tooltip("race_name", title="Race"),
            alt.Tooltip("year", title="Year"),
            alt.Tooltip("total_pit_time", title="Pit Time (ms)"),
            alt.Tooltip("finish_position", title="Finish Position")
        ]
    ).properties(
        width=900,
        height=500,
        title="Pit Stop Time vs Finish Position (Interactive)"
    ).interactive()

    chart.save("q3_pit_vs_finish_altair.html")


def main() -> None:
    """
    Run EDA for Questions 2 and 4.
    """

    datasets = load_datasets()

    merged_q2 = build_q2_dataset(
        datasets["races"],
        datasets["results"],
        datasets["driver_standings"]
    )

    inspect_q2_dataset(merged_q2)
    summarize_q2(merged_q2)
    visualize_q2(merged_q2)
    visualize_q2_altair(merged_q2, datasets["drivers"])

    merged_q3 = build_q3_dataset(
        datasets["pit_stops"],
        datasets["results"]
    )

    inspect_q3_dataset(merged_q3)
    summarize_q3(merged_q3)
    visualize_q3(merged_q3)
    visualize_q3_altair(merged_q3,  datasets["drivers"], datasets["races"])


if __name__ == "__main__":
    main()
