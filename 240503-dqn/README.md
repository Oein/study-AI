# 24년 5월 3일 DQN

[이 글](https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html)을 참조하여 DQN을 배움.

## DQN의 학습 방식

1. agent가 action을 고름
2. action을 수행하여 done, reward와 같은 정보를 받음
3. target 을 계산한다.
4. loss를 최소화 하는 방식으로 업데이트 한다.
