# Hackathon: “From Data Collection to AI Application”

**Duration**: 1 day


This mini project will guide you through the complete data analysis workflow, from collecting raw data to building visual insights, training a machine learning model, and creating a simple RAG chatbot.

You will use tools commonly used by data analysts and data scientists such as Pandas, Matplotlib, Seaborn, and Scikit-learn.

## Project Instructions

### 1. **Collect a Dataset**

- Visit the platform [Kaggle](https://www.kaggle.com/datasets)
- Search for a dataset that interests you (examples: finance, sports, health, movies, retail, transportation, etc.)
- Download the dataset in CSV format
- Requirements for the dataset:
  - At least 500 rows
  - At least 5 columns
  - Prefer datasets with a mix of numeric and categorical variables
- Save the dataset in your project folder


### 2. **Define Analysis Questions and Hypotheses**

> Before analysing the data, you must define 5 analytical questions and 5 hypotheses

- **Example structure**:
  - Question: Does advertising spending increase sales?
  - Hypothesis: Higher advertising spending is associated with higher sales.
- **Your task**
  - Write 5 questions you want to answer using the dataset
  - Write a testable hypothesis for each question

- **Example types of questions**:
  - Trend analysis
  - Comparison between groups
  - Correlation between variables
  - Distribution of values
  - Impact of one variable on another


### 3. Load and Explore the Data

**Using Pandas**:
- Load the dataset into a DataFrame
- Perform basic exploration:
  - View the first rows (`head`)
  - Check dataset structure (`info`)
  - Generate summary statistics (`describe`)
  - Identify missing values
  - Identify data types
- Document key observations


### 4. Clean and Transform the Data

*Prepare the dataset for analysis*

**Possible steps include**:
- Handling missing values
  - Remove rows
  - Fill values (`mean`, `median`, `mode`)
- Removing duplicates
- Converting data types
- Renaming columns
- Creating new features if useful
- Encoding categorical variables if necessary

> Your goal is to produce a clean dataset ready for analysis and modelling.


### 5. Exploratory Data Analysis (EDA)

*Create at least 5 visualisations to investigate your questions and hypotheses.*

**Use**:
- Matplotlib
- Seaborn

**Possible plot types**:
- Bar chart
- Histogram
- Box plot
- Scatter plot
- Heatmap (correlation matrix)
- Line chart

**For each plot**:
- Add a title
- Label axes
- Briefly explain what insight the plot provides
- Explain whether the result supports or contradicts your hypothesis


### 6. Train a Machine Learning Model

*Using Scikit-learn, train a model using your cleaned dataset.*

> **Important rule**: You cannot use Linear/Logistic Regression or KNN, since these models were already covered previously.

**Choose one new model, such as**:
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)

**Steps**
- Select input features (X)
- Select a target variable (y)
- Split data into:
  - Training set
  - Testing set
- Train the model
- Evaluate performance using appropriate metrics

**Examples of evaluation metrics**:
- Accuracy
- Precision / Recall
- Mean Squared Error
- R² score

**Explain**:
- Why you chose this model
- How well it performed
- What the predictions tell you


### 7. Build a Simple RAG Chatbot

*Use the cleaned dataset to create a Retrieval-Augmented Generation (RAG) chatbot.*

> The goal is to allow users to ask questions about the dataset in natural language.

**Steps**:
- Convert the dataset (or insights from it) into text documents
- Use an embedding model to create vector representations, and store them (a plain Python list is enough at this scale)
- Retrieve relevant data when a user asks a question, by comparing embeddings with cosine similarity
- Generate an answer using a language model

**Possible tools**:
- `sentence-transformers` for embeddings, and cosine similarity for retrieval — the same approach covered in lecture
- OpenAI (or another LLM) for generation
- *Optional stretch*: a real vector database (FAISS, Chroma) or a framework like LangChain, if you want to go beyond what was covered

**Example user questions**:
- “What are the main trends in this dataset?”
- “Which category has the highest values?”
- “What factors seem to influence the target variable?”


### 8. Final Deliverables

- Create a GitHub repository that *must* include:
  - The dataset
  - Jupyter Notebooks containing:
    - The Dataset
    - Data cleaning & transformation
    - EDA and visualisations
    - Machine learning model
- A beautiful README file
  - A summary of the 5 questions and hypotheses
  - Explanations of insights from your plots
  - ML model results and interpretation
  - A simple RAG chatbot demonstration
