# reg_resid_plot.py
import matplotlib.pyplot as plt
import seaborn as sns
import itertools

def reg_resid_plots(data):
    """
    Plot regression and residual plots for all combinations of columns in data.
    
    Parameters:
    data: DataFrame with columns to plot
    """
    # Get all combinations of columns (pairs)
    num_cols = data.shape[1]
    col_pairs = list(itertools.combinations(data.columns, 2))
    
    # Calculate number of rows needed for subplots (2 plots per pair)
    n_rows = len(col_pairs)
    
    # Create subplots
    fig, axes = plt.subplots(n_rows, 2, figsize=(12, 4 * n_rows))
    
    # Handle case when there's only one row
    if n_rows == 1:
        axes = axes.reshape(1, -1)
    
    # Create regression and residual plots for each pair
    for i, (x_col, y_col) in enumerate(col_pairs):
        # Regression plot
        sns.regplot(x=x_col, y=y_col, data=data, ax=axes[i, 0])
        axes[i, 0].set_title(f'Regression: {y_col} vs {x_col}')
        
        # Residual plot
        sns.residplot(x=x_col, y=y_col, data=data, ax=axes[i, 1])
        axes[i, 1].set_title(f'Residuals: {y_col} vs {x_col}')
    
    plt.tight_layout()
    plt.show()