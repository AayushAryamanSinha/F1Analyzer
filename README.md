These libraries must be installed on your Python: 
- kagglehub api
- altair
- plotly
- numpy
- pandas

Instructions on loading datasets: 
- If the csv are not downloaded please run get_data.py
- Ensure you have kagglehub in your enviorment to download the datasets needed to run the program

Instructions on loading graphs:
- Research Questions 1:
  - The program file for this question is research_question_1_development_plus_eda.py
  - Uncomment the portions of the main method code underneath the corresponding docstrings to run specific parts of the program
  - Comment every block of code in main() except for the code you would like to run whether it be:
    - The EDA constructor graphs
      - This will save hundreds of graphs onto your IDE folder so be careful 😥
    - The EDA driver graphs
      - This will also save hundreds of graphs onto your IDE folder so please kill the terminal when need be
    - Report research question interactive graph
      - This will pop out an html interactive plotly graph and also save the html file to your IDE folder
- Research Question 2 and 3: 
  - Run the research_questions_2_3_development_plus_eda.py and the plots will appear. Once you have looked at them you can cancel out of them and then go to file explorer and run q2_first_race.interactive.html and q4.pit_vs_finish_altair.html to run to see the interactive maps

Files:
- research_questions_1_development_plus_eda.py: Includes the developed implementations of the challenge goals and the EDA for the datasets needed for the question one.
- research_questions_2_3_development_plus_eda.py: Includes the developed implementations of the challenge goals and the EDA for the datasets needed for the questions two and three.
- get_data.py: gets data for someone running without csv files installed in a directory.
- testing_eda.py: tests eda results for the research questions.




