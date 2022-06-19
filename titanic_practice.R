library(rpart)
set.seed(20220311)
idx=sample(nrow(iris), size=nrow(iris)*0.7)


iris_train<-iris[idx,]
iris_test<-iris[-idx,]

iris_model<-rpart(Species ~ .,
                  data=iris_train,
                  method='class') 
iris_model 
iris_model$control

#1. minbucket값을 1~10으로 변경하며 모델 생성
#모델 평가, 가장 정확도 높은 모델의 minbucket과 정확도 출력
ylabel<-iris_test$Species
precision<-c()
for (i in 1:10){
  iris_model<-rpart(Species ~ .,
                    data=iris_train,
                    control= rpart.control(minbucket = i),
                    method='class') 
  prediction<-predict(iris_model, newdata =iris_test, type='class')
  precision<-c(precision, sum(ylabel==prediction) /nrow(iris_test)*100)
  
}
which(precision==max(precision))
#minbucket이 2와 3일 때 가장 정확도가 높다

#2.maxdepth를 얼마로 했을때 정확도가 높은지 조사
iris_model$control
#default:30

precision<-c()
for (i in 1:30){
  iris_model<-rpart(Species ~ .,
                    data=iris_train,
                    control= rpart.control(maxdepth = i),
                    method='class') 
  prediction<-predict(iris_model, newdata =iris_test, type='class')
  precision<-c(precision, sum(ylabel==prediction) /nrow(iris_test)*100)
  
}
which(precision==max(precision))
precision
#maxdepth가 1일때 외에는 정확도 차이가 없었다
#maxdepth를 30을 초과하게 설정할 수 없었음(에러뜸)

#3. 타이타닉 모델 튜닝
#4번참고


#4. 호칭정보 모델링시 포함하기

train<-read.csv('train.csv')
lst<-unlist(strsplit(train$Name, " "))
lst<-lst[grep('.{2,}\\.$', lst)] 

train$title<-lst

train$title[train$title %in% c("Mlle.", "Ms.", "Lady.", "Dona.")]<-'Miss.'
train$title[train$title == 'Mme.']<-'Mrs.'
train$title[train$title %in% c("Capt.", "Col.", "Major.", "Dr.", "Rev.", "Don.",  "Sir.", "Countess.", "Jonkheer.")] <-'Officer.'
train$title[train$Sex=='male'&train$Age<10]<-"boy"

table(train$title)

prop.table(table(train$title, train$Survived),1)

train$Ageg<-cut(train$Age, breaks=c(0,10,20,30,40,50,60,Inf), right=T)
levels(train$Ageg)<-c('10세미만', '10대', '20대', '30대', '40대', '50대', '60세 이상')

train$Pclass<-as.factor(train$Pclass)

aggregate(Survived~Sex+Ageg+Pclass,
          data= train, FUN =function(x){sum(x)/length(x)})

model<-rpart(Survived~ Pclass+Ageg+Sex+title,
             data=train,
            method='class')

test<-read.csv('test.csv')
#테스트데이터에 Ageg열과 title열이 없어 오류
#테스트데이터에도 두 개의 열을 만들어줌
#prediction<-predict(model, test, type='class')

lst<-unlist(strsplit(test$Name, " "))
lst<-lst[grep('.{2,}\\.$', lst)] 

test$title<-lst

test$title[test$title %in% c("Mlle.", "Ms.", "Lady.", "Dona.")]<-'Miss.'
test$title[test$title == 'Mme.']<-'Mrs.'
test$title[test$title %in% c("Capt.", "Col.", "Major.", "Dr.", "Rev.", "Don.",  "Sir.", "Countess.", "Jonkheer.")] <-'Officer.'
test$title[test$Sex=='male'& test$Age<10]<-"boy"

test$Ageg<-cut(test$Age, breaks=c(0,10,20,30,40,50,60,Inf), right=T)
levels(test$Ageg)<-c('10세미만', '10대', '20대', '30대', '40대', '50대', '60세 이상')

