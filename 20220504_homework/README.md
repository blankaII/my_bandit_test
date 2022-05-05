![alt text](https://github.com/blankaII/my_bandit_test/blob/main/20220504_homework/bandit_homework.svg?raw=true)
################################################################################

UML diagraom was drawed with
- http://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000
```
@startuml
Consumer -> WebA : click or not
Consumer -> WebB : click or not
Consumer -> WebC : click or not
WebA -> Growthbook : click was snapped
WebB -> Growthbook : click was snapped
WebC -> Growthbook : click was snapped
Growthbook -> DB : growthbook internal
WebA -> Collector : pass click info with json pack
WebB -> Collector : pass click info with json pack
WebC -> Collector : pass click info with json pack
Collector -> DB : append click information to
DB <-- StaticConfig : setup some static value
DB <-> Accounting : update current net/gross income
DB <-> Statistics : update click rate
DB <-> Statistics : update statistics
DB -> Report : KPI reports
DB -> Bandit : bandit algorithm with latest data
Growthbook -> Producer : fetch recommand option from growthbook
Bandit -> Producer : fetch recommand option from Bandit MachineAB
Producer -> User : feed greedy option to new user
@enduml
```
