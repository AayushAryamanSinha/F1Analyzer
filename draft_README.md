# ***ANALYSIS AND INTERPRETATIONS OF TRENDS IN FORMULA 1***

## Ali Al Ali	 &	Aayush Sinha


## SUMMARY OF RESEARCH QUESTIONS:

1. Formula 1 is both car and driver so management often trades drivers in hopes of bettering their odds of winning. Is this a statistically legitimate tactic or is this placebo? Can a good driver overpower a historically inconsistent car? In other words, is there a visible spike in the team’s position standing when their car is paired with a driver who’s faster than the rest of the players in that season.  
2. How often does the result of the first race of the season decide the rest of the season? The results from the first race are compared to the results of the World Driver’s Championship result. This question aims to see if trends can be seen from strong performances during the start of the season. If a trend were to exist, what are the reasons for its existence? Is it the fact that the driver did well in the beginning or is it because the driver themselves is historically a good driver that led to the results at the end of the championship?  
3. With more restrictions on car designs from 1950 to 2024, have cars gotten faster or stayed the same? Which years brought about restrictions that have caused stronger changes in lap times? This is a time varying analysis of lap time trends with cross referencing possible extrema in the data with that year’s regulations.  
4. How does pitstop time affect the outcome of the driver’s race? Does spending less time in pit stop fixing the car contribute more or less to the race’s results compared to other factors (such as qualifying position which is historically known to determine race outcomes). If a driver starts up front, they will likely win.

## MOTIVATION:

Formula 1 as a sport produces a lot of data. Every team invests millions of dollars trying to extract information from this data in hopes to find any way to improve speed. The questions we have asked for this project analyse statistics based on factors on an off track. For example, results in F1 matter not only on the car but also the driver. We want to see if there are trends where drivers switching teams make the average lap times faster. On the contrary, we want to see how the mechanic’s precision pays off by looking at the effect pit stops have on the outcome of the race and comparing it to other factors such as qualifying. Results in formula start at the factory. Cars are a big part of the sport. We also want to see how different regulations affect the speed of im f1. Over the years there have been many changes to the way the cars are made, we want to see if F1 as a whole has gotten faster as years have gone by. Though this may seem obvious it is important to consider that there have been regulation changes which mandates teams to go from engines that are weaker on paper. For example the 2005 regulations mandated all teams to use a naturally aspirated V10 engine whereas the latest 2026 regulation has made that a V6 engine with 50% percent of the power train being electric. Lastly we want to see how often the first race affects the story for the World driver’s championship where we would compare close to 75 years of data to see how often the driver that wins the first race every season becomes the world champion. 

## DATASET:

The dataset we will use was compiled by the Ergast Developer API which contains Formula 1 race data. The data includes general driver, car manufacturer (constructor), circuit, and season information as well as data regarding the results, standings, and lap times of the drivers and constructors throughout the years throughout different circuits and seasons.

[https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020)

## CHALLENGE GOALS:

Challenge Goal 1 \- Using multiple datasets: 

The data source that we use has multiple csv files having different statistics and methods of indexing to identify each driver, race, track, team etc. We would have to prune this data to link everything together and use this as something we can find trends in and have meaningful analysis. 

Challenge Goal 2: Learning a new library: 

We want to learn a new library and think using something like altair or plotly can help us make interactive and detailed graphs which helps us visualise the trends and show correlation. 

## METHOD:

Formula 1 is both car and driver so management often trades drivers in hopes of bettering their odds of winning. Is this a statistically legitimate tactic or is this placebo? Can a good driver overpower a historically inconsistent car? In other words, is there a visible spike in the team’s position standing when their car is paired with a driver who’s faster than the rest of the players in that season.

Question 1 Method: This question will use multiple data sets to compare and contrast the team’s standings (the points they have for that year) with the standings of players who have recently been put onto the team. Each Formula 1 team has 2 drivers so we will use the driver who has NOT been changed as our reference for if the team’s standings have gotten better or not when the new player was added. For example, a team (constructor) which consists of 2 drivers, driver A and driver B, replaces driver B with driver C. We can graph driver C’s standings in their previous team(s) alongside their former team’s overall standings to see if there are any correlations (a good driver will help their team’s standings). We will have a baseline for driver C (the driver who is being brought into the new team). We will do the same calculations with driver A and driver B to understand how these drivers have impacted their team’s standings and gain a baseline for them too. We will do one last comparison, this time with the new driver C’s standings compared with their new team’s standings to see if driver C has or hasn’t impacted the team. If the correlation between drivers A and C and the new team is similar to the correlation between drivers A and B and the team then we know driver C did not impact the team’s standings and thus trading them in was not beneficial. However, if there is in an increase or decrease in the team’s standing after the addition of driver C, then we know adding the driver did in fact have an impact on the team and trading players is viable option. For data, we will use the constructor\_standings.csv, constructors.csv, driver\_standings\_csv, and drivers.csv and specifically the raceId columns in constructor\_standings.csv and driver\_standings.csv to determine which drivers were driving for which team for that race. We will also use the points columns in both constructor\_standings.csv and driver\_standings.csv to correlate the points earned by a driver and the points earned by the team.

