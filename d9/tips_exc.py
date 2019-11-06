import seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


tips = seaborn.load_dataset("tips")
print(tips.head())
# tip/total_bill
tips_ratio = (100 * tips['tip'] / tips['total_bill']).astype(int)
tips['tips_ratio'] = tips_ratio
print(tips['tips_ratio'].mean())
print(tips.dtypes)

# plt.figure(0)
# tips.hist(column="tips_ratio", bins=20)
# plt.figure(1)
# tips.hist(column="tips_ratio", by="sex", bins=20)
# plt.show()

# pokazac wysokosc srednia tipa w zaleznosci od time na wykresie slupkowym
s = pd.Series(pd.Categorical(tips.loc[:, "time"]))
print(s)
tip_time_values = tips.groupby('time').mean()['tip']
tip_time_values.plot(kind='bar')
plt.show()