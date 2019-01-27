# --------------
import yaml

# Read the data of the format .yaml type
with open(path) as f:
     data =yaml.load(f)
# Find data type of the file
type_of_data =type(data)
print("Data type you working with is",type_of_data)

# In which city, and at which venue the match was played and where was it played ?
city= data['info']['city']
print("where the match was played is : " + city)
venue =data['info']['venue']
print("venue where it was played is "+ venue)

# Which are all the teams that played in the tournament ? How many teams participated in total?
teams= data['info']['teams']
print(type(teams))
print("team that are participated  are: "+ teams[0] + " and " + teams[1] )
print(str(len(teams)),'team particpated in the tournmment')

# Which team won the toss and what was the decision of toss winner ?
toss_winner = data['info']['toss']['winner']
toss_decision =data['info']['toss']['decision']
print('the team that won the toss',toss_winner,'and they choose to',toss_decision)

# Find the first bowler and first batsman who played the first ball of the first inning
first_bowler =data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler']
first_batsman =data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']

print("First bowler who deliverd the frist ball of the first innings is :",first_bowler)
print("First batsman who batted the frist ball of the first innings is :",first_batsman)

# How many deliveries were delivered in first inning ?
deliveries_first_innings =len(data['innings'][0]['1st innings']['deliveries'])
print('Number of  delieveries in the first inning is :',deliveries_first_innings)


# How many deliveries were delivered in second inning ?
deliveries_first_innings =len(data['innings'][0]['1st innings']['deliveries'])
print('Number of  delieveries in the first inning is :',deliveries_first_innings)

# Which team won and how ?
winner =data ['info']['outcome']['winner']
winning_runs = data ['info']['outcome']['by']['runs']
print('the team that won ',winner,'by the runs',winning_runs)





