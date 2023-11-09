import requests
import time
import csv
import pygame

#metodo per lanciare un segnale sonoro alla fine dell'esecuzione dello script (da rimuovere)
pygame.init()
sound_file = '/home/meeco/Downloads/Korok Find.mp3'

#setup url e query
prometheus_api_url = "http://172.16.2.18:32381/api/v1/query"
memory_query = 'node_memory_Active_bytes * on(instance) group_left(nodename) (node_uname_info)'
cpu_query = 'avg by (instance) (irate(node_cpu_seconds_total{mode!="idle"}[5m]))'

#raccolta dati e generazione csv
with open('risultatiHeavystressapp0%.csv', mode='a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    if csv_file.tell() == 0:
        header = ['Misurazioni']
        for i in range(1, 8):
            header.append(f'Nodo{i} CPU')
            header.append(f'Nodo{i} Memory')
        csv_writer.writerow(header)

    for _ in range(10):
        
        #----RACCOLTA DATI CPU----#        

        cpu_params = {'query': cpu_query}
        cpu_response = requests.get(prometheus_api_url, params=cpu_params)
        cpu_data = cpu_response.json()
        cpu_metrics = []

        for cpu_item in cpu_data["data"]["result"]:
            cpu_metrics.append(cpu_item["value"][1])
            
        #----RACCOLTA DATI MEMORIA----#

        memory_params = {'query': memory_query}
        memory_response = requests.get(prometheus_api_url, params=memory_params)
        memory_data = memory_response.json()
        memory_metrics = []
        
        for memory_item in memory_data["data"]["result"]:
            memory_metrics.append(memory_item["value"][1])
            
        #----INSERIMENTO DATI NEL CSV----#

        row = [_ + 1]
        for i in range(7):
            row.extend([cpu_metrics[i], memory_metrics[i]])
        csv_writer.writerow(row)
        
        #----INTERVALLO DI 30 SECONDI----#
        
        time.sleep(30)

#metodo per lanciare un segnale sonoro alla fine dell'esecuzione dello script (da rimuovere)
pygame.mixer.music.load(sound_file)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(4)

pygame.quit()