prediction<-predict(model, test, type='class')
#이제 해당 문장이 오류 없이 실행
mysubmit<-data.frame(PassengerId=test$PassengerId, Survived=prediction)
write.csv(mysubmit, file="new.csv", row.names = FALSE)

#제출결과-->2102등 0.78468

model
model$control
plot(model)
text(model, cex=0.5)
prp(model, type=4, extra =2, digits = 3)

train$title[train$Sex=='male'&train$Age<10]<-"boy"


#titanic knn모델 만들기
library(class)

train<-read.csv('train.csv', na.strings = "", stringsAsFactors = T)
test<-read.csv('test.csv', na.strings = "", stringsAsFactors = T)

labels<-train[,'Survived']

train<-train[,-2]


#knn(train=titanic_train, 
#           test=titanic_test, 
#           cl=labels, 
#           k=5)

#error no missing values are allowed
#knn모델 생성시 결측값이 없어야 하는듯
table(is.na(train$Cabin))
table(is.na(train$Age))
table(is.na(train$Embarked))
#열마다 확인해봤을 때 결측값 가진 열은 위의 3가지였음

train$Cabin
#Cabin열의 경우 NA값이 너무 많고 대체가 어려우므로 모델 생성시 아예 제외한다
train<-train[,-10]
test<-test[,-10]    

#Embarked열 NA를 S로 대체
train$Embarked[is.na(train$Embarked)]<-'S'
test$Embarked[is.na(test$Embarked)]<-'S'

train$Embarked


#AGE열
#age를 예측하는 모델을 만들어 NA를 대체해줌
library(rpart)
Agefit<-rpart(Age~Pclass+Sex+SibSp+Parch+Fare+Embarked,
              data=train[!is.na(train$Age),],
              method='anova')

train$Age[is.na(train$Age)]<-predict(Agefit, train[is.na(train$Age),])

table(is.na(train$Age))

#test데이터에 대해서도 모델 생성 후 적용
Agefit2<-rpart(Age~Pclass+Sex+SibSp+Parch+Fare+Embarked,
              data=test[!is.na(test$Age),],
              method='anova')

test$Age[is.na(test$Age)]<-predict(Agefit2, test[is.na(test$Age),])
table(is.na(test$Age))

#NA처리를 해주었는데 여전히
#no missing values are allowed
#오류가 뜬다
#knn(train=train, test=test, cl=labels, k=21)

levels(train$Sex)<-c(1,2) 
levels(test$Sex)<-c(1,2)  
levels(train$Pclass)<-c(1,2,3)
levels(test$Pclass)<-c(1,2,3)

str(train)
str(test)

train$Ageg<-cut(train$Age, breaks=c(0,10,20,30,40,50,60,Inf), right=T)
levels(train$Ageg)<-c(1,2,3,4,5,6,7)

test$Ageg<-cut(test$Age, breaks=c(0,10,20,30,40,50,60,Inf), right=T)
levels(test$Ageg)<-c(1,2,3,4,5,6,7)

#levels(train$Embarked)<-c(1,2,3)
#levels(train$Embarked)<-c(1,2,3) 
# Embarked넣으면 오류나서 안넣음


#factor만 되나 싶어서 나머지 변수 다 뺌
#제출을 위해 test$PassengerId는 따로 저장
psid<-test$PassengerId

train<-train[,c('Pclass','Sex','Ageg')]
test<-test[,c('Pclass','Sex','Ageg')]
dim(train)
dim(test)
model_k<-knn(train=train, test=test, cl=labels, k=21)

submit<-data.frame(PassengerId=psid,Survived=model_k)
write.csv(submit,file="neww.csv",row.names = FALSE)

#Score: 0.77272 
#knn은 유클리드거리 형식을 취하므로 데이터들을 수치형 데이터로 전환해야 함
#그러나 문자형 데이터를 수치형으로 전환시
#master=0, miss=1, mrs=2, off=3
#등으로 만들었을 때 error발생(미스 두 명==mrs?)

#--> 각각의 차원으로 만들어서
#1000
#0100
#0010
#0001

#등 각각의 차원을 주어 계산하도록 해야 함

