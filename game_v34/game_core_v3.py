import numpy as np

def random_predict(number:int=1) -> int:
    """ Рандомно угадываем число
    
    Args:
        number (int, optional): Загаданное число. Defoults to 1.
        
    Returns:
        int: Число попыток
    """
      
    count = 0 # количество попыток
    low = 1 # задаем диапазон от меньшего к большему
    high = 100
  
    while low <= high: 
        count+=1
        mid = round(low+high)/2 # находим среднее в диапазоне
        if mid == number: # если угадали число завершаем выполнение программы и выводим 'count'
            break
        if mid > number: # если предположение оказывается больше загаданного числа, то предположение становиться вершиной диапазона - 1
            high = mid - 1
        else:            # если предположение меньше загаданного числа, то предположение становиться низом диапазона + 1
            low = mid + 1
    return count
def score_game(random_predict) -> int:
    """Среднее кол-во попыток

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) # фиксируем сид для воспроизводительности
    random_array = np.random.randint(1, 101, size=(100)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))   

    print(f'Алгоритм угадывает число в среднем за:{score} попыток')
    print(count_ls)
    return(score)


if __name__ == '__main__':
    # RUN
    score_game(random_predict)