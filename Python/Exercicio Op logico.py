trabalho_terça = True
trabalho_quinta = False
sorvete = trabalho_quinta or trabalho_terça

tv_50 = trabalho_terça and trabalho_quinta
tv_32 = trabalho_terça != trabalho_quinta
mais_saudavel = not sorvete

print ("Tv50={} Tv32={} Sorvete={} Saudavel ={}" 
.format (tv_50, tv_32, sorvete, mais_saudavel))