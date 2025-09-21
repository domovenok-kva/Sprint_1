time_list = '1h 45m,360s,25m,30m 120s,2h 60s' # Исходные данные (всего 289 минут, столько же должно быть на выходе)
time_list_splt = time_list.split(',') 
summ_minutes = 0 
hours = 0
minutes = 0
seconds = 0

#Цикл подсчёта общего количества минут     
for time in time_list_splt:

   time = time.replace(' ', '') 

   if 'h' in time:
    hours, time = time.split('h')
    summ_minutes += int(hours) * 60

   if 'm' in time:
    minutes, time = time.split('m')
    summ_minutes += int(minutes)

   if 's' in time: 
    seconds,  time = time.split('s')
    summ_minutes += int(seconds) // 60
       

print(f"Общее количество минут: {summ_minutes}")  