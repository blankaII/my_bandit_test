     ┌────┐                      ┌────┐          ┌────┐          ┌─────────┐             ┌──┐             ┌──────┐          ┌───────────┐
     │User│                      │WebA│          │WebB│          │Collector│             │DB│             │Bandit│          │Web_Breeder│
     └─┬──┘                      └─┬──┘          └─┬──┘          └────┬────┘             └┬─┘             └──┬───┘          └─────┬─────┘
       │ 30% choose A, 10% choose B│               │                  │                   │                  │                    │      
       │ ──────────────────────────>               │                  │                   │                  │                    │      
       │                           │               │                  │                   │                  │                    │      
       │         10% choose A, 30% choose B        │                  │                   │                  │                    │      
       │ ──────────────────────────────────────────>                  │                   │                  │                    │      
       │                           │               │                  │                   │                  │                    │      
       │                           │           json from A            │                   │                  │                    │      
       │                           │ ────────────────────────────────>│                   │                  │                    │      
       │                           │               │                  │                   │                  │                    │      
       │                           │               │   json from B    │                   │                  │                    │      
       │                           │               │ ────────────────>│                   │                  │                    │      
       │                           │               │                  │                   │                  │                    │      
       │                           │               │                  │click history to DB│                  │                    │      
       │                           │               │                  │───────────────────>                  │                    │      
       │                           │               │                  │                   │                  │                    │      
       │                           │               │                  │                   │ AB test algorithm│                    │      
       │                           │               │                  │                   │ ─────────────────>                    │      
       │                           │               │                  │                   │                  │                    │      
       │                           │               │                  │                   │                  │   Better WebA/B    │      
       │                           │               │                  │                   │                  │ ──────────────────>│      
       │                           │               │                  │                   │                  │                    │      
       │                           │               │  feed greedy option to new user      │                  │                    │      
       │ <─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────      
     ┌─┴──┐                      ┌─┴──┐          ┌─┴──┐          ┌────┴────┐             ┌┴─┐             ┌──┴───┐          ┌─────┴─────┐
     │User│                      │WebA│          │WebB│          │Collector│             │DB│             │Bandit│          │Web_Breeder│
     └────┘                      └────┘          └────┘          └─────────┘             └──┘             └──────┘          └───────────┘
################################################################################
- http://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000

<p><code>
@startuml
User -> WebA : 30% choose A, 10% choose B
User -> WebB : 10% choose A, 30% choose B
WebA -> Collector : json from A
WebB -> Collector : json from B
Collector -> DB : click history to DB
DB -> Bandit : AB test algorithm
Bandit -> Web_Breeder : Better WebA/B
Web_Breeder -> User : feed greedy option to new user
@enduml
</code></p>