How often does the result of the first race of the season decide the rest of the season? The results from the first race are compared to the results of the World Driver’s Championship result. This question aims to see if trends can be seen from strong performances during the start of the season. If a trend were to exist, what are the reasons for its existence? Is it the fact that the driver did well in the beginning or is it because the driver themselves is historically a good driver that led to the results at the end of the championship?

Question 2 Method: We want to see if winning the first race often sets you up for the rest of the season. For this we are going to be comparing the first race of every season to see who wins it and then find who the winner. We will be using the races.csv to find the race id for each race and identify which one was the first one every season, thereafter we will use drivers.csv to find the driver and use driver\_standing.csv to find who was the eventual WDC for that season. From the mentioned datasets we would need columns such as driver id, race id, World Driver Champion and year to carry out statistical analysis.

With more restrictions on car designs from 1950 to 2024, have cars gotten faster or stayed the same? Which years brought about restrictions that have caused stronger changes in lap times? This is a time varying analysis of lap time trends with cross referencing possible extrema in the data with that year’s regulations.

Question 3 Method: This will be an analysis within specific teams, basically the data for lap times (good indication of how fast the car is) will be compared to lap times for that specific team over a period of time to see if cars have gotten faster over the years. F1 cars used to use V10’s until they eventually used less and less cylinders for efficiency (hybrid electric restrictions are being made for the near future). We will check the trends seen across multiple teams to see if the cars have gotten faster or not (this will reduce the impact different driver skills will have on the car trends). If we see spots where cars overall stay the same speed or get slower, then we can check the International Automobile Federation’s (FIA owns Formula 1\) engine restrictions for those years to see what may have caused these sudden stops or drops in lap times. We will use the time column in the lap\_times.csv with the driverId column to determine the lap time for that driver (in other words for the team they race for in constructors.csv and drivers.csv) and the raceId column to determine the time frame (each raceId has its own year in races.csv).

How does pitstop time affect the outcome of the driver’s race? Does spending less time in pit stop fixing the car contribute more or less to the race’s results compared to other factors (such as qualifying position which is historically known to determine race outcomes). If a driver starts up front, they will likely win.

Question 4 Method: We want to see how much time spent in the pitstop affects the result of the race. For this we will calculate the total time each driver spends in the pitstop and see what position they ended up finishing in the race. It would also be worth considering different things like starting positions to see which statistic is actually having a definitive trend. For this we will use the drivers.csv and race.csv to see the results for each driver. We will also use pit\_stop.csv to find each time for the driver and sum to total time (because teams can have more than 1 pitstop, it is also worth noting that rules mandate that each team has at least one pitstop every race). To the effect of qualifying to compare with the trends of the pitstop we will be using qualifying.csv. From the datasets mentioned above we will use columns like driver id, race id, duration (pitstop) and winner (race winner) to carry out the analysis. 

## WORK PLAN:

Complete data analysis \- Feb 16

(Expected time: 4 \- 5 hours)

- The goal here is to fully understand the datasets we have, what data we will actually use, and how we will use that data  
- Not all data in the datasets will be used, so it’s important to detail which data will actually be useful in helping us answer our research questions  
- Both authors will take 2 questions each and tackle the corresponding data sets required to answer the question  
  Code all tasks required to answer the research questions \- Feb 28  
  (Expected time: 10+ hours)  
- The goal here is to split each question into separate collections of Python tasks that will calculate and visualize trends in the data for the specific task so we can formulate answers to our questions  
- Tasks will be split based on who wants to answer which question and will have flexible workflows in case challenges in both coding or conceptualizing arise  
- The code will be tested in VS Code with lots of graphing aid to help us see if our code is selecting the correct data to compute  
- Graphs will help us see trends too which is useful for understanding our data further  
- Constant communication throughout the project will be key  
- We plan to develop and test our code in VS Code as we’re both familiar with it and it’s a pretty strong software for large data analysis  
  Complete the report \- March 5  
  	(Expected time: 10+ hours)  
- The goal here is to accumulate all the work we’ve done so far and document it in a way that is both presentable and orderly  
- The code calculates and provides visualizations but what does this mean? What do the trends tell us in the context of answering our research questions?  
- The report will be split research question by research question, preceded by an overview of the project (why we’re doing this particular project, what we wish to accomplish, and the tools and resources we used to accomplish our goals)  
- This report portion will be written simultaneously alongside the coding of the actual tasks as the report will be split up question by question and so are the coding tasks (everything is organized based on the aims of the research question)
