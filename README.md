# Coronavirus-World-stats
An Flask app that shows a simple graph on the rate of Coronavirus across the world

# libraries used

* Flask==1.1.2
* gunicorn==20.0.4
* numpy==1.19.1
* pandas==1.1.1
* plotly==4.9.0
* requests==2.24.0
* urllib3==1.25.10

Data fetched from [Apify](https://api.apify.com/)

 ### Motivation for the project
 This project was engineered by udacity
 
 Coronaviruses are a group of related RNA viruses that cause diseases in mammals and birds. In humans and birds, they cause respiratory tract infections that can range from mild to lethal. Mild illnesses in humans include some cases of the common cold (which is also caused by other viruses, predominantly rhinoviruses), while more lethal varieties can cause SARS, MERS, and COVID-19. In cows and pigs they cause diarrhea, while in mice they cause hepatitis and encephalomyelitis. There are as yet no vaccines or antiviral drugs to prevent or treat human coronavirus infections.

This apps shows the number of people infected, deceased and recovered in 48 countries  according to apify.com to unable people see the rising rate and the deaths inorder to understand how fast it spreads and how deadly if could be.

 Data Analysis is done with the flask and plotly,Boostrap and Jquery.
 
 * Flask is a python framework for web development
 * Plotly is a python library used for plotting render-able graphs
 * Boostrap is a CSS framework for frontend designs.
 
 
 ### Files in the repository 
 
 * coronavirus_world_stats 
  * Static - contains 
    * img - images folder
  * templates - html files
    * index.html - 
  * __ init__.py
  * routes.py - python files with routes to the html pages
 * wrangling_scripts - a folder with wrangling script
    * wrangle_data.py - a python script that does the data wrangling
 * coronavirus_world_stats.py - a base python file
 * Procfile
 * requirement.txt- contains all neccesary libraries needed
 
    
### Summary of the results of the analysis
  This project shows the update on coronavirus on each countries all over the world , the rate if infected peop;e, the deceased and the recovered.
  Coronavirus pandemic has affected a lots of people all over the world.



