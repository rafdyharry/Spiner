def counterclockwise(yourlist):     #membuat fungsi 
    datamutar=[[],[],[]]            #membuat list kosong untuk mengisi list yang sudah di putar
    for i in range (len(yourlist)):     #membuat pengulangan untuk list pada i dengan range sebanyak jumlah list pada fungsi
        for j in range(len(yourlist)):  #membuat pengulangan untuk list pada j dengan range sebanyak jumlah list pada fungsi
            datamutar[i].append(yourlist[(len(yourlist)-3)-j][i]) #menambahkan list pada list kosong untuk pemutaran list
                           
    return datamutar[::-1]      #mereturn list dan memutarkan list

    
data=[[1,2,3],[4,5,6],[7,8,9]] #nilai list yang akan di putar
print(counterclockwise(data))