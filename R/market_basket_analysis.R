blackFriday<-read.csv('blackfriday.csv', stringsAsFactors = T)

str(blackFriday)
#str로 대략적인 데이터 구조를 파악한다

summary(blackFriday)
#summary로 많은 정보를 확인 가능하다
#많이 팔린 productid들, 남녀 성비, age그룹별 수, 
#도시별 인원수, purchase boxplot값 등

#purchase를 구간화한 열 만들어줌
boxplot(blackFriday$Purchase)$stats
#min    12
#1st Qu. 5823
#median  8047
#3rd Qu. 12054
#Max. 21399
#구간화 위해 값 확인
blackFriday$Purchase2<- cut(blackFriday$Purchase, breaks=c(0,4000,8000,12000,16000,20000,24000))
table(blackFriday$Purchase2)


library(ggplot2)

plot(blackFriday$Gender)
plot(blackFriday$Age)
#plot함수로 간단히 성비, 나이대별 인원 확인
#ggplot으로 표현하면 보다 정돈된 그래프로 확인 가능 
ggplot(data=blackFriday, aes(x=Gender))+geom_bar()
ggplot(data=blackFriday, aes(x=Age))+geom_bar()

pie(prop.table(table(blackFriday$Age)),
    labels=paste(levels(blackFriday$Age)
      ,round(prop.table(table(blackFriday$Age)),3)*100, '%'))
#나이대가 26-35세의 비중이 가장 높음을 파이 차트로 쉽게 확인 가능

ggplot(data=blackFriday, aes(x=Age, fill=Gender))+geom_bar()
#특히 25-36세 남성의 구매 데이터가 가장 많았음
#여성의 경우도 해당 나이대의 구매수가 가장 많았음

#해당 나이대의 고객이 구매력도 갖췄는지 알아보고자 함
ggplot(data=blackFriday, aes(x=Age, fill=Purchase2))+geom_bar()
#bar의 크기로 보아 구매력도 충분한듯

ggplot(data=blackFriday, aes(x=Purchase2, fill=Age))
+geom_bar(position='dodge')
ggplot(data=blackFriday, aes(x=Purchase2, fill=Age))
+geom_bar(position='fill')


ggplot(data=blackFriday, aes(x=City_Category,fill=Purchase2 ))+geom_bar()
ggplot(data=blackFriday, aes(x=Age, fill=City_Category))+geom_bar()



library(dplyr)
#충성고객(단골고객)이 가장 많이 구매하는 물품 목록을 알아보고자 함
loyal_customer100<-blackFriday %>% 
  group_by(User_ID) %>% 
  summarise(n=n()) %>% 
  arrange(desc(n)) %>% 
  head(100)

#userId가 중복되는 경우= 구매 횟수가 잦은 경우로 봄
#loyal_customer(100)을 저장
loyal100<-loyal_customer100$User_ID

loyal_best5<-blackFriday %>% 
  filter(User_ID %in% loyal100) %>% 
  group_by(Product_ID) %>% 
  summarise(n=n()) %>% 
  arrange(desc(n)) %>% 
  head(5)

ggplot(data=loyal_best5, aes(x=reorder(Product_ID, n), y=n))+geom_col()+
  ylim(c(0,100))+
  coord_flip()
#충성고객의 베스트 판매상품
loyal_best5$Product_ID

best5<-blackFriday %>% 
  group_by(Product_ID) %>% 
  summarise(n=n()) %>% 
  arrange(desc(n)) %>% 
  head(5)

ggplot(data=best5, aes(x=reorder(Product_ID, n), y=n))+geom_col()+
  coord_flip()

loyal_best5$Product_ID %in% best5$Product_ID
#충성고객의 best5상품과 전체 best5상품은 하나도 겹치지 않았음
loyal_best5$Product_ID


best5_26.35<-blackFriday %>% 
  filter(Age=='26-35') %>% 
  group_by(Product_ID) %>% 
  summarise(n=n()) %>% 
  arrange(desc(n)) %>% 
  head(5)

#해당 나이대의 best5상품은 전체 best5상품과 같음
best5_26.35$Product_ID %in% best5$Product_ID


ggplot(data=best5_26.35, aes(x=reorder(Product_ID, n), y=n))+geom_col()+
  coord_flip()

loyal_best5$Product_ID



####################연관규칙#############
dataset <- read.csv("blackfriday.csv")

library(tidyverse)
library(scales)
library(arules)

customers_products <- dataset %>%
  select(User_ID, Product_ID) %>% 
  group_by(User_ID) %>%
  arrange(User_ID) %>% 
  mutate(id = row_number()) %>% 
  spread(User_ID, Product_ID) %>% 
  t()

write.csv(customers_products, file = 'customers_products.csv')
customersProducts <- read.transactions('customers_products.csv', sep = ',', rm.duplicates = TRUE)
#읽는데 상당시간 소요됨

summary(customersProducts)
#transactions as itemMatrix in sparse format with
#5893 rows (elements/itemsets/transactions) and
#11575 columns (items) and a density of 0.008180618 

#5893건의 거래와 11575건의 아이템(상품수), cell density
#most frequent items:
#  P00265242 P00025442 P00110742 P00112142 P00057642 
#1880      1615      1612      1562      1470 
#best상품들과 판매개수

#element (itemset/transaction) length distribution:
#한번 거래 이루어질때 아이템 몇 개씩 사는지


CP<-customersProducts
itemFrequencyPlot(CP,support=0.01,cex=0.5)
#지지도 0.01이상이 상당히 많은듯하다
itemFrequencyPlot(CP, topN=10, cex=0.5)
#지지도 상위 10개 아이템 품목 

#규칙 생성 
#앞서 본 지지도 그래프에서 0.01 이상이 많았으므로 지지도를 0.01로 설정해보았다.
apriori(CP,parameter=list(support=0.01, confidence=0.5, minlen=2))
#규칙이 너무 많다

#신뢰도와 지지도를 조정해주며 적정한 규칙개수를 가질 수 있게 한다
CPrules<-apriori(CP,parameter=list(support=0.015, confidence=0.65, minlen=2))

summary(CPrules)
#3  4 
#14 20 
# 품목 3개 규칙 14개, 품목 4개 규칙 20개 만들어짐
#min lift는 2.376으로 1보다 높아 유의한 규칙인듯


#만들어진 규칙에 대해 충성고객 best5룰과 
#전체(==26-35나이대)best5룰이 있는지 확인해보고자 함
best5_loyal<-as.vector(loyal_best5$Product_ID)
loyal_rules<-subset(CPrules, items %in% best5_loyal)
#충성고객의 best5와 관련 규칙이 16개 있음
#그 중 상위 10개의 규칙만 확인 
inspect(sort(loyal_rules, by='lift')[1:10])
#대충 봤을 때 ~~~42로 끝나는 물품들이 같이 구매된 경우가 많은듯
#가독성이 좋지 않다... 
best_5<-as.vector(best5$Product_ID)
best5_rules<-subset(CPrules, items %in% best_5)
summary(best5_rules)
#23개 룰 있음
#상위 10개만 확인 
inspect(sort(best5_rules, by='lift')[1:10])
#역시나 가독성이 좋지 않다 


install.packages('arulesViz')
library(arulesViz)

#1. 묶음 상품
plot(sort(best5_rules, by = 'lift'), method = 'grouped' )
plot(sort(loyal_rules, by = 'lift'), method = 'grouped')

sum(blackFriday$Product_ID=='P00270942')
sum(blackFriday$Product_ID=='P00151742') 
