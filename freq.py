freq = pd.DataFrame(results)[0].value_counts()
sort_freq = freq.sort_index() 
sort_freq.plot(kind='bar', color='blue', figsize=(15, 8))
mean = pd.Series(X_distri.index * X_distri['Prob']).sum()
var = pd.Series(((X_distri.index - mean)**2)*X_distri['Prob']).sum()

results.mean(), results.var()


sort_index()
kind=‘bar’, color
