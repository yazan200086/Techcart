
# from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = "all"
# import numpy as np
# import pandas as pd
# import math
# import json
# import time
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.model_selection import train_test_split

# import joblib

# import scipy.sparse
# from scipy.sparse import csr_matrix
# from scipy.sparse.linalg import svds
# import warnings; warnings.simplefilter('ignore')
# from .models import reviews


# df = pd.DataFrame(list(reviews.objects.all().values()))
# df = df.reindex(columns = ['user_id','product_id','rating'])
# df.sort_values(by=["user_id"], inplace = True)




# print(df.head(150))
# """#### Dropping the Unnamed: 0 column"""




# #Check the number of rows and columns
# rows,columns=df.shape
# print('Number of rows: ',rows)
# print('Number of columns: ',columns)

# #Check the datatypes
# df.dtypes

# #Summary statistics of rating variable
# df['rating'].describe().transpose()

# #Find the minimum and maximum ratings
# print('Minimum rating is: %d' %(df.rating.min()))
# print('Maximum rating is: %d' %(df.rating.max()))

# """* Rating are on the scale 1 to 5.

# # Handling Missing values
# """

# #Check for missing values
# print('Number of missing values across columns: \n',df.isnull().sum())

# """* There are no missing records in the dataset.

# ## Ratings

# * We can see that more number of users have given the rating of 5.
# """

# # Number of unique user id  in the data
# print('Number of unique users in Raw data = ', df['user_id'].nunique())
# # Number of unique product id  in the data
# print('Number of unique product in Raw data = ', df['product_id'].nunique())

# """# 3. Taking the subset of dataset to make it less sparse/ denser."""

# #Check the top 10 users based on ratings
# most_rated=df.groupby('user_id').size().sort_values(ascending=False)[:10]
# print('Top 10 users based on ratings: \n',most_rated)

# counts=df['user_id'].value_counts()
# df_final=df[df['user_id'].isin(counts[counts>=1].index)]
# print('Number of users who have rated 1 or more items =', len(counts))
# print('Number of unique users in the final data = ', df_final['user_id'].nunique())
# print('Number of unique products in the final data = ', df_final['product_id'].nunique())
# print(df_final.head())



# #constructing the pivot table
# final_ratings_matrix = df_final.pivot_table(index = 'user_id', columns ='product_id', values = 'rating').fillna(0)
# final_ratings_matrix.head()
# """* It shows that it is a sparse matrix. So, many cells are filled with 0 values."""

# print('Shape of final_ratings_matrix: ', final_ratings_matrix.shape)

# """* We can see that there are 44424 products and 5001 users."""

# given_num_of_ratings = np.count_nonzero(final_ratings_matrix)
# print('given_num_of_ratings = ', given_num_of_ratings)
# possible_num_of_ratings = final_ratings_matrix.shape[0] * final_ratings_matrix.shape[1]
# print('possible_num_of_ratings = ', possible_num_of_ratings)
# density = (given_num_of_ratings/possible_num_of_ratings)
# density *= 100
# print ('density: {:4.2f}%'.format(density))

# """* The density value of the matrix also shows that it is a sparse matrix.



# """## User Based Collaborative Filtering model"""

# # Matrix with row per 'user' and column per 'item' 
# pivot_df = df_final.pivot_table(index = 'user_id', columns ='product_id', values = 'rating').fillna(0)
# #print(pivot_df)
# #print(list(pivot_df.iloc[pivot_df.index==12,:].sort_index(ascending=False)))
# print('Shape of the pivot table: ', pivot_df.shape)

# """* As this is a sparse matrix we will use SVD.

# ### Singular Value Decomposition
# """

# # Singular Value Decomposition
# U, sigma, Vt = svds(pivot_df.to_numpy(), k = 7)

# print('Left singular matrix: \n',U)

# print('Sigma: \n',sigma)

# """* As sigma is not a diagonal matrix we have to convert it into diagonal matrix."""

# # Construct diagonal array in SVD
# sigma = np.diag(sigma)
# print('Diagonal matrix: \n',sigma)

# print('Right singular matrix: \n',Vt)

# #Predicted ratings
# all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) 
# # Convert predicted ratings to dataframe
# preds_df = pd.DataFrame(all_user_predicted_ratings,index= pivot_df.index , columns = pivot_df.columns)
# preds_df.head()
# #x=preds_df.iloc[preds_df.index==1]
# #print(x.iloc[0].sort_values(ascending=False))

# # Recommend the items with the highest predicted ratings

# def recommend_items(user_ID, pivot_df, preds_df):
#     # index starts at 0  
#     u=int(user_ID)
    
    

#     # Get and sort the user's ratings
#     sorted_user_ratings = pivot_df.iloc[pivot_df.index==u]
#     sorted_user_ratings1=sorted_user_ratings.iloc[0].sort_values(ascending=False)
#     sorted_user_predictions = preds_df.iloc[preds_df.index==u]
#     sorted_user_predictions1=sorted_user_predictions.iloc[0].sort_values(ascending=False)
#     #d=pd.DataFrame(sorted_user_predictions1)
#     #sorted_user_predictions
#     temp = pd.concat([sorted_user_ratings1, sorted_user_predictions1], axis=1)
#     temp.index.name = 'Recommended Items'
    
#     temp.columns = ['user_ratings', 'user_predictions']
#     temp = temp.loc[temp.user_ratings == 0]   
#     temp = temp.sort_values('user_predictions', ascending=False)
#     aa=temp.head(5)
#     A=aa.index.tolist()
    
#     return A

# """* Since, it is a Collaborative recommender model, so, all the three users are given different recommendations based on users past behaviour.

# # 6. Evaluation of Collabrative recommendation model
# """

# rmse_df = pd.concat([final_ratings_matrix.mean(), preds_df.mean()], axis=1)
# rmse_df.columns = ['Avg_actual_ratings', 'Avg_predicted_ratings']
# print(rmse_df.shape)
# rmse_df['item_index'] = np.arange(0, rmse_df.shape[0], 1)
# rmse_df.head()

# RMSE = round((((rmse_df.Avg_actual_ratings - rmse_df.Avg_predicted_ratings) ** 2).mean() ** 0.5), 5)

# print(RMSE)