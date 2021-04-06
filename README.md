# **알고리즘 개념과 알고리즘을 알아야 하는 이유**

## 알고리즘이란?

알고리즘은 어떤 문제를 해결하기 위한 자세한 방법이다.

목적은 같은데 방법이 다르듯이 같은 문제를 해결하기 위해서 다양한 알고리즘이 존재한다.

좋은 알고리즘은 문제를 더 잘 해결하는 것이다.

### 알고리즘의 중요성

예전에는 서비스를 만드는 것 자체만으로도 의미가 있었는데, 이제는 소프트웨어 개발에 대한 진입 장벽이 많이 낮아졌다. 때문에 차별성이 필요하다.

### 알고리즘은 개발자의 기본 소양이다

성공해있는 유능한 개발자는 알고리즘적 사고력을 갖추고 있다. 알고리즘에 대한 지식 없이는 원활한 소통이 어렵다.

### 알고리즘은 개발자의 실력

알고리즘을 모르면 사이트가 심각할 정도로 느려진다. 효율성에 대해 신경써야 한다. 모든 프로그램에 알고리즘이 포함되어 있다. 알고리즘을 알아야 더 좋은 코드를 작성할 수 있다. 개발자로써 성장하려면 알고리즘 공부를 필수로 해야 한다.

### 회사는 알고리즘을 잘하는 개발자를 선호한다.

실무적인 경험이 부족하더라도 알고리즘적 사고력이 검증된 지원자라면, 나머지는 충분히 가르칠 수 있다고 생각한다. 반대로 알고리즘을 잘 모르는 개발자라면 좋은 대우를 받기 어렵다. 취업을 생각해도 알고리즘은 의미있는 투자이다.

<br>

# **알고리즘 평가법**

## **1. 평가의 두 기준: 시간과 공간**

좋은 코드의 첫 번째 기준은 시간이다. 빨리 실행되야 한다.

두 번째는 공간이다. 공간은 컴퓨터의 저장 공간을 뜻한다. 메모리르 최대한 적게 사용해야 좋은 프로그램이다.

결국 시간과 메모리 둘다 신경 써야 하는데 그래도 둘 중 좀 더 중요한 하나를 고르자면 시간이다. 용량은 돈 주고 늘릴 수 있지만 시간을 살 순 없다.

<br>

## **2. 시간 복잡도**

프로그램은 다양한 외부 환경에 영향을 받기 때문에 단순작동 시간으로 알고리즘을 비교하기 힘들다. 그래서 컴퓨터 과학에서는 시간 복잡도(Time Complexity)라는 개념을 사용한다.

시간 복잡도는 데이터가 많아질 수록 걸리는 시간이 얼마나 급격히 증가하는 지를 나타내는 개념이다.

시간 복잡도를 더 쉽고 직관적으로 비교하기 위해서는 수학적인 개념이 들어간다.

<br>

## **3. 거듭제곱과 로그**

### 거듭제곱(Exponentiation)

**거꾸로 생각해보기**

2의 3제곱은 8이다.

2의 2제곱은 거꾸로 보면 2<sup>3</sup> / 2 이다. 따라서 8 / 2의 결과값인 4이다.

2의 1제곱은 2<sup>2</sup> / 2 이니 4 / 2 의 결과값인 2이다.

2의 0제곱은 2<sup>1</sup> / 2 이니 2 / 2 의 1이다.

2의 -1제곱은 2<sup>0</sup> / 2 이니 1 / 2 이다.

### 로그(Logarithms)

로그는 거듭제곱의 반대 개념

log<sub>a</sub> b = x → a<sup>x</sup> = b

log<sub>2</sub> 8 = 3 →  2<sup>3</sup>

log<sub>3</sub> 27 = 3 → 3<sup>3</sup> = 27

로그는 결국 이것이다.

'b를 a로 몇 번 나누어야 1이 되는가?

컴픁커 알고리즘 문제를 풀 때는 a가 2인 경우가 많다.

이렇게 생각하면 된다.

b를 몇 번 반 토막 내야 1이 나오는가?

로그의 밑수가 2인 경우에는 lg라고 쓰기도 한다.

log<sub>2</sub> 16이랑 lg16이랑 같은 것이다.

<br>

# **시간 복잡도**
알고리즘에 대해 의논을 하게 되면 "시간 복잡도" 이야기가 나온다. 시간 복잡도는 이중 하나이다.
- *O(1)*
- *O(lg n)*
- *O(n)*
- *O(n lg n)*
- *O(n<sup>2</sup>)*
- *O(n<sup>3</sup>)*
- *O(n<sup>4</sup>)*
- *O(2<sup>n</sup>)*
- *O(n<sup>!</sup>)*
  
<br>

**이 중 자주 사용되는건 6가지 이다.**

- *O(1)* : 인풋의 크기가 소요 시간에 영향이 없다.
- *O(lg n)* : 두 배씩 증가한다.
- *O(n)* : 반복문이 있고 반복되는 횟수가 인풋의 크기와 비례하다.
- *O(n lg n)* : O(n)과 O(lg n)이 겹쳐진 것으로 for 안의 while, while 안의 for문에 해당
- *O(n<sup>2</sup>)* : 크기에 비례하는 반복문이 두번 중첩된 경우
- *O(n<sup>3</sup>)* : 크기에 비례하는 반복문이 세번 중첩된 경우

<br>


# **알고리즘 평균의 경우(Average Case)**
리스트의 길이를 n이라고 가정한다.

<br>

<center>

## **List Operations**

</center>

<br>

