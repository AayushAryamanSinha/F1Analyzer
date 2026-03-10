import pandas as pd
import plotly.graph_objects as go


def load_csv(filepath):
    """
    Reads a CSV file and returns a pandas DataFrame
    """
    return pd.read_csv(filepath, na_values=['\\N'])


def main():
    # the team we wish to analyze the drivers of
    team = 'Mercedes'

    # save and merge names to results.csv
    drivers_df = load_csv('CSV\\drivers.csv')
    constructors_df = load_csv('CSV\\constructors.csv')
    races_df = load_csv('CSV\\races.csv')
    results_df = load_csv('CSV\\results.csv')
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
    # fig.write_html('racepoints.html')

    # test Hamilton vs Schumacher's average career earned points
    team_results.reset_index()
    assert (((team_results[team_results['driverId'] == 30]['points'].sum()) /
            (team_results[team_results['driverId'] == 30]['points'].count())) <
            ((team_results[team_results['driverId'] == 1]['points'].sum()) /
            (team_results[team_results['driverId'] == 1]['points'].count())))


if __name__ == '__main__':
    main()
