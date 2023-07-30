
# from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = "all"
# import numpy as np
# import pandas as pd

# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import NearestNeighbors
# from .models import reviews
# from scipy.sparse import csr_matrix
# from scipy.sparse.linalg import svds
# import warnings; warnings.simplefilter('ignore')



# df = pd.DataFrame(list(reviews.objects.all().values()))
# df = df.reindex(columns = ['user_id','product_id','rating'])
# df.sort_values(by=["user_id"], inplace = True)


# print(df.shape)

# df.head()



# df.info()

# rows,columns=df.shape


# df.dtypes

# df['rating'].describe().transpose()



# most_rated=df.groupby('user_id').size().sort_values(ascending=False)[:10]

# counts=df['user_id'].value_counts()
# df_final=df[df['user_id'].isin(counts[counts>=1].index)]


# final_ratings_matrix = df_final.pivot_table(index = 'user_id', columns ='product_id', values = 'rating').fillna(0)
# final_ratings_matrix.head()


# given_num_of_ratings = np.count_nonzero(final_ratings_matrix)
# print('given_num_of_ratings = ', given_num_of_ratings)
# possible_num_of_ratings = final_ratings_matrix.shape[0] * final_ratings_matrix.shape[1]
# print('possible_num_of_ratings = ', possible_num_of_ratings)
# density = (given_num_of_ratings/possible_num_of_ratings)
# density *= 100

# train_data, test_data = train_test_split(df_final, test_size = 0.3, random_state=0)
# train_data.head()


# train_data_grouped = train_data.groupby('product_id').agg(votes=('user_id', 'count'),rev=('rating','mean')).reset_index()
# train_data_grouped.head(40)
# v=train_data_grouped['votes'] 
# R=train_data_grouped['rev'] 
# C=train_data_grouped['rev'].mean()
# m=train_data_grouped['votes'].quantile(0.70)
# train_data_grouped['weighted_average']=((R*v)+ (C*m))/(v+m)
# train_data.rename(columns = {'weighted_average': 'score'},inplace=True)
# train_data_grouped.head(40)

# train_data_sort = train_data_grouped.sort_values(['weighted_average', 'product_id'], ascending = [0,1]) 
      
# train_data_sort['rank'] = train_data_sort['weighted_average'].rank(ascending=0, method='first') 
          
# popularity_recommendations = train_data_sort.head(5) 
# popularity_recommendations

# def recommend_pop(user_id):     
#     user_recommendations = popularity_recommendations 
          
#     user_recommendations['user_id'] = user_id 
      
#     cols = user_recommendations.columns.tolist() 
#     cols = cols[-1:] + cols[:-1] 
#     user_recommendations = user_recommendations[cols] 
          
#     return user_recommendations


