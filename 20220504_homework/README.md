![alt text](https://github.com/blankaII/my_bandit_test/blob/main/20220504_homework/bandit_homework.png?raw=true)
################################################################################

UML diagraom was drawed with
- http://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000
```
@startuml
User -> WebA0.3click300Earned : click or not
User -> WebB0.1click100Earned : click or not
WebA0.3click300Earned -> GrowthBook : click was snapped
WebB0.1click100Earned -> GrowthBook : click was snapped
Growthbook -> DB : growthbook internal
WebA0.3click300Earned -> Collector : information pack with json
WebB0.1click100Earned -> Collector : information pack with json
Collector -> DB : current gross/net profit
Collector -> DB : click click information to
DB -> Bandit : bandit algorithm with realtime data
Growthbook -> OptionFetcher : fetch recommand option from growthbook
Bandit -> OptionFetcher : fetch recommand option from Bandit MachineAB
OptionFetcher -> User : feed greedy option to new user
@enduml
```
