![alt text](https://github.com/blankaII/my_bandit_test/blob/main/20220504_homework/bandit_homework.svg?raw=true)
################################################################################

UML diagraom was drawed with
- http://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000
```
@startuml
User -> Web : browse (A or B or C) and click
Web -> Collector : pass click info with json pack
Collector -> DB : append click information to
DB <-- StaticConfig : setup some static value
DB <-> Accounting : update current net/gross income
DB <-> Statistics : update click rate
DB <-> Statistics : update statistics
DB -> Report : KPI reports
DB -> RecmdSys : Recommand System algorithm with latest data
RecmdSys -> DB : store recommandation to DB based on current result
DB -> Web : fetch current recommanded content to next user

Web -> Growthbook : click was snapped
Growthbook -> DB : growthbook internal
Growthbook -> DB : store recommand content to DB
@enduml
```
