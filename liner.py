# liner search algorithm
def averages():
    try:
        # soni so`rash`
        n = int(input("Son kiriting: "))
        sum = 0
        count = 0
        for i in range(n):
            num = float(input(f"{i + 1} - sonni kiriting: "))
            sum += num
            count += 1
        if count == 0:
            average = 0
        else:
            average = sum / count

        return average
    except Exception as error:
        print(f"Error!: {error}")


average = averages()
print(f"O`rta arifmetigi {average}")