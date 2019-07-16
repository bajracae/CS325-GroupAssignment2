change_val = 40;

coin_types = [1, 10, 25, 50];
list_len = len(coin_types);

coin_list = [];

i = list_len - 1;
while(i >= 0):
    while(change_val >= coin_types[i]):
        change_val -= coin_types[i];
        coin_list.append(coin_types[i]);
    
    i -= 1  

print("Coins used:");
for i in range(len(coin_list)):
    print(coin_list[i], end = " "); 

print("\n");

print("Number of coins used:", len(coin_list));

