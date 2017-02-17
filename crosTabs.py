# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 22:03:55 2017

@author: justinlboyer
"""

# creates preliminary crosstabs
MotionControl_Trained_PerfromNecess = pd.crosstab(sht1["TrainedWellOnDevice"],sht1["ICanEasilyPerformNecessaryTasksWithDevice"], margins=True)
MotionControl_Trained_PerfromNecess.columns = ["Disagree", "Agree", "StronglyAgree", "rowtotal"]
MotionControl_Trained_PerfromNecess.index = ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree", "ColTotal"]