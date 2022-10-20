'''
Name: Tan Yan Qi
Student Admin No: 210288D
Tutorial Group: IT2553-05
'''
import random

class DataRecord():

    def __init__(self, packageName, customerName, pax, costPerPax):
        self._packageName = packageName
        self._customerName = customerName
        self._pax = pax
        self._costPerPax = costPerPax

    def get_packageName(self):
        return self._packageName

    def get_customerName(self):
        return self._customerName

    def get_pax(self):
        return self._pax
    
    def get_costPerPax(self):
        return self._costPerPax

    def packageCost(self):
        return self._costPerPax * self._pax

    def set_packageName(self, packageName):
        self._packageName = packageName

    def set_customerName(self, customerName):
        self._customerName = customerName

    def set_pax(self, pax):
        self._pax = pax

    def set_costPerPax(self, costPerPax):
        self._costPerPax = costPerPax

    def __str__(self):
        return f"{self._packageName:>12} | {self._customerName:>13} | {self._pax:>11} | {self._costPerPax:>12} | {self.packageCost():>12}"

allRecords = []
validChoices = ['1','2','3','4','5','6','7','8','9','10','11','12','13','']

#-----------------BUBBLE-SORT-----------------#
def bubble_sort():
    for j in range(len(allRecords)):
        for i in range(0, len(allRecords)-j-1):
            if allRecords[i].get_customerName() > allRecords[i+1].get_customerName():
                allRecords[i],allRecords[i+1] = allRecords[i+1],allRecords[i]


#----------------SELECTION-SORT---------------#
def smallest_index():
    smallest = allRecords[0]
    index = 0

    for i in range(1, len(allRecords)):
        if smallest.get_packageName() > allRecords[i].get_packageName():
            smallest = allRecords[i]
            index = i

    return index

def selection_sort():
    global allRecords
    sortedRecords = []

    for i in range(len(allRecords)):
        smallestIndex = smallest_index()
        sortedRecords.append(allRecords.pop(smallestIndex))
    allRecords = sortedRecords

#-----------------INSERTION-SORT-----------------#
def insertion_sort():
    for i in range(1, len(allRecords)):
        rightSideValue = allRecords[i].packageCost()

        while (i > 0 and allRecords[i-1].packageCost() > rightSideValue):
            allRecords[i], allRecords[i-1] = allRecords[i-1], allRecords[i]
            i -= 1
    
#-----------------SLOW-SORT-----------------#
def slow_sort(arr, low, high):
    if (low >= high):
        return
         
    mid = (low + high) // 2
     
    slow_sort(arr, low, mid) # split left half
    slow_sort(arr, mid + 1, high) # split right half
 
    if (arr[high].packageCost() < arr[mid].packageCost()): # Swap if the first is lower than second
        arr[mid], arr[high] = arr[high], arr[mid]
 
    slow_sort(arr, low, high - 1) # sort the entire array again except the end of the list

#-----------------COUNTING-SORT-----------------#

def counting_sort():
    global allRecords
    size = len(allRecords)         # getting amount of records
    output = [0] * size            
    counting = [0] * (largest_value(allRecords).get_pax() + 1)          # multiply by 11 cause we start range from 0 to 10

    for record in allRecords:
        counting[record.get_pax()] += 1 # for each number eg. 10, store the count at the index of the list. at counting index 10 add 1

    for i in range(1, 11):
        counting[i] += counting[i-1] # from index 1 to 10 add the total amount of items before index i. not counting from 0 because there is no number before index 0

    for i in range(size):
        position = counting[allRecords[i].get_pax()] # get the no. of pax and put it as index of counting to get the position of the output 
        output[position-1] = allRecords[i]           # then input it as the output index ( minus 1 cause otherwise out of range also cause output contain only 10 items vs counting list which have 11 items) 
        position -= 1

    allRecords = output

#-----------------RADIX-SORT-----------------#

