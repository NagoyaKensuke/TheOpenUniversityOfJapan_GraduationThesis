
import random
import time
import math
import pandas as pd
import matplotlib.pyplot as plt


# 乱数でリストを生成
def generate_random_list(length):
    return [random.randint(1, 10000) for _ in range(length)]


# 線形探索
def linear_search(lst):
    max_value = lst[0]
    for value in lst:
        if value > max_value:
            max_value = value
    return max_value


# 二分探索（ソート済みリストで使用）
def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None


# バブルソート
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst[-1]


# 選択ソート
def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst[-1]


# 挿入ソート
def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst[-1]


# マージソート
def merge_sort(lst):
    if len(lst) <= 1:
        return lst


    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


# マージ
def merge(left, right):
    result = []
    left_index, right_index = 0, 0




    # リスト内の要素を比較してマージ
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1


    # 残りの要素を追加
    result += left[left_index:]
    result += right[right_index:]


    return result
# クイックソート
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = random.choice(lst)
    less_than_pivot = [x for x in lst if x < pivot]
    equal_to_pivot = [x for x in lst if x == pivot]
    greater_than_pivot = [x for x in lst if x > pivot]


    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)
# ヒープソート
def heap_sort(lst):
    import heapq
    heapq.heapify(lst)
    return [heapq.heappop(lst) for _ in range(len(lst))]


# カウントソート
def count_sort(lst):
    max_value = max(lst)
    count = [0] * (max_value + 1)


    for value in lst:
        count[value] += 1


    result = []
    for value, frequency in enumerate(count):
        result += [value] * frequency


    return result


# バケットソート
def bucket_sort(lst):
    num_buckets = round(math.sqrt(len(lst)))
    buckets = [[] for _ in range(num_buckets)]


    # バケットに要素を挿入
    for value in lst:
        index = value * num_buckets // (max(lst) + 1)
        buckets[index].append(value)


    # 各バケットをソート
    for bucket in buckets:
        bucket.sort()


    # バケットをマージ
    result = []
    for bucket in buckets:
        result += bucket


    return result
# リストを生成
lst = generate_random_list(10000)


# 各アルゴリズムの計算量比較のためのリスト
algorithms = [linear_search, binary_search, heap_sort, merge_sort, quick_sort, count_sort, bucket_sort, insertion_sort, selection_sort, bubble_sort]


# 結果を格納するためのリスト
results = []


# 二分探索を使用する前にリストをソート
sorted_lst = sorted(lst.copy())


for algorithm in algorithms:
    if algorithm == binary_search:
        start = time.time()
        max_value = max(sorted_lst)
        end = time.time()
    else:
        start = time.time()
        max_value = algorithm(lst.copy())
        end = time.time()
        if type(max_value) == list:
            max_value = max(max_value)
    results.append({"Algorithm": algorithm.__name__, "Max Value": max_value, "Time (seconds)": end - start})


# 結果をDataFrameに変換し、計算時間でソート
df = pd.DataFrame(results).sort_values("Time (seconds)")


# DataFrameを表示
print(df)


# 計算時間の棒グラフを作成
fig, ax = plt.subplots()
ax.bar(df["Algorithm"], df["Time (seconds)"])
ax.set_xlabel("Algorithm")
ax.set_ylabel("Time (seconds)")
ax.set_title("Algorithm Performance Comparison")
plt.xticks(rotation=45)
plt.show()
