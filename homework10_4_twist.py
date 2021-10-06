voting = 0
while voting < 4:
    total_number_of_countries = 170
    num_of_countries = 0
    count_pro = 0
    count_con = 0
    count_abst = 0
    while num_of_countries < total_number_of_countries:
        vote = int(input('Input your vote'))  # ( 1 / 2 / 3 / 4 )
        if vote == 1:
            count_pro += 1
        if vote == 2:
            count_con += 1
        if vote == 3:
            count_abst += 1
        if vote == 4:
            print('Country number ' + str(num_of_countries + 1) + ' voted vetto.')
            break
        num_of_countries += 1

    if num_of_countries == total_number_of_countries:
        print('Pro votes = ' + str(pro_count))
        print('Con votes = ' + str(con_count))
        print('Abstention votes = ' + str(abst_count))
    voting += 1

