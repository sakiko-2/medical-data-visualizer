import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
medical_examination_filepath = './medical_examination.csv'
df = pd.read_csv(medical_examination_filepath, index_col='id')

# Add 'overweight' column
df['bmi'] = df['weight'] / ((df['height'] / 100) * (df['height'] / 100))

df['overweight'] = (df['bmi'] > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.cholesterol = df.cholesterol.map(lambda x: 1 if x > 1 else 0)

df.gluc = df.gluc.map(lambda x: 1 if x > 1 else 0)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    variables = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    
    df_cat = pd.melt(df, id_vars='cardio', value_vars=variables)


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    cardio = df_cat.value_counts(sort=False).reset_index(name='total')
    

    # Draw the catplot with 'sns.catplot()'
    plot = sns.catplot(data=cardio, x='variable', y='total', col='cardio', kind='bar', hue='value')


    # Get the figure for the output
    fig = plot.figure


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
# def draw_heat_map():
#     # Clean the data
#     df_heat = None

#     # Calculate the correlation matrix
#     corr = None

#     # Generate a mask for the upper triangle
#     mask = None



#     # Set up the matplotlib figure
#     fig, ax = None

#     # Draw the heatmap with 'sns.heatmap()'



#     # Do not modify the next two lines
#     fig.savefig('heatmap.png')
#     return fig
