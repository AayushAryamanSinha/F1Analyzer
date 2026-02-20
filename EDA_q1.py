import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np


def load_csv(filepath):
    """
    Reads a CSV file and returns a pandas DataFrame
    """
    return pd.read_csv(filepath, na_values=["\\N"])


def constructors_graph_1(df):
    unique_names = df['name'].unique()
    names_per_plot = 20
    num_plots = math.ceil(len(unique_names) / names_per_plot)
    for i in range(num_plots):
        names_subset = unique_names[i * names_per_plot: (i+1)*names_per_plot]
        plt.figure(figsize=(12, 6))
        for name in names_subset:
            subset = df[df['name'] == name]
            plt.scatter(subset['raceId'], subset['points'], label=name)
        plt.xlabel('raceId')
        plt.ylabel('points')
        plt.title(f'Points vs RaceID (Names {i*names_per_plot + 1} to {(i+1) * names_per_plot})')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f'scatter_plot_{i+1}.jpg', format='jpg', dpi=300)


def constructors_graph_2(df):
    unique_names = df['name'].unique()
    names_per_plot = 20
    num_plots = math.ceil(len(unique_names) / names_per_plot)
    for i in range(num_plots):
        names_subset = unique_names[i * names_per_plot: (i+1) * names_per_plot]
        plt.figure(figsize=(14, 7))
        bar_width = 0.8 / len(names_subset)
        race_ids = sorted(df['raceId'].unique())
        x = np.arange(len(race_ids))
        for j, name in enumerate(names_subset):
            subset = df[df['name'] == name]
            points = [subset[subset['raceId'] == rid]['points'].values[0]
                      if rid in subset['raceId'].values else 0
                      for rid in race_ids]
            plt.bar(x + j*bar_width, points, width=bar_width, label=name)
        plt.xlabel('raceId')
        plt.ylabel('points')
        plt.title(f'Points vs RaceID (Names {i * names_per_plot + 1} to {(i+1) * names_per_plot})')
        plt.xticks(x + bar_width*(len(names_subset)/2 - 0.5), race_ids)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(axis='y')
        plt.tight_layout()
        plt.savefig(f'bar_plot_{i+1}.jpg', format='jpg', dpi=300)


def drivers_graph_1(df):
    unique_names = df['surname'].unique()
    names_per_plot = 20
    num_plots = math.ceil(len(unique_names) / names_per_plot)
    for i in range(num_plots):
        names_subset = unique_names[i * names_per_plot: (i+1)*names_per_plot]
        plt.figure(figsize=(12, 6))
        for name in names_subset:
            subset = df[df['surname'] == name]
            plt.scatter(subset['raceId'], subset['points'], label=name)
        plt.xlabel('raceId')
        plt.ylabel('points')
        plt.title(f'Points vs RaceID (Names {i*names_per_plot + 1} to {(i+1) * names_per_plot})')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f'scatter_plot_{i+1}.jpg', format='jpg', dpi=300)


def drivers_graph_2(df):
    unique_names = df['surname'].unique()
    names_per_plot = 20
    num_plots = math.ceil(len(unique_names) / names_per_plot)
    for i in range(num_plots):
        names_subset = unique_names[i * names_per_plot: (i+1) * names_per_plot]
        plt.figure(figsize=(14, 7))
        bar_width = 0.8 / len(names_subset)
        race_ids = sorted(df['raceId'].unique())
        x = np.arange(len(race_ids))
        for j, name in enumerate(names_subset):
            subset = df[df['surname'] == name]
            points = [subset[subset['raceId'] == rid]['points'].values[0]
                      if rid in subset['raceId'].values else 0
                      for rid in race_ids]
            plt.bar(x + j*bar_width, points, width=bar_width, label=name)
        plt.xlabel('raceId')
        plt.ylabel('points')
        plt.title(f'Points vs RaceID (Names {i * names_per_plot + 1} to {(i+1) * names_per_plot})')
        plt.xticks(x + bar_width*(len(names_subset)/2 - 0.5), race_ids)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(axis='y')
        plt.tight_layout()
        plt.savefig(f'bar_plot_{i+1}.jpg', format='jpg', dpi=300)


def main():
    dataframe2 = load_csv('datasets/raw/driver_standings.csv')
    dataframe1 = load_csv('datasets/raw/drivers.csv')

    merged_df = pd.merge(dataframe1[['driverId', 'forename', 'surname']], dataframe2,
                         on="driverId", how='left')
    drivers_graph_2(merged_df)


if __name__ == "__main__":
    main()
