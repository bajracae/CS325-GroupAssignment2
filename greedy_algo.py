change_val = 1.25;

coin_types = [.01, .05, .10, .25];
list_len = len(coin_types);

coin_list = [];

i = list_len - 1;
while(i >= 0):
    while(change_val >= coin_types[i]):
        change_val -= coin_types[i];
        coin_list.append(coin_types[i]);
    
    i -= 1

for i in range(len(coin_list)):
    print(coin_list[i], end = " ");

