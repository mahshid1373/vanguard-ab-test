# Project 2: Vanguard CX Digital Experiment Analysis

## Project Brief

### Context
You are a newly employed data analyst in the Customer Experience (CX) team at Vanguard, the US-based investment management company. You’ve been thrown straight into the deep end with your first task. Before your arrival, the team launched an exciting digital experiment, and now, they’re eagerly waiting to uncover the results and need your help!

### The Digital Challenge
The digital world is evolving, and so are Vanguard’s clients. Vanguard believed that a more intuitive and modern User Interface (UI), coupled with timely in-context prompts (cues, messages, hints, or instructions provided to users directly within the context of their current task or action), could make the online process smoother for clients. The critical question was: Would these changes encourage more clients to complete the process?

### The Experiment Conducted
An A/B test was set into motion from 3/15/2017 to 6/20/2017 by the team.

- **Control Group**: Clients interacted with Vanguard’s traditional online process.
- **Test Group**: Clients experienced the new, spruced-up digital interface.

Both groups navigated through an identical process sequence: an initial page, three subsequent steps, and finally, a confirmation page signaling process completion.

The goal is to see if the new design leads to a better user experience and higher process completion rates.

### AB Testing
Note: Review what A/B testing is [here](https://www.optimizely.com/optimization-glossary/ab-testing/) if you are not already aware of how it works.

## Getting Started
# Dataset Cleaning Project

This repository contains the code and dataset used for cleaning a web log dataset. The dataset consists of web visit logs with several attributes related to user activity on a website.

## Dataset

The dataset is provided in the file `df_final_web_data_pt_1.txt` and  `df_final_web_data_pt_2.txt`. It contains the following columns:

- `client_id`: An identifier for the client.
- `visitor_id`: An identifier for the visitor.
- `visit_id`: An identifier for the visit session.
- `process_step`: The step in the process the user is in.
- `date_time`: The date and time of the recorded step.

### Sample Data

| client_id | visitor_id          | visit_id                   | process_step | date_time           |
|-----------|---------------------|----------------------------|--------------|---------------------|
| 9988021   | 580560515_7732621733| 781255054_21935453173_531117 | step_3       | 2017-04-17 15:27:07 |
| 9988021   | 580560515_7732621733| 781255054_21935453173_531117 | step_2       | 2017-04-17 15:26:51 |
| 9988021   | 580560515_7732621733| 781255054_21935453173_531117 | step_3       | 2017-04-17 15:19:22 |
| 9988021   | 580560515_7732621733| 781255054_21935453173_531117 | step_2       | 2017-04-17 15:19:13 |
| 9988021   | 580560515_7732621733| 781255054_21935453173_531117 | step_3       | 2017-04-17 15:18:04 |

## Data Cleaning Process

The data cleaning process was performed in a Jupyter Notebook (`Dataset_pt_Cleaning.ipynb`) and involved the following steps:

1. **Remove Duplicates**
2. **Check for Missing Values**
3. **Convert Data Types**
4. **Normalize Data**
5. **Analyze Categories in process_step**

=======
### Prerequisites
- Python 3.x
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib / Seaborn (for data visualization)

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/vanguard-ab-test.git
    ```
2. Navigate to the project directory:
    ```sh
    cd vanguard-ab-test
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Open the Jupyter Notebook:
    ```sh
    jupyter notebook
    ```
2. Open the notebook file `main.ipynb` and run through the cells to see the analysis.

## Project Structure
- `Data/`: Contains the dataset used for the analysis.
- `Notebooks/`: Jupyter Notebooks with detailed analysis.
- `README.md`: Project documentation.

## Contributing
1. Fork the repository.
2. Create your feature branch:
    ```sh
    git checkout -b feature/YourFeature
    ```
3. Commit your changes:
    ```sh
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```sh
    git push origin feature/YourFeature
    ```
5. Open a pull request.

## License
This project is licensed under the Ironhack.

## Acknowledgments
- Mahshid Khatami [linkedin](https://www.linkedin.com/in/mahshidkhatami-data-analyst)
- Faheem Khan [linkedin](https://https://www.linkedin.com/in/faheem-j-khan-1b9ba19a/)

