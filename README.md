## Exploratory Data Analysis of Vehicles

### For anyone:
This project is an interactive web application that allows you to
visually explore a dataset of vehicles for sale.

Optimization and Performance
In this project, I focused not only on visualization but also on software efficiency:

- Data Caching: I used the @st.cache_data decorator to cache CSV processing. This prevents the application from reloading and cleaning data with each user interaction, reducing response time from seconds to milliseconds.

- Resource Efficiency: By processing transformations (such as mark extraction and null removal) within a cache function, I optimized CPU and RAM usage on the server.