def combine_the_buckets(theBuckets):
    combinedBuckets = []
    for bucket in theBuckets:
        for i in range(len(bucket)):
            combinedBuckets.append(bucket[i])

    return combinedBuckets

def get_num_digits(records):
    largest = 0

    for record in records:
        if largest < record.packageCost():
            largest = record.packageCost()
    return len(str(largest))

#LSD radix sort using bucket sort as subroutine
def radix_sort(records):
    global allRecords
    num_digits = get_num_digits(records)

    for digit in range(0, num_digits):
        buckets = [[] for i in range(10)]
        e = 10 ** digit
        for record in records:
            # num is the bucket number that the item will be put into
            num = (record.packageCost() // e) % 10
            buckets[num].append(record)
        records = combine_the_buckets(buckets)
    allRecords = records

#-----------------PIGEONHOLE-SORT-----------------#
def largest_value(records):
    largest = records[0]

    for record in records:
        if largest.get_pax() < record.get_pax():
            largest = record
    return largest

def smallest_value(records):
    smallest = records[0]

    for record in records:
        if smallest.get_pax() > record.get_pax():
            smallest = record
    return smallest

def pigeonhole_sort(records):
    global allRecords
    recMin = smallest_value(records).get_pax()
    recMax = largest_value(records).get_pax()
    recRange = recMax - recMin + 1

    holes = [[] for i in range(recRange)]

    for i in range(len(records)):
        holes[records[i].get_pax() - recMin].append(records[i])

    i = 0
    for hole in holes:
        for item in hole:
            records[i] = item
            i += 1
    allRecords = records


#-----------------UPDATE-RECORD-----------------#
def update_record(availableIndex):
    while True:
        choice = input('Do you want to update record? (Y/N): ').lower()
        if choice == 'y':

            while True:
                try:
                    indexToUpdate = int(input('Enter the index you want to update: '))
                    if indexToUpdate not in availableIndex:
                        print('Please enter a vaild index!')
                        continue
                    else:
                        break
                except ValueError:
                    print('Please enter a number')

            while True:
                upackageName = input('update package Name: ').lower()
                if upackageName:
                    break
                else:
                    print('Please enter package name')
            
            while True:
                ucustomerName = input('update customer Name: ').lower()
                if ucustomerName:
                    break
                else:
                    print('Please enter package name')

            while True:
                try:
                    upax = int(input('update pax: '))
                    break
                except ValueError:
                    print('Please enter a number')
            
            while True:
                try:
                    ucostPerPax = int(input('update cost per pax: '))
                    break
                except ValueError:
                    print('Please enter a number')

            allRecords[indexToUpdate].set_packageName(upackageName)
            allRecords[indexToUpdate].set_customerName(ucustomerName)
            allRecords[indexToUpdate].set_pax(upax)
            allRecords[indexToUpdate].set_costPerPax(ucostPerPax)

            print(f"Record at index {indexToUpdate} has been updated \n")
            break
        elif choice == 'n':
            break
        else:
            print('Enter a valid choice!')
            continue

#-----------------LINEAR-SEARCH-----------------#

def linear_search():
    customerName = input('Enter customer name: ').lower()
    availableIndex = []
    foundRecord = []

    for record in allRecords:
        if customerName == record.get_customerName().lower():
            foundRecord.append(record)
            availableIndex.append(allRecords.index(record))

    if foundRecord:
        print(f"{'Index':>3} | {'Package Name':>12} | {'Customer Name':>13} | {'No. of Pax':>11} | {'Cost Per Pax':>12} | {'Package Cost':>12}")
        print("===================================================================================")
        for record in foundRecord:
            print(f"  {allRecords.index(record):>3} | {record}")
        update_record(availableIndex)

    else:
        print('Record not found \n')

#-----------------BINARY-SEARCH-----------------#

def binary_search():
    packageName = input('Enter package name: ').lower()
    selection_sort()
    lowest = 0
    highest = len(allRecords) - 1
    availableIndex = []

    while lowest <= highest:
        mid = (lowest + highest) // 2
        midRecord = allRecords[mid]
        if midRecord.get_packageName() == packageName:
            print(f"{'Index':>3} | {'Package Name':>12} | {'Customer Name':>13} | {'No. of Pax':>11} | {'Cost Per Pax':>12} | {'Package Cost':>12}")
            print("===================================================================================")

            # Searching for duplicates----------------------#
            if (allRecords[mid+1].get_packageName() or allRecords[mid-1].get_packageName()) == allRecords[mid].get_packageName():
                firstOccur = mid
                lastOccur = mid
                while allRecords[firstOccur].get_packageName() == midRecord.get_packageName():
                    firstOccur -= 1
                
                while allRecords[lastOccur].get_packageName() == midRecord.get_packageName():
                    lastOccur += 1
                
                for i in range(firstOccur+1, lastOccur):
                    print(f"  {i:>3} | {allRecords[i]}")
                    availableIndex.append(i)

                update_record(availableIndex)
                return
            #------------------------------------------------#
                
            else:
                print(f"  {allRecords.index(midRecord):>3} | {midRecord}")
                availableIndex.append(allRecords.index(midRecord))
                update_record(availableIndex) 
                return
        
        elif midRecord.get_packageName() > packageName:
            highest = mid - 1 
        elif midRecord.get_packageName() < packageName:
            lowest = mid + 1
    
    print('Record not found \n')

#-----------------JUMP-SEARCH-----------------#

def jump_search():

    packageName = input('Enter package name: ').lower()

    insertion_sort()
    recordLength = len(allRecords)
    lowest = 0
    block = int(recordLength ** 1/2)
    availableIndex = []

    while allRecords[(min(block, recordLength)-1)].get_packageName() < packageName:
        lowest = block
        block += block
        if lowest >= len(allRecords):
            print("Record not found \n")
            return

    while allRecords[lowest].get_packageName() < packageName:
        lowest += 1
        if lowest == min(block, recordLength):
            print("Record not found \n")
            return 

    if allRecords[lowest].get_packageName() == packageName:
        print(f"{'Index':>3} | {'Package Name':>12} | {'Customer Name':>13} | {'No. of Pax':>11} | {'Cost Per Pax':>12} | {'Package Cost':>12}")
        print("===================================================================================")

        # Searching for duplicates
        if (allRecords[lowest+1].get_packageName() or allRecords[lowest-1].get_packageName()) == allRecords[lowest].get_packageName():
            firstOccur = lowest
            lastOccur = lowest
            while allRecords[firstOccur].get_packageName() == allRecords[lowest].get_packageName():
                firstOccur -= 1
            while allRecords[lastOccur].get_packageName() == allRecords[lowest].get_packageName():
                lastOccur += 1
            for i in range(firstOccur+1, lastOccur):
                availableIndex.append(i)
                print(f"    {i} | {allRecords[i]}")
            
            update_record(availableIndex)
            return
        else:
            print(f"    {lowest} | {allRecords[lowest]}")
            availableIndex.append(lowest)
            update_record(availableIndex)
            return
        #------------------------------------------------#

    print("Record not found \n")

#-----------------RECORD-RANGE-----------------#

def list_record_range():
    while True:
        try:
            start_range = int(input('Enter $X: '))
            break
        except ValueError:
            print("Please enter number")

    while True:
        try:
            end_range = int(input('Enter $Y: '))
            break
        except ValueError:
            print("Please enter number")

    foundRecord = []
    for record in allRecords:
        if start_range <= record.packageCost() <= end_range:
            foundRecord.append(record)
    
    if foundRecord:
        print(f"{'Index':>3} | {'Package Name':>12} | {'Customer Name':>13} | {'No. of Pax':>11} | {'Cost Per Pax':>12} | {'Package Cost':>12}")
        print("===================================================================================")
        for record in foundRecord:
            print(f"    {allRecords.index(record)} | {record}")
        return
    print(f"No records found ranged between {start_range}-{end_range}")

#-----------------INITIALIZING-LIST-----------------#

def create_list():
    names = ['alice','bob', 'cat', 'david', 'eric', 'fion', 'alice', 'hen', 'iris', 'john']
    packages = ['apack', 'apack', 'apack', 'apack', 'epack', 'fpack', 'gpack', 'hpack', 'ipack', 'jpack']
    for i,name,package in zip(range(1, 11), names, packages):
        record = DataRecord(package, name, i, i*10)
        allRecords.append(record)

    random.shuffle(allRecords)

#-----------------DISPLAY-RECORD-----------------#
def print_record():
    print(f"{'Index':>3} | {'Package Name':>12} | {'Customer Name':>13} | {'No. of Pax':>11} | {'Cost Per Pax':>12} | {'Package Cost':>12}")
    print("===================================================================================")
    for i in range(1, len(allRecords)+1):
        print(f"  {i:>3} | {allRecords[i-1]} ")

#-----------------SHUFFLE-LIST-----------------#
def shuffle_list():
    random.shuffle(allRecords)
    print("Shuffle Done \n")

#-----------------MAIN-MENU-----------------#
def display():
    global allRecords
    print('''\n
            1. Display all records \n
            2. Sort record by Customer Name using Bubble sort \n
            3. Sort record by Package Name using Selection sort \n
            4. Sort record by Package Cost using Insertion sort \n
            5. Search record by Customer Name using Linear Search and update record \n
            6. Search record by Package Name using Binary Search and update record \n
            7. List records range from $X to $Y. e.g $100-200 \n
            8. Shuffle records

            Extra
            9. Search record by Package Name using Jump Search and update record \n
            10. Sort record by Package Cost using Slow sort \n
            11. Sort record by No. of Pax using Counting sort \n
            12. Sort record by Package Cost using Radix sort \n
            13. Sort record by No. of Pax using Pigeonhole Sort \n
            Exit Application (press enter when option is empty) \n
            ''')
    
    user_input = input('Enter option: ')

    if user_input == '1':
        print_record()
        input('Press Enter to return to menu ')
        display()

    if user_input == '2':
        bubble_sort()
        print("Bubble sort is done")
        input('Press Enter to return to menu ')
        display()

    if user_input == '3':
        selection_sort()
        print("Selection sort is done")
        input('Press Enter to return to menu ')
        display()

    if user_input == '4':
        insertion_sort()
        print("Insertion sort is done")
        input('Press Enter to return to menu ')
        display()

    if user_input == '5':
        linear_search()
        input('Press Enter to return to menu ')
        display()

    if user_input == '6':
        binary_search()
        input('Press Enter to return to menu ')
        display()

    if user_input == '7':
        list_record_range()
        input('Press enter to return to menu')
        display()

    if user_input == '8':
        shuffle_list()
        input('Press Enter to return to menu ')
        display()

    if user_input == '9':
        jump_search()
        input('Press Enter to return to menu ')
        display()

    if user_input == '10':
        slow_sort(allRecords, 0, len(allRecords)-1)
        print("Slow sort is done")
        input('Press Enter to return to menu ')
        display()

    if user_input == '11':
        counting_sort()
        print("Counting sort is done")
        input('Press Enter to return to menu ')
        display()

    if user_input == '12':
        radix_sort(allRecords)
        print("Radix sort is done")
        input('Press Enter to return to menu ')
        display()

    if user_input == '13':
        pigeonhole_sort(allRecords)
        print("Pigeonhole sort is done")
        input('Press Enter to return to menu ')
        display()

    if user_input not in validChoices:
        input('Please enter a valid number (press enter to continue) ')
        display()

create_list()
display()