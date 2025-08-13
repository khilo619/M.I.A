# F1 Racer Diet Planning

## Project Overview
This project aims to predict the caloric requirements for Formula 1 racers based on various physiological and physical parameters. The model utilizes machine learning techniques to accurately estimate calorie needs, which is crucial for maintaining optimal performance in high-intensity racing environments.

## Dataset Description
The dataset contains approximately 750,000 samples of F1 drivers' calorie detection data. It includes several features related to F1 racers' physical attributes and race conditions:

- **Age**: Racer's age in years
- **Sex**: Gender of the racer (male/female)
- **Height**: Height in centimeters
- **Weight**: Weight in kilograms
- **Duration**: Activity duration in minutes
- **Heart_Rate**: Heart rate during activity in beats per minute
- **Body_Temp**: Body temperature in Celsius
- **Calories**: Target variable - calories burned during activity

## Project Structure

### 1. Exploratory Data Analysis (EDA)
- Checked for missing values in the dataset
- Examined basic statistical information and distributions
- Visualized feature distributions using histograms
- Analyzed sex distribution of racers
- Created correlation matrix to identify relationships between features
- Analyzed feature relationships with calories using scatter plots
- Identified outliers using box plots

### 2. Feature Engineering
- Created Body Mass Index (BMI) from height and weight
- Encoded categorical variables (Sex) to numerical values
- Generated interaction terms:
  - Duration × Heart_Rate
  - Duration × Body_Temp
  - Heart_Rate × Body_Temp
- Added polynomial features for key predictors:
  - Duration_squared
  - BodyTemp_squared
  - HeartRate_squared
- Standardized numerical features using StandardScaler

### 3. Model Development
Multiple regression models were implemented and evaluated:

#### Base Models:
- **Linear Regression**: Simple baseline model
- **LightGBM**: Gradient boosting framework using decision trees
- **XGBoost**: Advanced implementation of gradient boosted decision trees

#### Model Optimization:
- Implemented Bayesian optimization using Optuna for hyperparameter tuning
- Optimized parameters for LightGBM:
  - num_leaves, learning_rate, feature_fraction, bagging_fraction
  - min_child_samples, lambda_l1, lambda_l2, n_estimators
- Optimized parameters for XGBoost:
  - learning_rate, max_depth, min_child_weight, subsample
  - colsample_bytree, gamma, reg_alpha, reg_lambda, n_estimators

### 4. Ensemble Methods
Three ensemble approaches were tested to improve prediction performance:

- **Weighted Ensemble**: Optimized weight allocation between LightGBM and XGBoost
- **Stacking Ensemble**: Used Ridge regression as a meta-model to combine base model predictions
- **Simple Average**: Equal weighting of LightGBM and XGBoost predictions

### 5. Model Evaluation
Models were evaluated using:
- Root Mean Squared Error (RMSE)
- R-squared (R²) coefficient

### 6. Prediction
- Applied the same preprocessing steps to the test dataset
- Used the best ensemble method to generate final predictions
- Ensured no negative calorie predictions by clipping values at 0
- Generated submission file with predicted calorie values

## Technical Implementation
- **Language**: Python
- **Libraries**:
  - pandas & numpy: Data manipulation and numerical operations
  - matplotlib & seaborn: Data visualization
  - scikit-learn: Data preprocessing, model evaluation, and linear models
  - LightGBM & XGBoost: Gradient boosting frameworks
  - Optuna: Hyperparameter optimization

## Results
The project successfully developed models to predict caloric requirements for F1 racers. The ensemble approach improved prediction accuracy compared to individual models, with the best method being determined by lowest RMSE on the validation set.

## Usage
1. Ensure all required libraries are installed
2. Run the notebook cells sequentially to:
   - Load and preprocess the data
   - Train the models
   - Generate predictions for the test set
   - Create a submission file

