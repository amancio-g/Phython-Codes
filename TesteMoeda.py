import random


num_lancamentos = 5200

face_desejada = 0 

num_faces_desejadas = 0 
for i in range(num_lancamentos):
    if random.randint(0, 1) == face_desejada:   
        num_faces_desejadas +=1




probabilidade = num_faces_desejadas / num_lancamentos 



print("A probabilidade da moeda cair com a face desejada é de:", probabilidade)
        