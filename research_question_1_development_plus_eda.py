import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import math
import numpy as np


def load_csv(filepath: str) -> pd.DataFrame:
    """
    Reads a CSV file and returns a pandas DataFrame
    """
    return pd.read_csv(filepath, na_values=['\\N'])


def constructors_graph_1(df: pd.DataFrame) -> None:
    """
     Create scatter plots of constructor points vs raceId.
    """
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
        plt.title(f'Points vs RaceID (Names {i*names_per_plot + 1} to {
            (i+1) * names_per_plot})')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f'scatter_plot_{i+1}.jpg', format='jpg', dpi=300)


def constructors_graph_2(df: pd.DataFrame) -> None:
    """
    Create bar plots of constructor points vs raceId.
    """
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
        plt.title(f'Points vs RaceID (Names {i * names_per_plot + 1} to {
            (i+1) * names_per_plot})')
        plt.xticks(x + bar_width*(len(names_subset)/2 - 0.5), race_ids)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(axis='y')
        plt.tight_layout()
        plt.savefig(f'bar_plot_{i+1}.jpg', format='jpg', dpi=300)


def drivers_graph_1(df: pd.DataFrame) -> None:
    """
    Create scatter plots of driver points vs raceId.
    """
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
        plt.title(f'Points vs RaceID (Names {i*names_per_plot + 1} to {
            (i+1) * names_per_plot})')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f'scatter_plot_{i+1}.jpg', format='jpg', dpi=300)


def drivers_graph_2(df: pd.DataFrame) -> None:
    """
    Create bar plots of driver points vs raceId.
    """
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
        plt.title(f'Points vs RaceID (Names {i * names_per_plot + 1} to {
            (i+1) * names_per_plot})')
        plt.xticks(x + bar_width*(len(names_subset)/2 - 0.5), race_ids)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(axis='y')
        plt.tight_layout()
        plt.savefig(f'bar_plot_{i+1}.jpg', format='jpg', dpi=300)


def main():
    """
    Exploratory Data Analysis Portion:

    To create the driver graphs, please uncomment the following code and
    comment everything else out
    """
    # dataframe2 = load_csv('datasets/raw/driver_standings.csv')
    # dataframe1 = load_csv('datasets/raw/drivers.csv')
    # merged_df = pd.merge(dataframe1[['driverId', 'forename', 'surname']],
    #                      dataframe2, on='driverId', how='left')
    # drivers_graph_1(merged_df)
    # dataframe2 = load_csv('datasets/raw/driver_standings.csv')
    # dataframe1 = load_csv('datasets/raw/drivers.csv')
    # merged_df = pd.merge(dataframe1[['driverId', 'forename', 'surname']],
    #                      dataframe2, on='driverId', how='left')
    # drivers_graph_2(merged_df)

    """
    To create the constructor graphs, please uncomment the following code and
    comment everything else out
    """
    # dataframe2 = load_csv('datasets/raw/constructor_standings.csv')
    # dataframe1 = load_csv('datasets/raw/constructors.csv')
    # merged_df = pd.merge(dataframe1[['constructorId', 'name']],
    #                      dataframe2, on='constructorId', how='left')
    # constructors_graph_1(merged_df)
    # dataframe2 = load_csv('datasets/raw/constructor_standings.csv')
    # dataframe1 = load_csv('datasets/raw/constructors.csv')
    # merged_df = pd.merge(dataframe1[['constructorId', 'name']],
    #                      dataframe2, on='constructorId', how='left')
    # constructors_graph_2(merged_df)

    """
    Main Report Portion:

    To create the interactive "driver and constructor points won" graph please
    uncomment the following code and comment everything else out
    """
    # the team we wish to analyze the drivers of:
    team = 'McLaren'

    # save and merge names to results.csv
    drivers_df = load_csv('datasets/raw/drivers.csv')
    constructors_df = load_csv('datasets/raw/constructors.csv')
    races_df = load_csv('datasets/raw/races.csv')
    results_df = load_csv('datasets/raw/results.csv')
    results_merged_df = pd.merge(
        constructors_df[['constructorId', 'name']],
        results_df, on='constructorId', how='left'
    )
    results_merged_df = pd.merge(
        drivers_df[['driverId', 'forename', 'surname']],
        results_merged_df, on='driverId', how='left'
    )
    results_merged_df = pd.merge(
        races_df[['raceId', 'date']],
        results_merged_df, on='raceId', how='left'
    )
    results_merged_df['date'] = pd.to_datetime(results_merged_df['date'])

    # filter results to just one team
    team_results = results_merged_df[
        (results_merged_df['name'] == team)
    ]
    team_results['total_points'] = team_results.groupby('raceId')[
        'points'].transform('sum')
    team_results = team_results.sort_values(by=['date', 'driverId'])

    # graph driver vs constructor's total points
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=team_results['date'],
        y=team_results['total_points'],
        mode='lines',
        line=dict(color='#434343', width=0),
        fill='tozeroy',
        name='Total Points',
        opacity=0.3,
        showlegend=True
    ))
    drivers = team_results['driverId'].unique()
    for driver in drivers:
        driver_df = team_results[team_results['driverId'] == driver]
        driver_name = team_results.loc[
            team_results['driverId'] == driver, 'surname'].values[0]
        fig.add_trace(go.Scatter(
            x=driver_df['date'],
            y=driver_df['points'],
            mode='lines',
            name=driver_name,
            line=dict(width=2)
        ))
    fig.update_layout(
        title={
            'text': f'POINTS EARNED PER RACE BY {team.upper()} DRIVERS',
            'font': {
                'size': 40,
                'family': 'helvetica',
                'color': '#3C3C3C'}},
        xaxis_title={
            'text': 'DATE OF RACE', 'font': {
                'size': 24,
                'family': 'helvetica',
                'color': '#3C3C3C'}},
        yaxis_title={
            'text': 'POINTS EARNED', 'font': {
                'size': 24,
                'family': 'helvetica',
                'color': '#3C3C3C'}},
        legend=dict(
            font=dict(family='helvetica', size=16, color='#3C3C3C'),
            x=0,
            y=1,
            bgcolor='rgba(0,0,0,0.1)',
        ),
        paper_bgcolor='#e2e2e2',
        plot_bgcolor='#b5b5b5',
    )
    fig.show()
    fig.write_html('q1_racepoints.html')


if __name__ == '__main__':
    main()
