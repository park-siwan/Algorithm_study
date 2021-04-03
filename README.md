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

## **Divide and Conquer(분할정복)**

Divide and Conquer란 큰 문제를 작게 나누어 해결하는 방식이다.

분할 정복은 다음과 같은 절차를 거친다.

1. ***Divide***
   - 2개 이상의 작은 문제로 쪼갠다.
2. ***Conquer***
   - 나눠진 작은 문제를 푼다.
3. ***Combine***
   - 나눠 해결한 문제를 합친다.