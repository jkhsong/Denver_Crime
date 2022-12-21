<b><h1>Denver Crime</h1></b>

<br>
<p align = "center">
<img src="readme_images/homepage.png" width=90% height=90%><br>
</p>
<br>

<b><h2>Why this project?</h2></b>

Denver Crime initially started as a small, fun project with a <b>Flask, JavaScript, MongoDB, and Python</b> stack, and grew due to interest from friends in local law-enforcement.  The front end is currently being tested with Vue.js.<br><br>

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

<b><h2>What's left?</h2></b>
1. Integrating [Denver City's address database](https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-addresses) for additional incident address information (building type: apartment, etc.).  A business address database is also available for further locational information. 
2. Additional inferences:
 * "Crime waves": Time-clustered incidences of crime.
 * "Crime hotspots": Spatially-clustered incidences of crime, based on GPS coordinates. 
 * "Crime hotspots over time": A visualization of crime hotspots over time.
 * "Risky buildings": A simple inference on building types with the highest incidences of crime.
3. Implementation of Vue.js elements.
4. Containerization and deployment to AWS using Docker.

