'''''

Using the same vaccinations dataset, which includes the number of times people got the flu vaccine.

The dataset contains the following numbers:

never: 5

once: 8

twice: 4

3 times: 3



Calculate and output the variance.

We will soon learn about easier ways to calculate the variance and other summary statistics using Python. 
For now, use  Python code to calculate the result using the corresponding equation.
'''''


vac_nums = [0,0,0,0,0,

            1,1,1,1,1,1,1,1,

            2,2,2,2,

            3,3,3

            ]

#your code goes here

mean = sum(vac_nums)/len(vac_nums);

count=0;

for i in range(len(vac_nums)):

   variance = (vac_nums[i]-mean)**2;

   count += variance;

   

print (count/len(vac_nums));

