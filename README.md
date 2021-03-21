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
|:--------|:--------:|--------:|
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
|:--------|:--------:|--------:|
|값 찾기 | <code>my_dict[key]</code> |*O(1)* |
|값 넣어주기/덮어쓰기 | <code>my_dict[key] = value<br></code> |*O(1)* |
|값 삭제 | <code>del my_list[key]</code> |*O(1)* |

</center>