<center>

|  Operation |  Code |  Average Case |
|:--------:|:--------:|:--------:|
|인덱싱 | <code>my_list[index]</code> |*O(1)* |
|정렬 | <code>my_list.sort()<br>sorted(my_list)</code> |*O(n log n)* |
|뒤집기 | <code>my_list.reverse()</code> |*O(n)* |
|탐색 | <code>element in my_list</code> |*O(n)* |
|끝에 요소 추가 | <code>my_list.append(element)</code> |*O(n)* |
|중간에 요소 추가 | <code>my_list.insert(index, element)</code> |*O(n)* |
|삭제 | <code>del my_list[index]</code> |*O(n)* |
|최솟값, 최댓값 찾기 | <code>min(my_list)<br>max(my_list)</code> |*O(n)* |
|길이 구하기 | <code>len(my_list)</code> |*O(1)* |
|슬라이싱 | <code>my_list[a:b]</code> |*O(b-a)* |

</center>

<br>


<center>

## **Dictionary Operations**

</center>

<br>

<center>

|  Operation |  Code |  Average Case |
|:--------:|:--------:|:--------:|
|값 찾기 | <code>my_dict[key]</code> |*O(1)* |
|값 넣어주기/덮어쓰기 | <code>my_dict[key] = value<br></code> |*O(1)* |
|값 삭제 | <code>del my_list[key]</code> |*O(1)* |

</center>

<br>

# **알고리즘 패러다임**

## **Brute Force**
효율적인 알고리즘을 찾는 과정에 있어서 출발점은 항상 Brute Force이다. Brute Force에서 발전하는 것이니 이해할 필요가 있다.

장점
- 코드 구현이 쉽다.
- 직관적이고 명확하다
- 인풋이 크지 않을 때 유용하다.

단점
- 인풋이 크면 오래 걸린다.
- 결국 효율적인 알고리즘을 찾아야한다.
  
</br>

Brute Force는 아래 코드처럼 선형 구조를 전체적으로 탐색한다.

```python
def max_product(left_number, right_number):
    max_product = -1
    
    for left in left_number:
        for right in right_number:
            max_product = max(max_product, left * right)

    return max_product
    
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))
```

  

1. ***Divide***
   - 2개 이상의 작은 문제로 쪼갠다.
2. ***Conquer***
   - 나눠진 작은 문제를 푼다.
3. ***Combine***
   - 나눠 해결한 문제를 합친다.

아래 코드는 분할정복의 예시이다.

**1부터 n까지의 합**

```python
def consecutive_sum(start, end):
    if start == end:
        return start
    
    mid = (start + end) // 2
    return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)

# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))


```
### **퀵정렬(Quick sort)**

```python
# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

    
# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    i = start
    b = start
    p = end
    
    while i < p:
        if my_list[i] <= my_list[p]:
            swap_elements(my_list, i, b)
            b += 1
        i += 1
    swap_elements(my_list, b, p)
    p = b
    return p

    
# 퀵 정렬
def quicksort(my_list, start = 0, end = None):
    if end == None:
        end = len(my_list) - 1
    
    # base case
    if end - start < 1:
        return

    pivot = partition(my_list, start, end)
    quicksort(my_list, start, pivot - 1)
    quicksort(my_list, pivot + 1, end)
        

# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3)
print(list3)
```
<br>

## **Dynamic Programming(동적 프로그래밍)**

Dynamic Programming 중복되는 부분문제를 해결하는 방법이다. 즉, 한번 계산한 결과를 재활용해서 효율적인 알고리즘을 만든다.

<br>

### **네가지 개념**

1. ***최적 부분 구조(Optimal Substructure)***
   - 문제를 발견하면 부분 문제들의 최적의 답을 이용해서 기존 문제의 최적의 답을 구할 수 있는지 확인해보자.

<br>

2. ***중복되는 부분 문제(Overlapping Subproblems)***
   - 최적 부분 구조가 발견되면 중복되는 계산을 찾아서 대비해야 한다. 계산 결과를 재활용 하기위한 2가지 방법으로 Memoization과 Tabulation이 있다.

<br>

3. ***Memoization***
   - 캐시를 딕셔너리<code>{}</code>에 보관한다.
   - 재귀함수를 사용한다. (스택 과부화 리스크 존재)
   - 위에서 아래로 가는 사고방식(Top-down Approach)
   - 모든 문제를 해결하지 않아도 될 떄 효율적


<br>

4. ***Tabulation***
   - 캐시를 리스트<code>[]</code>에 보관 혹은 공간 최적화 후 swap
   - 반복문 for 등을 사용
   - 상향식 접근(Bottom-up Approach)
   - 모든 문제를 해결해야 할 때 효율적

<br>

### **TIP**

Dynamic Programming은 모든 값을 저장할 필요가 없는 경우 공간 최적화를 고려해야 한다. 즉, 공간 복잡도를 $O(1)$ 로 효율적인 구성을 하자. 예를들어 사용하는 메모리를 고정하기 위해 배열에 <code>.append</code>나 재귀를 쓰지말고 변수 초기화 후 값연산, 혹은 값대입후 swap을 해주면된다.

<br>

### **Dynamic Programming(동적 프로그래밍) 예제코드 : 피보나치 수열 공간 최적화**
```python
def fib_optimized(n):
    current = 1
    previous = 0

    for i in range(1, n)
        current, previous = current + previous, current

    return current

# 테스트
print(fib_optimized(16))  # 987

#  시간 복잡도 : O(n)
#  공간 복잡도 : O(1)
```
