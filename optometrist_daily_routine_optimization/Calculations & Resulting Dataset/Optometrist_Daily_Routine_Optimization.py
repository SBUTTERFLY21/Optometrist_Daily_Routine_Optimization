#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
df = pd.read_excel("C:\\Users\\d.carabadjac\\Desktop\\optometrist_daily_routine_optimization\\Initial Dataset\\initial data.xlsx")
def separate_columns_to_lists(df):
    # Create a dictionary to store each column as a separate list
    column_lists = {}
    for column_name in df.columns:
        column_lists[column_name] = df[column_name].tolist()
    return column_lists
columns_lists1 = separate_columns_to_lists(df)
print(columns_lists1)


# In[13]:


import pandas as pd
df2 = pd.read_excel("C:\\Users\\d.carabadjac\\Desktop\\optometrist_daily_routine_optimization\\Initial Dataset\\initial data.xlsx",sheet_name=1)
separate_columns_to_lists(df2)
columns_lists2 = separate_columns_to_lists(df2)
print(columns_lists2)


# In[27]:


# 1)
hours_per_year = columns_lists2['Work days per year'][0] * columns_lists2['Patients per day'][0]

# 2)
average_contlens_patients = sum(columns_lists1['ContLens patients']) / len(columns_lists1['ContLens patients'])

# 3)
optional_diagnostics_for_cont_lens_percent = average_contlens_patients * 100 / 40

# 4)
without_diagnostics_for_cont_lens_percent = 100 - optional_diagnostics_for_cont_lens_percent

# 5)
average_work_days = sum(columns_lists1['Work Days']) / len(columns_lists1['Work Days'])

# 6)
result6 = columns_lists2['Optometrist Salary(USD)'][0] / average_work_days / columns_lists2['Patients per day'][0] / 60 * 15 * hours_per_year

# 7)
result7 = columns_lists2['Optometrist Salary(USD)'][0] / average_work_days / columns_lists2['Patients per day'][0] / 60 * 5* hours_per_year

# 8)
сost_of_waiting_time1 = result6 * without_diagnostics_for_cont_lens_percent / 100

# 9)
сost_of_waiting_time2 = result7 * optional_diagnostics_for_cont_lens_percent / 100

# 10)
money_company_loses_per_optom_per_year = сost_of_waiting_time1 + сost_of_waiting_time2

#11)
money_company_loses_totally_per_year = money_company_loses_per_optom_per_year * columns_lists2['Number of optometrists'][0]

# 12)
money_save_per_optom = money_company_loses_per_optom_per_year - result7

# 13)
money_earn_per_optom = columns_lists2['Cost per diagnostic(USD)'][0] * columns_lists2['Work days per year'][0]

# 14)
money_save_totally = money_save_per_optom * columns_lists2['Number of optometrists'][0]

# 15)
money_earn_totally = money_earn_per_optom * columns_lists2['Number of optometrists'][0]

# Print the results
print("1) Working hours per year = number of patients = number of executions of one action during the diagnosis:", hours_per_year)
print("2) Average value of 'ContLens patients':", average_contlens_patients)
print("3) % of those willing to undergo optional diagnostics for prescribing contact lenses:", optional_diagnostics_for_cont_lens_percent)
print("4) % of those willing to undergo vision diagnostics without optional diagnostics for contact lenses:", without_diagnostics_for_cont_lens_percent)
print("5) Average value of working days per month:", average_work_days)
print("6) Result6(see UML-diagram 'Daily activity of an Optometrist' function'Average time until the next patient'):", result6)
print("7) Result7(see UML-diagram 'Daily activity of an Optometrist' function'Average time until the next patient'):", result7)
print("8) The сost of average patient waiting time in case of vision diagnostics without optional diagnostics for contact lenses in a non-optimized daily routine:", сost_of_waiting_time1)
print("9) The сost of average patient waiting time in case of optional diagnostics for prescribing contact lenses in a non-optimized daily routine:", сost_of_waiting_time2)
print("10) The amount of money a company loses per optometrist per year:", money_company_loses_per_optom_per_year)
print("11) The amount of money a company loses totally per year:", money_company_loses_totally_per_year)
print("12) My optimization will allow company to save per optometrist:", money_save_per_optom)
print("13) My optimization will allow company to earn per optometrist:", money_earn_per_optom)
print("14) My optimization will allow company to save totally:", money_save_totally)
print("15) My optimization will allow company to earn totally:", money_earn_totally)
results_dict = {
    'optional_diagnostics_for_cont_lens_percent' : optional_diagnostics_for_cont_lens_percent,
    'without_diagnostics_for_cont_lens_percent' : without_diagnostics_for_cont_lens_percent,
    'money_company_loses_per_optom_per_year' : money_company_loses_per_optom_per_year,
    "money_company_loses_totally_per_year:" : money_company_loses_totally_per_year,
    'money_save_per_optom' : money_save_per_optom,
    'money_earn_per_optom' : money_earn_per_optom,
    'money_save_totally' : money_save_totally,
    'money_earn_totally' : money_earn_totally
}
import json
# Save the results in a JSON file
with open('results.json', 'w') as json_file:
    json.dump(results_dict, json_file, indent=4)


# In[19]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[20]:


# Visualize result3 and result4 data
result_3_4_data = {'Results': ['Result 3', 'Result 4'], 'Values': [optional_diagnostics_for_cont_lens_percent, without_diagnostics_for_cont_lens_percent]}
sns.barplot(x='Results', y='Values', data=result_3_4_data)
plt.title('optional_diagnostics_for_cont_lens_percent and without_diagnostics_for_cont_lens_percent Data')
plt.show()

# Visualize result11 and result12 data
result_11_12_data = {'Results': ['Result 11', 'Result 12'], 'Values': [money_save_per_optom, money_earn_per_optom]}
sns.barplot(x='Results', y='Values', data=result_11_12_data)
plt.title('money_save_per_optom and money_earn_per_optom Data')
plt.show()

# Compare minus(result 10) and result 13 and result 14
comparison_data = {'Results': ['Minus(Result 10)', 'Result 13', 'Result 14'], 'Values': [-money_company_loses_per_optom_per_year, money_save_totally, money_earn_totally]}
sns.barplot(x='Results', y='Values', data=comparison_data)
plt.title('Comparison: Minus(money_company_loses_per_optom_per_year),  money_save_totally and money_earn_totally')
plt.show()


# In[ ]:




