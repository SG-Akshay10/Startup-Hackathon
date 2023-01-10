# NIT-Hackathon
## Capital Catalyst

Project from : 
* Akshay S G - Shiv Nadar University , Chennai
* Surya S - Shiv Nadar University , Chennai

## Prerequisites for the project : 
 * You need to have a postgre database created with the values of the Indian Startup.csv file loaded into it.
 * Install all required libraries

## Working of our project : 

We connect SQL database(PostgreSQL) with our /code app.py file which is then preprocessed and the data is used in our machine learning model.

![database](https://user-images.githubusercontent.com/83088512/211532057-1fb18478-0465-4716-b91c-2ceb020e52a2.png)


The same preprocessed data is used as training dataset for our machine learning algorithm.

In this algorithm we take in 2 or more feataures of the data set and derive a similarity matrix comparing those constrains(Cosine similarity) to find the most accurate/similar startups for the investors.

The front end of this project is done mostly with streamlit module of python database from postgreSQL and streamlit is connceted using psycog2.

![home](https://user-images.githubusercontent.com/83088512/211532226-546939b5-8866-4722-985d-9f2f33c6316b.png)
![input](https://user-images.githubusercontent.com/83088512/211532229-c9966eba-b858-4bfa-819f-b1e4a4ca9da0.png)

![out1](https://user-images.githubusercontent.com/83088512/211532207-efce8580-a2d4-4454-8993-92a0e848b9b7.png)
![out3](https://user-images.githubusercontent.com/83088512/211532211-32e5e04e-56a5-4b6c-a232-3b189083d96a.png)
![out2](https://user-images.githubusercontent.com/83088512/211532215-a9f22e5e-a11f-4c18-9f01-3de583057d2b.png)


[video.webm](https://user-images.githubusercontent.com/83088512/211532306-14f1d26a-7c98-4495-af32-9b90445d13df.webm)
