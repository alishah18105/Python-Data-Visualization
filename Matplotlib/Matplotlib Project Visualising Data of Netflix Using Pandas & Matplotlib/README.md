# Visualising Data of Netflix Using Pandas & Matplotlib 🎬📊

A data visualization project using **Python, Pandas, and Matplotlib** to explore and visualize the **Netflix Titles dataset**.

The project focuses on cleaning the dataset, analyzing different aspects of Netflix content, and representing the results through different types of charts and plots.

## 📌 Project Overview

The Netflix dataset contains information about movies and TV shows available on Netflix, including:

* Content type
* Title
* Director
* Cast
* Country
* Date added
* Release year
* Rating
* Duration
* Genre
* Description

In this project, I used **Pandas** for loading, cleaning, filtering, grouping, and analyzing the dataset, while **Matplotlib** was used to create and customize visualizations.

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **Matplotlib**
* **CSV Dataset**

## 🔄 Project Workflow

```text
Netflix Dataset
       ↓
Load Dataset with Pandas
       ↓
Check & Clean Missing Values
       ↓
Filter & Group Data
       ↓
Analyze Different Features
       ↓
Create Visualizations with Matplotlib
       ↓
Save Charts as PNG Images
```

## 🧹 Data Cleaning

The dataset contained missing values in several columns.

Missing values in the following columns were replaced with `"Unknown"`:

* `director`
* `cast`
* `country`

Rows with missing values in the following columns were removed:

* `date_added`
* `rating`
* `duration`

After cleaning, the dataset was checked again to verify the remaining missing values.

## 📊 Visualizations

### 1. Movies vs TV Shows

A **bar chart** was created to compare the number of Movies and TV Shows in the Netflix dataset.

**Concepts practiced:**

* `value_counts()`
* Bar charts
* Titles
* X/Y-axis labels
* Figure size
* Saving plots

### 2. Distribution of Ratings

A **pie chart** was used to visualize the distribution of different Netflix content ratings.

**Concepts practiced:**

* `value_counts()`
* Pie charts
* Percentage labels
* Legends
* `autopct`
* Chart customization

### 3. Movie Duration Distribution

A **histogram** was created to visualize the distribution of movie durations.

The duration values were converted from strings such as `"90 min"` into integers so they could be analyzed numerically.

**Concepts practiced:**

* Filtering Movies
* Creating a new column
* String manipulation
* Type conversion
* Histograms
* Bins

### 4. Release Year vs Number of Shows

A **scatter plot** was created to visualize the number of Netflix titles released in each year.

The data was grouped by `release_year` and counted before creating the visualization.

**Concepts practiced:**

* `value_counts()`
* `sort_index()`
* Scatter plots
* Grid
* Grouped data visualization

### 5. Top 10 Countries

A **horizontal bar chart** was used to show the top 10 countries with the highest number of Netflix titles.

**Concepts practiced:**

* `value_counts()`
* `head()`
* Horizontal bar charts
* Sorting and ranking data

### 6. Movies and TV Shows Released Over the Years

A comparison visualization was created using **subplots** to show the number of Movies and TV Shows released over the years.

The data was grouped by:

* `release_year`
* `type`

Two line charts were then created within the same figure.

**Concepts practiced:**

* `groupby()`
* `unstack()`
* `fillna()`
* Subplots
* Multiple axes
* Line charts
* Figure titles

## 📁 Project Structure

```text
Visualising Data of Netflix Using Pandas & Matplotlib/
│
├── netflix_titles.csv
├── Python visualization script
├── Visualization images
└── README.md
```

## 🎯 What I Learned

Through this project, I practiced working with a real-world dataset and learned how to:

* Load CSV data using Pandas
* Inspect and clean missing data
* Filter DataFrames
* Create new columns
* Convert string data into numerical values
* Count and group data
* Sort and rank data
* Use different Matplotlib charts
* Customize plots with titles, labels, legends, and grids
* Create multiple plots using subplots
* Save visualizations as image files

## 📈 Matplotlib Concepts Applied

This project brought together several concepts learned while practicing Matplotlib:

* Bar Chart
* Horizontal Bar Chart
* Pie Chart
* Histogram
* Scatter Plot
* Line Chart
* Subplots
* Figure and Axes
* Titles
* Axis Labels
* Legends
* Grid
* Figure Size
* Saving Figures

## 🎓 Learning Objective

The main objective of this project was to apply **Pandas and Matplotlib concepts to a real-world dataset** rather than working only with manually created data.

It helped me understand how raw data can be:

**Loaded → Cleaned → Analyzed → Visualized**

and transformed into charts that make patterns and comparisons easier to understand.

## 👨‍💻 Author

**Syed Ali Sultan**

BS Software Engineering
University of Karachi

---

Part of the [Python Data Visualization](../../) repository.
