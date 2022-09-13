from math import ceil
import datetime as dt

def calc_time_by_car(records):
    record_by_car = {}
    time_by_car = {}
    
    for record in records:
        time, car, kind = record.split(' ')
        time = change_time_format(time=time)
        if car in record_by_car:
            duration = (time - record_by_car[car]) / dt.timedelta(minutes=1)
            del record_by_car[car]
            if car in time_by_car:
                time_by_car[car] += duration
            else:
                time_by_car[car] = duration
        else:
            record_by_car[car] = time
    
    last_time = dt.timedelta(hours=23, minutes=59)
    for car, time in record_by_car.items():
        duration = (last_time - time) / dt.timedelta(minutes=1)
        if car in time_by_car:
            time_by_car[car] += duration
        else:
            time_by_car[car] = duration
    
    return time_by_car

def calc_fee(fees, time_by_car):
    fee_by_car = []
    for car, time in time_by_car.items():
        time = max(0, time - fees[0])
        fee = fees[1]
        
        if time > 0:
            fee += ceil(time / fees[2]) * fees[3]
        
        fee_by_car.append([car, fee])
    
    return fee_by_car

def change_time_format(time):
    hours, minutes = time.split(':')
    time = dt.timedelta(hours=int(hours), minutes=int(minutes))
    
    return time

def solution(fees, records):
    time_by_car = calc_time_by_car(records)
    
    fee_by_car = calc_fee(fees, time_by_car)
    fee_by_car = sorted(fee_by_car, key=lambda x: x[0])
    
    answer = [fee for car, fee in fee_by_car]
    
    return answer