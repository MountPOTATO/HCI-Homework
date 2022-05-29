# HCI-Lab-3

- Course: Human Computer Interaction
- Student: Chen Kaixin
- ID: 1951724
- Tutor: Shen Ying

## Introduction

This project is based on the dataset **Google Play Store Apps**, containing apps in google play store with properties like category, rating, size, etc. The Play Store apps data has many potential to drive app-making businesses to success. Actionable insights can be drawn for developers to work on and capture the Android market.

## Requirements

This Dashboard demo requires the following python package. 

- plotly~=5.8.0
- numpy~=1.22.4
- dash~=2.4.1
- pandas~=1.4

## Installation and Run

activate your environment and run

```bash
pip install -r requirements.txt
```

After that, locate to the project directory and enter:

```bash
python dashboard.py
```

Then click the link of [http://localhost:8050/](http://localhost:8050/) to see the result.



## Project Structure

```shell
.
├── dashboard.py
├── data
│   └── googleDataVis.csv
├── doc
│   ├── HCI-Lab-3\ 89debdce87374ac9adff3546af2a5749
│   │   ├── Untitled\ 1.png
│   │   ├── Untitled\ 2.png
│   │   ├── Untitled\ 3.png
│   │   ├── Untitled\ 4.png
│   │   └── Untitled.png
│   └── HCI-Lab-3\ 89debdce87374ac9adff3546af2a5749.md
├── draw_html.py
├── requirements.txt
└── utils.py
```



## Result Display

In this project, the user can view the data chart in the form of **pie chart, bar chart, line chart and scatter chart**. 



### Dashboard Layout

![Untitled](HCI-Lab-3%2089debdce87374ac9adff3546af2a5749/Untitled.png)

The filter of category and type, as well as the rating ratio serves as the classification bases. Their modification will lead to the  alternation of the below graphs.

### 1. Pie Chart

![Untitled](HCI-Lab-3%2089debdce87374ac9adff3546af2a5749/Untitled%201.png)

The pie chart describes the number of apps under each rating, with given category and type.

## 2. Bar Chart

![Untitled](HCI-Lab-3%2089debdce87374ac9adff3546af2a5749/Untitled%202.png)

There are two bar charts in the demo. One shows the relationships between reviews and ratings with given category, type and rating, while the other shows the relationships between installs and ratings 

## 3. Line Chart

![Untitled](HCI-Lab-3%2089debdce87374ac9adff3546af2a5749/Untitled%203.png)

The line chart shows the relationships between installs and size with given category, type and rating.

## 4. Scatter Chart

![Untitled](HCI-Lab-3%2089debdce87374ac9adff3546af2a5749/Untitled%204.png)

The scatter chart shows the relationships between reviews and installs with given category, type and rating.