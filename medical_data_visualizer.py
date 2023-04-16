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
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))].reset_index()
    df_heat = df_heat.drop('bmi', axis=1)

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with 'sns.heatmap()'
    cmap = sns.color_palette('blend:#4167c7,#38365f,#000000,#000000,#000000,#48242c,#6a2b3a,#a83044,#bb363f,#cc4139,#da5334,#f49d63,#ffd4ac', n_colors=12)
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', linewidth='.5', ax=ax, vmin=-0.15, vmax=0.3, cbar_kws={"shrink": 0.5, "format": "%0.2f", "ticks": [-0.08, 0.00, 0.08, 0.16, 0.24]}, cmap=cmap)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
