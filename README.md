<b><h1>Denver Crime</h1></b>

<br>
<p align = "center">
<img src="readme_images/homepage.png" width=90% height=90%><br>
</p>
<br>

<b><h2>Why this project?</h2></b>

Denver Crime initially started as a small web-app: A hobby project with <b>Flask, JavaScript, MongoDB, and Python</b> to showcase interactive queries, data visualization, and [seasonal forecasting (skip to section)](#forecasting) using Holt-Winters exponential smoothing and additive nonlinear regression models (explanation on the latter below, also see [Prophet model publication](https://www.tandfonline.com/doi/abs/10.1080/00031305.2017.1380080?journalCode=utas20)).  <br><br>Denver Crime then grew due to interest from friends in local law-enforcement.  It is currently being tested with Vue.js with Tableau embeds.<br><br>


<br>
<p id = "breakdown" align = "center">
<b>Quick visualization of the dataset</b><br>
<img src="readme_images/crimebreakdown.png" width=90% height=90%><br>
</p>
<br>

<p><b><h2>The Dataset</h2></b>
Denver Crime takes nearly 400,000 of <a href = "https://www.kaggle.com/datasets/paultimothymooney/denver-crime-data"> DenverPD's recorded incidents </a> from 2017 to 2022, and stores them in a NoSQL database.  Users can make queries through a web form to return query results, which are presented as tables and visual/interactive elements.<br><br>

<br>
<p align = "center">
<b>Making an incident query by crime type</b>  
<img src="readme_images/querying.gif" width=90% height=90%><br>
</p>
<br>


<b><h2>What does it do? </h2></b>
With the intent of making a full-stack testbed that I could easily repurpose for more complex projects in the future, I had to structure/OOP carefully.  I started by:
1. Extracting Crime data and Offense Codes from CSVs and inserting parsed data into a NoSQL DB using <b>MongoDB</b> using <b>PyMongo</b>.
2. Using <b>Flask</b> and <b>MongoDB Query Language (MQL)</b> for form-based queries and table outputs (with more query types and analyses to come).
3. Conducting higher-level analyses in Python (i.e. average time between specified crime types, time windows with the most crime, areas with the most crime types). 
4. Forming interactive visualizations of incidents (maps with tooltips, so far) on user queries using <b>Bokeh</b>.
*Initial CSS styling and layout were provided via <b>Bootstrap</b> and [<b>Grayscale</b>](https://github.com/StartBootstrap/startbootstrap-grayscale).

<br>
<p align = "center">
<b>Mapped query results (red dots), and tooltip information from database on mouse-over of each incident</b> 
<img src="readme_images/mapdemo.gif" width=90% height=90%><br>
</p>
<br>

<b><h2 id="forecasting">Forecasting Models</h2></b>

Given (cyclical) trends in crime over time ([Fig. 2](#breakdown)), it seems reasonable to apply forecasting models which well-accommodate <b>seasonality</b>--both exponential smoothing and Meta's Prophet forecasting model (additive nonlinear regression) do so.  How does Prophet work?  We can see seasonality is accommodated by Prophet (as a periodic Fourier term) in its general mathematical model:
<p align = "center"><img src="readme_images/eqn1.png" width=25% height=25%></p>  

where <img valign="middle" src="readme_images/eqn1.1.png" height=20px>represents the nonperiodic trend, <img valign="middle" src="readme_images/eqn1.2.png" height=20px>represents the periodic (seasonal) component, and <img valign="middle" src="readme_images/eqn1.3.png" height=15px>represents a normally distributed error term.  Seasonality may occur daily, weekly, monthly, and/or yearly.  Other seasonalities and events such as holidays are accommodated may be accounted for by Prophet as well.<br><br>

<b><h3>Why is seasonality significant?</h3></b>
We see strong periodic behavior in Denver Crime, and the most apparent are weekly and yearly seasonalities: Fridays and Summer/early Fall tend to have the highest reported incidences of crime.  Indeed, even the onset of the COVID pandemic in the US seems to have had little effect on the seasonality of crime.  However, the general (non-periodic) trend in reported crimes appears to be distinctly positive.<br><br>

<b><h3>How robust is forecasting in accommodating events such as COVID lockdown?</h3></b>
If we predict upon data up until the onset of the pandemic (but deprive the model of any data after March 2020), Prophet understandably <a href=/readme_images/forecastfailure1.png>fails to forecast</a> the post-COVID increase in reported crimes (see "Forecast on data up until March 2020").  This is expected, as Prophet's non-periodic component is fitting to the relatively flat period in reported crimes, and has no data regarding crime after the lockdown.<br><br>

<br>
<p align = "center">
<b>Clean forecast without post-lockdown data</b><br>
<img src="readme_images/forecastfailure1.png" width=60% height=60%><br>
</p>
<br>

Interestingly, with just 8 months more data (up until the end of 2020--8 months after the onset of lockdowns), Prophet proves <i>slightly over-sensitive</i> to recent trends, <a href=/readme_images/forecastfailure2.png>overpredicting</a> the number of reported crimes by 8% by Summer 2022.  This difference is once again, attributable to the <a href=/readme_images/forecastfailure2.png>non-periodic component disproportionately weighting the increase</a> in reported crimes at the <i>onset</i> of the pandemic. Tuning the non-periodic component would require de-weighting of recent values.  Since Tableau's exponential smoothing model works in much the same way as Prophet's, a similar adjustment may be required there as well. <br><br>

<br>
<p align = "center">
<b></b><br>
<img src="readme_images/forecastfailure2.png" width=60% height=60%><br>
</p>
<br>

<b><h3>Should we use forecasting in criminal policy decision-making?</h3></b>
In the context of policy-making, it is important to be able to form and test hypotheses on trends to <i>determine causative effects</i> (correlation does not imply causation).  To test an independent variable for causative effect, we would need to control for all other variables which may affect the outcome.  These variables may include the weather, quarantine lockdowns, and even the price of cars and car parts (Denver has seen a ~300% increase in the rate of auto theft).<br>

<br>
<p align = "center">
<b>Denver Crime Forecast for 2023</b><br>
<img src="readme_images/crimeforecast.png" width=60% height=60%><br>
</p>
<br>

<br>
<p align = "center">
<b>Seasonal (periodic) components in Crime Forecast </b><br>
<img src="readme_images/seasonalcrime.png" width=60% height=60%><br>
</p>
<br>
<p align = "center"> <i>Negative components are part of the <a href=#forecasting>additive model</a>. Forecasts generated with the <a href=https://www.tandfonline.com/doi/abs/10.1080/00031305.2017.1380080?journalCode=utas20>Prophet model</a>.</i></p>


<!-- <p align = "center">
<img src="readme_images/queryselect.png" width=90% height=90%><br>
<b>Figure 2. Selecting type of crime to examine.</b>  
</p>
<br> -->
<!-- 
<br>
<p align = "center">
<b>Query results for "White Collar Crime"</b> 
<img src="readme_images/queryresults.png" width=90% height=90%><br>
 
</p>
<br> -->

<b><h2>Challenges?</h2></b>
* Some incidents within the original dataset seem binned into a specific day (i.e., there are dozens of incidents occuring on midnight, January 1, 2018).  This needs to be taken into account if time analysis for certain phenomena (i.e. "crime-waves"), thought it has less of an impact on certain calculations such as mean time between incidents.
* <b>PostgreSQL</b> would have also been perfect for this project (though I may be biased due to familiarity with Postgres).  The rationale for using MongoDB was to perform higher-level queries in MQL, and with the new $lookup function, inner/left/outer multi-attribute joins were easy to implement and fast to execute!
<br>

<br>
<p align = "center">
<b>Query Results over Time in Plotly</b> 
<img src="readme_images/dvovertime.gif" width=90% height=90%><br>
</p>
<br>

<b><h2>What's left?</h2></b>
1. Integrating [Denver City's address database](https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-addresses) for additional incident address information (building type: apartment, etc.).  A business address database is also available for further locational information. 
2. Additional inferences:
 * "Crime waves": Time-clustered incidences of crime.
 * "Crime hotspots": Spatially-clustered incidences of crime, based on GPS coordinates. 
 * "Crime hotspots over time": A visualization of crime hotspots over time.
 * "Risky buildings": A simple inference on building types with the highest incidences of crime.
3. Implementation of Vue.js elements.
4. Containerization and deployment to AWS using Docker.


<br>
<p align = "center">
<b>Motor Crime Hotspots over Time</b> 
<img src="readme_images/hotspotsvtime2.gif" width=90% height=90%><br>
</p>
<br>