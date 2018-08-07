Statistics Visualization Tool For Indian States 
 
The data used here is 26 excel sheets (Districts-> columns , Attributes-> rows)
The visualization tool developed here aims to create meaningful graphs out of the raw data collected by the government agencies. The data in it's raw form cannot be interpreted. It cannot be used for the purpose of analysis. This data needs to be converted into a form which can be used to draw comparisons between various attributes and this helps the government in power to decide the sectors that require more attention and focus.


Brief information about the data set used

The data used has been procured by the agency named " National Family Health survey (NFHS) ".

National Family Health survey (NFHS) provides updates and evidence of trends in key population, health and nutrition indicators, including HIV prevalence. Moreover, the survey covers a range of health-related issues, including fertility, infant and child mortality, maternal and child health, prenatal mortality, adolescent reproductive health, high-risk sexual behaviour, safe injections, tuberculosis, and malaria, non-communicable diseases, domestic violence, HIV knowledge, and attitudes toward people living with HIV.

Procedure to execute:
1)	First place all the excel sheets in one folder. Put the script aggregate.py in same folder and run it.
2)	Put the new files created in a different folder and put the scripts graph1.py and graph2.py in that folder.
3)	Graph1.py plots multiple states vs a single attribute and graph2.py plots multiple attributes vs a single state.

This has all been done and to directly get results download the repository and 
go to   index->ans->try1.py/try2.py.

Sample snapshots below.

1.) The inputs given to the python program for generating graphs:
![alt text](stats tool pics/1.png?raw=true "1")
 
 
2.) The obtained graphs:

 

This graph compares the ""blood sugar level" of six states and makes it very easy to compare the levels for the different states. This can make it easy to formulate state-specific action plans to tackle blood sugar level with the highest attention being given to Gujarat and Haryana.

 

This graph compares the values of five different attributes for one particular state i.e. Gujarat. This can be utilized to track the changes in these levels and also to make decisions about which sector requires changes or modifications.

 

This graph compares six attributes for the state of Jammu and Kashmir. All the sectors or fields of concern that need to be compared or analyzed can be selected and their percentage levels can be compared using this type of graph.


